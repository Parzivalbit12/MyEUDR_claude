#!/usr/bin/env python3
"""Aggrega i file di rilievi prodotti dagli agenti di Fase B in REPORT_VERIFICA.md."""
import glob, json, os, re
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SHEETS = ["Italia","Germania","Finlandia","Danimarca","Svezia","Olanda","Belgio","Austria"]
GRAV = ["alta","media","bassa"]
SKIP = {"_records.json"}

def load():
    out = []
    for fp in sorted(glob.glob(os.path.join(HERE, "*.json"))):
        bn = os.path.basename(fp)
        if bn in SKIP: continue
        try:
            data = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            print(f"  !! {bn}: JSON illeggibile ({e})"); continue
        if not isinstance(data, list):
            print(f"  !! {bn}: non è un array"); continue
        for o in data:
            if not isinstance(o, dict): continue
            o["_file"] = bn
            o["gravita"] = (o.get("gravita") or "").strip().lower()
            if o["gravita"] not in GRAV: o["gravita"] = "media"
            out.append(o)
    return out

def esc(s): return str(s or "").replace("|", "\\|").replace("\n", " ").strip()

def main():
    R = load()
    print(f"{len(R)} rilievi da {len(set(r['_file'] for r in R))} file")
    by_sheet = defaultdict(list)
    for r in R: by_sheet[r.get("foglio","?")].append(r)

    o = []
    o.append("# REPORT DI VERIFICA — MyEUDR Lead Mapping\n")
    o.append("Verifica record per record del censimento (742 aziende, 8 fogli). "
             "Fase A: controlli deterministici offline. Fase B: riscontro sul web, record per record.\n")
    o.append(f"**Totale rilievi Fase B: {len(R)}** "
             f"(alta {sum(1 for r in R if r['gravita']=='alta')} · "
             f"media {sum(1 for r in R if r['gravita']=='media')} · "
             f"bassa {sum(1 for r in R if r['gravita']=='bassa')}).\n")

    o.append("\n## Sintesi per foglio\n")
    o.append("| Foglio | Rilievi | alta | media | bassa | Aziende toccate |")
    o.append("|---|--:|--:|--:|--:|--:|")
    for sn in SHEETS + [k for k in by_sheet if k not in SHEETS]:
        rs = by_sheet.get(sn, [])
        if not rs and sn not in SHEETS: continue
        c = Counter(r["gravita"] for r in rs)
        o.append(f"| {sn} | {len(rs)} | {c['alta']} | {c['media']} | {c['bassa']} | "
                 f"{len({r.get('denominazione','') for r in rs})} |")
    c = Counter(r["gravita"] for r in R)
    o.append(f"| **TOTALE** | **{len(R)}** | **{c['alta']}** | **{c['media']}** | **{c['bassa']}** | "
             f"**{len({(r.get('foglio'),r.get('denominazione')) for r in R})}** |")

    o.append("\n## Rilievi per campo\n")
    o.append("| Campo | Rilievi | alta |")
    o.append("|---|--:|--:|")
    fc = Counter(str(r.get("campo","?")).strip().lower() for r in R)
    fa = Counter(str(r.get("campo","?")).strip().lower() for r in R if r["gravita"]=="alta")
    for f, n in fc.most_common():
        o.append(f"| {esc(f)} | {n} | {fa[f]} |")

    alte = [r for r in R if r["gravita"] == "alta"]
    o.append(f"\n---\n\n## Casi di gravità ALTA ({len(alte)})\n")
    o.append("_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, "
             "oppure fuori dal perimetro dell'Allegato I EUDR._\n")
    if not alte:
        o.append("_Nessuno._")
    for sn in SHEETS + [k for k in by_sheet if k not in SHEETS]:
        rs = [r for r in alte if r.get("foglio") == sn]
        if not rs: continue
        o.append(f"\n### {sn} ({len(rs)})\n")
        for r in sorted(rs, key=lambda x: str(x.get("denominazione",""))):
            o.append(f"**{esc(r.get('denominazione'))}** — campo `{esc(r.get('campo'))}`  ")
            o.append(f"{esc(r.get('problema'))}  ")
            o.append(f"*Evidenza:* {esc(r.get('evidenza'))}  ")
            cp = esc(r.get("correzione_proposta"))
            o.append(f"*Correzione proposta:* {cp if cp else '— (nessun valore certo: rilievo aperto)'}\n")

    for g, tit in (("media","Casi di gravità MEDIA"), ("bassa","Casi di gravità BASSA")):
        rs_all = [r for r in R if r["gravita"] == g]
        o.append(f"\n---\n\n## {tit} ({len(rs_all)})\n")
        if not rs_all:
            o.append("_Nessuno._"); continue
        for sn in SHEETS + [k for k in by_sheet if k not in SHEETS]:
            rs = [r for r in rs_all if r.get("foglio") == sn]
            if not rs: continue
            o.append(f"\n### {sn} ({len(rs)})\n")
            o.append("| Azienda | Campo | Problema | Evidenza | Correzione proposta |")
            o.append("|---|---|---|---|---|")
            for r in sorted(rs, key=lambda x: str(x.get("denominazione",""))):
                o.append(f"| {esc(r.get('denominazione'))[:45]} | {esc(r.get('campo'))} | "
                         f"{esc(r.get('problema'))[:230]} | {esc(r.get('evidenza'))[:170]} | "
                         f"{esc(r.get('correzione_proposta'))[:120]} |")

    md = "\n".join(o) + "\n"
    open(os.path.join(HERE, "REPORT_VERIFICA_parziale.md"), "w", encoding="utf-8").write(md)
    print("scritto REPORT_VERIFICA_parziale.md")
    for sn in SHEETS:
        rs = by_sheet.get(sn, [])
        if rs: print(f"  {sn:11s} {len(rs):4d}  (alta {sum(1 for r in rs if r['gravita']=='alta')})")

if __name__ == "__main__":
    main()
