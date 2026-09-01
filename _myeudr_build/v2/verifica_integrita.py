#!/usr/bin/env python3
"""Confronta v2 col backup pre-modifica: righe per foglio, ordine dei fogli,
campi svuotati (deve essere ZERO) e ogni singola cella cambiata."""
import json, os, sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
A = load_workbook(os.path.join(HERE, "backup_v1.xlsx"))
B = load_workbook(os.path.join(REPO, "MyEUDR_Lead_Mapping_v2.xlsx"))
ORDINE = ["Italia","Germania","Finlandia","Danimarca","Svezia","Olanda","Belgio","Austria"]
CAMPI = ["denominazione","filiera","dimensione","referente","ruolo","linkedin","email","sito","sede","fonte"]

ok = True
print("ordine fogli v2 :", B.sheetnames)
if B.sheetnames != ORDINE: print("  ✗ ORDINE ERRATO"); ok = False
else: print("  ✓ ordine corretto")

def righe(wb, sn):
    return [[("" if c.value is None else str(c.value).strip()) for c in r]
            for r in wb[sn].iter_rows(min_row=3, max_col=10) if r[0].value]

svuotati, cambi = [], []
print("\nrighe per foglio (v1 → v2):")
for sn in ORDINE:
    ra, rb = righe(A, sn), righe(B, sn)
    flag = "✓" if len(ra) == len(rb) else "✗"
    if flag == "✗": ok = False
    print(f"  {flag} {sn:12s} {len(ra):4d} → {len(rb):4d}")
    if len(ra) != len(rb): continue
    for x, y in zip(ra, rb):
        for i, campo in enumerate(CAMPI):
            if x[i] == y[i]: continue
            rec = dict(foglio=sn, denominazione=y[0], campo=campo, da=x[i], a=y[i])
            cambi.append(rec)
            # svuotato = da valore reale a vuoto/"n.d."
            if x[i] and x[i].lower() not in ("n.d.", "") and (not y[i] or y[i].lower() == "n.d."):
                svuotati.append(rec)

print(f"\ncelle cambiate: {len(cambi)}")
print(f"campi SVUOTATI: {len(svuotati)}", "✓" if not svuotati else "✗ REGOLA 2 VIOLATA")
for s in svuotati: print("   ", s)
json.dump(cambi, open(os.path.join(HERE, "diff_v1_v2.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
if not ok or svuotati: sys.exit(1)
print("\n✓ integrita' verificata")
