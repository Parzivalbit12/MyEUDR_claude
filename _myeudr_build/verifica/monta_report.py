#!/usr/bin/env python3
"""Monta REPORT_VERIFICA.md: intestazione + sintesi Fase A + correzioni applicate + corpo Fase B."""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(HERE, "genera_report.py")], check=True)
corpo = open(os.path.join(HERE, "_corpo_report.md"), encoding="utf-8").read()

# --- sintesi Fase A dal report automatico ---
auto = open(os.path.join(HERE, "00_controlli_automatici.md"), encoding="utf-8").read()
riepilogo = re.search(r"## Riepilogo rilievi\n(.*?)\n\*\*Totale", auto, re.S)
tab_A = riepilogo.group(1).strip() if riepilogo else ""
tot_A = re.search(r"\*\*Totale rilievi automatici: (\d+)\*\*", auto)

# --- correzioni applicate ---
corr = []
for fp in sorted(glob.glob(os.path.join(HERE, "correzioni_*.json"))):
    corr += json.load(open(fp, encoding="utf-8"))

def esc(s): return str(s or "").replace("|", "\\|").replace("\n", " ").strip()

h = []
h.append("# REPORT DI VERIFICA — MyEUDR Lead Mapping\n")
h.append("> Controllo qualità **record per record** del censimento lead (**742 aziende, 8 fogli**), "
         "alla ricerca di refusi, attribuzioni errate e ogni altro errore introdotto durante la "
         "raccolta. Non è una ricerca di nuove aziende.\n")
h.append("\n## Come leggere questo report\n")
h.append("La verifica si è svolta in due fasi, con budget e coperture diverse:\n")
h.append("| Fase | Metodo | Copertura |")
h.append("|---|---|---|")
h.append("| **A — controlli deterministici** | 26 controlli automatici offline su tutti i JSON di "
         "build e sul workbook | **100%** dei 742 record |")
h.append("| **B — riscontro sul web** | agenti di verifica, blocchi di 15-20 aziende, 2-3 ricerche "
         "per record, ogni rilievo con URL o citazione | vedi §1 |")
h.append("\nDocumenti di dettaglio:\n")
h.append("- [`00_controlli_automatici.md`](00_controlli_automatici.md) — esito completo della Fase A")
h.append("- [`01_analisi_dimensione.md`](01_analisi_dimensione.md) — analisi del campo `Dimensione` "
         "(tipo di dato dichiarato, anno, obsolescenza)")
h.append("- `<foglio>_<blocco>.json` — rilievi grezzi di ciascun agente")
h.append("- `00_punti_noti.json` — verifica dei 13 punti lasciati aperti dalla raccolta\n")

h.append("\n## Vincolo d'ambiente che ha condizionato la verifica\n")
h.append("Il proxy di egress **nega per policy** (403 al CONNECT) tutti i domini esterni: registri "
         "societari e siti aziendali non sono raggiungibili né con WebFetch né con curl. "
         "**L'unico canale disponibile è WebSearch**, i cui frammenti contengono spesso — ma non "
         "sempre — il dato cercato. Di qui una regola applicata da tutti gli agenti: quando dopo "
         "2-3 ricerche il dato non emerge, il rilievo è marcato `DA CONFERMARE` e il campo "
         "**non viene toccato**. Un rilievo aperto è preferibile a una correzione inventata.\n")

h.append("\n---\n")
h.append("\n## 0. Esito della Fase A — controlli deterministici\n")
h.append("Il censimento è risultato **pulito su tutti i controlli di integrità**: nessun duplicato "
         "(né fra fogli né fra i JSON di build), nessuna entità HTML residua, nessun URL LinkedIn "
         "o sito malformato, nessuna email sintatticamente errata, nessun numero di registro "
         "rimasto nelle denominazioni, nessun campo `Fonte` vuoto o non-URL, e **nessuna divergenza "
         "fra i JSON di build e i fogli Excel** — segno che la pipeline `add_country.py` è "
         "rimasta coerente.\n")
h.append("I rilievi si concentrano invece su qualità e coerenza redazionale:\n")
h.append("> La tabella riflette lo stato **dopo** le correzioni applicate (§0-bis): per questo il "
         "controllo 6 sulla tassonomia è ora a zero, mentre prima dell'intervento segnalava "
         "**23 valori fuori elenco**.\n")
h.append(tab_A + "\n")
if tot_A:
    h.append(f"\n**Totale rilievi automatici: {tot_A.group(1)}.**\n")
h.append("\n> **Nota sul controllo 2 (email dedotte).** Il controllo grezzo segnalava 86 email con "
         "dominio diverso dal sito. Separando i casi innocui — stesso nome con TLD diverso "
         "(`azienda.de` vs `azienda.com`) e caselle freemail/PEC, entrambi legittimi — restano "
         "**24 casi con stem realmente diverso**, che sono quelli da confermare a fonte.\n")

