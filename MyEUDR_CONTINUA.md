# MyEUDR — Prompt di continuazione (handoff)

> **Come usarlo:** apri una nuova sessione di Claude Code nella cartella
> `C:\Users\39333\Desktop\EDUR da Studio` (dopo il reset del limite, ore 13:30 Europe/Rome)
> e incolla come primo messaggio: **"Leggi `MyEUDR_CONTINUA.md` e continua il lavoro da dove
> si è interrotto: completa la Danimarca, poi procedi un paese alla volta."**
> La memoria di progetto (`.claude/.../memory/myeudr-lead-mapping.md`) si carica da sola.

---

## 1. Contesto

Mappatura di **potenziali lead per il prodotto MyEUDR** (software di compliance all'EU
Deforestation Regulation). Cliente: utente a **binp.it**. Obiettivo: per ogni nazione,
**~100 aziende reali** soggette all'EUDR e **contattabili**, di taglia PMI.

**Filiere EUDR:** legno/carta/mobili/imballaggi, caffè, cacao, gomma, soia, olio di palma,
bovini/pelle (e derivati). Copertura ampia **adattata ai punti di forza industriali di ogni paese**.

## 2. Decisioni confermate dal cliente (NON ridiscutere)

- **Taglia target:** fatturato ~**10–20 M€** (sweet spot), tolleranza ~**5–40 M€**.
  ESCLUDERE grandi corporation/multinazionali (>~50 M€).
- **Campo "Contatto"** = referente (nome+ruolo) + LinkedIn + email/PEC aziendale.
  **MAI inventare** email, nomi o URL LinkedIn. Non trovato → `"n.d."` (email/dimensione) o `""` (referente/ruolo/linkedin).
- **Layout Excel esteso a 10 colonne** (confermato dal cliente), un **foglio per nazione**.
- **Un paese alla volta** (più risorse per nazione). ⚠️ **AGGIORNAMENTO cliente (16/08/2026):**
  non serve più chiedere il via libera tra un paese e l'altro — **procedere in automatico**
  fino a completare tutti e 8 i paesi.
- **8 paesi totali:** Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria
  (la Germania è stata **aggiunta** ai 7 iniziali).

## 3. Stato attuale

| Paese | Stato | Aziende |
|---|---|---:|
| Italia | ✅ CONSEGNATO (foglio nel workbook) | 95 |
| Germania | ✅ CONSEGNATO | 97 |
| Finlandia | ✅ CONSEGNATO | 84 |
| **Danimarca** | ✅ CONSEGNATO (residui minori in §11) | 89 |
| **Svezia** | ✅ CONSEGNATO (email 80/89 · §12) | 89 |
| **Olanda** | ✅ CONSEGNATO (email 77/100 · §13) | 100 |
| **Belgio** | ✅ CONSEGNATO (email 73/95 · §14) | 95 |
| **Austria** | ✅ CONSEGNATO (email 90/93, referente 92/93 · §15) | 93 |

**Deliverable finale:** `MyEUDR_Lead_Mapping.xlsx` — **8 fogli, 742 righe**, tutti e 8 i paesi
consegnati. Verifica globale: 0 entità HTML residue, 0 email malformate, 0 URL LinkedIn non validi.
Copertura complessiva: **email 626/742, referente 543/742, LinkedIn 297/742**.
⚠️ `add_country.py` ricrea il foglio in fondo al workbook: dopo un rebuild **ripristinare l'ordine
dei paesi** (Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria) con
`wb._sheets=[wb[n] for n in ordine]`.
Contiene Italia+Germania+Finlandia+Danimarca+Svezia+Olanda+Belgio+Austria. (Esiste anche `MyEUDR_Lead_Mapping_ITALIA_pilota.xlsx`, vecchio, **eliminabile**.)

## 4. File e infrastruttura

- `MyEUDR_Lead_Mapping.xlsx` — il workbook finale (IT/DE/FI già dentro). **Non ricostruirlo da zero: aggiungi i nuovi fogli.**
- `_myeudr_build/add_country.py` — script che **merge+aggiunge/sostituisce un foglio-paese** al workbook, lasciando intatti gli altri. Colori/formattazione identici agli altri fogli.
- ⚠️ Lo **scratchpad di sessione si azzera** a ogni sessione: lavora nella cartella persistente `_myeudr_build/` (mettici lì i JSON dei ricercatori).

## 5. Metodo (pipeline collaudata) — da ripetere per ogni paese

1. **6 ricercatori in parallelo** (Agent tool, `subagent_type: general-purpose`), uno per cluster di filiere, **pesati sui punti di forza del paese**. Lanciarli **tutti in un unico messaggio** (girano in background, notificano al termine).
2. Ogni ricercatore restituisce **SOLO un array JSON** con esattamente queste chiavi:
   `denominazione, filiera, sede, sito, email, referente, ruolo, linkedin, dimensione, fonte`.
3. Salva ogni risposta in `_myeudr_build/<prefix>_NN_nome.json` (prefissi: **dk** Danimarca, **se** Svezia, **nl** Olanda, **be** Belgio, **at** Austria). ⚠️ Decodifica/normalizza è automatica nello script (gestisce `&amp;`, `&gt;`).
4. Aggiungi il foglio al workbook:
   ```bash
   cd "C:/Users/39333/Desktop/EDUR da Studio/_myeudr_build"
   python add_country.py dk Danimarca "C:/Users/39333/Desktop/EDUR da Studio/MyEUDR_Lead_Mapping.xlsx"
   ```
   (rieseguibile: sostituisce il foglio se già presente; deduplica i doppioni cross-file).
5. Verifica (fogli, righe, 0 entità HTML residue) e consegna al cliente con un breve riepilogo:
   ripartizione per filiera + copertura contatti (email X/N, referente Y/N) + note di trasparenza
   (aziende "di confine" sopra soglia, legami di gruppo, taglie sotto i 5M dove il mercato lo impone).
6. Poi **passa direttamente al paese successivo** senza chiedere conferma (decisione cliente del
   16/08/2026; prima invece voleva approvare un paese alla volta).

