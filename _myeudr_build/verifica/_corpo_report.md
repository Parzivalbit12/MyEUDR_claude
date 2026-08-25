# REPORT DI VERIFICA — MyEUDR Lead Mapping

Controllo qualità record per record del censimento lead (**742 aziende, 8 fogli**). Non è una raccolta di nuove aziende: è la verifica del lavoro esistente.

La verifica si è svolta in due fasi:

- **Fase A — controlli deterministici**, offline, su tutti i JSON di build e sul workbook: 24 controlli automatici su duplicati, email dedotte, URL, entità HTML, tassonomia, forbice dimensionale, denominazioni e forme giuridiche. Dettaglio in [`00_controlli_automatici.md`](00_controlli_automatici.md) e [`01_analisi_dimensione.md`](01_analisi_dimensione.md).
- **Fase B — riscontro sul web**, record per record, tramite agenti di verifica che hanno lavorato a blocchi di 15-20 aziende con 2-3 ricerche ciascuna. Ogni rilievo porta un URL o la citazione del frammento a sostegno.


## 1. Copertura della verifica

| Foglio | Aziende | Blocchi verificati | Aziende verificate | Copertura |
|---|--:|---|--:|--:|
| Italia | 95 | 0/5 | 0 | 0% |
| Germania | 97 | 0/6 | 0 | 0% |
| Finlandia | 84 | 0/5 | 0 | 0% |
| Danimarca | 89 | 2/5 | 36 | 40% |
| Svezia | 89 | 1/5 | 18 | 20% |
| Olanda | 100 | 1/6 | 17 | 17% |
| Belgio | 95 | 1/5 | 19 | 20% |
| Austria | 93 | 0/5 | 0 | 0% |
| **TOTALE** | **742** | **5/42** | **90** | **12%** |

> La Fase A copre invece il **100%** dei 742 record: è un controllo offline e non dipende dal budget di ricerca.


_A questi si aggiunge la verifica mirata dei **13 punti già noti** lasciati aperti dalla raccolta, condotta separatamente e riportata per intero più sotto._


## 2. Rilievi per foglio

**Totale rilievi Fase B: 129** — alta 28 · media 60 · bassa 41.

| Foglio | Rilievi | alta | media | bassa | Aziende toccate |
|---|--:|--:|--:|--:|--:|
| Italia | 0 | 0 | 0 | 0 | 0 |
| Germania | 0 | 0 | 0 | 0 | 0 |
| Finlandia | 0 | 0 | 0 | 0 | 0 |
| Danimarca | 46 | 14 | 18 | 14 | 32 |
| Svezia | 36 | 6 | 15 | 15 | 18 |
| Olanda | 14 | 4 | 9 | 1 | 6 |
| Belgio | 32 | 4 | 18 | 10 | 19 |
| Austria | 0 | 0 | 0 | 0 | 0 |
| _(tutti)_ | 1 | 0 | 0 | 1 | 1 |
| **TOTALE** | **129** | **28** | **60** | **41** | **76** |

### Rilievi per campo

| Campo | Rilievi | di cui alta |
|---|--:|--:|
| dimensione | 53 | 13 |
| referente | 32 | 8 |
| denominazione | 15 | 6 |
| email | 9 | 0 |
| linkedin | 7 | 0 |
| sito | 4 | 0 |
| filiera | 3 | 1 |
| ruolo | 3 | 0 |
| fonte | 2 | 0 |
| sede | 1 | 0 |

---

## 3. Tema trasversale — legami di gruppo (45 rilievi)

È il problema **più diffuso e meno atteso** emerso dalla verifica: non era fra i 13 punti noti dell'handoff. Numerose aziende del censimento sono controllate di gruppi, spesso esteri o quotati. Per il criterio già applicato dal progetto — che aveva rimosso Lavazza Kaffee, Segafredo Zanetti Austria e Kaffee Partner Austria perché *«la compliance si decide a livello di gruppo, non nella filiale»* — sono **lead di valore dubbio**.

La tabella distingue i due casi, che non hanno la stessa gravità:

- **DICHIARATO** — il campo `Dimensione` del foglio già segnala il legame. Non è un errore di dato: la raccolta ha fatto quel che le regole chiedevano (*«segnalare sempre i legami di gruppo»*). È una **decisione di selezione** che spetta al cliente.

- **NON DICHIARATO / ERRATO** — il legame manca del tutto, oppure la capogruppo indicata è sbagliata. Questo **è** un errore di dato.

