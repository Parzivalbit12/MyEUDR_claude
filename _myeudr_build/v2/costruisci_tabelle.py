#!/usr/bin/env python3
"""Costruisce le tabelle di correzione v2 dai rilievi classificati AUTO/SPLIT.
Scarta tutto cio' che ha una riserva nella proposta O nel problema (va al PASSO 3)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "classificato.json"), encoding="utf-8"))

# riserva: nella proposta oppure nell'enunciato del problema
RISERVA = re.compile(r"DA CONFERMARE|da confermare|riconferm|in alternativa|da verificar|"
                     r"probabilment?e|presumib|forse|ipotes|non confermat|sembra", re.I)
PREF_N = re.compile(r"^referente\s*:\s*", re.I)
PREF_R = re.compile(r"^ruolo\s*:\s*", re.I)

# un valore di Ruolo deve contenere una parola-ruolo, altrimenti e' un nome finito
# nel campo sbagliato (es. BIOSERVICE Zach: proposta "Mag. DI (FH) Dr. Robert Zach")
PAROLE_RUOLO = re.compile(
    r"gesch.ftsf|direkt|\bvd\b|\bceo\b|\bcfo\b|\bcoo\b|directeur|bestuurder|zaakvoerder|"
    r"amministrat|president|titolare|toimitusjohtaja|manager|inhaber|eigenaar|bedrijfsleider|"
    r"styrelse|administrateur|g.rant|prokurist|fondat|propriet|deleg|socio|partner|"
    r"verantwoordelijk|owner|chairman|responsabile|legale rappresent|vertegenwoordig|"
    r"komplement|indehaver|verkst.llande", re.I)

def ruolo_valido(r):
    return bool(PAROLE_RUOLO.search(r or ""))

def pulisci_ruolo(r):
    r = PREF_R.sub("", r).strip()
    # una parentetica che contiene un recapito appartiene a un altro campo
    r = re.sub(r"\s*\([^()]*(?:@|https?://)[^()]*\)", "", r).strip()
    # il ruolo non deve trascinare e-mail o URL di altri campi
    parti = [p.strip() for p in r.split(";")]
    tenuti = [p for p in parti if not re.search(r"e-?mail|@|https?://", p, re.I)]
    return "; ".join(tenuti).strip() or parti[0]

gen, ref, riserva, scartati = [], [], [], []

for x in D:
    if x["_classe"] not in ("AUTO", "SPLIT"): continue
    testo = (x["correzione_proposta"] or "") + " || " + (x.get("problema") or "")
    if RISERVA.search(testo):
        riserva.append(x); continue
    base = dict(foglio=x["foglio"], denominazione=x["denominazione"],
                motivo=x["problema"], fonte=x["evidenza"], gravita=x["gravita"],
                origine=x["_file"])
    if x["_classe"] == "SPLIT":
        nome, ruolo = x["_valore"]
        nome = PREF_N.sub("", nome).strip().strip(",")
        ruolo = pulisci_ruolo(ruolo)
        # se il "nome" e' in realta' un titolo, la proposta riguarda il ruolo
        if nome and ruolo_valido(nome) and not ruolo:
            nome, ruolo = "", nome
        # se il "ruolo" non contiene una parola-ruolo non e' un ruolo: non lo scrivo
        if ruolo and not ruolo_valido(ruolo):
            if not nome:
                scartati.append(dict(base, campo=x["campo"], proposta=x["correzione_proposta"],
                                     perche="la proposta non contiene una parola-ruolo: non e' un ruolo"))
                continue
            ruolo = ""
        if not nome and not ruolo:
            scartati.append(dict(base, campo=x["campo"], proposta=x["correzione_proposta"],
                                 perche="proposta non scomponibile in nome/ruolo"))
            continue
        ref.append(dict(base, referente=nome, ruolo=ruolo))
    elif x["campo"] in ("referente", "ruolo"):
        v = x["_valore"]
        nome = PREF_N.sub("", v).strip() if x["campo"] == "referente" else ""
        ruolo = pulisci_ruolo(v) if x["campo"] == "ruolo" else ""
        if ruolo and not ruolo_valido(ruolo):
            scartati.append(dict(base, campo="ruolo", proposta=v,
                                 perche="la proposta non contiene una parola-ruolo: e' un nome di persona"))
            continue
        if nome and ruolo_valido(nome) and len(nome.split()) <= 2:
            scartati.append(dict(base, campo="referente", proposta=v,
                                 perche="la proposta e' un titolo, non un nome di persona"))
            continue
        ref.append(dict(base, referente=nome, ruolo=ruolo))
    else:
        gen.append(dict(base, campo=x["campo"], **{"da": x["_attuale"], "a": x["_valore"]}))

for nome, dati in (("correzioni_v2_generiche", gen), ("correzioni_v2_referenti", ref),
                   ("da_riverificare", riserva), ("scartati_v2", scartati)):
    json.dump(dati, open(os.path.join(HERE, nome + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{nome:28s} {len(dati):4d}")