### Template prompt per ogni ricercatore (riempi le [ ])

```
Sei un analista di lead generation B2B. Devo mappare PMI [PAESE] della filiera [FILIERE]
soggette all'EUDR e buoni lead per un software di compliance EUDR "MyEUDR". [motiva perché la filiera è EUDR].
TARGET: fatturato ~10–20 M€ (tollerabile 5–40 M€); ESCLUDI >~50 M€ e multinazionali ([nomina i big del paese da escludere]).
FONTI: [associazioni di categoria del paese] + directory [registri/DB del paese] + siti aziendali.
Per il referente usa [fonte CEO del paese: es. Impressum (DE/AT), Proff/registro (Nordics/DK), KVK (NL), NBB (BE)].
OBIETTIVO: ~16-18 aziende reali ed esistenti.
Per OGNI azienda: denominazione, filiera, sede (città+regione), sito (URL reale),
email (dal sito; se assente "n.d."; MAI inventarla), referente (nome+cognome del decisore SOLO se pubblicato; altrimenti ""),
ruolo, linkedin (URL reale trovato o ""; MAI costruito), dimensione (fatturato+dipendenti con fonte; valuta €),
fonte (URL).
REGOLE ANTI-INVENZIONE: nessuna azienda/email/nome/URL inventati; nel dubbio vuoto/"n.d."; sempre una fonte. Accuratezza > quantità.
OUTPUT: SOLO un array JSON (niente testo/markdown attorno) con ESATTAMENTE le chiavi:
denominazione, filiera, sede, sito, email, referente, ruolo, linkedin, dimensione, fonte.
```

## 6. DANIMARCA — piano (prossimo passo immediato)

Valuta i fatturati: **DKK ~7,46 kr/€** (10–20 M€ ≈ 75–150 M DKK). Referente = *adm. direktør/direktør* da **proff.dk**, **datacvr.virk.dk (CVR)**, **biq.dk**, siti aziendali.

**6 filoni (pesi danesi):**
1. **Mobili (møbler)** — forte industria del design; cluster Jutland (Salling/Skive/Herning/Ikast-Brande). ~18. Escludi Carl Hansen & Søn, Fritz Hansen, HAY (MillerKnoll), BoConcept.
2. **Legno/import (træ, tømmer, trægulve)** — importatori/commercio legname (Dansk Træforening), parquet, limtræ, porte/finestre. ~16. Escludi STARK, XL-BYG, Bygma.
3. **Carta/packaging (emballage, bølgepap, karton, tryk)** — ondulato, astucci, etichette, stampa. ~16.
4. **Caffè + cacao/cioccolato** — torrefazioni + import caffè verde; chokolade + import cacao. ~16.
5. **Mangimi/soia (foderstof, soja)** — **filiera forte** (colosso suinicolo → import soia). ~15. Escludi DLG, Danish Agro, Vestjyllands Andel.
6. **Gomma + carne bovina + pelle + palma** (gummi/oksekød/huder-garveri/palmeolie). ~14. Escludi Danish Crown, Tican, AAK.

**Leads parziali già emersi prima dell'interruzione (verificare e completare, NON dare per buoni senza fonte):**
- *Caffè:* The Coffee Collective (~11 M€), La Cabra (~20 M€), Stillers Coffee (piccola).
- *Packaging:* escludere DS Smith, Smurfit Westrock, Schur Pack, VPK, August Faller (grandi); indipendenti mid: **All Creative**, **Boxen**, **H. Emballage**.
- *Mangimi:* **CR Foderservice**, **Nordvest Foder**, **A-One** (verificare). ⚠️ `nutrimin.com` è canadese — usare il dominio danese corretto.
- *Legno:* **Sommer-Savex** (email `info@sommer-savex.dk`, CEO **Line Hjort**, ~14 dip.).

**Grandi da escludere (già confermati):** DS Smith (627 dip.), Smurfit Westrock (589), Schur Pack (212), VPK (110), August Faller (92).

## 7. Guida pesi per gli altri paesi

- **Svezia (se):** enorme su **legno/segherie/carta-cellulosa** (come Finlandia) + **caffè** (alto consumo, torrefazioni) + mobili + packaging. Valuta **SEK ~11,3 kr/€**. Referente = *VD (verkställande direktör)*. Fonti: allabolag.se, proff.se, ratsit.se. Escludi i giganti forestali (SCA, Holmen, Stora Enso, IKEA-suppliers troppo grandi).
- **Olanda (nl):** **HUB di import** → **caffè** (grande), **cacao** (Amsterdam/Zaandam, hub mondiale), **soia** (Rotterdam), **olio di palma**, **legname tropicale**; carta/packaging; trading+trasformazione. EUR. Referente = *directeur*. Fonti: **KVK** (Kamer van Koophandel), company.info, drimble.
- **Belgio (be):** **Anversa** = hub **cacao/caffè/legname**; **cioccolato** (mid-sized chocolatiers); carta/packaging; legno; gomma. EUR. Referente = *gedelegeerd bestuurder/zaakvoerder* (NL) o *administrateur délégué* (FR). Fonti: **NBB/BNB** (bilanci depositati gratis → ottimi per fatturato), KBO/BCE, trendstop.
- **Austria (at):** forte su **legno/segherie/mobili/carta** (come DE/FI) + **caffè** (tradizione viennese). EUR. Referente = **Geschäftsführer** — **obbligo di Impressum** sui siti (come Germania → ottima copertura referenti!). Fonti: firmenabc.at, herold.at, compass.at, firmenbuch/WKO.

## 8. Regole ferree & note di qualità

