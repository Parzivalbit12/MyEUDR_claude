#!/usr/bin/env python3
"""Classifica i rilievi aperti sul campo Dimensione.

Il campo e' testo libero, quindi la correzione sicura non e' sostituirlo (si perderebbero
dati gia' verificati) ma AGGIUNGERE in coda la clausola mancante. Vengono trattate come
applicabili solo le proposte che sono una clausola aggiuntiva accertata — tipicamente un
legame di gruppo non dichiarato (§3: e' un errore di dato) o un numero di registro.

Restano al cliente, come rilievo aperto: i fuori taglia, le stime da riconfermare e le
proposte che sono istruzioni ("indicare l'anno") invece che dati.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
D = [x for x in json.load(open(os.path.join(HERE,"classificato.json"), encoding="utf-8"))
     if x["_classe"] == "REVIEW" and x["campo"] == "dimensione"]

AGGIUNGI  = re.compile(r"^\s*aggiunge?re\s*(?:in|al|nel)?\s*(?:campo\s*)?(?:dimensione\s*)?[:,]?\s*", re.I)
GRUPPO    = re.compile(r"^\s*(controllata|filiale|capogruppo|legame di gruppo|assetto propriet|"
                       r"societ[àa'] del gruppo|partecipata|acquisita|fa parte del gruppo|"
                       r"n\.? ?impresa|org\.?nr|cvr |fn |hrb |p\.?iva)", re.I)
# proposte che sono istruzioni, non dati
ISTRUZIONE = re.compile(r"^\s*(indicare|specificare|precisare|aggiornare il campo|va indicat|"
                        r"segnalare|valutare|verificare|confermare|sostituire il dato|"
                        r"escludere|rimuovere|declassare)", re.I)
TAGLIA     = re.compile(r"fuori (la )?forbice|fuori taglia|sopra (il tetto|la soglia)|"
                        r"sotto la forbice|sotto il minimo|oltre i 50", re.I)

# clausole rivolte al compilatore, non al lettore: non vanno scritte nel foglio
CLAUSOLA_ISTRUZIONE = re.compile(
    r"^\s*(indicare|specificare|precisare|va indicat|da consultare|da reperire|"
    r"sostituirlo|sostituire il dato|aggiornare|da confermare|DA CONFERMARE|"
    r"resta da|verificare|confermare)", re.I)

def pulisci(p):
    p = AGGIUNGI.sub("", p).strip().strip("«»\"' ").strip()
    parti = [q.strip() for q in re.split(r";|(?<=\.)\s+(?=[A-Z])", p) if q.strip()]
    tenute = [q for q in parti if not CLAUSOLA_ISTRUZIONE.match(q)]
    out = "; ".join(tenute).strip().strip(";").strip()
    out = out.strip("«»\"'` ").strip()          # virgolette residue della proposta
    return (out[:1].upper() + out[1:]) if out else out

app, decisione, aperti = [], [], []
for x in D:
    p = x["correzione_proposta"].strip()
    if ISTRUZIONE.match(p):
        decisione.append(dict(x, _perche="la proposta e' un'istruzione, non un dato")); continue
    if TAGLIA.search(p):
        decisione.append(dict(x, _perche="fuori taglia: decisione del cliente, il mandato non "
                                         "autorizza a rimuovere per sola dimensione")); continue
    if AGGIUNGI.match(p) or GRUPPO.match(p):
        clau = pulisci(p)
        cur  = (x["_attuale"] or "").strip()
        if not clau: 
            aperti.append(dict(x, _perche="clausola vuota dopo la pulizia")); continue
        if clau.lower() in cur.lower():
            aperti.append(dict(x, _perche="clausola gia' presente nel campo")); continue
        if not clau.endswith("."): clau += "."
        # forma __APPEND__ + ancora: cosi' due clausole sulla stessa azienda si sommano
        # invece di annullarsi a vicenda sulla guardia "da" (che dopo la prima e' stale)
        app.append(dict(foglio=x["foglio"], denominazione=x["denominazione"], campo="dimensione",
                        a="__APPEND__ " + clau, ancora=cur[:28],
                        motivo=x["problema"], fonte=x["evidenza"],
                        gravita=x["gravita"], origine=x["_file"]))
    else:
        aperti.append(dict(x, _perche="proposta non riconducibile a una clausola aggiuntiva "
                                      "accertata: resta rilievo aperto"))

for n, v in (("correzioni_v2_dimensione", app), ("dimensione_decisione_cliente", decisione),
             ("dimensione_restano_aperti", aperti)):
    json.dump(v, open(os.path.join(HERE, n + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{n:34s} {len(v):4d}")