if corr:
    h.append("\n---\n")
    h.append(f"\n## 0-bis. Correzioni già applicate al workbook ({len(corr)})\n")
    h.append("Applicate **solo le correzioni certe**, secondo il mandato: refusi formali, entità "
             "HTML, forme giuridiche, filiere fuori Allegato I, aziende cessate. Tutto il resto "
             "resta come rilievo aperto in questo report.\n")
    h.append("Ogni correzione di campo è stata applicata con un **controllo di guardia**: lo script verifica "
             "che il valore attuale del campo coincida esattamente con quello atteso, altrimenti "
             "salta la correzione, così lo script è rieseguibile senza rischi. Dopo l'applicazione le "
             "righe sono **740** (due rimozioni motivate, vedi sotto) e l'ordine dei fogli è "
             "ripristinato (Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria).\n")
    rim  = [c for c in corr if c["a"] is None]
    perf = [c for c in corr if c["a"] is not None and c["campo"] == "filiera"]
    altre = [c for c in corr if c["a"] is not None and c["campo"] != "filiera"]
    if rim:
        h.append(f"\n### Record rimossi dal censimento ({len(rim)})\n")
        h.append("Sono le uniche righe **tolte** dai fogli. Entrambe rientrano in una categoria che "
                 "il mandato autorizza a correggere, e in entrambi i casi il progetto aveva già "
                 "applicato lo stesso criterio a un caso analogo.\n")
        for c in rim:
            h.append(f"**{esc(c['denominazione'])}** — foglio {esc(c['foglio'])}  ")
            h.append(f"{esc(c['motivo'])}\n")
        h.append("Il totale del censimento passa quindi da **742 a 740 aziende** "
                 "(Belgio 95→94, Olanda 100→99).\n")
    h.append(f"\n### Tassonomia `Filiera` ({len(perf)})\n")
    h.append("Il foglio **Finlandia** conteneva varianti storiche della tassonomia "
             "(`Legno/Compensato-Prodotti`, `Legno/Segheria-Piallatura`, `Legno/CLT`, "
             "`Legno/Commercio-export sahatavara`, `Legno/Piallatura`) mai allineate agli altri "
             "fogli. La riconduzione **non è arbitraria**: gli altri sette fogli sono unanimi nel "
             "classificare compensato, impiallacciature, finestre/porte, parquet, glulam e CLT "
             "sotto `Legno/Arredo — <dettaglio>`, e segheria/piallatura sotto `Legno/Segheria`.\n")
    h.append("| Foglio | Azienda | Da | A |")
    h.append("|---|---|---|---|")
    for c in perf:
        h.append(f"| {esc(c['foglio'])} | {esc(c['denominazione'])[:38]} | {esc(c['da'])[:52]} | {esc(c['a'])[:52]} |")
    if altre:
        h.append(f"\n### Refusi formali ({len(altre)})\n")
        h.append("| Foglio | Azienda | Campo | Correzione | Motivo |")
        h.append("|---|---|---|---|---|")
        for c in altre:
            da, a = esc(c["da"]), esc(c["a"])
            if len(da) > 70:   # mostra solo il frammento che cambia
                import difflib
                sm = difflib.SequenceMatcher(None, da, a)
                fr = [(da[i1:i2], a[j1:j2]) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag != "equal"]
                testo = " · ".join(f"«{x[:45]}» → «{y[:45]}»" for x, y in fr) or "(riscrittura)"
            else:
                testo = f"«{da}» → «{a}»"
            h.append(f"| {esc(c['foglio'])} | {esc(c['denominazione'])[:32]} | {esc(c['campo'])} | "
                     f"{testo[:170]} | {esc(c['motivo'])[:110]} |")

h.append("\n### Correzioni deliberatamente NON applicate\n")
h.append("Tre categorie di rilievi formali sono state lasciate aperte nel report invece che "
         "corrette nei fogli. Il motivo è sempre lo stesso: la correzione automatica avrebbe "
         "introdotto un errore nuovo.\n")
h.append("| Rilievo | Record | Perché non è stata applicata |")
h.append("|---|--:|---|")
h.append("| **Maiuscolo integrale nel foglio Danimarca** (controllo 9d) | 52 | Il foglio mescola "
         "51 denominazioni in MAIUSCOLO (stile del registro CVR) e 38 in forma normale. "
         "Un *title case* automatico però **rovinerebbe gli acronimi**: `JKE DESIGN` diventerebbe "
         "`Jke Design`, e lo stesso vale per NPI, MC, KLS, H.C., DHS. Servirebbe una decisione "
         "caso per caso, che non è una correzione certa. |")
h.append("| **Conceria Beschin** e **Conceria Daniela** (foglio Italia) | 2 | Ciascuna corrisponde "
         "a **due entità distinte e omonime** al Registro Imprese, nello stesso comune (una S.n.c. "
         "e una S.r.l.). Aggiungere una forma giuridica significherebbe **scegliere** quale sia "
         "l'operatore EUDR: va accertato prima del contatto. |")
h.append("| **Email da confermare** | 24+ | Le email con dominio diverso dal sito, e quelle non "
         "ritrovate letteralmente in una fonte pubblica, restano **`DA CONFERMARE`**. Il mandato "
         "vieta sia di inventarle sia di cancellarle d'ufficio: il campo non è stato toccato. |")

h.append("\n---\n")
# il corpo comincia col proprio titolo H1: lo tolgo e tengo dalla sezione 1
corpo_body = corpo.split("\n## 1. Copertura della verifica\n", 1)
corpo_finale = "\n## 1. Copertura della verifica\n" + corpo_body[1] if len(corpo_body) > 1 else corpo
h.append("\n# Fase B — verifica sul web, record per record\n")

out = "\n".join(h) + "\n" + corpo_finale
op = os.path.join(HERE, "REPORT_VERIFICA.md")
open(op, "w", encoding="utf-8").write(out)
print(f"scritto {op} — {len(out)} byte, {out.count(chr(10))} righe")
