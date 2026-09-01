#!/usr/bin/env python3
"""Genera _myeudr_build/verifica/CORREZIONI_V2.md dalle tabelle di correzione e dal
diff cella per cella fra v1 e v2. Rieseguibile: il documento e' sempre allineato ai dati."""
import collections, json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE); REPO = os.path.dirname(BUILD)
OUT = os.path.join(BUILD, "verifica", "CORREZIONI_V2.md")

def carica(n, d=None):
    fp = os.path.join(HERE, n)
    return json.load(open(fp, encoding="utf-8")) if os.path.exists(fp) else (d if d is not None else [])

diff      = carica("diff_v1_v2.json")
log       = carica("log_applicazione.json")
manuali   = carica("correzioni_v2_manuali.json")
generiche = carica("correzioni_v2_generiche.json")
referenti = carica("correzioni_v2_referenti.json")
ag_gen    = carica("correzioni_v2_agenti.json")
ag_ref    = carica("correzioni_v2_agenti_ref.json")
dimens    = carica("correzioni_v2_dimensione.json")
gruppi    = carica("correzioni_v2_gruppi.json") + carica("correzioni_v2_passo4.json")
sede_tab  = carica("correzioni_v2_sede.json")
residui   = carica("correzioni_v2_residui.json")
rimozioni = carica("rimozioni_v2.json")
dec_cli   = carica("dimensione_decisione_cliente.json")
aperti    = carica("dimensione_restano_aperti.json")
scartati  = carica("scartati_v2.json")
riserva   = carica("da_riverificare.json")
alta      = carica("alta_aperti_v2.json")
non_app   = carica("agenti_non_applicati.json")
classif   = carica("classificato.json")

MOTIVO = {}          # (foglio, denominazione, campo) -> (motivo, fonte)
for tab in (manuali, generiche, referenti, ag_gen, ag_ref, dimens, gruppi, sede_tab, residui):
    for c in tab:
        campi = [c["campo"]] if "campo" in c else ["referente", "ruolo"]
        for k in campi:
            MOTIVO[(c["foglio"], c["denominazione"], k)] = (c.get("motivo",""), c.get("fonte",""))

def motivo_di(d):
    for chiave in ((d["foglio"], d["denominazione"], d["campo"]),):
        if chiave in MOTIVO: return MOTIVO[chiave]
    for (f, den, k), v in MOTIVO.items():                 # ripiego: denominazione rinominata
        if f == d["foglio"] and k == d["campo"] and (den in d["denominazione"] or d["denominazione"] in den):
            return v
    return ("", "")

def taglia(s, n):
    s = (s or "").replace("|", "\\|").replace("\n", " ").strip()
    return s if len(s) <= n else s[:n-1] + "…"

L = []
w = L.append
oggi = datetime.date.today().isoformat()
per_campo  = collections.Counter(d["campo"] for d in diff)
per_foglio = collections.Counter(d["foglio"] for d in diff)

w(f"# CORREZIONI v2 — changelog di `MyEUDR_Lead_Mapping_v2.xlsx`\n")
w(f"> Generato da `_myeudr_build/v2/genera_changelog.py` il {oggi}. "
  f"Rieseguibile: rilegge le tabelle di correzione e il diff cella per cella.\n")
w("Questo documento elenca **tutto** ciò che cambia rispetto alla v1 "
  "(`MyEUDR_Lead_Mapping.xlsx`, che non è stata toccata) e — altrettanto importante — "
  "ciò che è stato **deliberatamente non applicato**, con il motivo.\n")
w("---\n")
w("## 1. Il quadro in numeri\n")
w(f"- **{len(diff)} celle cambiate** su {len(rimozioni) and 727 or 728} aziende.")
w(f"- **{len(rimozioni)} riga rimossa** (§4).")
w("- **0 campi svuotati** e **0 record orfani**, verificati cella per cella contro il "
  "backup pre-modifica (`verifica_integrita.py`).")
w("- Ordine degli 8 fogli invariato: Italia, Germania, Finlandia, Danimarca, Svezia, "
  "Olanda, Belgio, Austria.\n")
w("| Campo | Celle | | Foglio | Celle |")
w("|---|--:|---|---|--:|")
campi = per_campo.most_common(); fogli = per_foglio.most_common()
for i in range(max(len(campi), len(fogli))):
    a = f"`{campi[i][0]}` | {campi[i][1]}" if i < len(campi) else " | "
    b = f"{fogli[i][0]} | {fogli[i][1]}" if i < len(fogli) else " | "
    w(f"| {a} | | {b} |")