| Foglio | Azienda | Stato nel foglio | Rilievo |
|---|---|---|---|
| (tutti) | (controllo di rientro) | — (record non risolto) | nessuna delle 7 aziende rimosse e' rientrata nei fogli. Controllo eseguito su _records.json (742 record, tutti i fogli) cercando in ogni campo, con radici tolleranti alle varianti: 'getama', 'dragsb', |
| Belgio | Belignum NV | **dichiarato** | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato i |
| Belgio | Buzzispace NV | **dichiarato** | Il campo indica la produzione 'in Kempen' (implicitamente Belgio): le fonti aziendali collocano lo stabilimento produttivo a Bladel, nei Paesi Bassi. La sede sociale ad Anversa resta corretta, ma l'at |
| Belgio | Sas NV (Sas Coffee) | **dichiarato** | CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elen |
| Belgio | Silco NV | **NON dichiarato** | RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui president |
| Belgio | Tannerie Masure SA | **NON dichiarato** | Societa' non indipendente: dal 2014 Tannerie Masure fa parte del Groupe Saturne insieme alla francese Tannerie Fortier-Beaulieu (Roanne). Il referente indicato, Olivier Lesage, risulta anche dirigente |
| Danimarca | BØJSØ DØRE & VINDUER A/S | **dichiarato** | Lead non indipendente: dal 2017 la società è controllata da INWIDO DENMARK A/S, parte del gruppo quotato svedese Inwido AB (fatturato di gruppo ~9 mld SEK nel 2025). Secondo il mandato una controllata |
| Danimarca | COPENHAGEN CHOCOLATE FACTORY ApS | **dichiarato** | IDENTITA' ANNOTATA CONFERMATA CORRETTA: CVR 32761844, Amager Landevej 123, 2770 Kastrup, costituita il 26-01-2010, ApS; opera con i binavne 'Simply Chocolate Copenhagen' e www.simplychocolate.dk; dire |
| Danimarca | HVIDBJERG VINDUET A/S | **dichiarato** | Assetto proprietario errato e lead non indipendente: il campo indica come controllante "Hvidbjerg i A/S", ma la società è controllata dal gruppo ACO Nordic, a sua volta parte del gruppo tedesco ACO (f |
| Danimarca | HØRNING PARKET A/S | **NON dichiarato** | Referente e ruolo errati: Peter (Christian Saaby) Mathiasen è presidente del consiglio di amministrazione (bestyrelsesformand), non adm. direktør. Il vertice esecutivo della società è Peter Vissing, d |
| Danimarca | INNOVATION LIVING A/S (già Innovation Ra | **dichiarato** | Dato obsoleto: il campo cita il bruttofortjeneste 2023 (47,3 M DKK) mentre l'ultimo bilancio disponibile (2025) riporta 40 M DKK, quindi in calo. Anche la composizione del gruppo è imprecisa: INNOVATI |
| Danimarca | JKE DESIGN A/S | **dichiarato** | Lead non indipendente: la società appartiene al gruppo BALLINGSLÖV INTERNATIONAL DANMARK A/S / Ballingslöv International AB (gruppo svedese, Stena Adactum), con presidente del CdA e consigliere espres |
| Danimarca | KRYDSFINER-HANDELEN A/S | **dichiarato** | Controllata di gruppo estero: dall'autunno 2023 la societa' e' stata venduta da Carsten Rittig a Fritzoe Nordic Holding AS (Norvegia), che ne detiene il controllo. Il record lo accenna in forma dubita |
| Danimarca | KVIST INDUSTRIES A/S | **NON dichiarato** | Assetto proprietario non dichiarato: la societa' figura nel portafoglio del fondo di private equity danese Dansk Ejerkapital ed e' controllata tramite KVIST HOLDING A/S (CVR 21746886, Esbjerg). Il cam |
| Danimarca | Klim Furniture A/S (gia' Klim Mobelfabri | **NON dichiarato** | Referente non attuale: dal 2024 il direktor in carica e' Kasper Hogenhaug (che ha acquisito il 50% della societa'); Jan Middelboe resta comproprietario al 50% ma non e' piu' il vertice operativo indic |
| Danimarca | LILLEHEDEN A/S | **dichiarato** | Controllata di gruppo: la societa' fa parte di Nordic Wood Industries A/S (CVR 37385603), che dal 12.05.2025 ha un nuovo adm. direktor di gruppo (Holger Carsten Hansen). Il legame e' gia' correttament |
| Danimarca | MULTIFORM A/S | **dichiarato** | Controllata di gruppo: capogruppo BALLINGSLOV INTERNATIONAL DANMARK A/S (gruppo svedese Ballingslov International / Stena Adactum). Il legame e' gia' dichiarato correttamente nel record, quindi il ril |
| Danimarca | N. EILERSEN A/S | **dichiarato** | Referente errato: Anders Michael Juul Ejlersen risulta membro del consiglio di amministrazione (bestyrelse) e comproprietario, non direktor. Il direktor registrato di N. EILERSEN A/S (CVR 35118519) e' |
| Danimarca | Naturli' Foods | **dichiarato** | RILIEVO EMERSO DAL CONTROLLO DI RIENTRO. Il record dichiara esso stesso che Naturli' Foods e' 'parte del gruppo Dragsbaek/Orkla': e' quindi una controllata del gruppo norvegese quotato Orkla ASA, per  |
| Danimarca | Skagerak Denmark A/S | **NON dichiarato** | Referente errato e legame di gruppo non dichiarato: Skagerak Denmark A/S e' stata acquisita da Fritz Hansen A/S nel dicembre 2021 ed e' oggi il marchio 'Skagerak by Fritz Hansen'. Josef Theodor Kaiser |
| Danimarca | Skagerak Denmark A/S | **NON dichiarato** | Dati economici obsoleti: utile lordo 53,7 M DKK riferito al 2021 e addetti al dicembre 2022, cioe' antecedenti o coevi all'acquisizione da parte di Fritz Hansen. La stima ricavi '~15-22 M€' non e' ver |
| Danimarca | TIMBERMAN DENMARK A/S | **dichiarato** | Assetto proprietario errato/obsoleto: il record indica solo 'controllata da Timberman Holding ApS ... azionariato nordico'. In realta' nel dicembre 2024 la societa' e' stata acquistata dal gruppo indu |
| Danimarca | TJOERNEHOEJ MOELLE A/S | — (record non risolto) | LEAD NON VALIDO. A/S Tjoernehoej Moelle (CVR 34175012) NON e' un'impresa indipendente: e' stata acquistata da DLG nel 1989 dal mugnaio Sander Petersen ed e' oggi una controllata della cooperativa DLG  |
| Danimarca | VERMUND LARSEN A/S (VELA / VERMUND) | **NON dichiarato** | Disallineamento tra i canali: il sito indicato (vermund.eu) e' quello del solo marchio di design 'Vermund', mentre il sito istituzionale della societa' e del marchio principale e' vela.dk (coerente co |
| Olanda | Bangma Verpakking B.V. | **dichiarato** | LEAD NON VALIDO — aggravamento rispetto a quanto annotato. Non solo De Jong Verpakking ha acquisito Bangma (closing 30-07-2020), ma nel 2023 l'INTERO De Jong Packaging Group è stato acquisito da STORA |
| Olanda | BeBo Parket B.V. | **dichiarato** | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dich |
| Olanda | Rompa Tanneries B.V. | **dichiarato** | Denominazione obsoleta: la societa' e' stata ridenominata VITELCO LEATHER B.V. Vitelco (gruppo PALI) ha rilevato le quote di Rompa Leather sciogliendo la joint venture ed e' oggi socio unico al 100%.  |
| Olanda | Rompa Tanneries B.V. | **dichiarato** | Assetto proprietario dichiarato errato: il campo indica ancora 'Soci: PALI Group (Den Bosch, vitello) e Rompa Leather (Rijen)', ma la JV e' stata sciolta e Vitelco (PALI Group) e' socio unico al 100%. |
| Olanda | Rompa Tanneries B.V. | **dichiarato** | Email e sito legati al vecchio marchio (sales@rompa-tanneries.com / www.rompa-tanneries.com). Con la ridenominazione in Vitelco Leather il dominio di riferimento del gruppo e' vitelco.nl; il vecchio s |
| Svezia | Abstracta AB | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata al 100% di Lammhults Design Group AB, gruppo quotato — la compliance EUDR si decide alla capogruppo. Il legame è però già dichiarato correttam |
| Svezia | Aktiebolaget Karlaträ | **NON dichiarato** | Legame di gruppo non dichiarato: la società appartiene a una koncern di 2 società con moderbolag Karlaträ Försäljning Aktiebolag (holding di famiglia/vendita). |
| Svezia | Balungstrands Sågverk AB | **dichiarato** | Capogruppo incompleta/superata: il record si ferma a Green Wood Sverige AB. Green Wood Sverige AB (con Bäckebrons e Balungstrands) è stata riacquistata da Profura dopo il fallimento del gruppo tedesco |
| Svezia | Brattby Sågverks AB | **NON dichiarato** | Legame di gruppo non dichiarato: la società fa parte di una koncern con moderbolag Brattby Trading Aktiebolag. Fatturato 143,4 MSEK (~12,7 M€) e 32 dipendenti 2024 confermati. |
| Svezia | Brännfors Träförädling Aktiebolag | **NON dichiarato** | Legame di gruppo non dichiarato: moderbolag Brännfors Holding AB. Inoltre il dato 2024 confermato dalle fonti è 53.348 KSEK ≈ 4,7 M€ con 15 dipendenti (crescita -4,4%): il fatturato 2025 di 79.011 KSE |
| Svezia | Bäckebrons Sågverk Aktiebolag | **dichiarato** | Capogruppo SBAGLIATA e superata: il record indica 'capogruppo Ziegler Holding GmbH'. Il gruppo tedesco Ziegler è FALLITO e Profura ha riacquistato Green Wood Sverige AB con Bäckebrons e Balungstrands; |
| Svezia | Drömtrappor AB | **NON dichiarato** | Legame di gruppo non dichiarato (moderbolag Förvaltnings AB Klätterbjörken) e forte discontinuità del fatturato non segnalata: 126.413 KSEK nel 2024 (~11,2 M€) contro 83.213 KSEK nel 2025 (~7,4 M€), c |
| Svezia | Ekstrands Dörrar & Fönster AB | **dichiarato** | Lead di dubbia validità (non errore di dato): società di un gruppo di 6 società con capogruppo Ekstrand & Son Aktiebolag, correttamente dichiarata nel record. Tutti gli altri dati (167.769 KSEK 2025 ≈ |
| Svezia | Fogia Collection Aktiebolag | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Scandinavian Design Partners AB, legame già dichiarato correttamente. Tutti i dati (108.304 KSEK 2024 ≈ 9,6 M€, risultato 15.276 KSEK, 18 d |
| Svezia | Glimakra of Sweden AB | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Garpco Aktiebolag dal 2007, gruppo di 25 società con 311 addetti e 667,0 MSEK. Il legame è dichiarato ma il record lo sottodimensiona ('con |
| Svezia | Gärsnäs Aktiebolag | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Bordet i Stockholm Aktiebolag, legame già dichiarato correttamente. Esiste inoltre notizia stampa di cambio di proprietà ('Gärsnäs AB får n |
| Svezia | Hjältevadshus AB | **dichiarato** | Rischio economico rilevante non segnalato: a fronte dei 140.766 KSEK (~12,5 M€) del 2025 la società ha una marginalità di -32,6% (perdita nell'ordine dei 45 MSEK). Inoltre la koncern è molto più ampia |
| Svezia | Hjältevadshus AB | **dichiarato** | Referente confermato (Johan Bynell, VD; ordförande Magnus Agervald) ma la nomina è annunciata da Pulsen Group: verificare che sia ancora in carica alla data di uso del lead. |
| Svezia | Horreds Möbel Aktiebolag | **dichiarato** | Dato 2022 NON aggiornabile con certezza e anzi CONTRADDETTO. allabolag.se riporta oggi per Horreds Möbel AB (556365-1974) 45 dipendenti (contro i 50 del 2022) e un intervallo di fatturato 50.000-99.99 |
| Svezia | Horreds Möbel Aktiebolag | **dichiarato** | Società CONFERMATA ATTIVA (scheda allabolag corrente, nessuna procedura concorsuale rilevata). Va però esplicitato il legame di gruppo: la capogruppo è Horreds Holding AB (esiste anche Horreds Möbel U |
| Svezia | Tärnsjö Garveri Aktiebolag | **NON dichiarato** | Legame di gruppo NON dichiarato: il record definisce l'azienda 'la principale conceria indipendente attiva', ma allabolag indica come moderbolag Axel Bodéns Handels Aktiebolag. L'affermazione di indip |

---

## 4. Casi di gravità ALTA (28)

_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, oppure fuori dal perimetro dell'Allegato I EUDR._


### Danimarca (14)

#### AUBO PRODUCTION A/S — campo `referente`

Referente non attuale: Torben Andersen è il PREDECESSORE. La carica di administrerende direktør è passata a Torben Paulin (ingresso registrato 22.01.2026 secondo lasso.dk). Contattare Torben Andersen come vertice attuale è un dato falso.

**Evidenza:** https://lasso.dk/firmaer/28854846/ny-administrerende-direktr-i-aubo-production-as/ — titolo "Ny administrerende direktør i AUBO PRODUCTION A/S"; frammento: "Torben Paulin overtook the position of administrerende direktør (CEO) at AUBO PRODUCTION A/S from Torben Andersen"

**Correzione proposta:** Torben Paulin — Adm. direktør

#### BØJSØ DØRE & VINDUER A/S — campo `denominazione`

Lead non indipendente: dal 2017 la società è controllata da INWIDO DENMARK A/S, parte del gruppo quotato svedese Inwido AB (fatturato di gruppo ~9 mld SEK nel 2025). Secondo il mandato una controllata di un gruppo estero non è un lead valido, perché la due diligence EUDR viene decisa a livello di capogruppo. Il campo dimensione lo segnala ma il record resta classificato come lead.

**Evidenza:** https://www.proff.dk/firma/b%C3%B8js%C3%B8-d%C3%B8re-vinduer-as/vorbasse/producenter/GJL0QJI016D — frammento: "Bøjsø Døre & Vinduer A/S has INWIDO DENMARK A/S as its parent company. Since 2017, Bøjsø has been part of the listed company Inwido"

**Correzione proposta:** Escludere o riclassificare il lead: indirizzare il contatto alla capogruppo Inwido Denmark A/S

#### HVIDBJERG VINDUET A/S — campo `referente`

Referente errato: Claus Arberg non risulta l'administrerende direktør attuale. Il vertice esecutivo è Morten Filtenborg Mortensgaard (pagina Kontakt del sito ufficiale, aprile 2026).

**Evidenza:** https://www.hvidbjergvinduet.dk/kontakt/ — frammento: "Morten F. Mortensgaard is the managing director (based on their contact page from April 2026)"; "Morten Filtenborg Mortensgaard is the Managing Director (Administrerende direktør)"

**Correzione proposta:** Morten Filtenborg Mortensgaard — Adm. direktør

#### HVIDBJERG VINDUET A/S — campo `dimensione`

Assetto proprietario errato e lead non indipendente: il campo indica come controllante "Hvidbjerg i A/S", ma la società è controllata dal gruppo ACO Nordic, a sua volta parte del gruppo tedesco ACO (famiglia Ahlmann), dal rilevamento del gruppo Plastmo nel 1995. Controllata di gruppo estero: la due diligence EUDR si decide a livello di capogruppo.

**Evidenza:** https://da.wikipedia.org/wiki/Hvidbjerg_Vinduet — frammento: "is a subsidiary of ACO Nordic Group, which is part of the German ACO Group, owned by Thomas Iver Ahlmann. In 1995, ACO Group took over the Danish company Plastmo Group, which consisted of Plastmo A/S and Hvidbjerg Vinduet A/S"; cfr. https://www.aco.dk/aco/aco-nordic

**Correzione proposta:** Controllata del gruppo tedesco ACO (via ACO Nordic) — escludere o riclassificare il lead, contatto a livello di capogruppo

#### HØRNING PARKET A/S — campo `referente`

Referente e ruolo errati: Peter (Christian Saaby) Mathiasen è presidente del consiglio di amministrazione (bestyrelsesformand), non adm. direktør. Il vertice esecutivo della società è Peter Vissing, direktør/adm. direktør e co-proprietario dal 2016.

**Evidenza:** https://www.proff.dk/firma/h%C3%B8rning-parket-as/skanderborg/producenter/GTM41UI016D — frammento: "a director named Peter Vissing and board chairman Peter Christian Saaby Mathiasen ... has 24 employees"; https://rocketreach.co/peter-vissing-email_99791140 — "Peter Vissing ... CEO and Partner at Hørning Parket A/S"

**Correzione proposta:** Peter Vissing — Adm. direktør

#### JKE DESIGN A/S — campo `denominazione`

Lead non indipendente: la società appartiene al gruppo BALLINGSLÖV INTERNATIONAL DANMARK A/S / Ballingslöv International AB (gruppo svedese, Stena Adactum), con presidente del CdA e consigliere espressi dalla capogruppo (Björn Friedrich Hauber, Magnus Hegdal). Secondo il mandato una controllata di un gruppo estero non è un lead valido: la due diligence EUDR si decide a livello di capogruppo.

**Evidenza:** https://ballingslovinternational.se/en/businesses/jke-design/ e https://www.proff.dk/firma/jke-design-as/jerslev-j/producenter/GKNXIBI016D — frammento: "The company is part of the Ballingslöv International Danmark A/S and Ballingslöv International AB group ... Björn Friedrich Hauber serves as board chairman and Magnus Hegdal is a board member"

**Correzione proposta:** Escludere o riclassificare il lead: contatto a livello di capogruppo Ballingslöv International AB

#### Klim Furniture A/S (gia' Klim Mobelfabrik) — campo `referente`

Referente non attuale: dal 2024 il direktor in carica e' Kasper Hogenhaug (che ha acquisito il 50% della societa'); Jan Middelboe resta comproprietario al 50% ma non e' piu' il vertice operativo indicato dalle fonti. Lo stesso campo dimensione del record segnala Kasper Hogenhaug come 'co-proprietario e direttore (dal 2024)', in contraddizione con il campo referente.

**Evidenza:** https://jammerbugtavis.dk/kasper-hoegenhaug-bliver-medejer-i-klim-furniture/ ; https://www.wood-supply.dk/article/view/1092962/traditionsrig_mobelproducent_far_ny_medejer_og_direktor - 'Ejerskabet i Klim Furniture er ligeligt fordelt mellem Kasper Hogenhaug og Jan Middelboe, og Kasper Hogenhaug er direktor i selskabet'

**Correzione proposta:** Kasper Hogenhaug, Direktor

#### N. EILERSEN A/S — campo `referente`

Referente errato: Anders Michael Juul Ejlersen risulta membro del consiglio di amministrazione (bestyrelse) e comproprietario, non direktor. Il direktor registrato di N. EILERSEN A/S (CVR 35118519) e' Marianne Lind Koch-Pedersen. Nota anche la grafia ufficiale al CVR: 'Ejlersen'.

**Evidenza:** https://www.proff.dk/roller/n.-eilersen-as/skamby/m%C3%B8bler/GKEJPJI015G ; https://ownr.dk/companies/public-profile/35118519 - direktor: Marianne Lind Koch-Pedersen; bestyrelse: Anders Michael Juul Ejlersen, Bettina Elisabeth Juul Ejlersen, Simon Kristian Frosig

**Correzione proposta:** Marianne Lind Koch-Pedersen, Direktor (Anders Michael Juul Ejlersen resta comproprietario/consigliere)

#### Naturli' Foods — campo `dimensione`

RILIEVO EMERSO DAL CONTROLLO DI RIENTRO. Il record dichiara esso stesso che Naturli' Foods e' 'parte del gruppo Dragsbaek/Orkla': e' quindi una controllata del gruppo norvegese quotato Orkla ASA, per la stessa ragione per cui Dragsbaek era stata rimossa dalla raccolta. Non e' un rientro formale (denominazione diversa) ma sostanzialmente reintroduce nel foglio un'entita' dello stesso gruppo: la compliance EUDR si decide a livello di capogruppo Orkla, quindi il lead non e' valido. Si aggiunge che la dimensione e' 'n.d.' (nessun dato di fatturato o dipendenti) e che la filiera dichiarata e' 'Olio di palma' sulla base di una FAQ del sito che dichiara solo l'uso di olio di palma RSPO in parte della gamma: perimetro EUDR marginale e non quantificato.

**Evidenza:** Record _records.json, foglio Danimarca riga 86, campo dimensione: 'parte del gruppo Dragsbaek/Orkla (CVR 25476573)'; fonte del record https://www.naturli-foods.com/faq/oils/

**Correzione proposta:** Rimuovere il lead (controllata Dragsbaek/Orkla, stessa motivazione della rimozione di Dragsbaek)

#### SKOVS KORN A/S. KORN- OG FODERSTOFAGENTUR — campo `filiera`

Perimetro EUDR dubbio: la societa' si qualifica pubblicamente come broker/agenzia di intermediazione internazionale ('brokers indenfor international handel med korn, foderstoffer og oliefro' dal 1987) e la ragione sociale stessa e' 'Korn- og Foderstofagentur'. Un agente che non acquista in proprio non immette la commodity sul mercato UE e quindi non e' operatore ai sensi EUDR (analogia con gli operatori di sola logistica). Inoltre le commodity trattate (cereali, mangimi, semi oleosi) ricadono in Allegato I solo per la parte soia, non verificata. Il modesto bruttofortjeneste (12 M DKK ~1,6 M€) e' coerente con un'attivita' di pura intermediazione.

**Evidenza:** http://skovskorn.dk/ - 'Skovs Korn A/S har siden 1987 opereret som brokers indenfor international handel med korn, foderstoffer og oliefro' ; https://www.proff.dk/firma/skovs-korn-as.-korn-og-foderstofagentur/vejle/jordbrugsr%C3%A5varer-levende-dyr-tekstilr%C3%A5varer-og-indsatsvarer-agentur/064Z69I10OL (settore: agentur)

**Correzione proposta:** Escludere o declassare il lead salvo verifica che la societa' operi anche in conto proprio su soia (import fisico nell'UE)

#### Skagerak Denmark A/S — campo `referente`

Referente errato e legame di gruppo non dichiarato: Skagerak Denmark A/S e' stata acquisita da Fritz Hansen A/S nel dicembre 2021 ed e' oggi il marchio 'Skagerak by Fritz Hansen'. Josef Theodor Kaiser indicato come referente e' (era) l'amministratore delegato della capogruppo Fritz Hansen, non il vertice della controllata (all'atto della cessione l'ad di Skagerak era Jesper Panduro). Il campo dimensione non menziona in alcun modo il controllo di Fritz Hansen: lead non valido, la compliance EUDR si decide in capogruppo.

**Evidenza:** https://www.dezeen.com/2021/12/15/fritz-hansen-acquires-skagerak/ ; https://www.hjulmandkaptain.dk/english/news/hjulmandkaptain-has-advised-the-owners-of-skagerak-denmark-on-the-sale-to-fritz-hansen/ - 'Fritz Hansen CEO Josef Kaiser ... Skagerak CEO Jesper Panduro'

**Correzione proposta:** Dichiarare: controllata di Fritz Hansen A/S dal dicembre 2021; referente da riverificare presso la controllata (non l'ad di gruppo)

#### TIMBERMAN DENMARK A/S — campo `dimensione`

Assetto proprietario errato/obsoleto: il record indica solo 'controllata da Timberman Holding ApS ... azionariato nordico'. In realta' nel dicembre 2024 la societa' e' stata acquistata dal gruppo industriale svedese quotato Volati AB (Nasdaq Stockholm, ~2.000 dipendenti, ~7,7 mld SEK di ricavi), che l'ha rilevata dalla portoghese Corticeira Amorim. Controllata di gruppo quotato estero: lead non valido, compliance EUDR accentrata in capogruppo.

**Evidenza:** https://ligeher.nu/mariagerfjord/nyheder/mennesker/svensk-koncern-koeber-hadsund-firma-for-kaempe-millionbeloeb/5355430 ; https://nordjyske.dk/nyheder/erhverv/hadsund-firma-solgt-for-kaempe-millionbeloeb/5355340 - 'Timberman ... blev kobt af den svenske industrikoncern Volati fra portugisiske Corticeira Amorim' (dicembre 2024)

**Correzione proposta:** Controllata del gruppo svedese quotato Volati AB dal dicembre 2024 (in precedenza Corticeira Amorim); Mogens Albaek Fisker resta direktor e comproprietario

#### TJOERNEHOEJ MOELLE A/S — campo `dimensione`

LEAD NON VALIDO. A/S Tjoernehoej Moelle (CVR 34175012) NON e' un'impresa indipendente: e' stata acquistata da DLG nel 1989 dal mugnaio Sander Petersen ed e' oggi una controllata della cooperativa DLG (25.000 agricoltori danesi), che la elenca esplicitamente tra le proprie societa' insieme a Vitfoss e Dangroent; la produzione e' commercializzata sotto il marchio Equsana, brand DLG dal 2012. Coerentemente, la sede legale registrata risulta a Koebenhavn V (sede DLG) e non a Hedehusene (dove resta lo stabilimento, Tingstedvej 47, 2640 Hedehusene). La compliance EUDR si decide a livello di capogruppo DLG.

**Evidenza:** https://equsana.dk/om-equsana/tjoernehoej-moelle/ e https://www.dlg.dk/Energy-and-Retail/Retail/Equsana-alt-til-hest - 'DLG ejer datterselskaberne Tjoernehoej Moelle, Vitfoss og Dangroent'; 'Tjoernehoej Moelle blev koebt af DLG i 1989 af moeller Sander Petersen'; https://lasso.dk/firmaer/34175012/as-tjrnehj-mlle - 'A/S TJOERNEHOEJ MOELLE - Koebenhavn V'

**Correzione proposta:** Rimuovere il lead (controllata del gruppo DLG) oppure riqualificarlo come stabilimento del gruppo DLG

#### VESTJYSK SPECIALFODER ApS — campo `denominazione`

Ambiguita' PARZIALMENTE risolta: il fallimento riguarda l'omonima 'VestjyDsk Specialfoder ApS' CVR 39680718 (konkurs decretato dallo Skifteretten di Holstebro il 26-02-2020, curatore avv. Michael Joergensen, Bliddal & Holmstroem, Videbaek), NON la societa' del foglio. Resta pero' un'incoerenza nel record stesso: il campo dimensione indica CVR 38786709 mentre il campo fonte cita anche lasso.dk/firmaer/42242993 (un TERZO numero CVR) per la stessa denominazione. Esiste inoltre la ditta individuale omonima CVR 86607514. Quale delle entita' 'Vestjysk' sia quella operativa e attiva oggi resta DA CONFERMARE.

**Evidenza:** https://konkurser.dk/konkurs/?id=102386 e https://www.proff.dk/firma/vestjydsk-specialfoder-aps-under-konkurs/vemb/n%C3%A6rings-og-nydelsesmidler/GXIFOUI116S/ - 'Vestjydsk Specialfoder ApS Under Konkurs - 39680718 ... ved dekret af 26. februar 2020 tog Skifteretten i Holstebro Vestjydsk Specialfoder ApS under konkursbehandling'; https://www.proff.dk/firma/vestjysk-specialfoder-aps/vemb/engroshandel-annet/GYZVKCI10N6/ - 'Vestjysk Specialfoder ApS, CVR 38786709, Industrivej 2, 7570 Vemb, startdato 11-07-2017'; https://lasso.dk/firmaer/42242993/vestjysk-specialfoder-aps

**Correzione proposta:** Allineare il record a un unico CVR (38786709 secondo proff.dk) ed eliminare il riferimento a lasso.dk/42242993 se non pertinente


### Svezia (6)

#### Balungstrands Sågverk AB — campo `dimensione`

Capogruppo incompleta/superata: il record si ferma a Green Wood Sverige AB. Green Wood Sverige AB (con Bäckebrons e Balungstrands) è stata riacquistata da Profura dopo il fallimento del gruppo tedesco Ziegler; il koncernmoderbolag oggi è Profuragruppen AB (181 società, 1.293 addetti, 7.501 MSEK). Lead non valido: la compliance EUDR si decide a livello Profura.

**Evidenza:** allabolag.se: «Balungstrands Sågverk AB är ett dotterbolag med Profuragruppen AB som koncernmoderbolag ... totalt 181 bolag, 1 293 anställda, 7 501 MSEK»; https://www.lesprom.com/en/news/Profura_reacquires_B%C3%A4ckebrons_and_Balungstrands_sawmills_in_Sweden_after_Ziegler_Group%E2%80%99s_bankruptcy_117770/

**Correzione proposta:** Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dal 2025, dopo il fallimento di Ziegler Group)

#### Brännfors Träförädling Aktiebolag — campo `dimensione`

Legame di gruppo non dichiarato: moderbolag Brännfors Holding AB. Inoltre il dato 2024 confermato dalle fonti è 53.348 KSEK ≈ 4,7 M€ con 15 dipendenti (crescita -4,4%): il fatturato 2025 di 79.011 KSEK (~7,0 M€) citato nel record non trova riscontro e resta DA CONFERMARE. Con il solo dato 2024 l'azienda è SOTTO la soglia minima di 5 M€.

**Evidenza:** allabolag/bolagsfakta (556103-8695): «15 anställda, omsättning 53 348 KSEK, resultat 2 677 KSEK (2024), tillväxt −4,4%»; «moderbolaget är Brännfors Holding AB»

**Correzione proposta:** Dichiarare moderbolag Brännfors Holding AB e riportare il dato certificato 2024 (53.348 KSEK ≈ 4,7 M€, 15 dip.) finché il 2025 non è confermato

#### Bäckebrons Sågverk Aktiebolag — campo `dimensione`

Capogruppo SBAGLIATA e superata: il record indica 'capogruppo Ziegler Holding GmbH'. Il gruppo tedesco Ziegler è FALLITO e Profura ha riacquistato Green Wood Sverige AB con Bäckebrons e Balungstrands; il koncernmoderbolag attuale è Profuragruppen AB. Lead non valido: la compliance EUDR si decide a livello Profura.

**Evidenza:** https://www.lesprom.com/en/news/Profura_reacquires_B%C3%A4ckebrons_and_Balungstrands_sawmills_in_Sweden_after_Ziegler_Group%E2%80%99s_bankruptcy_117770/ ; Skogsaktuellt «Bäckebrons och Balungstrands Sågverk förvärvas av nygammal ägare» — https://www.skogsaktuellt.se/artikel/2237233/backebrons-och-balungstrands-sagverk-forvarvas-av-nygammal-agare.html

**Correzione proposta:** Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dopo il fallimento di Ziegler Group)

#### Drömtrappor AB — campo `dimensione`

Legame di gruppo non dichiarato (moderbolag Förvaltnings AB Klätterbjörken) e forte discontinuità del fatturato non segnalata: 126.413 KSEK nel 2024 (~11,2 M€) contro 83.213 KSEK nel 2025 (~7,4 M€), con dipendenti scesi da 96 a 74.

**Evidenza:** allabolag.se (556309-7038): «Omsättning 2024: 126 413 tkr; 2025: 83 213 KSEK»; «96 anställda ... senare data visar 74»; «moderbolaget är Förvaltnings AB Klätterbjörken» — https://www.allabolag.se/organisation/dr%C3%B6mtrappor-ab/norsj%C3%B6/tr%C3%A4varor/2K04H5AI5YI6G

**Correzione proposta:** Aggiungere: 'moderbolag Förvaltnings AB Klätterbjörken; fatturato in calo da 126,4 MSEK (2024) a 83,2 MSEK (2025)'

#### Hjältevadshus AB — campo `dimensione`

Rischio economico rilevante non segnalato: a fronte dei 140.766 KSEK (~12,5 M€) del 2025 la società ha una marginalità di -32,6% (perdita nell'ordine dei 45 MSEK). Inoltre la koncern è molto più ampia di quanto indicato: 56 società con moderbolag Pulsen AB (il record cita solo 'azionista di controllo gruppo Pulsen'), quindi la compliance EUDR si deciderebbe a livello Pulsen.

**Evidenza:** allabolag.se (556232-9135): «omsättning 2025: 140 766 tkr ... vinstmarginal -32,6%»; «ingår i en koncern med 56 bolag, moderbolag Pulsen AB» — https://www.allabolag.se/5562329135/koncern ; pulsen.se/vara-bolag/hjaltevadshus/

**Correzione proposta:** Aggiungere: 'perdita d'esercizio 2025 (marginalità -32,6%); koncern Pulsen AB, 56 società'

#### Tärnsjö Garveri Aktiebolag — campo `dimensione`

Legame di gruppo NON dichiarato: il record definisce l'azienda 'la principale conceria indipendente attiva', ma allabolag indica come moderbolag Axel Bodéns Handels Aktiebolag. L'affermazione di indipendenza è falsa e la compliance EUDR si deciderebbe alla capogruppo.

**Evidenza:** allabolag.se (556474-7797): «Tärnsjö Garveri Aktiebolag har 46 anställda och dess moderbolag är Axel Bodéns Handels Aktiebolag» — https://www.allabolag.se/foretag/t%C3%A4rnsj%C3%B6-garveri-aktiebolag/t%C3%A4rnsj%C3%B6/producenter/2K13UVPI63IK3

**Correzione proposta:** Sostituire 'principale conceria indipendente attiva' con: 'controllata di Axel Bodéns Handels Aktiebolag (moderbolag)'


### Olanda (4)

#### Bangma Verpakking B.V. — campo `dimensione`

LEAD NON VALIDO — aggravamento rispetto a quanto annotato. Non solo De Jong Verpakking ha acquisito Bangma (closing 30-07-2020), ma nel 2023 l'INTERO De Jong Packaging Group è stato acquisito da STORA ENSO (multinazionale finlandese quotata). Bangma Verpakking opera oggi 'as part of the De Jong Verpakking and Stora Enso family': non è più un'entità autonoma sotto il profilo decisionale e la compliance EUDR si determina a livello di capogruppo Stora Enso, che ha già un proprio programma EUDR di gruppo. Da rimuovere dalla lista lead.

**Evidenza:** https://dejongverpakking.com/en/news/de-jong-packaging-completes-acquisition-of-bangma-verpakking/ ; https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - 'in 2023 werd De Jong Packaging Group overgenomen door Stora Enso ... vandaag maakt Bangma Verpakking deel uit van de De Jong Verpakking en Stora Enso familie'; https://www.agf.nl/article/9238854/de-jong-verpakking-neemt-bangma-verpakking-over/

**Correzione proposta:** Rimuovere il lead (controllata Stora Enso via De Jong Packaging Group dal 2023)

#### BeBo Parket B.V. — campo `referente`

Referente obsoleto: Frans Bolier e Johan van de Beek (fondatori 2006) hanno ceduto l'azienda nel 2022 alla seconda generazione. La direzione e' oggi di Kees van de Beek e Marielle Zwolsman.

**Evidenza:** https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Kees van de Beek en Marielle Zwolsman maakten al deel uit van het management van Bebo en blijven het bedrijf leiden na de overdracht'

**Correzione proposta:** Kees van de Beek / Marielle Zwolsman - Directeur

#### Rompa Tanneries B.V. — campo `denominazione`

Denominazione obsoleta: la societa' e' stata ridenominata VITELCO LEATHER B.V. Vitelco (gruppo PALI) ha rilevato le quote di Rompa Leather sciogliendo la joint venture ed e' oggi socio unico al 100%. Anche la pagina LinkedIn indicata (nl.linkedin.com/company/rompa-tanneries) si presenta ora come 'Vitelco Leather'.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco and Rompa Leder however decided to dissolve this joint venture and Vitelco took over the Rompa Tanneries shares from Rompa Leder. Vitelco is now 100% owner of the tannery and changes its name to Vitelco Leather B.V.'

**Correzione proposta:** Vitelco Leather B.V.

#### Rompa Tanneries B.V. — campo `dimensione`

Assetto proprietario dichiarato errato: il campo indica ancora 'Soci: PALI Group (Den Bosch, vitello) e Rompa Leather (Rijen)', ma la JV e' stata sciolta e Vitelco (PALI Group) e' socio unico al 100%. La societa' e' quindi una controllata integrale di gruppo (PALI Group, 's-Hertogenbosch): la compliance EUDR si decide a livello di capogruppo, il lead va riqualificato o scartato.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco is now 100% owner of the tannery'

**Correzione proposta:** Controllata al 100% di Vitelco B.V. (PALI Group), 's-Hertogenbosch


### Belgio (4)

#### Extremis NV — campo `referente`

Referente non aggiornato: Dirk Wynants e' oggi owner e chief designer, NON il vertice esecutivo. L'amministratore delegato in carica e' Valentine Batjoens, nominata CEO in successione a Yff Vandendriessche. Il campo attribuisce erroneamente a Wynants la funzione di vertice.

**Evidenza:** https://www.lovethatdesign.com/?post_type=news&p=378797 e https://www.linkedin.com/posts/extremis_meet-our-new-ceo-aka-captain-of-the-ship-activity-7046080915592069121-Z6QI - frammento: "Extremis appointed Valentine Batjoens as its new Chief Executive Officer... continue the course of outgoing CEO Yff Vandendriessche. However, Dirk Wynants remains as the owner and chief designer of Extremis"

**Correzione proposta:** Valentine Batjoens — CEO (Dirk Wynants resta fondatore/proprietario e chief designer)

#### Sas NV (Sas Coffee) — campo `dimensione`

CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elenca come societa' di portafoglio con 'complete repositioning and rebranding'. Le decisioni di compliance EUDR si prendono a livello di gruppo/fondo: lead NON valido come impresa familiare indipendente.

**Evidenza:** https://nimbus.com/ - 'Sas Coffee, a specialist in private label coffee, recently became part of the Nimbus portfolio'; https://www.made-in.be/kempen/kempens-koffiebedrijf-miko-blijft-achter-met-financiele-kater-van-20-miljoen-euro-na-verkoop-sas-koffie/ ; https://fd.nl/bedrijfsleven/1517530/investeerder-nimbus-koopt-belgische-koffiebrander-sas

**Correzione proposta:** Segnalare nel campo dimensione: 'controllata di Nimbus Investments (NL) dal 24-05-2024 - non indipendente' oppure rimuovere il lead

#### Silco NV — campo `denominazione`

RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui presidente e' Philippe Van Gestel e che e' controllata dalla famiglia Van Gestel (Noord Natie). L'amministratore di Silco indicato nel foglio e' 'Philip Van Gestel'. Forte indizio che Silco sia un veicolo del gruppo Efico/Van Gestel e non una trading house indipendente: in tal caso la compliance EUDR si deciderebbe a livello di capogruppo e il lead non sarebbe valido. DA CONFERMARE il legame societario.

**Evidenza:** https://www.tendata.com/en/buyer/efico-nv-italielei-181-2000-antwerp-belgium-BELN376bec4ab92398acd7b73f7696701f41.html - 'EFICO NV. ITALIELEI 181. 2000 ANTWERP BELGIUM'; https://www.companyweb.be/en/0431096011/efico ; frammento: 'Philippe Van Gestel is the chairman of Efico... Noord Natie (the Van Gestel family) has control over Efico'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Tannerie Masure SA — campo `denominazione`

Societa' non indipendente: dal 2014 Tannerie Masure fa parte del Groupe Saturne insieme alla francese Tannerie Fortier-Beaulieu (Roanne). Il referente indicato, Olivier Lesage, risulta anche dirigente della holding francese FINANCIERE SATURNE: le decisioni di compliance EUDR si giocano a livello di capogruppo francese, non sulla controllata belga.

**Evidenza:** https://groupe-saturne.com/en/saturne-group/ - frammento: "In 2014, Fortier-Beaulieu associated with the Masure tannery in Estaimbourg (Belgium) to form the independent Groupe Saturne"; https://www.societe.com/manager/Olivier.LESAGE.s8sT-HgWTfO.html (Olivier LESAGE - FINANCIERE SATURNE)

**Correzione proposta:** Valutare il lead a livello di capogruppo Groupe Saturne / Financiere Saturne (FR): la societa' belga non e' un centro decisionale autonomo per la compliance EUDR


---

## 5. Casi di gravità MEDIA (60)

_Dato dubbio o obsoleto: da rinfrescare prima del contatto, non necessariamente errato._


### Danimarca (18)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| ALL CREATIVE A/S | dimensione | Il campo non contiene alcun dato economico: non riporta ne' fatturato ne' bruttofortjeneste ne' anno di riferimento, ma solo una fascia di dipendenti '11-50' presa da LinkedIn e priva di data. La collocazione nella forbice target 5-40 M€ resta quindi | https://www.proff.dk/firma/all-creative-as/r%C3%B8dovre/producenter/GSG8C7I016D (scheda regnskab della societa', CVR 21124796) |  |
| COPENHAGEN CHOCOLATE FACTORY ApS | email | L'email pubblicata come recapito ufficiale nelle condizioni di vendita e sulle schede societarie e' kundeservice@simplychocolate.dk (tel. +45 3634 0070). info@simplychocolate.dk, riportata nel foglio, non e' stata ritrovata letteralmente in nessuna f | https://www.simplychocolate.dk/pages/handelsbetingelser e https://www.proff.dk/firma/copenhagen-chocolate-factory-aps/kastrup/producenter/0JI778I016D  | kundeservice@simplychocolate.dk |
| Estate Coffee Copenhagen A/S | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: il CVR 18179407 e' oggi registrato come Smage-Compagniet A/S, Holmevej 10, 5683 Haarby. La cronologia e' ricostruita dall'azienda stessa: fondata nei primi anni '90 (tra i fondatori Claus Meyer) come Chokolade  | https://smage-compagniet.dk/estate-coffee/ - 'Virksomhedens historie gaar tilbage til starten af 1990'erne, hvor den blev grundlagt af blandt andre Cl | Smage-Compagniet A/S (CVR 18179407) - gia' Estate Coffee Copenhagen A/S / Chokolade Compagniet |
| INNOVATION LIVING A/S (già Innovation Rander | dimensione | Dato obsoleto: il campo cita il bruttofortjeneste 2023 (47,3 M DKK) mentre l'ultimo bilancio disponibile (2025) riporta 40 M DKK, quindi in calo. Anche la composizione del gruppo è imprecisa: INNOVATION HOLDING A/S conta 10 società, non 8. | https://www.proff.dk/firma/innovation-living-as/randers-n%C3%B8/m%C3%B8bler/13462KI015G — frammento: "In 2025, the company reported a gross profit of  | Bruttofortjeneste 40 mio DKK (~5,4 M€) nel 2025 (proff.dk, CVR 65699516); fatturato non pubblicato; gruppo INNOVATION HO |
| JKE DESIGN A/S | dimensione | Dato obsoleto: il campo riporta il bruttofortjeneste 2023 (55,6 M DKK) mentre il bilancio 2024 depositato indica 50 M DKK, in ulteriore calo rispetto al 2022 (58,7 M DKK). La stima ricavi "~20-27 M€" resta non verificata. | https://regnskaber.cvrapi.dk/21017236/ (Årsrapport 2024 JKE DESIGN A/S, Gl Klæstrupvej 75, 9740 Jerslev J) — frammento: "In 2024, the company showed a | Bruttofortjeneste 50 mio DKK (~6,7 M€) nel 2024 (årsrapport 2024, CVR 63271012); fatturato non pubblicato |
| Just Coffee | denominazione | Ragione sociale CVR ora VERIFICATA: non e' ne' ApS ne' A/S ne' amba, e' un INTERESSENTSKAB. Denominazione legale 'Just Coffee I/S', CVR 35492380, costituita il 01-01-2014, sede Frederiksborgvej 551, 4000 Roskilde; soci illimitatamente responsabili Ma | https://cvrapi.dk/virksomhed/dk/just-coffee-is/35492380 e https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Just Coffee I/ | Just Coffee I/S - CVR 35492380 (forma giuridica: interessentskab) |
| KRYDSFINER-HANDELEN A/S | dimensione | Controllata di gruppo estero: dall'autunno 2023 la societa' e' stata venduta da Carsten Rittig a Fritzoe Nordic Holding AS (Norvegia), che ne detiene il controllo. Il record lo accenna in forma dubitativa ('riconducibile a proprieta' nordica/scandina | https://fritzoenordic.no/en/selskap/krydsfiner-handelen-a-s/ ; https://www.wood-supply.dk/article/view/1053393/nordmaend_kober_95_ar_gammelt_dansk_fam | Dichiarare in modo esplicito: controllata al 100% da Fritzoe Nordic Holding AS (NO) dall'autunno 2023 |
| KVIST INDUSTRIES A/S | dimensione | Assetto proprietario non dichiarato: la societa' figura nel portafoglio del fondo di private equity danese Dansk Ejerkapital ed e' controllata tramite KVIST HOLDING A/S (CVR 21746886, Esbjerg). Il campo dimensione non menziona il legame di gruppo/par | https://www.danskejerkapital.dk/portefoelje/kvist-industries/ ; https://www.proff.dk/firma/kvist-industries-as/esbjerg/hovedkontortjenester/GMGAWAI10N | Aggiungere: controllata da KVIST HOLDING A/S, partecipata dal fondo Dansk Ejerkapital; fatturato non pubblicato (bilanci |
| LILLEHEDEN A/S | dimensione | Controllata di gruppo: la societa' fa parte di Nordic Wood Industries A/S (CVR 37385603), che dal 12.05.2025 ha un nuovo adm. direktor di gruppo (Holger Carsten Hansen). Il legame e' gia' correttamente dichiarato nel campo, quindi non e' un errore di | https://nowi.dk/limtraesproducent-styrker-produktionen-markant/ ; https://www.proff.dk/firma/nordic-wood-industries-as/hampen/investeringsselskaper/0M | Aggiornare il bruttofortjeneste all'ultimo esercizio disponibile e valutare il lead a livello di Nordic Wood Industries  |
| MULTIFORM A/S | dimensione | Controllata di gruppo: capogruppo BALLINGSLOV INTERNATIONAL DANMARK A/S (gruppo svedese Ballingslov International / Stena Adactum). Il legame e' gia' dichiarato correttamente nel record, quindi il rilievo riguarda la validita' del lead (compliance EU | https://www.proff.dk/firma/multiform-as/kib%C3%A6k/producenter/GLGFCDI016D - 'Multiform er en del af en koncern, hvor modervirksomheden er BALLINGSLOV |  |
| NPI (Nordic Panel Import) | referente | Campo referente vuoto pur essendo il direktor reperibile nelle fonti pubbliche: risulta Theis Graves Larsen (uno dei due fondatori, 2002). | https://www.proff.dk/firma/npi-as/l%C3%B8sning/t%C3%B8mmer-tr%C3%A6last-og-byggevarer-agentur-og-engros/0MA0H6I10LA - direktor: Theis Graves Larsen ;  | Theis Graves Larsen, Direktor (da riconfermare al primo contatto) |
| SIKA DESIGN A/S | dimensione | Dato di bilancio obsoleto: l'utile lordo di 29 M DKK e' riferito al 2021 (cinque esercizi fa) e la stima ricavi '~8-10 M€' non e' verificata. Anche il numero di addetti e' disallineato: le fonti aggiornate riportano 19 dipendenti / 17 FTE a novembre  | https://www.paqle.dk/p/sika-design-a-s/330977 (19 ansatte, 17 FTE nov. 2025) ; https://ownr.dk/companies/public-profile/31476712 | Aggiornare bruttofortjeneste e addetti all'ultimo bilancio disponibile |
| SOFTLINE A/S | dimensione | Dato di margine lordo riferito al 2023 e stima ricavi '~12-18 M€' non verificata: la collocazione nella forbice target 5-40 M€ resta non dimostrata. DA CONFERMARE su bilancio piu' recente. Referente Finn Herluf Sorensen e stato 'Normal' della societa | https://ownr.dk/companies/public-profile/27266355 (status Normal) ; https://folketidende.dk/erhverv/produktudvikling-er-krumtappen-hos-softline-a-s (' |  |
| SOMMER-SAVEX A/S | dimensione | Il campo dichiara 'fatturato non verificato / dati di bilancio non accessibili', ma i dati esistono e sono pubblici: bruttofortjeneste 13,06 M DKK nel 2024 (~1,75 M€) contro 14,82 M DKK nel 2023, con esercizio 2024-25 chiuso in perdita (-1,37 M DKK). | https://ownr.dk/companies/public-profile/13923795 ; https://vismarating.dk/firma/13923795-sommer-savex-as - 'bruttofortjeneste i 2024 pa 13.059.301 DK | Bruttofortjeneste 13,06 M DKK (2024, ~1,75 M€), risultato 2024-25 negativo; fatturato non pubblicato (classe B). Taglia  |
| Skagerak Denmark A/S | dimensione | Dati economici obsoleti: utile lordo 53,7 M DKK riferito al 2021 e addetti al dicembre 2022, cioe' antecedenti o coevi all'acquisizione da parte di Fritz Hansen. La stima ricavi '~15-22 M€' non e' verificata e non e' piu' rappresentativa dell'assetto | https://estatistik.dk/virksomhed/skagerak-denmark-as/28855990 ; https://www.dezeen.com/2021/12/15/fritz-hansen-acquires-skagerak/ |  |
| SØRENSEN LÆDER A/S (Sorensen Leather) | dimensione | Dato obsoleto e non allineato alla fonte: il record indica bruttofortjeneste 23,85 mio DKK (2022) e ca. 20 dipendenti, mentre la scheda proff.dk attuale (CVR 50828514) riporta bruttofortjeneste 13.056 tkr (13,06 mio DKK ≈ 1,75 M€) e 16 dipendenti. In | https://www.proff.dk/regnskab/s%C3%B8rensen-l%C3%A6der-as/lystrup/skind-l%C3%A6der-og-pels/GKJEN4I07RD — frammento: "Bruttofortjeneste: 13.056 tkr ... | Bruttofortjeneste 13,06 mio DKK (~1,75 M€) e 16 dipendenti — proff.dk, CVR 50828514 (ultimo bilancio disponibile); fattu |
| TJOERNEHOEJ MOELLE A/S | dimensione | Fatturato recente NON reperito: il dato del foglio resta quello del 2003 (80 M DKK). In 3 ricerche l'unico bilancio individuato e' il PDF dell'esercizio 2011 su regnskaber.cvrapi.dk e menzioni di dati fino al 2014; nessuna cifra 2023-2025 emerge dall | https://regnskaber.cvrapi.dk/21057143/Y3ZyLmRrOi8vcGRmcy8zNDE3NTAxMjtBL1M1MDg2MTsyMDExMDEwMTsyMDExMTIzMTtSO1I.pdf - bilancio 01-01-2011/31-12-2011; ht |  |
| VESTJYSK SPECIALFODER ApS | filiera | Perimetro EUDR DA CONFERMARE: l'oggetto sociale registrato e' generico ('handelsvirksomhed inden for specialfoder'), classificato proff.dk come 'engroshandel - annet'. Nessuna fonte pubblica conferma l'impiego di soia (unica commodity EUDR plausibile | https://royalfireworks.dk/forhandler/vestjysk-specialfoder-aps/ - scheda rivenditore fuochi d'artificio a Vemb; https://www.proff.dk/firma/vestjysk-sp |  |

### Svezia (15)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Abstracta AB | dimensione | Lead di dubbia validità (non errore di dato): controllata al 100% di Lammhults Design Group AB, gruppo quotato — la compliance EUDR si decide alla capogruppo. Il legame è però già dichiarato correttamente nel campo. | allabolag.se: «Abstracta Aktiebolags moderbolag är Lammhults Design Group AB»; lammhultsdesigngroup.com/en/companies/abstracta/ — parte del gruppo dal |  |
| Aktiebolaget Karlaträ | referente | Campo referente e ruolo vuoti benché il dato sia pubblico: VD registrato è Bo Anders Ingemar Larsson. | allabolag.se befattningshavare (556081-8782): «VD för Aktiebolaget Karlaträ är Bo Anders Ingemar Larsson» — https://www.allabolag.se/befattningshavare | Referente: Bo Anders Ingemar Larsson — Ruolo: VD (verkställande direktör) |
| Aktiebolaget Karlaträ | dimensione | Fatturato obsoleto: il record riporta 89 711 KSEK (~7,9 M€); l'ultimo esercizio disponibile (2025) è 100 399 KSEK ≈ 8,9 M€. | hitta.se/allabolag: «AB Karlaträ omsatte 100 399 000,00 kr senaste räkenskapsåret (2025)»; 12 anställda confermati. | ≈8,9 M€ (100 399 KSEK, esercizio 2025) / 12 dipendenti |
| Aktiebolaget Karlaträ | dimensione | Legame di gruppo non dichiarato: la società appartiene a una koncern di 2 società con moderbolag Karlaträ Försäljning Aktiebolag (holding di famiglia/vendita). | allabolag.se: «Aktiebolaget Karlaträ ingår i en koncern med totalt 2 bolag, där moderbolaget är Karlaträ Försäljning Aktiebolag» — https://allabolag.s | Aggiungere: 'koncern di 2 società, moderbolag Karlaträ Försäljning AB (holding di vendita del medesimo gruppo familiare) |
| Balungstrands Sågverk AB | dimensione | Rischio di continuità operativa non segnalato: nuovo 'varsel' (procedura di licenziamento collettivo) alla segheria; il fatturato 2025 di 114.525 KSEK (~10,1 M€) è confermato ma con calo -70,1% e risultato di soli 25 KSEK. | Skogsaktuellt, «Nytt varsel vid Balungstrands sågverk» — https://www.skogsaktuellt.se/artikel/2238122/nytt-varsel-vid-balungstrands-sgverk.html ; alla |  |
| Baseco Golv Aktiebolag | referente | Campo referente e ruolo vuoti benché il dato sia pubblico: VD registrato è Karl Eskil Marcus Abrahamsson. | allabolag.se befattningar (556295-1953): «VD är Karl Eskil Marcus Abrahamsson» — https://www.allabolag.se/5562951953/befattningar | Referente: Marcus Abrahamsson — Ruolo: VD (verkställande direktör) |
| Brattby Sågverks AB | dimensione | Legame di gruppo non dichiarato: la società fa parte di una koncern con moderbolag Brattby Trading Aktiebolag. Fatturato 143,4 MSEK (~12,7 M€) e 32 dipendenti 2024 confermati. | allabolag.se (556415-5066): «företaget ingår i en koncern med moderbolag Brattby Trading Aktiebolag»; «omsättning 143,4 MSEK, vinst 11,3 MSEK, +26% (2 | Aggiungere: 'koncern con moderbolag Brattby Trading Aktiebolag' |
| Brännfors Träförädling Aktiebolag | email | Email indicata come 'n.d.' benché l'azienda abbia una pagina contatti pubblica: dato mancante recuperabile. | https://brannforstraforadling.se/kontakta-oss/ — «Kontakta oss - Brännfors Träförädling»; tel. 0910-71 51 00, Ostvik 152, 934 91 Kåge |  |
| Brännfors Träförädling Aktiebolag | referente | Referente e ruolo vuoti. Le fonti non indicano un VD registrato ma solo cariche di consiglio (Åsa Kärr; Lars Stefan Edström come ordförande): DA CONFERMARE chi sia il vertice operativo. | allabolag/proff (556103-8695): risultano ordförande/styrelseledamot Åsa Kärr e Lars Stefan Edström; nessun VD riportato. |  |
| Bäckebrons Sågverk Aktiebolag | dimensione | Fatturato 2025 discordante tra le fonti (142.474 KSEK su allabolag vs 148.264 KSEK su altra fonte) e risultato crollato a 28 KSEK (-99,8%): il dato ≈12,6 M€ va indicato come stimato/DA CONFERMARE. Confermato invece il calo -66,7% sul 2024. | allabolag: «142 474 kSEK, -66,7% 2024→2025, resultat 28 kSEK (-99,8%)»; vf.se 31/07/2025 «Omsättningen tar fart – men resultatet sjunker för Bäckebron |  |
| Ekstrands Dörrar & Fönster AB | dimensione | Lead di dubbia validità (non errore di dato): società di un gruppo di 6 società con capogruppo Ekstrand & Son Aktiebolag, correttamente dichiarata nel record. Tutti gli altri dati (167.769 KSEK 2025 ≈ 14,8 M€, 84 dip., VD Heidi Ekstrand) risultano co | allabolag.se (556570-0621): «84 anställda, resultat 1 565 KSEK, omsättning 167 769 KSEK (2025) ... ingår i en koncern med totalt 6 bolag, moderbolaget |  |
| Fogia Collection Aktiebolag | dimensione | Lead di dubbia validità (non errore di dato): controllata di Scandinavian Design Partners AB, legame già dichiarato correttamente. Tutti i dati (108.304 KSEK 2024 ≈ 9,6 M€, risultato 15.276 KSEK, 18 dip. da 21 nel 2023, VD Franz Marcus Huber) risulta | allabolag.se (556204-6218): «omsättning 108 304 KSEK, resultat 15 276 KSEK (2024), 18 anställda ... ingår i en koncern där moderbolaget är Scandinavia |  |
| Glimakra of Sweden AB | dimensione | Lead di dubbia validità (non errore di dato): controllata di Garpco Aktiebolag dal 2007, gruppo di 25 società con 311 addetti e 667,0 MSEK. Il legame è dichiarato ma il record lo sottodimensiona ('controllata di Garpco AB, con 2 sub-controllate'): la | allabolag.se koncern (556120-7837): «moderbolaget är Garpco Aktiebolag ... koncernen omfattar totalt 25 bolag med 311 anställda och 667,0 MSEK i omsät | Controllata di Garpco Aktiebolag (dal 2007), koncern di 25 società / 311 addetti / 667 MSEK |
| Gärsnäs Aktiebolag | dimensione | Lead di dubbia validità (non errore di dato): controllata di Bordet i Stockholm Aktiebolag, legame già dichiarato correttamente. Esiste inoltre notizia stampa di cambio di proprietà ('Gärsnäs AB får ny ägare') di cui andrebbe verificata la data. Dati | allabolag.se (556044-4746): «moderbolaget är Bordet i Stockholm Aktiebolag»; «37 anställda, resultat 583 KSEK, omsättning 80 711 KSEK (2023)»; https:/ |  |
| Horreds Möbel Aktiebolag | dimensione | Dato 2022 NON aggiornabile con certezza e anzi CONTRADDETTO. allabolag.se riporta oggi per Horreds Möbel AB (556365-1974) 45 dipendenti (contro i 50 del 2022) e un intervallo di fatturato 50.000-99.999 tkr, cioè 50-99,9 MSEK ≈ 4,4-8,8 M€: sarebbe una | https://www.allabolag.se/foretag/horreds-m%C3%B6bel-aktiebolag/horred/butiksinredningar-butiksutrustningar/2K0GDC6I5YDBD - '45 anställda ... omsättnin |  |

### Olanda (9)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Arco Meubelfabriek B.V. | referente | Referente da riconfermare: le fonti pubbliche indicano Jorre van Ast alla guida dell'azienda familiare dal 2011 come creative director, affiancato dal managing director Jan Tichelaar. 'F. van Ast' risulta solo dal dato Company.info (algemeen directeu | https://www.vno-ncw.nl/forum/meubelfabriek-arco-120-jaar-vallen-opstaan-en-weer-doorgaan - frammento: 'In 2011 kwam het familiebedrijf onder leiding v |  |
| BeBo Parket B.V. | dimensione | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dichiarata nel campo (solo il legame con BeBo Groep B. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'samen met investeerder Nobel Capital Partners' |  |
| BeBo Parket B.V. | dimensione | Il fatturato di ca. 20 M EUR e' datato 2024 nel record, ma il dato di 20 milioni compare nell'articolo sul passaggio generazionale del 2022 (riferito all'esercizio precedente). Anno del dato DA CONFERMARE. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Vorig jaar had Bebo Parket een omzet van 20 mil |  |
| BeBo Parket B.V. | linkedin | Il link LinkedIn e' il profilo personale di Frans Bolier (nl.linkedin.com/in/frans-bolier-b64b394a), non la pagina aziendale di BeBo Parket. Trattandosi di un ex titolare uscito nel 2022, il link non e' utilizzabile. | https://nl.linkedin.com/in/frans-bolier-b64b394a - titolo: 'Frans Bolier - directeur mede-eigenaar beboparket BV' |  |
| De Leeuw Huidenhandel N.V. | referente | Referente e ruolo assenti. Il direttore statutario iscritto al KVK e' una persona giuridica (LHST B.V., algemeen directeur dal 2022): manca un nome fisico per il contatto commerciale. Nei frammenti pubblici compare solo Christian Hossu (chossu@deleeu | https://companyinfo.nl/organisatieprofiel/groothandel-in-huiden-en-vellen/de-leeuw-huidenhandel-n-v-winterswijk-08011164-000017531705 - frammento: 'LH |  |
| Origin Bridge (Barchem) | denominazione | Forma giuridica NON risolta dopo 3 ricerche: nessuna fonte pubblica indicizzata riporta la rechtsvorm né una denominazione legale con suffisso. Restano solo KVK 70878315 e P.IVA NL001587917B24 pubblicati dall'azienda stessa. La struttura del numero I | https://originbridge.coffee/legal-information/ e https://originbridge.coffee/contact/ - 'Heidehoflaan 2B, 7244AG Barchem, The Netherlands ... CoC: 708 |  |
| Origin Bridge (Barchem) | email | L'email del foglio (info@bridgetoorigin.com) NON è quella principale del sito ufficiale: la pagina di contatto di originbridge.coffee indica come recapito dell'entità olandese europe@originbridge.coffee, tel. +31 85 301 6984. info@bridgetoorigin.com  | https://originbridge.coffee/contact/ - 'Origin Bridge Netherlands, Heidehoflaan 2B, 7244AG Barchem ... +31 85 301 6984 ... europe@originbridge.coffee' | europe@originbridge.coffee |
| Rompa Tanneries B.V. | email | Email e sito legati al vecchio marchio (sales@rompa-tanneries.com / www.rompa-tanneries.com). Con la ridenominazione in Vitelco Leather il dominio di riferimento del gruppo e' vitelco.nl; il vecchio sito hulshof.com rimanda ancora a 'Rompa Tanneries' | http://www.hulshof.com/ (titolo pagina: 'Rompa Tanneries') e https://www.vitelco.nl/en/about-us |  |
| Rompa Tanneries B.V. | referente | Referente e ruolo vuoti. Le fonti stampa locali citano Twan de Bie come 'directeur leerlooierij' dello stabilimento di Lichtenvoorde. DA CONFERMARE la carica attuale dopo il passaggio a Vitelco Leather. | https://www.gld.nl/nieuws/2414011/directeur-leerlooierij-laat-de-wethouder-bellen-dan-lossen-we-het-als-volwassen-mensen-op - frammento: 'De directeur |  |

### Belgio (18)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Bulo NV | referente | Referente probabilmente non aggiornato. Dirk Busschop risulta CEO in fonti risalenti (2009); l'azienda e' oggi guidata dalla terza generazione, Carlo e Louis Busschop, con Carlo Busschop indicato come Managing Director / CEO in fonti recenti. Da rico | https://www.bulo.com/third_generation/ e https://rocketreach.co/carlo-busschop-email_93406361 - frammento: "Carlo Busschop, based in Mechelen, BE, is  | Carlo Busschop — gedelegeerd bestuurder / Managing Director (DA CONFERMARE) |
| Buzzispace NV | email | Email 'n.d.': record privo di indirizzo di contatto nonostante il sito buzzi.space sia attivo. DA CONFERMARE. | https://www.buzzi.space/brand (sito attivo, nessun indirizzo e-mail nei frammenti) |  |
| Carlens NV | referente | Referente e ruolo assenti. Le fonti pubbliche citano 'Carl Carlens' in contesto gestionale, mentre il campo dimensione ipotizza 'Luc Carlens' da FinCheck: nomi discordanti, nessuno dei due confermato come gedelegeerd bestuurder. DA CONFERMARE su BCE/ | https://www.limoco-industries.be/referenties/240-houthandel-carlens-keuze-voor-leverancier-dicht-bij-huis - frammento: risultati che referenziano "Car |  |
| Confortluxe NV | referente | Referente e ruolo assenti benche' gli amministratori siano pubblici e confermati (Jacqueline Pauwels, Jimmy Ollevier, Heidi Ollevier). Il fondatore Andre Ollevier, storico gedelegeerd bestuurder, e' deceduto: non usarlo come referente. Da attribuire  | https://fincheck.be/en/confortluxe/0412.863.078/Wervik/connections - frammento: "The current board members of Confortluxe are Jacqueline Pauwels, Jimm | Jimmy Ollevier — bestuurder (ruolo di gedelegeerd bestuurder DA CONFERMARE) |
| Decolvenaere BV | dimensione | Fatturato fortemente sottostimato. Il campo riporta 'oltre 10 milioni di euro' (fonte giornalistica Sterck Magazine), ma i dati di bilancio piu' recenti indicano un fatturato totale di 38.585.036 EUR, con altre fonti che collocano l'azienda nella fas | Frammenti di ricerca su Decolvenaere BV (BE 0400.079.171): "The most recent financial statements show a total turnover of EUR 38,585,036.00" e "turnov | Fatturato ~38,6 M EUR (ultimo bilancio depositato NBB) — DA RICONFERMARE sulla fonte NBB primaria |
| Extremis NV | dimensione | Fatturato potenzialmente obsoleto: il campo riporta 12.900.125 EUR e 24,8 FTE dall'ultimo bilancio, ma risulta gia' depositato un bilancio piu' recente (deposito 02-07-2026) i cui dati non sono riflessi nel record. DA AGGIORNARE. | https://www.companyweb.be/en/0434625128/extremis - frammento: "The most recent financial statements of Extremis were filed on 02-07-2026" |  |
| Houthandel Denis Luyten NV | referente | Referente e ruolo assenti; il campo dimensione dichiara esplicitamente che il nome del gestore non e' pubblicato. Nemmeno le ricerche mirate restituiscono il gedelegeerd bestuurder in carica (azienda alla 4a generazione della famiglia Luyten). DA CON | https://www.companyweb.be/en/0403778831/houthandel-denis-luyten - frammento: "At the time of its most recent financial statements, Houthandel Denis Lu |  |
| Hulpiau Hides BV | referente | Referente e ruolo assenti. Le fonti pubbliche citano Raimond Hulpiau come 'current senior manager' (fratello del fondatore Christiaan Hulpiau), ma il ruolo formale (zaakvoerder/gedelegeerd bestuurder) non e' pubblicato: DA CONFERMARE. | https://www.hulpiauhides.com/en/about-us/ - frammento: "Christiaan Hulpiau, brother of current senior manager Raimond Hulpiau, founded Hulpiau Hides" |  |
| Jori NV | referente | Referente e ruolo assenti e non ricostruibili dalle fonti pubbliche consultate: nessun nome di gedelegeerd bestuurder/CEO emerge per Jori NV (BE 0888.984.313). DA CONFERMARE. Fatturato 16.143.273 EUR, 106,8 FTE e sede Hoogweg 52, 8940 Wervik risultan | https://www.companyweb.be/en/0888984313/jori - frammento: "with a revenue of EUR 16.143.273, Jori from Wervik ranks 19th in the furniture manufacturin |  |
| Keukenontwerpers NV | filiera | Perimetro EUDR debole. L'azienda opera con l'insegna SieMatic Keukenontwerpers come rivenditore/installatore a valle di cucine prodotte dalla tedesca SieMatic: non e' l'operatore che immette per primo il prodotto in legno sul mercato UE (lo e' il fab | https://www.keukenontwerpers.com/ e https://trustlocal.be/antwerpen/geel/keukenbouwer/siematic-keukenontwerpers/ - frammento: "SieMatic Keukenontwerpe |  |
| Keukenontwerpers NV | referente | Referente e ruolo assenti; nessuna fonte pubblica restituisce il gedelegeerd bestuurder di Keukenontwerpers NV (BE 0472.648.534). L'email geel@keukenontwerpers.com non e' inoltre riscontrabile letteralmente nei frammenti. DA CONFERMARE entrambi. Fatt | https://trendstop.knack.be/nl/detail/472648534/keukenontwerpers.aspx - frammento: "With a turnover of 16,033,016 euros, Keukenontwerpers is ranked 7th |  |
| Lavrijsen Houtbedrijf NV | dimensione | Fatturato obsoleto e indirizzo errato. Il campo riporta 12.763.339 EUR (dato trendstop), mentre l'ultimo bilancio depositato indica 14.093.447 EUR e 23,1 FTE (non '20-49 addetti'). Inoltre la sede legale registrata e' Koning-Albertstraat 123, 2440 Ge | https://www.companyweb.be/en/0407106030/houtbedrijf-lavrijsen - frammento: "Houtbedrijf Lavrijsen recorded a total turnover of EUR 14,093,447.00... Th | Fatturato 14.093.447 EUR e 23,1 FTE (ultimo bilancio NBB); sede Koning-Albertstraat 123, 2440 Geel |
| Radermecker SRL | referente | Referente e ruolo assenti. La conceria e' stata rilevata nell'aprile 2016 da due ingegneri francesi, Loic Honore e Nicolas Quintin, che ne sono gli attuali gestori: candidati referenti (gerant / administrateur delegue) da confermare su fonte societar | https://www.lavenir.net/regions/wallonie-picarde/comines-warneton/2022/01/14/cuirs-selliers-la-specialite-de-la-tannerie-radermecker-a-comines-YLAPU6L |  |
| Radermecker SRL | email | Email 'n.d.': nessun indirizzo di contatto nel record. Il sito radermecker.com espone una pagina contatti, ma l'indirizzo non e' recuperabile via frammenti di ricerca. DA CONFERMARE. | https://www.radermecker.com/pages/on-parle-de-nous-dans-la-presse (sito attivo, indirizzo e-mail non estraibile dai frammenti) |  |
| Sas NV (Sas Coffee) | referente | Herman Sas risulta ancora 'gedelegeerd bestuurder' negli estratti KBO pubblicati (pappers.be, insieme a Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HELFINCO), ma nessuna fonte post-cessione a Nimbus (05/2024) lo riconferma al vertice operati | https://www.pappers.be/nl/company/sas-0404190783 - 'Herman Sas is de gedelegeerd bestuurder; overige bestuurders: Dominic Sas, Danielle Vanden Eede, M |  |
| Sas NV (Sas Coffee) | email | L'email nel foglio (info@sas-koffie.be) NON e' quella pubblicata sul sito ufficiale sas-coffee.com: la pagina di contatto riporta CUSTOMERSERVICE@SAS-COFFEE.COM, tel. +32 14 61 12 00, indirizzo LILSEDIJK 36 - 2340 BEERSE. info@sas-koffie.be resta rep | https://sas-coffee.com/en/contact/ - 'CUSTOMERSERVICE@SAS-COFFEE.COM \| +32 14 61 12 00 \| LILSEDIJK 36 - 2340 BEERSE - BELGIUM' | customerservice@sas-coffee.com ; sede Lilsedijk 36, 2340 Beerse DA CONFERMARE |
| Silco NV | dimensione | Discordanza 4,8 vs 8,4 M€ NON risolta: le due banche dati continuano a riportare cifre diverse per lo stesso ultimo bilancio depositato (14-06-2024). Trendstop: EUR 8.358.215 (23a nel settore 'koffie en thee'); Companyweb/Fincheck: EUR 4.843.986. Sen | https://trendstop.knack.be/nl/detail/715792692/silco.aspx - 'omzet van 8.358.215 euro, 23e in de sector Koffie en thee'; https://www.companyweb.be/en/ |  |
| Tannerie Masure SA | email | Email 'n.d.'. Il sito masure.be ha una pagina contatti attiva ma l'indirizzo non e' verificabile dai frammenti. DA CONFERMARE. | https://www.masure.be/contact (pagina contatti esistente; indirizzo e-mail non presente nei frammenti) |  |

---

## 6. Casi di gravità BASSA (41)

_Refusi formali e incoerenze di stile._


### Danimarca (14)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| ALL CREATIVE A/S | referente | Nome del referente incompleto: l'adm. direktor registrato e' Mette Juhl Christensen. Email info@allcreative.dk e sede (vendite Islevdalvej 214, Rodovre; produzione Tulipvej 3, Vejle) risultano confermate. | https://www.proff.dk/firma/all-creative-as/r%C3%B8dovre/papir-og-papirprodukter-produktion/GSG8C7I10K1 (adm. direktor Mette Juhl Christensen) ; https: | Mette Juhl Christensen, Adm. direktor |
| BØJSØ DØRE & VINDUER A/S | dimensione | Organico non allineato: le fonti reperite indicano 43 dipendenti, il record ne indica 41. Inoltre il campo non riporta alcun dato economico verificato (né fatturato né bruttofortjeneste): la collocazione in forbice 5-40 M€ resta una stima non verific | https://www.proff.dk/firma/b%C3%B8js%C3%B8-d%C3%B8re-vinduer-as/vorbasse/producenter/GJL0QJI016D — frammento: "Bøjsø doors and windows was founded in  | 43 dipendenti (proff.dk, CVR 12224494); dato economico da recuperare a bilancio |
| COPENHAGEN CHOCOLATE FACTORY ApS | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: CVR 32761844, Amager Landevej 123, 2770 Kastrup, costituita il 26-01-2010, ApS; opera con i binavne 'Simply Chocolate Copenhagen' e www.simplychocolate.dk; direttore Niels Ostenkaer; capogruppo SOLSTRA INVESTME | https://cvrapi.dk/virksomhed/dk/copenhagen-chocolate-factory-aps/32761844 ; https://www.simplychocolate.dk/pages/handelsbetingelser - 'www.simplychoco |  |
| FREDERICIA FURNITURE A/S | dimensione | Refuso nell'unità di misura: "risultato ante imposte 6,5 M€ DKK" mescola euro e corone danesi. Il valore va espresso in una sola valuta. | Testo del campo dimensione del record stesso: "risultato ante imposte 6,5 M€ DKK" | risultato ante imposte 6,5 mio DKK (~0,87 M€) |
| Farstrup Furniture A/S | ruolo | DA CONFERMARE: i registri elencano due direktør (Jan Andersen e Steen Cederholm-Johansen) senza qualificare esplicitamente Cederholm-Johansen come administrerende direktør. Il ruolo indicato non è riconfermato. | https://www.proff.dk/firma/farstrup-furniture-as/s%C3%B8nders%C3%B8/producenter/GKF1OMI016D — frammento: "The directors are Jan Andersen and Steen Ced |  |
| INNOVATION LIVING A/S (già Innovation Rander | linkedin | URL LinkedIn con prefisso di locale tedesco (de.linkedin.com) per una società danese. Non è un errore di pagina ma è incoerente con lo standard del dataset (dk. o www.). | Valore del record: https://de.linkedin.com/company/innovation-living-a-s | https://dk.linkedin.com/company/innovation-living-a-s |
| Just Coffee | sede | La sede registrata al CVR e' Frederiksborgvej 551, 4000 Roskilde, non Jyllinge: il riferimento a Jyllinge deriva dal testo promozionale del sito ('risteriet ligger paa en gaard i Jyllinge lige uden for Roskilde'). Il comune e' comunque Roskilde, Regi | https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Frederiksborgvej 551, 4000 Roskilde'; https://estatistik.dk/virksomhed/j | Frederiksborgvej 551, 4000 Roskilde, Regione Sjaelland |
| N. EILERSEN A/S | fonte | Il CVR corretto della societa' e' 35118519 (non indicato nel record, che non riporta il numero) e nel registro esiste anche una omonima 'Eilersen A/S' CVR 42555932: rischio di confusione tra le due entita' in fase di contatto/verifica. | https://ownr.dk/companies/public-profile/35118519 ; https://virmo.dk/firma/42555932-eilersen-as | Indicare esplicitamente CVR 35118519 per N. EILERSEN A/S |
| NIELAUS A/S | dimensione | Numero di dipendenti non allineato alla fonte citata: la scheda proff.dk (CVR 35480943) riporta 19 addetti, il record ne indica 11. | https://www.proff.dk/firma/nielaus-as/bramming/m%C3%B8bler/GUJZBOI015G — frammento: "NIELAUS A/S is a furniture production company located at Vejrup S | 19 dipendenti (proff.dk, CVR 35480943) — verificare l'anno di riferimento |
| NIELAUS A/S | email | DA CONFERMARE: l'indirizzo info@nielaus.dk non compare letteralmente in nessuna fonte pubblica reperita; la pagina Kontakt del sito ufficiale protegge l'indirizzo dagli spambot e non lo espone in chiaro nei frammenti. | https://www.nielaus.dk/da/om-os/kontakt — frammento: "Email: Available on their website (protected against spambots)" |  |
| NPI (Nordic Panel Import) | denominazione | Ragione sociale imprecisa: la societa' e' registrata al CVR 37418730 come 'NPI A/S' (forma giuridica A/S, non ApS). Il record lascia il punto come non verificato. | https://www.proff.dk/firma/npi-as/l%C3%B8sning/t%C3%B8mmer-tr%C3%A6last-og-byggevarer-agentur-og-engros/0MA0H6I10LA (NPI A/S - CVR-nr 37418730 - Losni | NPI A/S (Nordic Panel Import) |
| ONECOLLECTION A/S (House of Finn Juhl) | fonte | DA CONFERMARE: l'ID proff nell'URL citato (GXS757I015G) non coincide con quello della scheda ONECOLLECTION A/S CVR 29787786 reperita (GQYY8HI016D). L'URL potrebbe puntare a una scheda diversa/obsoleta. | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D — titolo: "ONECOLLECTION A/S - CVR-nr 29787786 - Ringkøbing" | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D |
| Skagerak Denmark A/S | linkedin | Il link LinkedIn punta alla vecchia denominazione 'trip-trap-denmark-a-s'; il marchio comunica oggi come Skagerak (by Fritz Hansen). DA CONFERMARE quale pagina sia quella ufficiale attiva. | https://www.linkedin.com/company/trip-trap-denmark-a-s (denominazione storica) ; https://www.dezeen.com/2021/12/15/fritz-hansen-acquires-skagerak/ |  |
| VERMUND LARSEN A/S (VELA / VERMUND) | sito | Disallineamento tra i canali: il sito indicato (vermund.eu) e' quello del solo marchio di design 'Vermund', mentre il sito istituzionale della societa' e del marchio principale e' vela.dk (coerente con l'email mail@vela.dk e con la pagina LinkedIn 'v | https://www.vela.dk/om-vela ; https://estatistik.dk/virksomhed/vermund-larsen-as/52796628/roller - 'Ny Vela Holding ApS tiltradte som ejer 100% af vir | https://www.vela.dk/ (con vermund.eu come sito del marchio design) |

### Svezia (15)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Abstracta AB | denominazione | Ragione sociale di registro imprecisa: il registro riporta 'Abstracta Aktiebolag' (org.nr 556046-3852), non 'Abstracta AB'. | https://www.allabolag.se/foretag/abstracta-aktiebolag/lammhult/m%C3%B6bler-produktion/2JYK1D8I63IJF — «Abstracta Aktiebolag - Org.nr 556046-3852 - Lam | Abstracta Aktiebolag |
| Blå Station Aktiebolag | linkedin | URL LinkedIn probabilmente errato: la pagina aziendale reperibile è linkedin.com/company/bla_station_ab, non /company/blastation. | https://www.linkedin.com/company/bla_station_ab/ («Blå Station AB \| LinkedIn») emerso in ricerca; nessun risultato per /company/blastation | https://www.linkedin.com/company/bla_station_ab/ |
| Blå Station Aktiebolag | sito | Dominio ufficiale da verificare: il sito istituzionale che compare nelle fonti è blastation.com (pagina 'Company'), mentre il record indica blastation.se. | https://blastation.com/company — «Company \| Blå Station» | https://blastation.com/ |
| Brattby Sågverks AB | referente | Nome del VD incompleto rispetto al registro: risulta Anne Marie Bergstrand (il record riporta solo 'Marie Bergstrand'). | allabolag.se befattningar: «VD: Anne Marie Bergstrand, 47 år» — https://www.allabolag.se/5564155066/befattningar | Anne Marie Bergstrand |
| Brattby Sågverks AB | linkedin | URL LinkedIn con slug anomalo (brattby-s-gverks-ab) non riscontrato in nessuna fonte: DA CONFERMARE che la pagina aziendale esista. | Nessun risultato LinkedIn nelle ricerche su 'Brattby Sågverks AB'; le fonti reperite sono allabolag, bolagsfakta, byggkatalogen, merinfo. |  |
| Bäckebrons Sågverk Aktiebolag | referente | Nome del VD incompleto rispetto al registro: risulta Rolf Stefan Gillberg (extern VD). | allabolag/syna (556099-7008): «extern VD är Rolf Stefan Gillberg» | Rolf Stefan Gillberg |
| Drömtrappor AB | referente | Nome del VD incompleto rispetto al registro: Johan Ludvig Gösta Jonsson. | allabolag/bolagsfakta (556309-7038): «VD är Johan Ludvig Gösta Jonsson» | Johan Ludvig Gösta Jonsson |
| Ekstrands Dörrar & Fönster AB | linkedin | Campo LinkedIn vuoto benché esista una pagina aziendale pubblica. | https://se.linkedin.com/company/ekstrand-&-son-ab — titolo «Ekstrands Dörrar & Fönster AB \| LinkedIn» | https://se.linkedin.com/company/ekstrand-&-son-ab |
| Fegens Sågverk AB | linkedin | URL LinkedIn con prefisso regionale 'ca.' (Canada) su azienda svedese: incoerente e da riportare al dominio se./www. La pagina non è stata riscontrata in nessuna fonte — DA CONFERMARE che esista. | Record: https://ca.linkedin.com/company/fegens-s%C3%A5gverk-ab ; nelle ricerche su 'Fegens Sågverk' non compare alcuna pagina LinkedIn (solo allabolag |  |
| Fegens Sågverk AB | referente | Nome del VD incompleto rispetto al registro: Lars Johan Andersson. Fatturato 189.377 KSEK (2025) ≈ 16,8 M€ e 28 dipendenti confermati. | allabolag.se befattningar (556080-4857): «Lars Johan Andersson, 38 år, VD»; «omsättning 189 377 KSEK, resultat 1 722 KSEK, 28 anställda (2025)» | Lars Johan Andersson |
| Gyllsjö Träindustri AB | denominazione | Ragione sociale di registro imprecisa: il registro riporta 'Aktiebolaget Gyllsjö Träindustri' (org.nr 556083-9671). Dati economici confermati (303.142 KSEK ≈ 26,8 M€, risultato 22.414 KSEK, 82 dip. 2024; VD Björn Olsson Lissner). | https://www.bolagsfakta.se/5560839671-Aktiebolaget_Gyllsjo_Traindustri — «Aktiebolaget Gyllsjö Träindustri ... omsättning 303 142 KSEK, resultat 22 41 | Aktiebolaget Gyllsjö Träindustri |
| Gärsnäs Aktiebolag | referente | RICONFERMATO, nessuna correzione necessaria. Magnus Eriksson risulta tuttora VD di Gärsnäs Aktiebolag (556044-4746) e Dag Klockby styrelseordförande, coerentemente con l'annuncio ufficiale del sito (VD dal 01-01-2023, in precedenza platschef per quas | https://garsnas.se/en/new-ceo-at-garsnas/ ('Ny vd på Gärsnäs'); https://www.bolagsfakta.se/5560444746-Garsnas_Aktiebolag - 'Magnus Eriksson är VD ...  | Magnus Eriksson, VD (confermato) |
| Hjältevadshus AB | referente | Referente confermato (Johan Bynell, VD; ordförande Magnus Agervald) ma la nomina è annunciata da Pulsen Group: verificare che sia ancora in carica alla data di uso del lead. | https://www.mynewsdesk.com/se/pulsen/pressreleases/johan-bynell-ny-vd-paa-hjaeltevadshus-2948844 ; allabolag befattningar: «VD Johan Bynell, ordförand |  |
| Horreds Möbel Aktiebolag | denominazione | Società CONFERMATA ATTIVA (scheda allabolag corrente, nessuna procedura concorsuale rilevata). Va però esplicitato il legame di gruppo: la capogruppo è Horreds Holding AB (esiste anche Horreds Möbel Utvecklings AB, 559016-3324). Nel foglio si legge g | https://www.allabolag.se/5563651974/koncern e frammento allabolag: 'moderbolag är Horreds Holding AB'; https://www.allabolag.se/5590163324/horreds-mob | Indicare la capogruppo: Horreds Holding AB |
| Tärnsjö Garveri Aktiebolag | dimensione | Numero dipendenti non allineato alla fonte: il record indica 43 dipendenti (2024), allabolag riporta 46. | allabolag.se: «Tärnsjö Garveri Aktiebolag har 46 anställda». Fatturato 51,9 MSEK 2024 (+6%) confermato. | 46 dipendenti |

### Olanda (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Bangma Verpakking B.V. | sito | Il sito indicato nel foglio (https://www.bangma.nl) non è il dominio istituzionale usato oggi dall'azienda, che pubblica i propri contenuti su bangmaverpakking.nl (pagina 'Historie Bangma Verpakking'). DA CONFERMARE quale dei due sia il dominio attiv | https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - pagina istituzionale corrente dell'azienda | https://bangmaverpakking.nl/ (DA CONFERMARE) |

### Belgio (10)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Belignum NV | dimensione | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato il 02-07-2024 (esercizio 2023). La cifra di EUR 16. | https://trendstop.knack.be/nl/detail/405348449/belignum.aspx - 'omzet van 14.746.642 euro, 40e in de sector houthandel... laatst neergelegde jaarreken | Fatturato EUR 14.746.642, esercizio 2023 (bilancio depositato 02-07-2024), 10,8 FTE - eliminare il riferimento a 16.075. |
| Buzzispace NV | dimensione | Il campo indica la produzione 'in Kempen' (implicitamente Belgio): le fonti aziendali collocano lo stabilimento produttivo a Bladel, nei Paesi Bassi. La sede sociale ad Anversa resta corretta, ma l'attivita' manifatturiera non e' belga; l'azienda ha  | https://officeinsight.com/officenewswire/buzzispace-appoints-new-ceo-announces-new-role-for-former-ceo-and-founder/ - frammento: "showrooms in Antwerp |  |
| Callens NV (Callens African Woods) | referente | Thierry Maelfait risulta confermato alla guida, ma dal 2021-2022 e' entrata in azienda la figlia Sam Maelfait, indicata dalle fonti come zaakvoerster/marketingverantwoordelijke: verificare chi sia oggi il rappresentante legale. Nota formale: per una  | https://www.voka.be/nieuws/west-vlaanderen-ondernemers-2024-19/callens-african-woods-heeft-productiefaciliteiten-kameroen - frammento: "Sam Maelfait,  |  |
| Decadt Houthandel NV | ruolo | Stefaan Decadt e' confermato al vertice, ma il ruolo pubblicato e' 'bedrijfsleider' (LinkedIn) e non 'Algemeen directeur'; per una NV il titolo statutario sarebbe 'gedelegeerd bestuurder'. Inoltre coesistono due siti web riferiti a Decadt a Vlamertin | https://be.linkedin.com/in/stefaan-decadt-8b8144113 - frammento: "Stefaan Decadt - bedrijfsleider bij decadt houthandel nv"; siti concorrenti https:// | Ruolo: Bedrijfsleider / gedelegeerd bestuurder |
| Decadt Houthandel NV | dimensione | Data di fondazione discordante: il campo indica 01-01-1975 (data di costituzione della NV) mentre le fonti aziendali datano l'attivita' al 1927. Fatturato 13.460.408 EUR confermato. | https://trendstop.knack.be/nl/detail/415284714/decadt-houthandel.aspx - frammento: "With a turnover of 13,460,408 euros, Decadt Houthandel is ranked 4 |  |
| Denderwood NV | dimensione | Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta indeterminata e potenzialmente sotto la soglia dei 5 M EUR. Il campo lo dichiara ('TAGLIA DA VERIFICARE'), ma il dato non e' riscontrabile su NBB. Resto del record | https://www.atibt.org/en/members/24/denderwood e https://www.denderwood.com/over-ons/ - frammento: "Denderwood is located at J. Cardijnstraat, 3 B-942 |  |
| Hulpiau Hides BV | dimensione | Il campo usa come proxy dimensionale il margine lordo (2.284.726 EUR) di UN'ALTRA entita' giuridica (Hulpiau BV, BE 0429.082.864), non della societa' target BE 0777.875.662, che deposita a schema abbreviato e non pubblica il fatturato. Dato confermat | https://www.companyweb.be/en/0777875662/hulpiau-hides - frammento: "There are 6.1 FTEs working at Hulpiau Hides according to staff figures in the most |  |
| Lavrijsen Houtbedrijf NV | ruolo | Jan e Bert Lavrijsen sono confermati alla guida dell'azienda, ma per una NV il titolo statutario corretto e' 'gedelegeerd bestuurder / bestuurder', non 'zaakvoerder' (termine proprio delle BV). | https://lavrijsen.be/over-ons/ - frammento: "Jan and Bert Lavrijsen are at the helm of the company with secured succession" | Bestuurders / gedelegeerd bestuurders |
| Radermecker SRL | dimensione | Discordanza sugli addetti: il record indica 9,1 FTE (bilancio BNB), mentre la scheda Europages dichiara 20-49 dipendenti. Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta non verificabile. | https://www.europages.fr/TANNERIE-RADERMECKER/BEL069426-000019048001.html - frammento: "The company employs between 20 and 49 people" |  |
| Silco NV | sito | Nessun sito web proprio reperito per Silco NV in 3 ricerche: l'azienda compare solo su banche dati societarie (trendstop, companyweb, fincheck, northdata, staatsbladmonitor). Coerente con la struttura a 1 FTE. Il campo vuoto e' quindi corretto, ma va | https://www.northdata.com/Silco%20N.V.,%20Antwerpen/KBO%200715.792.692 - solo scheda registro; nessun dominio aziendale nei risultati | n.d. (nessun sito web aziendale) |

### (tutti) (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| (controllo di rientro) | denominazione | nessuna delle 7 aziende rimosse e' rientrata nei fogli. Controllo eseguito su _records.json (742 record, tutti i fogli) cercando in ogni campo, con radici tolleranti alle varianti: 'getama', 'dragsb', 'pacorini', 'immobra', 'lavazza', 'segafredo', 'k | Verifica programmatica su _myeudr_build/verifica/_records.json: per ciascuna delle 7 radici, 0 corrispondenze nel campo 'denominazione' su tutti i 742 |  |
