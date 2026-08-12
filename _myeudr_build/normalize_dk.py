#!/usr/bin/env python3
"""
Normalizza i JSON danesi sulla convenzione già usata nei fogli Italia/Germania/Finlandia:

  - `filiera`  -> "<Macro> — <dettaglio breve>" con le macro-famiglie del foglio Italia
                  (Legno/Arredo, Carta/Packaging, Caffè, Cacao/Cioccolato, Gomma,
                   Mangimi/Soia, Olio di palma, Bovini/Carne, Pelle/Concia).
  - `denominazione` -> solo ragione sociale (+ eventuale nome commerciale tra parentesi);
                  il codice CVR viene spostato in coda a `dimensione`, dove stanno già
                  le annotazioni di fonte/anno.

Uso: python normalize_dk.py [--dry-run]
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# --- filiera: mappa esplicita per azienda (chiave = denominazione originale, troncata) ---
FILIERA = {
    # dk_01 mobili -> macro "Legno/Arredo" (come Italia/Finlandia)
    "SKOVBY MØBELFABRIK": "Legno/Arredo — mobili in legno massello/pannelli",
    "KVIST INDUSTRIES": "Legno/Arredo — componenti e sedute (subfornitura)",
    "GETAMA DANMARK": "Legno/Arredo — mobili in legno massello/pelle",
    "Farstrup Furniture": "Legno/Arredo — sedute e imbottiti",
    "NIELAUS": "Legno/Arredo — sedute in legno e pelle",
    "ONECOLLECTION": "Legno/Arredo — mobili in legno massello/pelle",
    "VERMUND LARSEN": "Legno/Arredo — sedute e tavoli (contract/healthcare)",
    "HAMMEL FURNITURE": "Legno/Arredo — sistemi contenitivi e sedute",
    "FREDERICIA FURNITURE": "Legno/Arredo — mobili in legno massello/imbottiti",
    "Skagerak Denmark": "Legno/Arredo — arredi indoor/outdoor",
    "N. EILERSEN": "Legno/Arredo — mobili imbottiti",
    "SIKA DESIGN": "Legno/Arredo — arredi in rattan/legno",
    "Klim Furniture": "Legno/Arredo — imbottiti e sedute",
    "GRAMRODE MØBELFABRIK": "Legno/Arredo — mobili",
    "SOFTLINE": "Legno/Arredo — mobili imbottiti",
    "INNOVATION LIVING": "Legno/Arredo — divani letto",
    "AUBO PRODUCTION": "Legno/Arredo — cucine e arredo bagno",
    "JKE DESIGN": "Legno/Arredo — cucine",
    "MULTIFORM": "Legno/Arredo — cucine su misura",
    # dk_02 legno
    "SOMMER-SAVEX": "Legno/Arredo — import legname (hårdttræ/impiallacciature)",
    "KEFLICO": "Legno/Arredo — import legname (hårdttræ/pannelli)",
    "GLOBAL TIMBER": "Legno/Arredo — import/export legname",
    "TIMBERMAN DENMARK": "Legno/Arredo — import parquet/pavimenti in legno",
    "KRYDSFINER-HANDELEN": "Legno/Arredo — commercio pannelli (compensato/MDF)",
    "LILLEHEDEN": "Legno/Arredo — legno lamellare/glulam",
    "SUPERWOOD": "Legno/Arredo — impregnazione legno/rivestimenti",
    "HØRNING PARKET": "Legno/Arredo — parquet/pavimenti in legno",
    "DINESEN FLOORS": "Legno/Arredo — segheria/pavimenti in tavole",
    "HVIDBJERG VINDUET": "Legno/Arredo — finestre e porte in legno",
    "BØJSØ DØRE": "Legno/Arredo — porte e finestre in legno",
    "DANSK HÅRDTTRÆ SAVVÆRK": "Legno/Arredo — segheria/import legni duri",
    "NPI": "Legno/Arredo — import pannelli a base legno",
    "HårdtTrælasten": "Legno/Arredo — commercio legni nobili",
    # dk_04 caffè/cacao
    "The Coffee Collective": "Caffè — torrefazione + import caffè verde",
    "La Cabra": "Caffè — torrefazione + import caffè verde",
    "I.M. FRELLSEN": "Caffè — import caffè verde + cacao/cioccolato",
    "Kontra": "Caffè — torrefazione/engros (import caffè verde)",
    "Copenhagen Coffee Lab": "Caffè — torrefazione/engros B2B",
    "Estate Coffee": "Caffè — torrefazione + cacao/cioccolato",
    "DANSK KAFFE": "Caffè — import/export caffè verde",
    "Just Coffee": "Caffè — import caffè verde bio + torrefazione",
    "Nordic Coffee House": "Caffè — engros e import",
    "CAFÉU DENMARK": "Caffè — engros B2B",
    "Xocolatl": "Cacao/Cioccolato — produzione ed engros",
    "PR CHOKOLADE": "Cacao/Cioccolato — produzione ed engros",
    # dk_05 mangimi
    "SKOVS KORN": "Mangimi/Soia — trading korn og foderstof",
    "CEBECO FOURAGE": "Mangimi/Soia — kraftfoder bovini da latte",
    "COMPEX": "Mangimi/Soia — minerali/premix zootecnici",
}

# --- filiera: fallback per valore letterale (dk_03 e categorie già canoniche) ---
FILIERA_LITERAL = {
    "Carta/Imballaggio": "Carta/Packaging — imballaggi",
    "Carta/Cartiera": "Carta/Packaging — cartiera",
    "Carta/Stampa": "Carta/Packaging — stampa",
    "Carta/Etichette": "Carta/Packaging — etichette",
    "Cacao/Cioccolato": "Cacao/Cioccolato",
    "Mangimi/Soia": "Mangimi/Soia",
    "Gomma": "Gomma",
    "Bovini/Carne": "Bovini/Carne",
    "Pelle/Concia": "Pelle/Concia",
    "Olio di palma": "Olio di palma",
}

CVR_RE = re.compile(r"\s*\(CVR\s*(\d{8})\)")

# nomi che portano una nota di qualità: la nota si sposta in `dimensione`
NAME_FIX = {
    "Just Coffee (torrefazione bio, Jyllinge) - ragione sociale CVR non verificata":
        ("Just Coffee", "ragione sociale CVR non verificata"),
}


def norm_filiera(rec):
    for key, val in FILIERA.items():
        if rec["denominazione"].upper().startswith(key.upper()):
            return val
    return FILIERA_LITERAL.get(rec["filiera"], rec["filiera"])


def norm_denominazione(rec):
    """Toglie il codice CVR dal nome e lo restituisce a parte; normalizza ' - alias'."""
    name, cvr = rec["denominazione"], None
    if name in NAME_FIX:
        name, note = NAME_FIX[name]
        dim = (rec.get("dimensione") or "").strip() or "n.d."
        if note not in dim:
            rec["dimensione"] = f"{dim} · {note}"
        return name, None
    m = CVR_RE.search(name)
    if m:
        cvr = m.group(1)
        name = CVR_RE.sub("", name)
    # "X - alias" -> "X (alias)", ma solo se non c'è già una parentesi
    if " - " in name and "(" not in name:
        head, tail = name.split(" - ", 1)
        name = f"{head.strip()} ({tail.strip()})"
    return re.sub(r"\s{2,}", " ", name).strip(" -"), cvr


def main():
    dry = "--dry-run" in sys.argv
    for fp in sorted(glob.glob(os.path.join(HERE, "dk_*.json"))):
        with open(fp, encoding="utf-8") as f:
            rows = json.load(f)
        for r in rows:
            new_fil = norm_filiera(r)
            new_name, cvr = norm_denominazione(r)
            if cvr:
                dim = (r.get("dimensione") or "").strip() or "n.d."
                if "CVR" not in dim:
                    r["dimensione"] = f"{dim} · CVR {cvr}"
            if dry and (new_fil != r["filiera"] or new_name != r["denominazione"]):
                print(f"  {r['denominazione']}\n    nome    -> {new_name}\n    filiera -> {new_fil}")
            r["filiera"], r["denominazione"] = new_fil, new_name
        if not dry:
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(rows, f, ensure_ascii=False, indent=1)
        print(("[dry-run] " if dry else "normalizzato ") + os.path.basename(fp))


if __name__ == "__main__":
    main()