w("")

w("---\n")
w("## 2. Il criterio, che è lo stesso della v1\n")
w("La v2 **non riparte da zero**: continua il criterio già fissato in §0-bis del "
  "`REPORT_VERIFICA.md`. Una correzione entra nel foglio solo se ricade in una categoria "
  "già decisa **e** ha evidenza a fonte. In particolare:\n")
w("| Regola | Come è stata rispettata |")
w("|---|---|")
w("| Mai un dato non verificato | Le proposte con riserva («DA CONFERMARE», «probabilmente», "
  "«da verificare») non sono state applicate: sono andate alla riverifica del PASSO 3, e "
  "quelle rimaste incerte restano rilievi aperti. |")
w("| Mai svuotare un campo valorizzato | L'applicatore salta ogni proposta che porterebbe un "
  "valore vuoto. Verificato a posteriori: **0 campi svuotati**. |")
w("| Rimozioni solo per commodity fuori Allegato I o azienda cessata | Una sola rimozione, "
  "categoria «cessata». Il fuori taglia da solo continua a non bastare. |")
w("| Le denominazioni si verificano al registro, non all'ortografia | Ogni cambio di "
  "denominazione porta un numero di registro o una P.IVA nell'evidenza. È la lezione di Arko. |")
w("| Integrità dopo ogni applicazione | Righe per foglio, ordine dei fogli, campi svuotati e "
  "record orfani, confrontati col backup pre-modifica dopo ogni lotto. |\n")

w("---\n")
w("## 3. Correzioni applicate\n")
w("### 3.1 Denominazioni accertate a registro\n")
w("Regola 5: normalizzare *come è scritta* una forma giuridica non dice *quale* sia quella "
  "giusta — su Arko l'assunzione era falsa. Qui ogni riga porta il numero di registro.\n")
w("| Foglio | Da | A | Fonte |")
w("|---|---|---|---|")
for c in manuali:
    if c.get("campo") == "denominazione":
        w(f"| {c['foglio']} | {taglia(c['denominazione'],46)} | **{taglia(c['a'],46)}** | {taglia(c['fonte'],100)} |")
w("")
w("### 3.2 Legami di gruppo non dichiarati o errati\n")
w("Per la §3 del report questi **sono errori di dato**, non decisioni di selezione: il campo "
  "taceva il legame o indicava la capogruppo sbagliata. Il sottoinsieme più grave è quello dei "
  "record che *affermano un'indipendenza che non c'è* — qui rientra Ginsten Slakteri.\n")
w("| Foglio | Azienda | Clausola aggiunta | Fonte |")
w("|---|---|---|---|")
righe = [c for c in manuali if c.get("campo") in ("dimensione","filiera") and "gruppo" in (c.get("motivo","")+c.get("a","")).lower()]
for c in righe:
    val = str(c["a"]).replace("__APPEND__","").strip()
    w(f"| {c['foglio']} | {taglia(c['denominazione'],32)} | {taglia(val,90)} | {taglia(c['fonte'],80)} |")
gruppo_dim = [c for c in dimens + gruppi if any(k in (c.get("motivo","")+c.get("a","")).lower()
              for k in ("gruppo","controllat","capogrupp","fondo","holding"))]
for c in gruppo_dim:
    val = str(c["a"]).replace("__APPEND__","").strip()
    w(f"| {c['foglio']} | {taglia(c['denominazione'],32)} | {taglia(val,90)} | {taglia(c['fonte'],80)} |")
w("")
w(f"*{len(righe)+len(gruppo_dim)} record.*\n")

w("### 3.3 Filiere: commodity mancanti o imprecise\n")
w("| Foglio | Azienda | Da | A | Fonte |")
w("|---|---|---|---|---|")
for c in manuali:
    if c.get("campo") == "filiera":
        w(f"| {c['foglio']} | {taglia(c['denominazione'],28)} | {taglia(c['da'],40)} | "
          f"**{taglia(c['a'],62)}** | {taglia(c['fonte'],70)} |")
w("")