- **Anti-invenzione assoluta.** Ogni azienda reale ed esistente; email/nomi/LinkedIn solo da fonte realmente vista; altrimenti `"n.d."`/`""`. Sempre una `fonte` (URL).
- **Caffè in paesi Nordici**: spesso micro-torrefazioni sotto il target — includere solo le più sostanziose + gli **importatori di caffè verde** (molto rilevanti EUDR), segnalando la taglia. In FI ne sono state curate 9 su 17.
- **Segnalare sempre** nel campo *Dimensione*: aziende sopra ~50 M€ ma indipendenti, taglie sotto i 5 M€ tenute per copertura, e i **legami di gruppo** (es. controllata di X).
- **Copertura contatti tipica:** IT referente 11/95 (fonti pubbliche scarse); DE 96/97 e FI 77/84 (Impressum/registri con CEO). AT sarà alta (Impressum); SE/DK/NL/BE medie (registri con direttore).
- **Deduplica**: `add_country.py` normalizza i nomi ignorando le parentesi (già gestiti i doppioni tipo "X" vs "X (Y)").

## 9. Come rigenerare/riparare

- **Aggiungere un paese:** metti i `<prefix>_NN.json` in `_myeudr_build/` e lancia `add_country.py` (vedi §5.4).
- **Recuperare i dati IT/DE/FI in JSON** (se mai servisse) leggendo il workbook:
  ```python
  from openpyxl import load_workbook
  wb = load_workbook(r"C:/Users/39333/Desktop/EDUR da Studio/MyEUDR_Lead_Mapping.xlsx")
  keys=["denominazione","filiera","dimensione","referente","ruolo","linkedin","email","sito","sede","fonte"]
  for sn in wb.sheetnames:
      ws=wb[sn]; rows=[]
      for r in ws.iter_rows(min_row=3, values_only=True):
          if r and r[0]: rows.append(dict(zip(keys, r)))
      import json; open(f"{sn.lower()}_recovered.json","w",encoding="utf-8").write(json.dumps(rows,ensure_ascii=False,indent=1))
  ```
  (l'ordine colonne del foglio è: Denominazione, Filiera, Dimensione, Referente, Ruolo, LinkedIn, Email, Sito, Sede, Fonte).

## 10. Task list (stato)

Completati: Italia, Germania, Finlandia, **Danimarca** (ricerca + arricchimento + foglio nel workbook).
In corso: **Svezia** (foglio consegnato, rifinitura in §12). Da fare: Olanda, Belgio, Austria, poi rifinitura workbook finale a 8 fogli.

---

## 11. Ambiente "Claude Code on the web" — vincoli scoperti (IMPORTANTE)

Il lavoro sulla Danimarca è stato svolto nel repository GitHub `Parzivalbit12/MyEUDR_claude`
(branch `claude/myeudr-lead-census-k3i1rk`) anziché sul PC locale. In quell'ambiente valgono
due limiti che **cambiano il metodo** rispetto alle sessioni desktop:

1. **WebFetch/curl sono bloccati dalla policy di egress** (HTTP 403 al CONNECT) su *tutti* i
   domini esterni: `proff.dk`, `datacvr.virk.dk`, `biq.dk`, `lasso.dk`, `dakofo.dk` e i siti
   aziendali. Non è aggirabile e non va ritentato.
   → **Funziona solo WebSearch**, i cui frammenti però contengono spesso proprio i dati di
   contatto (query efficaci: `"<azienda>" kontakt e-mail telefon`, `"<azienda>" kontakt info@ mail adresse`).
   Verificato: la query `Skovby Møbelfabrik kontakt email adresse` restituisce `skovby@skovby.dk`.
2. **Budget WebSearch ~200 chiamate per agente** e limite di sessione sul totale.
   → Meglio 6 ricercatori "ricerca aziende" + un secondo giro di agenti "arricchimento contatti"
   che leggono il JSON e riempiono solo i campi vuoti.

### Metodo in due giri (adottato per la Danimarca, da riusare per SE/NL/BE/AT)

Il primo giro di 6 ricercatori ha prodotto le aziende ma solo **3 email su 88**: senza accesso ai
siti aziendali non c'era modo di estrarle. Un **secondo giro di 6 agenti di arricchimento**
(uno per file `dk_0N_*.json`, solo WebSearch, che riempiono *unicamente* i campi vuoti) ha portato
la copertura a **email 81/89, referente 77/89, sito 86/89, LinkedIn 57/89** — in linea con DE/FI.
Le query che funzionano: `"<azienda>" kontakt e-mail telefon` e `"<azienda>" kontakt info@ mail adresse`.
Dopo l'arricchimento: rieseguire `normalize_dk.py` e poi `add_country.py` (sostituisce il foglio).

### Residui aperti sulla Danimarca

- **Mangimi/soia: 11 aziende invece di ~15.** Piste ancora da battere: pagina DAKOFO
  "Ansvarlig soja/Virksomheder", elenchi krak.dk/degulesider "korn og foderstoffer", conferma di
  Tjørnehøj Mølle (il dato di fatturato trovato è del 2003).
- **Olio di palma: solo 2 aziende** dopo l'esclusione di Dragsbæk (vedi sotto). Da integrare.
- **Senza email (8):** H. Emballage, Color Label (indirizzo protetto anti-spam), Dansk Kaffe,
  La Cabra (solo form di contatto), A-One Danmark, AB Neo e 2 dei nuovi record mangimi.
- **`dimensione`**: per le società in forma ridotta (ApS/K/S), che per legge danese non pubblicano
  il fatturato, il campo riporta il *bruttofortjeneste* con anno e fonte, sempre dichiarato come tale.

### Due aziende rimosse dopo verifica (motivi da ricordare)

- **Getama Danmark A/S** — stabilimento di Gedsted distrutto da un incendio nel feb. 2024,
  produzione non ricostruita e portafoglio rilevato da **Carl Hansen & Søn** (tra i big esclusi):
  non è più un produttore, quindi non è un operatore EUDR. Stessa logica già applicata a
  Magnus Olesen (fallita) e Bent Krogh (cessata).
- **Dragsbæk A/S** — fatturato ~1,9 mld DKK (≈255 M€): ben oltre la soglia dei ~50 M€ decisa dal
  cliente, non un caso "di confine".

### Da verificare prima del contatto

- **Vestjysk Specialfoder**: allo stesso indirizzo risulta un'omonima società **sotto fallimento**.
- **Estate Coffee Copenhagen A/S** = Smage-Compagniet A/S (stesso CVR); **Copenhagen Chocolate
  Factory ApS** = marchio Simply Chocolate Copenhagen. Annotato nel campo `dimensione`.

### File aggiunti in questo giro

- `_myeudr_build/dk_01..06_*.json` — output dei 6 ricercatori + arricchimento (89 aziende).
- `_myeudr_build/normalize_dk.py` — normalizza `filiera` sulla tassonomia dei fogli IT/DE/FI
  (`<Macro> — <dettaglio>`) e ripulisce `denominazione` spostando il codice CVR in `dimensione`.
  Da rieseguire prima di `add_country.py` se si rigenerano i JSON danesi.

---

## 12. SVEZIA — stato e piano (prossimo passo immediato)

**Stato: foglio Svezia nel workbook, 89 aziende.** Ripartizione: legno/arredo 29,
legno/segheria 18, carta/packaging 14, caffè 8, cacao/cioccolato 6, gomma 5, mangimi/soia 4,
bovini/carne 3, pelle/concia 1, olio di palma 1.
Copertura contatti: **email 71/89, referente 74/89, sito 87/89, LinkedIn 48/89.**

### Rifinitura ancora da fare

- ~~`se_04_carta.json` fermo a email 4/14~~ → **RISOLTO**: email 13/14, LinkedIn 14/14.
- `se_02_legno_edilizia.json` è a 12 aziende invece di ~16 (email però già 12/12); LinkedIn 1/12.
- `se_06_gomma_soia_carne.json`: LinkedIn 4/14 e 4 email mancanti.
- Dopo ogni rifinitura: rieseguire `python add_country.py se Svezia <xlsx>` (sostituisce il foglio).

### Lezioni operative (importanti, valgono per NL/BE/AT)

1. **I 6 ricercatori in parallelo saturano il limite di sessione dell'account.** Lanciarne
   **2-3 per volta**. Il limite si è riattivato 4 volte durante Danimarca+Svezia.
2. **Il salvataggio incrementale è ciò che salva il lavoro.** Va chiesto esplicitamente nel prompt
   ("scrivi il file appena hai 3-5 aziende, poi riscrivilo ogni 3-4"): senza, un'interruzione da
   quota fa perdere tutto (successo alla Svezia primo tentativo, dove 6 agenti su 6 non salvarono nulla).
3. **Avvisare i ricercatori dell'insidia delle unità di misura locali.** In Svezia allabolag
   riporta spesso in **KSEK** (migliaia): un'azienda da "10 820 KSEK" fa ~1 M€, non 10 M€.
   Senza l'avviso esplicito nel prompt il rischio di includere micro-imprese fuori target è alto.

Valuta: **SEK ~11,3 kr/€** → 10–20 M€ ≈ 113–226 MSEK, tolleranza 5–40 M€ ≈ 56–450 MSEK.
Referente = **VD (verkställande direktör)**. Fonti (solo via WebSearch): allabolag.se, proff.se,
ratsit.se, largestcompanies.se, associazioni (Skogsindustrierna, Svenskt Trä, TMF, Grafiska
Företagen, Packbridge, Foder & Spannmål, KCF, Svenska Kaffeinformation).

**6 filoni (pesi svedesi), file `se_01..06`:**
1. **Segherie e legname** (sågverk, hyvleri, virkeshandel) — la filiera più forte. ~18.
   Escludi SCA, Holmen, Stora Enso, Setra, Vida, Bergs Timber, Norra Skog, Södra, Martinsons, Moelven.
2. **Prodotti in legno per edilizia** (limträ/glulam, KL-trä/CLT, trähus, trägolv, fönster/dörrar,
   takstolar, träemballage/pallar). ~16. Escludi Derome, Myresjöhus/OBOS, Älvsbyhus, Inwido.
3. **Mobili e arredo** (distretti Småland/Tibro/Nässjö/Virserum). ~16.
   Escludi IKEA e i fornitori maggiori (Inter IKEA Industry), Kinnarps, EFG, Nobia/Ballingslöv/Marbodal.
4. **Carta/imballaggio/stampa/etichette**. ~16. Escludi Billerud, SCA, Smurfit Westrock, DS Smith, Tetra Pak.
5. **Caffè + cacao/cioccolato** — consumo pro capite altissimo, filiera ricca; priorità agli
   importatori di **råkaffe**. ~16. Escludi Löfbergs, Arvid Nordquist, Zoégas (Nestlé), Gevalia/JDE, Cloetta, Fazer.
6. **Gomma + mangimi/soia + bovini/carne + pelle + palma**. ~14.
   Escludi Trelleborg, Lantmännen, Svenska Foder, HKScan/Scan, Atria, KLS Ugglarps, AAK/Karlshamns.

**Miglioramenti al metodo già applicati nei prompt svedesi (da riusare per NL/BE/AT):**
- **Tassonomia `filiera` imposta ai ricercatori** (`<Macro> — <dettaglio>`, max 5 parole), così
  non serve un `normalize_XX.py` a posteriori come per la Danimarca.
- **Organisationsnummer/n. registro fuori dalla `denominazione`**, direttamente in `dimensione`.
- **Raccolta email opportunistica già al primo giro**, così il giro di arricchimento parte da
  una base migliore invece che da zero.
- Ai ricercatori va detto **subito** che i registri non sono raggiungibili (policy di egress):
  evita che sprechino il budget in tentativi WebFetch/curl.

---

## 13. OLANDA — stato e rifiniture aperte

**Stato: CONSEGNATA — 100 aziende** (email 77/100, referente 61/100, LinkedIn 67/100).
Ripartizione: legno/arredo 21, cacao/cioccolato 19, caffè 17, carta/packaging 17, mangimi/soia 10,
bovini/carne 5, olio di palma 5, gomma 4, pelle/concia 2.

Valuta già in **EUR** (nessuna conversione). Referente = *directeur / algemeen directeur / eigenaar*.
Fonti (solo via WebSearch): kvk.nl, company.info, drimble.nl + associazioni (VVNH per il legname,
KNVKT per il caffè, VBZ per il cacao, Nevedi per i mangimi, NVC/VNP/KVGO per carta e stampa, COV
per la carne, CBM per i mobili).

### Residui minori

- `nl_01_cacao.json` ha referente 7/19: è il file meno coperto sui nomi dei decisori.
- Restano senza email: SRC, Snel Industrie, Bannink (contatto solo telefonico o indirizzo non pubblicato).
- **Marine Olie Handel Maatschappij** risulta acquisita dal trading house STX (Amsterdam) — mantenuta
  con avvertenza nel campo `dimensione`. **OTR Oiltrade** muove >100.000 t/anno con 11-50 addetti:
  possibile fatturato sopra fascia, segnalato.
- **Bangma Verpakking**: maggioranza di **De Jong Verpakking** (De Lier) dal luglio 2020, autorizzazione
  ACM del 20/05/2020 — la compliance potrebbe essere decisa a livello di gruppo.

### Difficoltà specifica olandese

**Le B.V. depositano quasi sempre bilanci abbreviati senza fatturato.** Il campo `dimensione`
riporta quindi n. dipendenti + anno + n. KVK, dichiarando esplicitamente che il fatturato non è
pubblicato. È lo stesso trattamento usato per le ApS danesi (bruttofortjeneste).

### Esclusioni verificate da ricordare

- **Houthandel Van Dam Bunnik** e **Centrop Houtimport**: non indipendenti, sono *vestigingen* di
  TABS Holland Groothandels B.V. (gruppo con 100+ sedi) → fuori soglia.
- **Droste Vaassen**: produzione cessata. **Commodity Centre**: solo warehousing, non operatore EUDR.
- **Coldenhove**: fallita nel maggio 2026. **ECCO Leather**: uscita da Dongen.
- **La concia bovina olandese è di fatto estinta**: il distretto Waalwijk/Dongen non è più attivo e
  l'unica conceria bovina rimasta è Rompa Tanneries (ex Koninklijke Hulshof). Compensato con
  un commerciante di pelli grezze e un quinto operatore della carne.
- Fuori target per taglia: Cocoanect (158 M€), Tony's Chocolonely (240 M€), Delicia Tilburg,
  Dutch Cocoa/Theobroma (ECOM), Crown of Holland (Tradin Organic), Nedcoffee (Sucden),
  Trabocca (Tradin Organic), Weekamp Deuren (Deli Home), Kegro, Fetim Group, Foreco.

---

## 14. BELGIO — stato

**Stato: CONSEGNATO — 90 aziende** (email 65/90, referente 45/90, LinkedIn 34/90).
Ripartizione: legno/arredo 25, cacao/cioccolato 18, carta/packaging 16, bovini/carne 9,
gomma 5, caffè 5, mangimi/soia 5, olio di palma 4, pelle/concia 3.

**Vantaggio belga: i bilanci depositati alla NBB/BNB sono pubblici**, quindi a differenza di
Olanda (B.V. con bilanci abbreviati) e Danimarca (ApS senza fatturato) qui il **fatturato reale
è quasi sempre disponibile**. È la copertura economica migliore dopo Italia e Germania.
Referente = *gedelegeerd bestuurder / zaakvoerder* (Fiandre) o *administrateur délégué / gérant* (Vallonia).

### Esclusioni di merito da ricordare

- **Pacorini Antwerp**: *soft commodity warehouse keeper* (230.000 m² di magazzini doganali) che
  movimenta cacao per conto terzi → **non immette la commodity sul mercato UE, non è operatore EUDR**.
  Stesso criterio applicato a Commodity Centre in Olanda. ⚠️ Anversa e Gand sono piene di operatori
  puramente logistici: vanno sempre esclusi.
- **Immobra** (24,9 M€) e **Oliefabriek Lichtervelde**: producono **olio di lino industriale**, che
  NON è commodity dell'Allegato I → nessun obbligo EUDR, quindi lead inutili. Sostituita con Repro NV.
- Fuori soglia con fatturato verificato: Efico (289 M€), Vleeswaren De Keyser (194), Viangro (168),
  Meat & More (163), Kim's Chocolates (114), Dovy (110), Vlevia/Devameat (103), Natra Chocolate (93),
  Aigremont (106), Rima (65-123), Aveno (61), Scaldis Ruien (61,9), The Belgian Chocolate Group (54,5,
  gruppo Baronie), Tribù (51,2).
- **Vlaemynck**: esclusa per attività ambigua (arredo vs ortofrutta) — meglio fuori che classificata a caso.

### Note di filiera

- **Concia belga esilissima**: restano di fatto due sole concerie attive, Tannerie Masure (Estaimpuis,
  17,2 M€, concia vegetale bovina — il lead migliore del filone) e Radermecker. Compensato con il
  commercio di pelli bovine (Hulpiau Hides) e con Sopraco, che unisce carne e pelle.
- **Forte rilevanza EUDR nei mobili**: Ethnicraft, Manutti, Royal Botania ed Extremis importano
  teak e legni tropicali da Indonesia/Asia — esposizione diretta, non semplice uso di pannelli europei.
- Segnalate le taglie gonfiate dal costo materia prima (carne e mangimi): Royale Lacroix (49,3 M€ /
  18,6 FTE), Ameloot (49,3), Jos Leemput (45,0 M€ con 16 FTE), Dierickx (40,8), Baert (38,9).
- ~~Il filone caffè è a 5 aziende~~ → **RISOLTO**: portato a 10 (The Java Coffee Company 12,3 M€,
  coffeeRoots 12,6 M€, Mokafina 8,0 M€, Cafés Delahaut, OR Coffee). Il file `be_02` è ora a 21 record
  (10 caffè + 11 legno), email 20/21 e referenti 18/21.
  Gli importatori belgi di caffè verde sono quasi tutti fuori soglia: Group Sopex (282 M€),
  Coffeeteam (108), Briz (75), Charles Liégeois (72), Supremo (67); **32Cup NV è oggi Sucafina NV**
  (stesso numero d'impresa) → escluso.
- Da riverificare prima del contatto: **Sas NV non è più familiare** (Miko 2021 → Nimbus Investments
  05/2024, referente Herman Sas da riconfermare); discrepanze di fatturato su Silco (4,8 vs 8,4 M€)
  e Belignum (16,1 vs 14,7 M€).

---

## 15. AUSTRIA — stato

**Stato: CONSEGNATA — 93 aziende.** Copertura contatti **email 90/93, referente 92/93**:
la migliore dell'intero progetto, meglio anche della Germania.
Ripartizione: legno/arredo 29, carta/packaging 17, mangimi/soia 11, caffè 7, legno/segheria 6,
cacao/cioccolato 6, bovini/carne 6, gomma 5, pelle/concia 3, olio di palma 3.

**Perché l'Austria ha la copertura migliore:** l'**Impressum è obbligatorio per legge** sui siti
aziendali e riporta Geschäftsführer ed e-mail. Nel prompt va detto esplicitamente al ricercatore
di cercare `"<azienda>" Impressum Geschäftsführer E-Mail`: è ciò che ha prodotto filoni interi
con copertura 19/19, 17/17 e 16/16.

### Esclusioni di merito da ricordare

- **Filiali nazionali di gruppi esteri**: rimosse a posteriori Segafredo Zanetti Austria,
  Lavazza Kaffee e Kaffee Partner Austria — la compliance si decide a livello di gruppo, non in
  Austria. Il ricercatore aveva già escluso per lo stesso motivo illy, Dallmayr Austria e
  Hausbrandt: **la regola va enunciata nel prompt fin dall'inizio** per evitare la pulizia manuale.
- **Aziende in Insolvenz**: escluse HAKA Küche, KAPO Möbel, ADA, Schletterer (mobili),
  SBG-Verpackung (packaging), Alexander Schärf & Söhne (caffè), Lederfabrik Vogl (concia).
  In Austria è un rischio concreto: un elenco datato le proporrebbe ancora come lead validi.
  **Franz Hauswirth** è invece inclusa perché risanata: insolvenza chiusa e rilevata al 100% da
  Landgarten nel marzo 2025, ~70 dipendenti mantenuti.
- **Fuori perimetro EUDR** (stessa trappola del Belgio): scartate Ölmühle Raab e Plattner Mühle
  (lino/girasole/colza/zucca — **non commodity dell'Allegato I**), RICO Elastomere (silicone),
  k-tec (plastica), Münzer/ABID (biodiesel da colza e oli esausti), saponi e candele (HS 3401/3406).
- Fuori soglia con dato verificato: Mosser (170 M€), Alpenrind (245), Fleischhof Raabtal (135),
  Rattpack (145), Lenzing Papier (102), VM Holz (~100), Kaufmann Bausysteme (80-95), Voglauer (75),
  sedda (69), sedie hali (67), Marzek Etiketten (60), Scheucher (56), Neudoerfler (56), Grüne Erde (~56).

### Note di filiera

- **Gomma austriaca strutturalmente povera di PMI 10-20 M€**: sopra soglia ci sono solo Semperit e
  KRAIBURG; il filone si regge su realtà più piccole (Deisenhammer, Czermak & Feger che lavora
  lattice di caucciù naturale, TEGUM, Persicaner, Zrunek).
- **Concia esile**: Boxmark e Wollsdorf sono sopra soglia, Vogl è cessata. Restano Waldviertler
  Werkstätten/GEA, Ludwig Reiter e la conceria artigianale Tschurtschenthaler.
- **Oli tropicali quasi assenti**: compensato con i mangimi. Lead multi-commodity interessante:
  **BIOSERVICE Zach** (grassi di palma bio + cacao + caffè) e **KUK-Austria** (membro RSPO dal 2014).
  **BAG Ölmühle** (33-35 M€ con ~25 addetti) è il maggiore oleificio di soia austriaco: lead primario.
- Per le segherie il campo `dimensione` riporta spesso i **volumi di taglio (fm/anno)** quando il
  fatturato non è pubblicato: per l'esposizione EUDR è un indicatore più significativo del fatturato.

---

## 16. VERIFICA QUALITÀ — esito (sessione di controllo)

Controllo qualità **record per record** dell'intero censimento, su branch
`claude/myeudr-lead-quality-check-r1lx7u` (PR #1). Non era una raccolta di nuove aziende:
era la caccia a refusi, attribuzioni errate ed errori introdotti durante la raccolta.
Tutti i materiali stanno in **`_myeudr_build/verifica/`**; il documento di sintesi è
**`REPORT_VERIFICA.md`**.

### Com'è organizzata la verifica

| File | Contenuto |
|---|---|
| `REPORT_VERIFICA.md` | **il deliverable**: sintesi per foglio, conteggi per gravità, casi `alta` con evidenza, correzioni proposte |
| `00_controlli_automatici.md` | Fase A: 26 controlli deterministici offline sul 100% dei 742 record |
| `01_analisi_dimensione.md` | analisi del campo `Dimensione`: tipo di dato dichiarato, anno, obsolescenza |
| `00_punti_noti.json` | verifica dei 13 punti lasciati aperti dalla raccolta |
| `<foglio>_<blocco>.json` | rilievi grezzi di ciascun agente di Fase B |
| `MANDATO_AGENTE.md` | il mandato dato agli agenti — **riusabile** per completare i blocchi mancanti |
| `blocchi/` | i 42 blocchi di lavoro (15-20 record ciascuno) in cui è diviso il censimento |

Script (tutti rieseguibili):
`controlli_automatici.py` (Fase A) · `analisi_dimensione.py` ·
`aggrega_rilievi.py` / `genera_report.py` / `monta_report.py` (report) ·
**`applica_correzioni.py`** (applica le correzioni certe).

### Esito della Fase A: l'integrità del censimento regge

Zero duplicati (né fra fogli né fra JSON), zero entità HTML, zero URL malformati, zero email
sintatticamente errate, zero numeri di registro rimasti nelle denominazioni, zero fonti vuote,
**zero divergenze fra i JSON di build e i fogli Excel**. La pipeline `add_country.py` è coerente.
I rilievi riguardano qualità redazionale, non integrità.

### ⚠️ Il problema principale trovato: i legami di gruppo

**Non era fra i 13 punti noti.** Molte aziende del censimento sono **controllate di gruppi**,
spesso esteri o quotati. Per il criterio che il progetto stesso aveva già applicato — rimuovendo
Lavazza Kaffee, Segafredo Zanetti Austria e Kaffee Partner Austria perché *«la compliance si decide
a livello di gruppo, non nella filiale»* — sono lead di valore dubbio.

Vanno però distinti due casi, che **non hanno la stessa gravità**:
- **legame già dichiarato** nel campo `Dimensione` → non è un errore di dato. La raccolta ha fatto
  quel che le regole chiedevano (§8: *«segnalare sempre i legami di gruppo»*). È una **decisione di
  selezione che spetta al cliente**.
- **legame non dichiarato, o capogruppo sbagliata** → **è** un errore di dato.

Casi accertati con fonte: Tjørnehøj Mølle (gruppo **DLG**, cioè uno dei big esplicitamente esclusi),
Naturli' Foods (gruppo **Dragsbæk/Orkla**, lo stesso per cui Dragsbæk era stata rimossa),
Bangma Verpakking (oggi **Stora Enso** via De Jong Packaging), Hvidbjerg Vinduet (gruppo tedesco
**ACO** — e la capogruppo indicata nel foglio era *sbagliata*), Timberman Denmark (svedese quotato
**Volati AB** dal 12/2024, non più Corticeira Amorim), Skagerak Denmark (**Fritz Hansen**, tra i big
esclusi), Sas NV (**Nimbus Investments** dal 05/2024), Tärnsjö Garveri (dichiarata «principale
conceria indipendente» ma ha moderbolag Axel Bodéns Handels AB), Bäckebrons e Balungstrands Sågverk
(capogruppo indicata fallita: oggi **Profuragruppen AB**), Tannerie Masure (**Groupe Saturne**, FR).

Il secondo problema ricorrente sono i **referenti superati**: nomi che erano il vertice al momento
della raccolta e oggi non lo sono più (Aubo Production, Hvidbjerg Vinduet, Hørning Parket,
Klim Furniture, N. Eilersen, Extremis, Bulo).

### Correzioni applicate al workbook

Applicate **solo le correzioni certe** ammesse dal mandato (refusi formali, entità HTML, forme
giuridiche, filiere fuori Allegato I, aziende cessate). Tutto il resto è rimasto **rilievo aperto
nel report**, non toccato nei fogli.

- **21 filiere finlandesi** ricondotte alla tassonomia standard: le varianti storiche
  (`Legno/Compensato-Prodotti`, `Legno/Segheria-Piallatura`, `Legno/CLT`, `Legno/Commercio-export`,
  `Legno/Piallatura`) → `Legno/Arredo` e `Legno/Segheria`. La riconduzione non è arbitraria: gli
  altri **sette fogli sono unanimi** nel classificare compensato, impiallacciature, finestre/porte,
  parquet, glulam e CLT sotto `Legno/Arredo — <dettaglio>`.
- **2 filiere italiane**: `Caffè (import caffè verde)` → `Caffè — import caffè verde`.
- **4 refusi formali danesi**: `6,5 M€ DKK` di Fredericia Furniture (mescolava le due valute) →
  `6,5 M DKK (≈0,87 M€)`; **`Just Coffee` → `Just Coffee I/S`** (interessentskab, CVR 35492380 —
  la ragione sociale che la raccolta aveva lasciato non verificata) con la riserva sciolta nel
  campo `dimensione`; prefisso LinkedIn `de.` → `dk.` per Innovation Living.
- **22 correzioni al foglio Italia** (era il più vecchio e il meno verificato, come sospettato):
  4 forme giuridiche accertate al Registro Imprese con P.IVA — fra cui **`Fonpelli S.p.A.` →
  `Fonpelli S.r.l.`**, che era proprio *sbagliata* — più 18 normalizzazioni ortografiche
  `Srl`/`SpA` → `S.r.l.`/`S.p.A.` (lo stile già usato da 41 record su 59).

- **5 denominazioni accertate ai registri**: `NPI (Nordic Panel Import)` → **`NPI A/S`** (CVR
  37418730); `Rompa Tanneries B.V.` → **`Vitelco Leather B.V.`** (sciolta la joint venture, Vitelco
  socio unico al 100%); `Karnische Massiv Möbel GmbH` → `Karnische-Massiv-Möbel Gesellschaft m.b.H.`
  (Firmenbuch FN 094638z); `Confiserie Vandenbulcke NV` → `Vandenbulcke Confiserie NV` (ordine
  registrale KBO); `Paletten Meyer` → `Josef Meyer Palettenbau Inh. Julian Meyer` (impresa
  individuale, non società di capitali).

- **2 record rimossi**, gli unici tolti dai fogli. Entrambi in una categoria che il mandato
  autorizza a correggere, ed entrambi con un precedente già applicato dal progetto:
  - **Helvoet Rubber & Plastic Technologies NV** (Belgio) — **fuori perimetro EUDR**: la gamma
    elastomeri dichiarata dall'azienda stessa è solo sintetica (IIR, CR, EPDM, NBR, FKM, HNBR,
    FFKM, silicone LSR); la gomma naturale non compare. Stesso criterio di RICO Elastomere (AT).
  - **Marine Olie Handel Maatschappij B.V.** (Olanda) — **fuori taglia**: bilancio 2022 a quasi
    **400 M€**, dieci volte il tetto della forbice, mentre il campo dichiarava il fatturato «non
    pubblicato». Stesso criterio di Dragsbæk (rimossa a ~255 M€). In più: acquisita da STX Group
    (closing 01/12/2024) e filiera reale = UCO/sottoprodotti per biocarburanti, non olio di palma.

  - **Weissengruber Möbelmanufaktur GmbH** (Austria) — **in insolvenza**: Sanierungsverfahren
    aperto al Landesgericht Linz, curatore nominato, voto dei creditori in aprile (registro KSV,
    EUWID Holz, Nachrichten.at). È esattamente la regola già applicata dal progetto: escluse
    HAKA Küche, KAPO Möbel, ADA e Schletterer per insolvenza **in corso**, mentre Franz Hauswirth
    fu mantenuta proprio perché **risanata**. Qui la procedura è aperta.

  - **Odense Seglmærkefabrik A/S** (Danimarca) — **società estinta**: il CVR 17620487 risulta
    «opløst efter fusion». L'attività è oggi un sito di Optimum Group Nordic (gruppo olandese),
    trasferito da Odense ad Ans By nel 2025. La persona giuridica censita non esiste più. Stesso
    criterio di Getama Danmark, Magnus Olesen e Bent Krogh.

**In totale 59 correzioni applicate**, di cui 4 rimozioni. Il censimento passa da **742 a 738
aziende** (Danimarca 89→88, Olanda 100→99, Belgio 95→94, Austria 93→92); l'ordine dei fogli è
ripristinato.

⚠️ **Nota sul criterio di rimozione.** Ho tolto una riga **solo** quando ricadeva in una delle
categorie che il mandato autorizza a correggere (filiere fuori Allegato I, aziende cessate) **e**
il progetto aveva già applicato lo stesso criterio a un caso analogo, citato nella motivazione.
Il **fuori taglia da solo non basta**: STOK Emballage (92 M€ reali contro una stima «>50 M€» nel
foglio, e maggioranza al fondo USA A&M Capital) è rimasta nel foglio come rilievo `alta`, perché
la taglia non è fra le categorie correggibili d'ufficio.

**Tre cose NON sono state corrette, di proposito** (il dettaglio è in `REPORT_VERIFICA.md` §0-bis):
1. **Il maiuscolo integrale del foglio Danimarca** (51 record su 89, stile del registro CVR).
   Un *title case* automatico rovinerebbe gli acronimi: `JKE DESIGN` → `Jke Design`, e lo stesso
   per NPI, MC, KLS, H.C., DHS. Serve una decisione caso per caso.
2. **Conceria Beschin** e **Conceria Daniela**: ciascuna corrisponde a **due entità omonime
   distinte** al Registro (una S.n.c. e una S.r.l. nello stesso comune). Aggiungere la forma
   giuridica significherebbe *scegliere* quale sia l'operatore EUDR: va accertato prima.
3. **Le email dubbie** restano `DA CONFERMARE`: il mandato vieta sia di inventarle sia di
   cancellarle d'ufficio.

⚠️ **Limite della normalizzazione ortografica italiana, scoperto strada facendo.** Le 18 riscritture
`Srl`→`S.r.l.` e `SpA`→`S.p.A.` correggono **come è scritta** la forma giuridica, non **quale** sia:
assumono che il foglio l'avesse indovinata. Su **Arko** l'assunzione era falsa (le fonti camerali
danno `ARKO S.R.L.` con la stessa P.IVA 03278760263), e la normalizzazione aveva reso più autorevole
una forma sbagliata. Corretto dopo la verifica di merito. **Lo stesso può valere per i blocchi Italia
non ancora verificati**: solo il controllo record per record distingue un refuso di scrittura da una
forma giuridica errata.

Non sono state applicate nemmeno le **espansioni di ragioni sociali abbreviate ma corrette**
(Göbel, Fuhlrott in Germania) né `AB` → `Aktiebolag` in Svezia, dove il foglio **non ha uno stile
maggioritario** (47 `AB` contro 42 `Aktiebolag`): normalizzare sarebbe stato arbitrario. In Italia
invece la normalizzazione è stata fatta proprio perché la maggioranza era netta (41 su 59).

⚠️ **Attenzione per chi riprende**: `applica_correzioni.py` usa **due percorsi diversi**, perché i
fogli non hanno tutti la stessa origine:
- **DK/SE/NL/BE/AT** hanno i JSON di build → si corregge il JSON e si rigenera con `add_country.py`
  (rigenerazione verificata **identica** riga per riga).
- **IT/DE/FI** esistono **solo** come foglio Excel → si corregge **la cella in posto**. Rigenerarli
  da un JSON esportato **riordinerebbe le righe** già consegnate (verificato: l'ordine interno ai
  gruppi-filiera non è alfabetico e non si conserva).

Ogni correzione ha un **controllo di guardia**: lo script confronta il valore attuale con quello
atteso e **salta** la correzione se non coincidono. Così è rieseguibile senza rischi.

### Cosa resta da fare

La Fase A copre il **100%** dei record. La **Fase B è parziale**: il limite di sessione degli agenti
si è riattivato ancora (uccidendo 2 agenti a metà lavoro), quindi non tutti i 42 blocchi sono stati
verificati. Lo stato di avanzamento è nella **§1 del `REPORT_VERIFICA.md`**, che elenca blocco per
blocco quali sono fatti.

**Per continuare:** prendere un blocco non ancora verificato da `_myeudr_build/verifica/blocchi/`,
lanciare un agente con il testo di `MANDATO_AGENTE.md` + i promemoria specifici del paese, e far
scrivere `_myeudr_build/verifica/<nome_blocco>.json`. Poi rilanciare `monta_report.py`.
Regole che hanno funzionato e vanno mantenute:
1. **massimo 2-3 agenti per volta** (il limite si è riattivato 9 volte in tutto il progetto);
2. **salvataggio incrementale obbligatorio** nel prompt («scrivi il file ogni 3-4 record»): è ciò
   che ha salvato il lavoro quando due agenti sono stati interrotti;
3. dire subito all'agente che **registri e siti sono irraggiungibili** (403 di egress) e che
   funziona **solo WebSearch**, altrimenti spreca il budget in tentativi WebFetch.
