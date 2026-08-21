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
| **Svezia** | 🟡 **FOGLIO NEL WORKBOOK** — arricchimento da completare su `se_04_carta` (§12) | 89 |
| **Olanda** | 🟡 **FOGLIO NEL WORKBOOK** — 3 filoni da completare + arricchimento (§13) | 73 |
| Belgio | ⏳ da fare | — |
| Austria | ⏳ da fare | — |

**Deliverable attuale:** `MyEUDR_Lead_Mapping.xlsx` — **6 fogli, 527 righe**, integro, 0 entità HTML residue.
Contiene Italia+Germania+Finlandia+Danimarca+Svezia+Olanda. (Esiste anche `MyEUDR_Lead_Mapping_ITALIA_pilota.xlsx`, vecchio, **eliminabile**.)

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

- **`se_04_carta.json` è l'unico file rimasto indietro: email 4/14.** L'agente di arricchimento
  è stato ucciso dal limite di sessione appena iniziato. Va rilanciato (stesso prompt degli altri)
  e con l'occasione il filone può salire da 14 a ~16-18 aziende.
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

**Stato: foglio nel workbook, 73 aziende** (email 54/73, referente 42/73, LinkedIn 42/73).
Ripartizione: cacao/cioccolato 19, caffè 17, legno/arredo 17, carta/packaging 11, gomma 4,
mangimi/soia 3, olio di palma 2.

Valuta già in **EUR** (nessuna conversione). Referente = *directeur / algemeen directeur / eigenaar*.
Fonti (solo via WebSearch): kvk.nl, company.info, drimble.nl + associazioni (VVNH per il legname,
KNVKT per il caffè, VBZ per il cacao, Nevedi per i mangimi, NVC/VNP/KVGO per carta e stampa, COV
per la carne, CBM per i mobili).

### Da completare (i 3 filoni interrotti dal limite di quota)

| File | Aziende | Target | Nota |
|---|---:|---:|---|
| `nl_04_carta.json` | 11 | ~16 | email già 9/11 |
| `nl_05_soia_palma.json` | 5 | ~15 | il porto di Rotterdam è il maggiore hub UE di soia e olio di palma: filone potenzialmente ricco |
| `nl_06_gomma_carne_mobili.json` | 4 | ~14 | gomma ~4, bovini/carne ~4, pelle/concia ~2 (distretto Waalwijk/Dongen), mobili ~4 |

Poi: giro di arricchimento contatti sui file con email/referente scoperti (soprattutto
`nl_01_cacao` con referente 7/19) e rieseguire `python add_country.py nl Olanda <xlsx>`.

### Difficoltà specifica olandese

**Le B.V. depositano quasi sempre bilanci abbreviati senza fatturato.** Il campo `dimensione`
riporta quindi n. dipendenti + anno + n. KVK, dichiarando esplicitamente che il fatturato non è
pubblicato. È lo stesso trattamento usato per le ApS danesi (bruttofortjeneste).

### Esclusioni verificate da ricordare

- **Houthandel Van Dam Bunnik** e **Centrop Houtimport**: non indipendenti, sono *vestigingen* di
  TABS Holland Groothandels B.V. (gruppo con 100+ sedi) → fuori soglia.
- **Droste Vaassen**: produzione cessata. **Commodity Centre**: solo warehousing, non operatore EUDR.
- Fuori target per taglia: Cocoanect (158 M€), Tony's Chocolonely (240 M€), Delicia Tilburg,
  Dutch Cocoa/Theobroma (ECOM), Crown of Holland (Tradin Organic), Nedcoffee (Sucden),
  Trabocca (Tradin Organic), Weekamp Deuren (Deli Home), Kegro, Fetim Group, Foreco.