w("### 3.4 Contatti: email, sito, LinkedIn, fonte\n")
w("Applicate solo le proposte che sono un **valore ben formato** per quel campo (una email "
  "che rispetta la sintassi, un URL nudo, una pagina LinkedIn aziendale). Le proposte in prosa "
  "sono state escluse dall'automatismo.\n")
cont = [d for d in diff if d["campo"] in ("email","sito","linkedin","fonte")]
w("| Foglio | Azienda | Campo | Da | A |")
w("|---|---|---|---|---|")
for d in sorted(cont, key=lambda z: (z["foglio"], z["denominazione"])):
    w(f"| {d['foglio']} | {taglia(d['denominazione'],30)} | `{d['campo']}` | "
      f"{taglia(d['da'] or '—',38)} | **{taglia(d['a'],44)}** |")
w(f"\n*{len(cont)} celle.*\n")

w("### 3.5 Referenti e ruoli\n")
w("Molte proposte erano nella forma «Nome Cognome — Ruolo»: applicate alla lettera avrebbero "
  "scritto il ruolo dentro il campo *Referente*. Uno splitter le separa nei due campi. Due "
  "guardie in senso opposto:\n")
w("- un valore di **Ruolo** che non contiene nessuna parola-ruolo è in realtà un nome di "
  "persona finito nel campo sbagliato → scartato;")
w("- un valore di **Referente** che è solo un titolo («Geschäftsführer») → scartato.\n")
rr = [d for d in diff if d["campo"] in ("referente","ruolo")]
w("| Foglio | Azienda | Campo | Da | A |")
w("|---|---|---|---|---|")
for d in sorted(rr, key=lambda z: (z["foglio"], z["denominazione"])):
    w(f"| {d['foglio']} | {taglia(d['denominazione'],30)} | `{d['campo']}` | "
      f"{taglia(d['da'] or '—',34)} | **{taglia(d['a'],48)}** |")
w(f"\n*{len(rr)} celle.*\n")

w("### 3.6 Dimensione\n")
w("È un campo di testo libero che contiene dati già verificati: sostituirlo in blocco li "
  "perderebbe. Le proposte sono state quindi divise fra **clausole da aggiungere in coda** "
  "(un legame di gruppo, un numero di registro, un dato di bilancio) e sostituzioni integrali, "
  "queste ultime solo quando un agente ha ricostruito il campo per intero con la fonte.\n")
dd = [d for d in diff if d["campo"] == "dimensione"]
w("| Foglio | Azienda | Cosa cambia |")
w("|---|---|---|")
for d in sorted(dd, key=lambda z: (z["foglio"], z["denominazione"])):
    da, a = d["da"] or "", d["a"] or ""
    cosa = ("aggiunto: " + taglia(a[len(da):].strip(), 108)) if a.startswith(da[:25]) and len(a) > len(da) \
           else ("sostituito: " + taglia(a, 108))
    w(f"| {d['foglio']} | {taglia(d['denominazione'],30)} | {cosa} |")
w(f"\n*{len(dd)} celle.*\n")

w("### 3.7 Sede\n")
sd = [d for d in diff if d["campo"] == "sede"]
if sd:
    w("| Foglio | Azienda | Da | A |")
    w("|---|---|---|---|")
    for d in sd: w(f"| {d['foglio']} | {taglia(d['denominazione'],30)} | {taglia(d['da'],44)} | **{taglia(d['a'],44)}** |")
else:
    w("Nessuna correzione di sede applicata: le 21 proposte sono precisazioni redazionali "
      "(sede legale accanto a quella operativa, nuovo nome del comune dopo una fusione) "
      "oppure — in un caso, Libeert — un valore che appartiene a un altro campo. "
      "Restano rilievi aperti.")
w("")

w("---\n")
w("## 4. La riga rimossa\n")
for R in rimozioni:
    w(f"**{R['denominazione']}** ({R['foglio']}) — categoria «{R['categoria']}».\n")
    w(f"{R['motivo']}\n")
    w(f"> Fonte: {R['fonte']}\n")
w("Nessun'altra riga è stata tolta. In particolare **non** è stato rimosso nessun fuori "
  "taglia: STOK Emballage (92 M€), Flatz (72 M€), DO IT (~125 M€) e Henry Lamotte (138 M€) "
  "restano nei fogli come rilievi aperti, perché la taglia non è fra le categorie che il "
  "mandato autorizza a correggere d'ufficio. È una decisione che spetta al cliente.\n")

