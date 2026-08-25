#!/usr/bin/env python3
"""Genera REPORT_VERIFICA.md: sintesi Fase A + Fase B, casi alta, correzioni proposte."""
import glob, json, os, re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SHEETS = ["Italia","Germania","Finlandia","Danimarca","Svezia","Olanda","Belgio","Austria"]
ATTESI = dict(zip(SHEETS, [95,97,84,89,89,100,95,93]))
GRAV = ["alta","media","bassa"]
SKIP = ("_records", "correzioni_")

def esc(s): return str(s or "").replace("|", "\\|").replace("\n", " ").strip()

def carica_rilievi():
    out, files = [], []
    for fp in sorted(glob.glob(os.path.join(HERE, "*.json"))):
        bn = os.path.basename(fp)
        if bn.startswith(SKIP): continue
        try: data = json.load(open(fp, encoding="utf-8"))
        except Exception: continue
        if not isinstance(data, list): continue
        files.append(bn)
        for o in data:
            if not isinstance(o, dict): continue
            o["_file"] = bn
            g = (o.get("gravita") or "").strip().lower()
            o["gravita"] = g if g in GRAV else "media"
            out.append(o)
    return out, files

def blocchi_coperti(files):
    """quali blocchi di ciascun foglio sono stati verificati"""
    tot = defaultdict(list); fatti = defaultdict(list)
    for fp in sorted(glob.glob(os.path.join(HERE, "blocchi", "*.json"))):
        bn = os.path.basename(fp)[:-5]
        sh = bn.rsplit("_", 1)[0].capitalize()
        n = len(json.load(open(fp, encoding="utf-8")))
        tot[sh].append((bn, n))
        if bn + ".json" in files: fatti[sh].append((bn, n))
    return tot, fatti

