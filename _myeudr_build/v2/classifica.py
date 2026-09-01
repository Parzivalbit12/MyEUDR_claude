#!/usr/bin/env python3
"""Classifica i rilievi aperti in: AUTO (valore applicabile), SPLIT (referente compound),
DECISIONE (proposta = scelta del cliente, non un dato), REVIEW (da guardare a mano)."""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
INV  = json.load(open(os.path.join(HERE,"inventario.json"), encoding="utf-8"))

# la proposta non e' un valore ma una decisione di selezione/perimetro
DECISIONE = re.compile(
    r"^(rimuover|escluder|valutare|declassar|mantenere|segnalare|indicare|considerar|"
    r"spostare|sostituire il lead|verificare|confermare|contattare|riclassificar)", re.I)
DECISIONE_IN = re.compile(
    r"rimuovere il record|escludere o |escludere il lead|declassare il lead|"
    r"valutare (il lead|come lead)|non e' un lead|spetta al cliente", re.I)

EMAIL  = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
URL    = re.compile(r"^https?://[^\s<>()\[\]\"']+$")
LINKED = re.compile(r"^https?://([a-z]{2}\.)?linkedin\.com/[^\s<>()\[\]\"']+$", re.I)
# "Nome Cognome — Ruolo", "Nome Cognome - Ruolo", "Nome Cognome, Ruolo"
SPLITRE = re.compile(r"^(?P<nome>.{3,60}?)\s*(?:[—–]|\s-\s|,)\s*(?P<ruolo>.{2,160})$")
PREFISSO = re.compile(r"^(ruolo|referente)\s*:\s*", re.I)

def classify(x):
    camp = x["campo"]; p = x["correzione_proposta"].strip()
    if DECISIONE.match(p) or DECISIONE_IN.search(p):
        return "DECISIONE", None
    if camp == "email":
        return ("AUTO", p) if EMAIL.match(p) else ("REVIEW", None)
    if camp in ("sito", "fonte"):
        return ("AUTO", p) if URL.match(p) else ("REVIEW", None)
    if camp == "linkedin":
        return ("AUTO", p) if LINKED.match(p) else ("REVIEW", None)
    if camp in ("referente", "ruolo"):
        m = SPLITRE.match(PREFISSO.sub("", p))
        if m:
            return "SPLIT", (m.group("nome").strip(), m.group("ruolo").strip())
        p2 = PREFISSO.sub("", p)
        if len(p2) <= 90:
            return "SPLIT", ((p2, "") if camp == "referente" else ("", p2))
        return "REVIEW", None
    return "REVIEW", None            # dimensione, filiera, denominazione, sede: sempre a mano

def main():
    out = []
    for x in INV:
        if x["_stato"] != "aperta": continue
        k, v = classify(x)
        out.append(dict(x, _classe=k, _valore=v))
    json.dump(out, open(os.path.join(HERE,"classificato.json"),"w",encoding="utf-8"),
              ensure_ascii=False, indent=1)
    c = collections.Counter((y["_classe"], y["campo"]) for y in out)
    tot = collections.Counter(y["_classe"] for y in out)
    for k in ("AUTO","SPLIT","DECISIONE","REVIEW"):
        print(f"\n### {k}  ({tot[k]})")
        for (kk,camp),n in sorted(c.items()):
            if kk==k: print(f"   {camp:14s} {n:4d}")

if __name__=="__main__": main()