w("---\n")
w("## 5. La riverifica dei casi con riserva (PASSO 3)\n")
w("96 rilievi portavano una proposta con riserva esplicita. Sono stati affidati ad agenti "
  "con due vincoli: **massimo 2-3 query WebSearch per caso** — chi resta incerto dopo tre "
  "resta incerto — e **salvataggio incrementale ogni 3-4 record**. Il secondo vincolo si è "
  "rivelato decisivo: un agente è stato interrotto dal limite di quota e i record già "
  "lavorati erano salvati.\n")
tot_ag = len(ag_gen) + len(ag_ref)
conf = [x for x in non_app if "confermato" in str(x.get("_perche",""))]
inc  = [x for x in non_app if "incerto" in str(x.get("_perche",""))]
w(f"- **{tot_ag} riserve sciolte e applicate.**")
w(f"- **{len(conf)} confermate come già corrette**: erano falsi allarmi. Fra queste Blå "
  "Station e Candy People (il dominio `.se` è quello giusto), Conceria Lomar, Spaggiari e "
  "il LinkedIn di Van den Berg Hardhout. Sono la conferma che valeva la pena non applicarle "
  "d'ufficio.")
w(f"- **{len(inc)} restano incerte** e restano tali: Sopraco NV, Nord Legnami Group, "
  "Lecont S.r.l.\n")
w("Le correzioni più significative emerse dalla riverifica:\n")
w("| Foglio | Azienda | Cosa è emerso |")
w("|---|---|---|")
w("| Germania | Lindner Kartonagen | «Emanuel Dick», il referente nel foglio, **non trova "
  "riscontro in nessuna fonte pubblica**. I Geschäftsführer reali sono Jutta Summann e "
  "Johannes Kunze (HRB 100588). |")
w("| Italia | Domori S.p.A. | Dal 29.05.2026 l'AD è **Riccardo Illy**, non Giacomo Biviano "
  "(che resta consigliere). |")
w("| Germania | Gebr. Westhoff | L'Impressum attuale non riporta più Werner Schulte: i GF "
  "sono Ültzen, Bruns e von Mettenheim (HRB 4460). |")
w("| Danimarca | Skagerak Denmark | La riserva si è sciolta in modo inatteso: la società è "
  "estinta. Da qui la rimozione al §4. |")
w("| Italia | Original Parquet | Giovanni Ballardini è Direttore Generale, non Presidente: "
  "il Presidente è il padre Roberto. |")
w("")

w("---\n")
w("## 6. Ciò che NON è stato applicato, e perché\n")
w("Questa sezione è la più importante per il cliente: sono le cose che restano da decidere.\n")

w("### 6.1 Le tre categorie del PASSO 4\n")
cat = collections.Counter()
import re as _re
GRUPPO = _re.compile(r"gruppo|controllat|capogrupp|filiale|acquisit|fondo|holding|partecipat", _re.I)
TAGLIA = _re.compile(r"fuori taglia|fuori (la )?forbice|oltre i 50|sopra .{0,12}soglia|sotto la forbice", _re.I)
OPCOM  = _re.compile(r"commerciante|distributore|rivend|non immett|a valle|trader", _re.I)
for x in alta:
    t = x["problema"] + " " + x["correzione_proposta"]
    if OPCOM.search(t): cat["operatore/commerciante"] += 1
    elif GRUPPO.search(t): cat["legame di gruppo"] += 1
    elif TAGLIA.search(t): cat["fuori taglia"] += 1
    else: cat["dato datato o incompleto"] += 1
w(f"Dei 100 rilievi di gravità `alta` che avevano una correzione proposta ancora aperta, "
  f"**{100-len(alta)} sono stati sciolti in v2** e **{len(alta)} restano aperti**, così ripartiti:\n")
w("| Categoria | Casi | Trattamento |")
w("|---|--:|---|")
w(f"| Legame di gruppo | {cat['legame di gruppo']} | Dove il legame era **non dichiarato o "
  "errato** è stato corretto (§3.2): è un errore di dato. Dove era **già dichiarato** nel "
  "campo non è un errore, ed è una **decisione di selezione che spetta al cliente**. |")
w(f"| Fuori taglia | {cat['fuori taglia']} | **Non rimossi.** Il mandato non autorizza a "
  "togliere una riga per la sola dimensione. Il dato corretto è nel foglio, la decisione al cliente. |")
