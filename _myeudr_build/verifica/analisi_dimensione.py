#!/usr/bin/env python3
"""Analisi offline del campo Dimensione: tipo di dato dichiarato, anno del dato, obsolescenza."""
import json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
recs = json.load(open(os.path.join(HERE, "_records.json"), encoding="utf-8"))
PIPE = "\\|"
SHEETS = ["Italia","Germania","Finlandia","Danimarca","Svezia","Olanda","Belgio","Austria"]

# tipo di dato: parola esplicita OPPURE notazione compatta inequivocabile (12,5 M€ / ~30 dip.)
TIPO_ESPL = re.compile(r"fatturat|omzet|omsättning|omsattning|umsatz|turnover|ricav|revenue|"
                       r"bruttofortjeneste|totale di bilancio|balanstotal|bilancio|dipend|addett|"
                       r"\bFTE\b|impiegat|mitarbeit|employees|anställda|medarbejder|volumi|"
                       r"fm/anno|t/anno|tonnellate|liikevaihto|chiffre d'affaires|\bMA\b|\bdip\.", re.I)
TIPO_IMPL = re.compile(r"\d\s*(M€|mln €|Mio\.? ?€|MSEK|M DKK|mio\.? DKK|MEUR)", re.I)

# anno del DATO: escludo gli anni di fondazione ("dal 1923", "gegr. 1908", "fondata nel 1964")
FOND = re.compile(r"(?:dal|since|gegr\.?|gegründet|fondat\w*(?: nel)?|costituit\w*(?: il| nel)?|"
                  r"gründung|opgericht|gestart|gr\.|gründungsjahr|anno)\s*(?:in\s*)?(1[5-9]\d{2}|20[0-2]\d)", re.I)
ANNO = re.compile(r"\b(19\d{2}|20[0-2]\d)\b")

def anni_dato(t):
    fond = {m.group(1) for m in FOND.finditer(t)}
    # anche "dal 1976," in coda a una descrizione ("grossista di carne dal 1976")
    return sorted({int(y) for y in ANNO.findall(t) if y not in fond}, reverse=True)

rows = defaultdict(list)
for r in recs: rows[r["_sheet"]].append(r)

o = []
o.append("# Analisi del campo `Dimensione`\n")
o.append("_Controllo offline: il campo dichiara **che tipo di dato** riporta, **con quale anno**, "
         "e quanto è recente. Gli anni di fondazione sono esclusi dal calcolo dell'anno del dato._\n")
o.append("\n| Foglio | Record | Tipo non dichiarato | Anno assente | Dato ≤ 2020 | Dato ≤ 2018 |")
o.append("|---|--:|--:|--:|--:|--:|")

stale, notype, noyear = [], [], []
for sn in SHEETS:
    rs = rows[sn]; nt = na = o20 = o18 = 0
    for r in rs:
        d = r["dimensione"]
        if not (TIPO_ESPL.search(d) or TIPO_IMPL.search(d)):
            nt += 1; notype.append((sn, r["denominazione"], d))
        ys = anni_dato(d)
        if not ys:
            na += 1; noyear.append((sn, r["denominazione"], d))
        else:
            if ys[0] <= 2020: o20 += 1; stale.append((sn, r["denominazione"], ys[0], d))
            if ys[0] <= 2018: o18 += 1
    o.append(f"| {sn} | {len(rs)} | {nt} | {na} | {o20} | {o18} |")
o.append(f"| **TOTALE** | **{len(recs)}** | **{len(notype)}** | **{len(noyear)}** | "
         f"**{len(stale)}** | **{sum(1 for x in stale if x[2] <= 2018)}** |")

o.append(f"\n---\n\n## Dato dimensionale del 2020 o anteriore ({len(stale)})\n")
o.append("_Il dato non è necessariamente sbagliato, ma è **obsoleto** rispetto alla forbice "
         "5–40 M€ su cui il cliente seleziona i lead: va rinfrescato prima del contatto._\n")
o.append("| Foglio | Azienda | Anno | Campo Dimensione |")
o.append("|---|---|--:|---|")
for sn, den, y, d in sorted(stale, key=lambda x: (x[2], x[0])):
    o.append(f"| {sn} | {den[:42]} | {y} | {d.replace(chr(124), PIPE)[:190]} |")

o.append(f"\n---\n\n## Nessun anno associato al dato ({len(noyear)})\n")
o.append("_Impossibile stabilire a che esercizio si riferisce il dato._\n")
o.append("| Foglio | Azienda | Campo Dimensione |")
o.append("|---|---|---|")
for sn, den, d in noyear:
    o.append(f"| {sn} | {den[:42]} | {d.replace(chr(124), PIPE)[:190]} |")

o.append(f"\n---\n\n## Tipo di dato non dichiarato ({len(notype)})\n")
o.append("_Il mandato di raccolta chiede che il campo dichiari se il numero è fatturato, "
         "bruttofortjeneste, totale di bilancio, dipendenti o volumi._\n")
o.append("| Foglio | Azienda | Campo Dimensione |")
o.append("|---|---|---|")
for sn, den, d in notype:
    o.append(f"| {sn} | {den[:42]} | {d.replace(chr(124), PIPE)[:190]} |")

open(os.path.join(HERE, "01_analisi_dimensione.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"scritto 01_analisi_dimensione.md")
print(f"  tipo non dichiarato: {len(notype)} | anno assente: {len(noyear)} | dato <=2020: {len(stale)}")