def main():
    R, files = carica_rilievi()
    tot_b, fatti_b = blocchi_coperti(files)
    by_sheet = defaultdict(list)
    for r in R: by_sheet[r.get("foglio", "?")].append(r)
    c_all = Counter(r["gravita"] for r in R)

    o = []
    o.append("# REPORT DI VERIFICA — MyEUDR Lead Mapping\n")
    o.append("Controllo qualità record per record del censimento lead (**742 aziende, 8 fogli**). "
             "Non è una raccolta di nuove aziende: è la verifica del lavoro esistente.\n")
    o.append("La verifica si è svolta in due fasi:\n")
    o.append("- **Fase A — controlli deterministici**, offline, su tutti i JSON di build e sul "
             "workbook: 24 controlli automatici su duplicati, email dedotte, URL, entità HTML, "
             "tassonomia, forbice dimensionale, denominazioni e forme giuridiche. "
             "Dettaglio in [`00_controlli_automatici.md`](00_controlli_automatici.md) e "
             "[`01_analisi_dimensione.md`](01_analisi_dimensione.md).")
    o.append("- **Fase B — riscontro sul web**, record per record, tramite agenti di verifica "
             "che hanno lavorato a blocchi di 15-20 aziende con 2-3 ricerche ciascuna. "
             "Ogni rilievo porta un URL o la citazione del frammento a sostegno.\n")

    # ---------- copertura ----------
    o.append("\n## 1. Copertura della verifica\n")
    o.append("| Foglio | Aziende | Blocchi verificati | Aziende verificate | Copertura |")
    o.append("|---|--:|---|--:|--:|")
    tot_ver = 0
    for sn in SHEETS:
        nb, nf = tot_b.get(sn, []), fatti_b.get(sn, [])
        nrec = sum(n for _, n in nf); tot_ver += nrec
        o.append(f"| {sn} | {ATTESI[sn]} | {len(nf)}/{len(nb)} | {nrec} | "
                 f"{100*nrec/ATTESI[sn]:.0f}% |")
    o.append(f"| **TOTALE** | **742** | **{sum(len(v) for v in fatti_b.values())}/"
             f"{sum(len(v) for v in tot_b.values())}** | **{tot_ver}** | "
             f"**{100*tot_ver/742:.0f}%** |")
    o.append("\n> La Fase A copre invece il **100%** dei 742 record: è un controllo offline "
             "e non dipende dal budget di ricerca.\n")
    o.append("\n_A questi si aggiunge la verifica mirata dei **13 punti già noti** lasciati aperti "
             "dalla raccolta, condotta separatamente e riportata per intero più sotto._\n")

    # ---------- sintesi rilievi ----------
    o.append("\n## 2. Rilievi per foglio\n")
    o.append(f"**Totale rilievi Fase B: {len(R)}** — alta {c_all['alta']} · "
             f"media {c_all['media']} · bassa {c_all['bassa']}.\n")
    o.append("| Foglio | Rilievi | alta | media | bassa | Aziende toccate |")
    o.append("|---|--:|--:|--:|--:|--:|")
    for sn in SHEETS:
        rs = by_sheet.get(sn, [])
        c = Counter(r["gravita"] for r in rs)
        o.append(f"| {sn} | {len(rs)} | {c['alta']} | {c['media']} | {c['bassa']} | "
                 f"{len({r.get('denominazione','') for r in rs})} |")
    altri = [k for k in by_sheet if k not in SHEETS]
    for sn in altri:
        rs = by_sheet[sn]; c = Counter(r["gravita"] for r in rs)
        o.append(f"| _{sn}_ | {len(rs)} | {c['alta']} | {c['media']} | {c['bassa']} | "
                 f"{len({r.get('denominazione','') for r in rs})} |")
    o.append(f"| **TOTALE** | **{len(R)}** | **{c_all['alta']}** | **{c_all['media']}** | "
             f"**{c_all['bassa']}** | **{len({(r.get('foglio'),r.get('denominazione')) for r in R})}** |")

    o.append("\n### Rilievi per campo\n")
    fc = Counter(str(r.get("campo","?")).strip().lower() for r in R)
    fa = Counter(str(r.get("campo","?")).strip().lower() for r in R if r["gravita"]=="alta")
    o.append("| Campo | Rilievi | di cui alta |")
    o.append("|---|--:|--:|")
    for f, n in fc.most_common():
        o.append(f"| {esc(f)} | {n} | {fa[f]} |")

    # ---------- casi alta ----------
    alte = [r for r in R if r["gravita"] == "alta"]
    o.append(f"\n---\n\n## 3. Casi di gravità ALTA ({len(alte)})\n")
    o.append("_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, "
             "oppure fuori dal perimetro dell'Allegato I EUDR._\n")
    if not alte: o.append("_Nessuno._")
    for sn in SHEETS + altri:
        rs = [r for r in alte if r.get("foglio") == sn]
        if not rs: continue
        o.append(f"\n### {sn} ({len(rs)})\n")
        for r in sorted(rs, key=lambda x: str(x.get("denominazione",""))):
            o.append(f"#### {esc(r.get('denominazione'))} — campo `{esc(r.get('campo'))}`\n")
            o.append(f"{esc(r.get('problema'))}\n")
            o.append(f"**Evidenza:** {esc(r.get('evidenza'))}\n")
            cp = esc(r.get("correzione_proposta"))
            o.append(f"**Correzione proposta:** {cp if cp else '— nessun valore certo: rilievo lasciato aperto'}\n")

    # ---------- media / bassa ----------
    for g, tit, nota in (
        ("media","4. Casi di gravità MEDIA","_Dato dubbio o obsoleto: da rinfrescare prima del contatto, non necessariamente errato._"),
        ("bassa","5. Casi di gravità BASSA","_Refusi formali e incoerenze di stile._")):
        rs_all = [r for r in R if r["gravita"] == g]
        o.append(f"\n---\n\n## {tit} ({len(rs_all)})\n")
        o.append(nota + "\n")
        if not rs_all: o.append("_Nessuno._"); continue
        for sn in SHEETS + altri:
            rs = [r for r in rs_all if r.get("foglio") == sn]
            if not rs: continue
            o.append(f"\n### {sn} ({len(rs)})\n")
            o.append("| Azienda | Campo | Problema | Evidenza | Correzione proposta |")
            o.append("|---|---|---|---|---|")
            for r in sorted(rs, key=lambda x: str(x.get("denominazione",""))):
                o.append(f"| {esc(r.get('denominazione'))[:44]} | {esc(r.get('campo'))} | "
                         f"{esc(r.get('problema'))[:250]} | {esc(r.get('evidenza'))[:150]} | "
                         f"{esc(r.get('correzione_proposta'))[:120]} |")

    md = "\n".join(o) + "\n"
    open(os.path.join(HERE, "_corpo_report.md"), "w", encoding="utf-8").write(md)
    print(f"corpo report: {len(R)} rilievi, {len(files)} blocchi, copertura {tot_ver}/742")
    return R, files, tot_ver

if __name__ == "__main__":
    main()