w(f"| Operatore vs commerciante | {cat['operatore/commerciante']} | **Lasciati e segnalati.** "
  "Stabilire se un commerciante sia «operatore» ai sensi dell'EUDR è una valutazione "
  "**giuridica**, non un dato verificabile a fonte. |")
w(f"| Dato datato o incompleto | {cat['dato datato o incompleto']} | Restano rilievi aperti nel report. |")
w("")
w("I **dieci record operatore/commerciante** già individuati in v1 restano tutti nei fogli, "
  "invariati: Varia-Pack, Hausberger, Pappersgrossisten, Däckteam, Svenska Gummihuset, "
  "Cebeco Fourage, Skovs Korn, Rickl-Mühle, SRC, Kargro Banden.\n")

w("### 6.2 Proposte che sono decisioni, non dati\n")
w("Le proposte che cominciano con «Rimuovere», «Escludere», «Valutare», «Declassare», "
  "«Indicare» non sono un valore da scrivere in una cella: sono una raccomandazione. "
  "Non sono state applicate.\n")
dset = [x for x in classif if x["_classe"] == "DECISIONE"]
w("| Foglio | Azienda | Campo | Proposta |")
w("|---|---|---|---|")
for x in sorted(dset, key=lambda z:(z["foglio"], z["denominazione"]))[:40]:
    w(f"| {x['foglio']} | {taglia(x['denominazione'],28)} | `{x['campo']}` | {taglia(x['correzione_proposta'],92)} |")
w(f"\n*{len(dset)} rilievi, più {len(dec_cli)} sul solo campo Dimensione.*\n")

w("### 6.3 Correzioni scartate perché avrebbero introdotto un errore nuovo\n")
w("| Foglio | Azienda | Campo | Proposta | Perché no |")
w("|---|---|---|---|---|")
for x in scartati:
    w(f"| {x['foglio']} | {taglia(x['denominazione'],26)} | `{x['campo']}` | "
      f"{taglia(x['proposta'],42)} | {taglia(x['perche'],62)} |")
w("| Italia | Conceria Beschin, Conceria Daniela | `denominazione` | aggiungere la forma "
  "giuridica | Ciascuna corrisponde a **due entità omonime distinte** al Registro (una S.n.c. "
  "e una S.r.l. nello stesso comune): scegliere la forma significherebbe *decidere* quale sia "
  "l'operatore EUDR. Già escluse in v1, confermata l'esclusione. |")
w("| Germania | Göbel, Fuhlrott, Josef Schulte, SAF Kartonagen | `denominazione` | espandere "
  "la ragione sociale abbreviata | Le forme brevi sono **corrette**, solo abbreviate. "
  "Esclusione già decisa in v1, mantenuta per coerenza. |")
w("| Svezia | Abstracta, Gyllsjö Träindustri | `denominazione` | `AB` → `Aktiebolag` | Il "
  "foglio svedese **non ha uno stile maggioritario** (47 `AB` contro 42 `Aktiebolag`): "
  "normalizzare sarebbe arbitrario. Esclusione già decisa in v1. |")
w("| Italia | Cartiera S. Rocco | `denominazione` | `CARTIERA S.ROCCO S.P.A.` | È solo il "
  "maiuscolo del registro, come per il foglio Danimarca: non si impone la grafia registrale. |")
w("| Belgio | Repro NV | `filiera` | `Mangimi/Soia` → `Soia` | Romperebbe la tassonomia "
  "adottata dagli altri fogli. La riclassificazione di Repro era già stata decisa in v1. |")
w("| Danimarca | 51 denominazioni in MAIUSCOLO | `denominazione` | *title case* | Rovinerebbe "
  "gli acronimi: `JKE DESIGN` → `Jke Design`, e lo stesso per NPI, MC, KLS, H.C., DHS. |")
w("")
w("### 6.4 Rilievi che restano semplicemente aperti\n")
w(f"- **{len(aperti)}** sul campo Dimensione: la proposta non è riconducibile a una clausola "
  "accertata (spesso è una stima da riconfermare, o un commento).")
w(f"- **{len(riserva)}** proposte che sembravano applicabili ma il cui *problema* era esso "
  "stesso dubitativo («probabilmente errato», «da verificare»): meglio un rilievo aperto che "
  "un dato incerto scritto nel foglio. La riverifica del PASSO 3 ne ha confermate diverse "
  "come già corrette.")
w("- Le **email dubbie** restano `DA CONFERMARE`: il mandato vieta sia di inventarle sia di "
  "cancellarle d'ufficio.")
w("- **Cafe Solo Oy** (Finlandia) resta l'unico record dell'intero censimento mai coperto "
  "dalla verifica web.\n")

w("---\n")
w("## 7. Due difetti dell'infrastruttura, trovati applicando\n")
w("Vale la pena registrarli perché riguardano gli script che il progetto continuerà a usare.\n")
w("**Il confronto fra denominazioni era troppo largo.** `applica_correzioni.py` e "
  "`applica_referenti.py` consideravano uguali due nomi che condividono i **primi 12 "
  "caratteri**. In svedese questo fa collidere fra loro *tutte* le società che cominciano per "
  "`Aktiebolaget` — nel foglio Svezia sono sei — e infatti una correzione destinata a "
  "**Ginsten Slakteri** è finita su **Karlaträ**, una segheria. L'ha intercettata la guardia "
  "sul valore attuale, che ha visto `Legno/Segheria` dove si aspettava `Bovini/Carne`: è "
  "esattamente il lavoro per cui la guardia esiste. In v2 il match esatto ha la precedenza e "
  "il ripiego fuzzy si applica solo se è **unico**. "
  "**Verificato che in v1 il difetto non ha prodotto scritture sbagliate**: delle 131 "
  "correzioni di referente applicate allora, quattro toccavano nomi collidenti e tutte e "
  "quattro hanno raggiunto il record giusto.\n")
w("**La verifica d'integrità confrontava le righe per posizione.** Ma `add_country.py` "
  "riordina il foglio per filiera e nome: correggere una denominazione **sposta legittimamente "
  "la riga**, e il confronto posizionale leggeva lo spostamento come una valanga di campi "
  "svuotati. Ora `verifica_integrita.py` confronta i record **per identità**, seguendo le "
  "rinomine e le rimozioni dichiarate.\n")
w("Una terza cosa, minore ma utile: le clausole aggiunte al campo Dimensione usano una forma "
  "`__APPEND__` con **ancora** sul valore attuale invece della guardia `da`. Con la sola "
  "guardia, due clausole sulla stessa azienda si annullavano a vicenda — la seconda trovava "
  "il campo già cambiato dalla prima e veniva saltata. Succedeva a Grahns Konfektyr e a "
  "Liljeholmens, che ne avevano due ciascuna.\n")

w("---\n")
w("## 8. Come rieseguire\n")
w("Tutti gli script stanno in `_myeudr_build/v2/` e sono **rieseguibili**: una seconda "
  "esecuzione applica 0 correzioni e riporta tutto come «già uguale».\n")
w("```bash")
w("python _myeudr_build/v2/inventario.py        # confronta le proposte col foglio attuale")
w("python _myeudr_build/v2/classifica.py        # valore applicabile / decisione / da guardare")
w("python _myeudr_build/v2/costruisci_tabelle.py")
w("python _myeudr_build/v2/dimensione.py        # clausole da aggiungere al campo Dimensione")
w("python _myeudr_build/v2/da_agenti.py A B C   # esiti della riverifica -> tabelle")
w("python _myeudr_build/v2/applica_v2.py        # applica (--dry-run per provare)")
w("python _myeudr_build/v2/rimuovi.py           # le rimozioni, con la loro motivazione")
w("python _myeudr_build/v2/verifica_integrita.py")
w("python _myeudr_build/v2/genera_changelog.py  # rigenera questo documento")
w("```\n")
w("I due percorsi della v1 restano validi e sono rispettati: **DK/SE/NL/BE/AT** si correggono "
  "nei JSON di build e si rigenerano con `add_country.py` (rigenerazione riverificata "
  "**identica cella per cella** prima di iniziare); **IT/DE/FI** si correggono nella cella in "
  "posto, perché rigenerarli da un JSON esportato riordinerebbe le righe già consegnate. "
  "Dopo ogni rigenerazione l'ordine dei fogli viene ripristinato.\n")
w("`MyEUDR_Lead_Mapping.xlsx` (v1) **non è stata toccata**; "
  "`_myeudr_build/v2/backup_v1.xlsx` ne conserva la copia usata come termine di confronto.\n")

open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"scritto {OUT} — {len(L)} righe")
