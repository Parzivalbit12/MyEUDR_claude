# REPORT DI VERIFICA — MyEUDR Lead Mapping

> Controllo qualità **record per record** del censimento lead (**742 aziende, 8 fogli**), alla ricerca di refusi, attribuzioni errate e ogni altro errore introdotto durante la raccolta. Non è una ricerca di nuove aziende.


## Come leggere questo report

La verifica si è svolta in due fasi, con budget e coperture diverse:

| Fase | Metodo | Copertura |
|---|---|---|
| **A — controlli deterministici** | 26 controlli automatici offline su tutti i JSON di build e sul workbook | **100%** dei 742 record |
| **B — riscontro sul web** | agenti di verifica, blocchi di 15-20 aziende, 2-3 ricerche per record, ogni rilievo con URL o citazione | vedi §1 |

Documenti di dettaglio:

- [`00_controlli_automatici.md`](00_controlli_automatici.md) — esito completo della Fase A
- [`01_analisi_dimensione.md`](01_analisi_dimensione.md) — analisi del campo `Dimensione` (tipo di dato dichiarato, anno, obsolescenza)
- `<foglio>_<blocco>.json` — rilievi grezzi di ciascun agente
- `00_punti_noti.json` — verifica dei 13 punti lasciati aperti dalla raccolta


## Vincolo d'ambiente che ha condizionato la verifica

Il proxy di egress **nega per policy** (403 al CONNECT) tutti i domini esterni: registri societari e siti aziendali non sono raggiungibili né con WebFetch né con curl. **L'unico canale disponibile è WebSearch**, i cui frammenti contengono spesso — ma non sempre — il dato cercato. Di qui una regola applicata da tutti gli agenti: quando dopo 2-3 ricerche il dato non emerge, il rilievo è marcato `DA CONFERMARE` e il campo **non viene toccato**. Un rilievo aperto è preferibile a una correzione inventata.


---


## 0. Esito della Fase A — controlli deterministici

Il censimento è risultato **pulito su tutti i controlli di integrità**: nessun duplicato (né fra fogli né fra i JSON di build), nessuna entità HTML residua, nessun URL LinkedIn o sito malformato, nessuna email sintatticamente errata, nessun numero di registro rimasto nelle denominazioni, nessun campo `Fonte` vuoto o non-URL, e **nessuna divergenza fra i JSON di build e i fogli Excel** — segno che la pipeline `add_country.py` è rimasta coerente.

I rilievi si concentrano invece su qualità e coerenza redazionale:

> La tabella riflette lo stato **dopo** le correzioni applicate (§0-bis): per questo il controllo 6 sulla tassonomia è ora a zero, mentre prima dell'intervento segnalava **23 valori fuori elenco**.

| # | Controllo | Rilievi |
|---|---|--:|
| 1 | 1 · Duplicati fra fogli del workbook | 0 |
| 1b | 1b · Duplicati fra i JSON di build | 0 |
| 1c | 1c · Denominazioni diverse con lo stesso sito web | 1 |
| 2 | 2 · Email con dominio diverso dal sito (sospette di deduzione) | 24 |
| 2b | 2b · Email presente ma sito assente (non verificabile per dominio) | 1 |
| 2c | 2c · Email su dominio freemail/PEC (accettabile ma non aziendale) | 10 |
| 2d | 2d · Email su dominio affine al sito (TLD/variante) — rischio basso | 52 |
| 3 | 3 · Stessa email su aziende diverse | 0 |
| 3b | 3b · Stesso LinkedIn su aziende diverse | 1 |
| 4 | 4 · URL malformati (LinkedIn / sito) | 0 |
| 4b | 4b · Email sintatticamente non conformi | 0 |
| 5 | 5 · Entità HTML residue | 0 |
| 6 | 6 · Tassonomia Filiera fuori elenco | 0 |
| 6b | 6b · Separatore filiera non em-dash | 0 |
| 7 | 7 · Fonte vuota o non URL | 0 |
| 7b | 7b · Dimensione vuota o n.d. | 6 |
| 7c | 7c · Sito web mancante | 26 |
| 8 | 8 · Dimensione fuori forbice 5–40 M€ senza segnalazione esplicita | 8 |
| 9 | 9 · Denominazione: registri, spazi, numeri | 0 |
| 9b | 9b · Forma giuridica incoerente col paese del foglio | 0 |
| 9c | 9c · Nessuna forma giuridica nel nome | 17 |
| 9d | 9d · Maiuscolo/minuscolo incoerente dentro il foglio | 52 |
| 9e | 9e · Forma giuridica scritta in stile incoerente (foglio Italia) | 0 |
| 10 | 10 · TLD del sito estraneo al paese del foglio | 7 |
| 11 | 11 · Divergenze fra JSON di build e foglio Excel | 0 |
| 11b | 11b · Record presente nei JSON ma assente dal foglio | 0 |


**Totale rilievi automatici: 205.**


> **Nota sul controllo 2 (email dedotte).** Il controllo grezzo segnalava 86 email con dominio diverso dal sito. Separando i casi innocui — stesso nome con TLD diverso (`azienda.de` vs `azienda.com`) e caselle freemail/PEC, entrambi legittimi — restano **24 casi con stem realmente diverso**, che sono quelli da confermare a fonte.


---


## 0-bis. Correzioni già applicate al workbook (54)

Applicate **solo le correzioni certe**, secondo il mandato: refusi formali, entità HTML, forme giuridiche, filiere fuori Allegato I, aziende cessate. Tutto il resto resta come rilievo aperto in questo report.

Ogni correzione è stata applicata con un **controllo di guardia**: lo script verifica che il valore attuale del campo coincida esattamente con quello atteso, altrimenti salta la correzione. Dopo l'applicazione: **742 righe invariate**, ordine dei fogli ripristinato (Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria).


### Tassonomia `Filiera` (23)

Il foglio **Finlandia** conteneva varianti storiche della tassonomia (`Legno/Compensato-Prodotti`, `Legno/Segheria-Piallatura`, `Legno/CLT`, `Legno/Commercio-export sahatavara`, `Legno/Piallatura`) mai allineate agli altri fogli. La riconduzione **non è arbitraria**: gli altri sette fogli sono unanimi nel classificare compensato, impiallacciature, finestre/porte, parquet, glulam e CLT sotto `Legno/Arredo — <dettaglio>`, e segheria/piallatura sotto `Legno/Segheria`.

| Foglio | Azienda | Da | A |
|---|---|---|---|
| Finlandia | Alavus Ikkunat Oy | Legno/Compensato-Prodotti — finestre/porte in legno | Legno/Arredo — finestre/porte in legno |
| Finlandia | Aureskosken Jalostetehdas Oy | Legno/Segheria e trasformazione | Legno/Segheria — trasformazione |
| Finlandia | CWP Coloured Wood Products Oy | Legno/Compensato-Prodotti — impiallacciatura betulla | Legno/Arredo — impiallacciatura betulla colorata |
| Finlandia | Hoisko CLT (CLT Finland Oy) | Legno/Compensato-Prodotti — CLT | Legno/Arredo — CLT |
| Finlandia | Hollolan Viilu ja Laminaatti Oy (HVL) | Legno/Compensato-Prodotti — impiallacciatura/laminat | Legno/Arredo — impiallacciatura/laminati |
| Finlandia | Jet-Puu Oy | Legno/Segheria-Piallatura | Legno/Segheria — piallatura |
| Finlandia | Kiilax Oy | Legno/Compensato-Prodotti — compensato betulla/lamel | Legno/Arredo — compensato betulla/lamellare |
| Finlandia | Kinnaskoski Oy | Legno/Segheria-Piallatura | Legno/Segheria — piallatura |
| Finlandia | Lammin Ikkuna Oy | Legno/Compensato-Prodotti — finestre/porte in legno- | Legno/Arredo — finestre/porte in legno-alluminio |
| Finlandia | Lappiporras Oy | Legno/Compensato-Prodotti — scale in legno | Legno/Arredo — scale in legno |
| Finlandia | Late-Rakenteet Oy | Legno/Compensato-Prodotti — legno lamellare/glulam | Legno/Arredo — legno lamellare/glulam |
| Finlandia | Mahogany Oy | Legno/Compensato-Prodotti — impiallacciatura ed erik | Legno/Arredo — impiallacciatura ed erikoisvaneri |
| Finlandia | Ollikaisen Hirsirakenne Oy | Legno/Compensato-Prodotti — hirsi/lamellare (glulam) | Legno/Arredo — hirsi/lamellare (glulam) |
| Finlandia | Orasko Oy | Legno/Commercio-export sahatavara | Legno/Segheria — commercio/export sahatavara |
| Finlandia | Oy CrossLam Kuhmo Ltd | Legno/CLT (trasformazione) | Legno/Arredo — CLT |
| Finlandia | Oy Haka-Wood Ab | Legno/Segheria (betulla) | Legno/Segheria — betulla |
| Finlandia | Piklas Oy | Legno/Compensato-Prodotti — finestre/porte in legno- | Legno/Arredo — finestre/porte in legno-alluminio |
| Finlandia | Sepa Oy | Legno/Compensato-Prodotti — capriate/prodotti strutt | Legno/Arredo — capriate/prodotti strutturali |
| Finlandia | Siparila Oy | Legno/Piallatura (pannelli/paneelit) | Legno/Segheria — piallatura (pannelli/paneelit) |
| Finlandia | Sysmän Ikkuna ja Ovi Oy (Päijänne-Ovet | Legno/Compensato-Prodotti — finestre/porte in legno | Legno/Arredo — finestre/porte in legno |
| Finlandia | Timberwise Oy | Legno/Compensato-Prodotti — parquet/pavimenti in leg | Legno/Arredo — parquet/pavimenti in legno |
| Italia | Imperator S.r.l. | Caffè (import caffè verde) | Caffè — import caffè verde |
| Italia | Sandalj Trading Company S.p.A. | Caffè (import caffè verde) | Caffè — import caffè verde |

### Refusi formali (31)

| Foglio | Azienda | Campo | Correzione | Motivo |
|---|---|---|---|---|
| Danimarca | NPI (Nordic Panel Import) | denominazione | «NPI (Nordic Panel Import)» → «NPI A/S (Nordic Panel Import)» | forma giuridica mancante: al CVR 37418730 la societa' è registrata come NPI A/S (proff.dk) |
| Olanda | Rompa Tanneries B.V. | denominazione | «Rompa Tanneries B.V.» → «Vitelco Leather B.V. (già Rompa Tanneries B.V.)» | denominazione obsoleta: sciolta la joint venture, Vitelco è socio unico al 100% e la societa' è stata ridenomi |
| Austria | Karnische Massiv Möbel GmbH | denominazione | «Karnische Massiv Möbel GmbH» → «Karnische-Massiv-Möbel Gesellschaft m.b.H.» | ragione sociale a Firmenbuch FN 094638z (LG Klagenfurt); «Karnische Massiv Möbel GmbH» è il nome commerciale |
| Belgio | Confiserie Vandenbulcke NV | denominazione | «Confiserie Vandenbulcke NV» → «Vandenbulcke Confiserie NV» | ordine dei termini invertito rispetto alla denominazione registrale KBO |
| Germania | Paletten Meyer | denominazione | «Paletten Meyer» → «Josef Meyer Palettenbau Inh. Julian Meyer (Paletten Meyer)» | «Paletten Meyer» è il solo nome commerciale: la ditta è iscritta come impresa individuale Josef Meyer Paletten |
| Danimarca | FREDERICIA FURNITURE A/S | dimensione | «» → « DKK (≈0,87 M» · « DKK» → «)» | refuso di unità di misura: «6,5 M€ DKK» mescolava euro e corone danesi |
| Danimarca | Just Coffee | denominazione | «Just Coffee» → «Just Coffee I/S» | forma giuridica verificata al registro: interessentskab, CVR 35492380 (cvrapi.dk, proff.dk) |
| Danimarca | Just Coffee | dimensione | «» → «verificata al » · « non » → «: Just Coffee I/S, CVR 35492380 (interessents» · «rificata» → «j 551, 4000 Roskilde» | la riserva «ragione sociale CVR non verificata» è stata sciolta dalla verifica: sostituita col dato accertato |
| Danimarca | INNOVATION LIVING A/S (già Innov | linkedin | «https://de.linkedin.com/company/innovation-living-a-s» → «https://dk.linkedin.com/company/innovation-living-a-s» | prefisso di locale tedesco su società danese: stessa pagina, prefisso allineato allo standard del dataset |
| Italia | Fonpelli S.p.A. | denominazione | «Fonpelli S.p.A.» → «Fonpelli S.r.l.» | forma giuridica errata: al Registro Imprese è FONPELLI - S.R.L., P.IVA 01705980249 |
| Italia | Conceria Cilp | denominazione | «Conceria Cilp» → «Conceria CILP S.r.l.» | forma giuridica mancante: al Registro Imprese è CONCERIA CILP S.R.L., P.IVA 00190610501 |
| Italia | Conceria Emmedue | denominazione | «Conceria Emmedue» → «Conceria Emmedue S.r.l.» | forma giuridica mancante: al Registro Imprese è CONCERIA EMMEDUE S.R.L., P.IVA 00793250242 |
| Italia | 3C Lavorazione Pelli S.r.l. | denominazione | «3C Lavorazione Pelli S.r.l.» → «3 C - Lavorazione Pelli S.r.l.» | ragione sociale a registro: «3 C - LAVORAZIONE PELLI S.R.L.» (due fonti concordi) |
| Italia | A. Brivio Compensati SpA | denominazione | «A. Brivio Compensati SpA» → «A. Brivio Compensati S.p.A.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Arko SpA | denominazione | «Arko SpA» → «Arko S.p.A.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Aster Cucine SpA | denominazione | «Aster Cucine SpA» → «Aster Cucine S.p.A.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Basso Legnami Srl | denominazione | «Basso Legnami Srl» → «Basso Legnami S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Bedogna F.lli Srl | denominazione | «Bedogna F.lli Srl» → «Bedogna F.lli S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | C.I.M.A. Srl (Compensati Impiall | denominazione | «C.I.M.A. Srl (Compensati Impiallacciature Materiali Affini)» → «C.I.M.A. S.r.l. (Compensati Impiallacciature Materiali Affini)» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Caccaro Srl | denominazione | «Caccaro Srl» → «Caccaro S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Cadorin Group Srl | denominazione | «Cadorin Group Srl» → «Cadorin Group S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Compensati Toro SpA | denominazione | «Compensati Toro SpA» → «Compensati Toro S.p.A.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Fratelli Berti Legnami Srl | denominazione | «Fratelli Berti Legnami Srl» → «Fratelli Berti Legnami S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Holzland Fuchs Srl | denominazione | «Holzland Fuchs Srl» → «Holzland Fuchs S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Itlas Srl Società Benefit | denominazione | «Itlas Srl Società Benefit» → «Itlas S.r.l. Società Benefit» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Nord Legnami Group Srl | denominazione | «Nord Legnami Group Srl» → «Nord Legnami Group S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Nuova River Srl | denominazione | «Nuova River Srl» → «Nuova River S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Original Parquet SpA | denominazione | «Original Parquet SpA» → «Original Parquet S.p.A.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | PALM SpA SB | denominazione | «PALM SpA SB» → «PALM S.p.A. SB» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Segheria Saccavini Srl | denominazione | «Segheria Saccavini Srl» → «Segheria Saccavini S.r.l.» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |
| Italia | Zalf SpA (Zalf Industria Mobili  | denominazione | «Zalf SpA (Zalf Industria Mobili Componibili)» → «Zalf S.p.A. (Zalf Industria Mobili Componibili)» | normalizzazione ortografica della forma giuridica allo stile del foglio (S.r.l./S.p.A.) |

### Correzioni deliberatamente NON applicate

Tre categorie di rilievi formali sono state lasciate aperte nel report invece che corrette nei fogli. Il motivo è sempre lo stesso: la correzione automatica avrebbe introdotto un errore nuovo.

| Rilievo | Record | Perché non è stata applicata |
|---|--:|---|
| **Maiuscolo integrale nel foglio Danimarca** (controllo 9d) | 52 | Il foglio mescola 51 denominazioni in MAIUSCOLO (stile del registro CVR) e 38 in forma normale. Un *title case* automatico però **rovinerebbe gli acronimi**: `JKE DESIGN` diventerebbe `Jke Design`, e lo stesso vale per NPI, MC, KLS, H.C., DHS. Servirebbe una decisione caso per caso, che non è una correzione certa. |
| **Conceria Beschin** e **Conceria Daniela** (foglio Italia) | 2 | Ciascuna corrisponde a **due entità distinte e omonime** al Registro Imprese, nello stesso comune (una S.n.c. e una S.r.l.). Aggiungere una forma giuridica significherebbe **scegliere** quale sia l'operatore EUDR: va accertato prima del contatto. |
| **Email da confermare** | 24+ | Le email con dominio diverso dal sito, e quelle non ritrovate letteralmente in una fonte pubblica, restano **`DA CONFERMARE`**. Il mandato vieta sia di inventarle sia di cancellarle d'ufficio: il campo non è stato toccato. |

---


# Fase B — verifica sul web, record per record


## 1. Copertura della verifica

| Foglio | Aziende | Blocchi completi | Blocchi parziali | Blocchi da fare | Aziende verificate | Copertura |
|---|--:|--:|--:|--:|--:|--:|
| Italia | 95 | 1 | 0 | 4 | 19 | 20% |
| Germania | 97 | 1 | 0 | 5 | 17 | 18% |
| Finlandia | 84 | 0 | 0 | 5 | 0 | 0% |
| Danimarca | 89 | 2 | 0 | 3 | 36 | 40% |
| Svezia | 89 | 1 | 0 | 4 | 18 | 20% |
| Olanda | 100 | 2 | 0 | 4 | 34 | 34% |
| Belgio | 95 | 1 | 2 | 2 | 19 | 20% |
| Austria | 93 | 1 | 0 | 4 | 19 | 20% |
| **TOTALE** | **742** | **9** | **2** | **31** | **162** | **22%** |

_I **blocchi parziali** sono quelli il cui agente è stato interrotto dal limite di sessione: i rilievi già salvati sono validi e inclusi nel report, ma il blocco non è coperto per intero. Il salvataggio incrementale ogni 3-4 record è ciò che ha evitato di perdere quel lavoro._

> La Fase A copre invece il **100%** dei 742 record: è un controllo offline e non dipende dal budget di ricerca.


_A questi si aggiunge la verifica mirata dei **13 punti già noti** lasciati aperti dalla raccolta, condotta separatamente e riportata per intero più sotto._


## 2. Rilievi per foglio

**Totale rilievi Fase B: 275** — alta 36 · media 154 · bassa 85.

| Foglio | Rilievi | alta | media | bassa | Aziende toccate |
|---|--:|--:|--:|--:|--:|
| Italia | 25 | 0 | 11 | 14 | 17 |
| Germania | 29 | 1 | 20 | 8 | 17 |
| Finlandia | 0 | 0 | 0 | 0 | 0 |
| Danimarca | 46 | 14 | 18 | 14 | 32 |
| Svezia | 36 | 6 | 15 | 15 | 18 |
| Olanda | 44 | 5 | 30 | 9 | 22 |
| Belgio | 79 | 9 | 50 | 20 | 42 |
| Austria | 15 | 1 | 10 | 4 | 12 |
| _(tutti)_ | 1 | 0 | 0 | 1 | 1 |
| **TOTALE** | **275** | **36** | **154** | **85** | **161** |

### Rilievi per campo

| Campo | Rilievi | di cui alta |
|---|--:|--:|
| dimensione | 126 | 19 |
| referente | 63 | 9 |
| denominazione | 28 | 6 |
| email | 18 | 1 |
| linkedin | 14 | 0 |
| sito | 8 | 0 |
| ruolo | 7 | 0 |
| sede | 4 | 0 |
| filiera | 3 | 1 |
| fonte | 3 | 0 |
| esistenza_stato | 1 | 0 |

---

## 3. Tema trasversale — legami di gruppo (47 rilievi)

È il problema **più diffuso e meno atteso** emerso dalla verifica: non era fra i 13 punti noti dell'handoff. Numerose aziende del censimento sono controllate di gruppi, spesso esteri o quotati. Per il criterio già applicato dal progetto — che aveva rimosso Lavazza Kaffee, Segafredo Zanetti Austria e Kaffee Partner Austria perché *«la compliance si decide a livello di gruppo, non nella filiale»* — sono **lead di valore dubbio**.

La tabella distingue i due casi, che non hanno la stessa gravità:

- **DICHIARATO** — il campo `Dimensione` del foglio già segnala il legame. Non è un errore di dato: la raccolta ha fatto quel che le regole chiedevano (*«segnalare sempre i legami di gruppo»*). È una **decisione di selezione** che spetta al cliente.

- **NON DICHIARATO / ERRATO** — il legame manca del tutto, oppure la capogruppo indicata è sbagliata. Questo **è** un errore di dato.

| Foglio | Azienda | Stato nel foglio | Rilievo |
|---|---|---|---|
| Austria | BRAUN LOCKENHAUS GmbH | **dichiarato** | Filiale di gruppo estero: la societa' e' controllata da SCHNEEWEISS AG / SCHNEEWEISS interior, con sede del gruppo a Kippenheim (Baden-Württemberg, DE), dal 2006. La decisione di compliance EUDR si as |
| Belgio | A & A Chocolaterie NV | **dichiarato** | Il legame di gruppo e' correttamente dichiarato, ma va valutato l'effetto sul perimetro commerciale: A & A Chocolaterie (22,1 M€) e Pralinart (18,4 M€) sono entrambe controllate al 100% da Hamlet NV,  |
| Belgio | Corné Port-Royal Chocolatier SA | **NON dichiarato** | LEGAME DI GRUPPO NON DICHIARATO. Corne Port-Royal Chocolatier SA (BE 0433.283.558, denominazione abbreviata registrale 'CPR CHOCOLATIER') e' controllata dal gruppo Neuhaus dal 2013: Neuhaus figura dir |
| Belgio | Delafaille NV | **dichiarato** | Il legame di gruppo e' dichiarato ma la conclusione tratta nel campo ('resta pero' PMI belga autonoma con obblighi EUDR propri') e' opinabile: Maestrani Schweizer Schokoladen ha acquisito il 100% dell |
| Belgio | Dolfin SA | **NON dichiarato** | Dato aziendale incompleto e ormai superato dagli eventi: nell'aprile 2026 Dolfin e' diventata azionista di maggioranza della Chocolaterie Galler (rilevata da un consorzio vallone insieme a Wallonie En |
| Belgio | Koffiebranderij Or BV (OR Coffee Roaster | **dichiarato** | Controllata di gruppo: dall'aprile 2024 la societa' e' stata acquisita da Anaerobic Holding (Anversa), gia' proprietaria di Mister Barish Beans & Machines. Il legame e' dichiarato nel campo, ma va ten |
| Belgio | Manutti BV | **dichiarato** | Legame di gruppo con Manutti Invest BV (BE 0478.148.434) dichiarato nel record: si tratta della holding familiare che controlla l'operativa. Segnalato come 'media' perche' gia' dichiarato; la decision |
| Belgio | Mecam NV | **NON dichiarato** | Il record riporta 32.145.268 € e 111,6 FTE per la sola Mecam NV, mentre la stampa parla di 37 M€ cumulati e ~220 dipendenti per l'intero Mecam Group (Mecam + Neo-Style). Il legame di gruppo esiste ed  |
| Belgio | Sas NV (Sas Coffee) | **dichiarato** | CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elen |
| Belgio | Silco NV | **NON dichiarato** | RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui president |
| Belgio | Tannerie Masure SA | **NON dichiarato** | Societa' non indipendente: dal 2014 Tannerie Masure fa parte del Groupe Saturne insieme alla francese Tannerie Fortier-Beaulieu (Roanne). Il referente indicato, Olivier Lesage, risulta anche dirigente |
| Belgio | Vanerum Belgie NV | **dichiarato** | Il legame di gruppo e' dichiarato ma incompleto: i3-Group non e' piu' interamente familiare. WorxInvest ha acquistato circa il 25% per 10 M€ e nel novembre 2023 anche il gruppo americano Steelcase ha  |
| Belgio | Vincent Sheppard NV | **NON dichiarato** | Assetto proprietario non dichiarato: dal 2002 la societa' e' controllata dalla famiglia Claeys tramite Cennini Holding e oggi il capitale e' 50/50 tra la famiglia Claeys e Jos Destrooper. Il fatturato |
| Danimarca | BØJSØ DØRE & VINDUER A/S | **dichiarato** | Lead non indipendente: dal 2017 la società è controllata da INWIDO DENMARK A/S, parte del gruppo quotato svedese Inwido AB (fatturato di gruppo ~9 mld SEK nel 2025). Secondo il mandato una controllata |
| Danimarca | HVIDBJERG VINDUET A/S | **dichiarato** | Assetto proprietario errato e lead non indipendente: il campo indica come controllante "Hvidbjerg i A/S", ma la società è controllata dal gruppo ACO Nordic, a sua volta parte del gruppo tedesco ACO (f |
| Danimarca | JKE DESIGN A/S | **dichiarato** | Lead non indipendente: la società appartiene al gruppo BALLINGSLÖV INTERNATIONAL DANMARK A/S / Ballingslöv International AB (gruppo svedese, Stena Adactum), con presidente del CdA e consigliere espres |
| Danimarca | KRYDSFINER-HANDELEN A/S | **dichiarato** | Controllata di gruppo estero: dall'autunno 2023 la societa' e' stata venduta da Carsten Rittig a Fritzoe Nordic Holding AS (Norvegia), che ne detiene il controllo. Il record lo accenna in forma dubita |
| Danimarca | KVIST INDUSTRIES A/S | **NON dichiarato** | Assetto proprietario non dichiarato: la societa' figura nel portafoglio del fondo di private equity danese Dansk Ejerkapital ed e' controllata tramite KVIST HOLDING A/S (CVR 21746886, Esbjerg). Il cam |
| Danimarca | LILLEHEDEN A/S | **dichiarato** | Controllata di gruppo: la societa' fa parte di Nordic Wood Industries A/S (CVR 37385603), che dal 12.05.2025 ha un nuovo adm. direktor di gruppo (Holger Carsten Hansen). Il legame e' gia' correttament |
| Danimarca | MULTIFORM A/S | **dichiarato** | Controllata di gruppo: capogruppo BALLINGSLOV INTERNATIONAL DANMARK A/S (gruppo svedese Ballingslov International / Stena Adactum). Il legame e' gia' dichiarato correttamente nel record, quindi il ril |
| Danimarca | Naturli' Foods | **dichiarato** | RILIEVO EMERSO DAL CONTROLLO DI RIENTRO. Il record dichiara esso stesso che Naturli' Foods e' 'parte del gruppo Dragsbaek/Orkla': e' quindi una controllata del gruppo norvegese quotato Orkla ASA, per  |
| Danimarca | Skagerak Denmark A/S | **NON dichiarato** | Referente errato e legame di gruppo non dichiarato: Skagerak Denmark A/S e' stata acquisita da Fritz Hansen A/S nel dicembre 2021 ed e' oggi il marchio 'Skagerak by Fritz Hansen'. Josef Theodor Kaiser |
| Danimarca | TIMBERMAN DENMARK A/S | **dichiarato** | Assetto proprietario errato/obsoleto: il record indica solo 'controllata da Timberman Holding ApS ... azionariato nordico'. In realta' nel dicembre 2024 la societa' e' stata acquistata dal gruppo indu |
| Danimarca | TJOERNEHOEJ MOELLE A/S | **NON dichiarato** | LEAD NON VALIDO. A/S Tjoernehoej Moelle (CVR 34175012) NON e' un'impresa indipendente: e' stata acquistata da DLG nel 1989 dal mugnaio Sander Petersen ed e' oggi una controllata della cooperativa DLG  |
| Germania | H. Heitz Furnierkantenwerk GmbH & Co. KG | **NON dichiarato** | CONTROLLO DI GRUPPO NON DICHIARATO: dal 2016 Heitz e societa del gruppo INDUS Holding AG (holding industriale quotata, Bergisch Gladbach). Il record non riporta alcun legame di gruppo: la decisione di |
| Germania | Weinheimer Leder GmbH | **NON dichiarato** | Struttura di gruppo non dichiarata: Weinheimer Leder GmbH e collegata a Das Lederband GmbH (Weinheim, HRB 724382), con Uwe Holubeck Geschäftsführer di entrambe; le fonti aperte non chiariscono il vers |
| Olanda | BeBo Parket B.V. | **dichiarato** | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dich |
| Olanda | GWW Houtimport B.V. | **dichiarato** | Controllata di gruppo: dal 01/01/2026 GWW Houtimport, GWW Agency e Van den Berg Hardhout confluiscono nella holding Van den Berg Houtgroep. Il legame e' gia' dichiarato correttamente nel campo, ma la  |
| Olanda | Houthandel Jos Dennebos B.V. | **NON dichiarato** | Referente e ruolo assenti. Il socio unico e' la persona giuridica Jos Dennebos Exploitatie B.V.; il fondatore storico e' Jos Dennebos (attivo anche in Dennebos Suriname). Nome e carica del directeur a |
| Olanda | Houtplex B.V. | **dichiarato** | Controllata di gruppo estero: Houtplex appartiene al gruppo Wood United, con sede a Singapore; dal febbraio 2019 le quote sia di Houtplex sia di Wood United sono di Timothy Paul, che ha rilevato la pa |
| Olanda | Montis B.V. | **NON dichiarato** | Legame di gruppo: Montis e uno dei sei marchi della Lande Groep (con Artifort, Lande, Portner, Zwaardvis, A Lott Of Space), che produce in NL, BE, DE e TR. Il legame e dichiarato nel campo ma senza pr |
| Olanda | Rompa Tanneries B.V. | **dichiarato** | Denominazione obsoleta: la societa' e' stata ridenominata VITELCO LEATHER B.V. Vitelco (gruppo PALI) ha rilevato le quote di Rompa Leather sciogliendo la joint venture ed e' oggi socio unico al 100%.  |
| Olanda | Rompa Tanneries B.V. | **dichiarato** | Assetto proprietario dichiarato errato: il campo indica ancora 'Soci: PALI Group (Den Bosch, vitello) e Rompa Leather (Rijen)', ma la JV e' stata sciolta e Vitelco (PALI Group) e' socio unico al 100%. |
| Olanda | Van Ierssel Houtimport B.V. | **dichiarato** | Controllata di gruppo: Van Ierssel Houtimport e stata rilevata da Boogaerdt Hout nel 1986 e fa parte della Koninklijke Boogaerdt Groep. Il legame e dichiarato nel campo, ma il lead resta una controlla |
| Olanda | Van den Berg Hardhout B.V. | **dichiarato** | Legame di gruppo dichiarato ma imminente: dal 01/01/2026 la societa e nella holding Van den Berg Houtgroep insieme a GWW Houtimport e GWW Agency. Con 6 dipendenti confermati e fatturato non pubblicato |
| Svezia | Aktiebolaget Karlaträ | **NON dichiarato** | Legame di gruppo non dichiarato: la società appartiene a una koncern di 2 società con moderbolag Karlaträ Försäljning Aktiebolag (holding di famiglia/vendita). |
| Svezia | Balungstrands Sågverk AB | **dichiarato** | Capogruppo incompleta/superata: il record si ferma a Green Wood Sverige AB. Green Wood Sverige AB (con Bäckebrons e Balungstrands) è stata riacquistata da Profura dopo il fallimento del gruppo tedesco |
| Svezia | Brattby Sågverks AB | **NON dichiarato** | Legame di gruppo non dichiarato: la società fa parte di una koncern con moderbolag Brattby Trading Aktiebolag. Fatturato 143,4 MSEK (~12,7 M€) e 32 dipendenti 2024 confermati. |
| Svezia | Brännfors Träförädling Aktiebolag | **NON dichiarato** | Legame di gruppo non dichiarato: moderbolag Brännfors Holding AB. Inoltre il dato 2024 confermato dalle fonti è 53.348 KSEK ≈ 4,7 M€ con 15 dipendenti (crescita -4,4%): il fatturato 2025 di 79.011 KSE |
| Svezia | Bäckebrons Sågverk Aktiebolag | **dichiarato** | Capogruppo SBAGLIATA e superata: il record indica 'capogruppo Ziegler Holding GmbH'. Il gruppo tedesco Ziegler è FALLITO e Profura ha riacquistato Green Wood Sverige AB con Bäckebrons e Balungstrands; |
| Svezia | Drömtrappor AB | **NON dichiarato** | Legame di gruppo non dichiarato (moderbolag Förvaltnings AB Klätterbjörken) e forte discontinuità del fatturato non segnalata: 126.413 KSEK nel 2024 (~11,2 M€) contro 83.213 KSEK nel 2025 (~7,4 M€), c |
| Svezia | Fogia Collection Aktiebolag | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Scandinavian Design Partners AB, legame già dichiarato correttamente. Tutti i dati (108.304 KSEK 2024 ≈ 9,6 M€, risultato 15.276 KSEK, 18 d |
| Svezia | Glimakra of Sweden AB | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Garpco Aktiebolag dal 2007, gruppo di 25 società con 311 addetti e 667,0 MSEK. Il legame è dichiarato ma il record lo sottodimensiona ('con |
| Svezia | Gärsnäs Aktiebolag | **dichiarato** | Lead di dubbia validità (non errore di dato): controllata di Bordet i Stockholm Aktiebolag, legame già dichiarato correttamente. Esiste inoltre notizia stampa di cambio di proprietà ('Gärsnäs AB får n |
| Svezia | Hjältevadshus AB | **dichiarato** | Rischio economico rilevante non segnalato: a fronte dei 140.766 KSEK (~12,5 M€) del 2025 la società ha una marginalità di -32,6% (perdita nell'ordine dei 45 MSEK). Inoltre la koncern è molto più ampia |
| Svezia | Horreds Möbel Aktiebolag | **dichiarato** | Società CONFERMATA ATTIVA (scheda allabolag corrente, nessuna procedura concorsuale rilevata). Va però esplicitato il legame di gruppo: la capogruppo è Horreds Holding AB (esiste anche Horreds Möbel U |
| Svezia | Tärnsjö Garveri Aktiebolag | **NON dichiarato** | Legame di gruppo NON dichiarato: il record definisce l'azienda 'la principale conceria indipendente attiva', ma allabolag indica come moderbolag Axel Bodéns Handels Aktiebolag. L'affermazione di indip |

---

## 4. Casi di gravità ALTA (36)

_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, oppure fuori dal perimetro dell'Allegato I EUDR._


### Germania (1)

#### H. Heitz Furnierkantenwerk GmbH & Co. KG — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: dal 2016 Heitz e societa del gruppo INDUS Holding AG (holding industriale quotata, Bergisch Gladbach). Il record non riporta alcun legame di gruppo: la decisione di compliance EUDR si colloca a livello di capogruppo, quindi il lead ha valore dubbio. Manca inoltre qualsiasi dato dimensionale ('Umsatz/MA n.d.').

**Evidenza:** https://www.h-heitz.de/aktuelles/presse/ - 'Seit 2016 gehoert Heitz zur INDUS, einem weltweit agierenden Unternehmen, das Beteiligungen an mittelstaendischen Hidden Champions haelt'

**Correzione proposta:** Controllata di INDUS Holding AG (gruppo quotato) dal 2016; dato dimensionale da integrare con fonte e anno


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


### Olanda (5)

#### Bangma Verpakking B.V. — campo `dimensione`

LEAD NON VALIDO — aggravamento rispetto a quanto annotato. Non solo De Jong Verpakking ha acquisito Bangma (closing 30-07-2020), ma nel 2023 l'INTERO De Jong Packaging Group è stato acquisito da STORA ENSO (multinazionale finlandese quotata). Bangma Verpakking opera oggi 'as part of the De Jong Verpakking and Stora Enso family': non è più un'entità autonoma sotto il profilo decisionale e la compliance EUDR si determina a livello di capogruppo Stora Enso, che ha già un proprio programma EUDR di gruppo. Da rimuovere dalla lista lead.

**Evidenza:** https://dejongverpakking.com/en/news/de-jong-packaging-completes-acquisition-of-bangma-verpakking/ ; https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - 'in 2023 werd De Jong Packaging Group overgenomen door Stora Enso ... vandaag maakt Bangma Verpakking deel uit van de De Jong Verpakking en Stora Enso familie'; https://www.agf.nl/article/9238854/de-jong-verpakking-neemt-bangma-verpakking-over/

**Correzione proposta:** Rimuovere il lead (controllata Stora Enso via De Jong Packaging Group dal 2023)

#### BeBo Parket B.V. — campo `referente`

Referente obsoleto: Frans Bolier e Johan van de Beek (fondatori 2006) hanno ceduto l'azienda nel 2022 alla seconda generazione. La direzione e' oggi di Kees van de Beek e Marielle Zwolsman.

**Evidenza:** https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Kees van de Beek en Marielle Zwolsman maakten al deel uit van het management van Bebo en blijven het bedrijf leiden na de overdracht'

**Correzione proposta:** Kees van de Beek / Marielle Zwolsman - Directeur

#### L. Verhoeven's Emballagefabriek en Houthandel B.V. — campo `dimensione`

Appartenenza a gruppo non dichiarata: l'azienda opera in gruppo con la consociata Zagerij Verhoeven (Harskamp) e con Kist&Co (Ridderkerk) e Harskamp Timber (Harskamp). Il campo la presenta come singola azienda familiare: la struttura di gruppo incide sia sul perimetro EUDR (segheria a monte) sia sul dimensionamento.

**Evidenza:** https://verhoeven-emballage.nl/en/about-us/ - frammento: 'works closely with sister company Zagerij Verhoeven in Harskamp; the group also includes Kist&Co in Ridderkerk and Harskamp Timber in Harskamp'

**Correzione proposta:** Gruppo Verhoeven: Zagerij Verhoeven (Harskamp), Kist&Co (Ridderkerk), Harskamp Timber (Harskamp)

#### Rompa Tanneries B.V. — campo `denominazione`

Denominazione obsoleta: la societa' e' stata ridenominata VITELCO LEATHER B.V. Vitelco (gruppo PALI) ha rilevato le quote di Rompa Leather sciogliendo la joint venture ed e' oggi socio unico al 100%. Anche la pagina LinkedIn indicata (nl.linkedin.com/company/rompa-tanneries) si presenta ora come 'Vitelco Leather'.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco and Rompa Leder however decided to dissolve this joint venture and Vitelco took over the Rompa Tanneries shares from Rompa Leder. Vitelco is now 100% owner of the tannery and changes its name to Vitelco Leather B.V.'

**Correzione proposta:** Vitelco Leather B.V.

#### Rompa Tanneries B.V. — campo `dimensione`

Assetto proprietario dichiarato errato: il campo indica ancora 'Soci: PALI Group (Den Bosch, vitello) e Rompa Leather (Rijen)', ma la JV e' stata sciolta e Vitelco (PALI Group) e' socio unico al 100%. La societa' e' quindi una controllata integrale di gruppo (PALI Group, 's-Hertogenbosch): la compliance EUDR si decide a livello di capogruppo, il lead va riqualificato o scartato.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco is now 100% owner of the tannery'

**Correzione proposta:** Controllata al 100% di Vitelco B.V. (PALI Group), 's-Hertogenbosch


### Belgio (9)

#### Corné Port-Royal Chocolatier SA — campo `dimensione`

LEGAME DI GRUPPO NON DICHIARATO. Corne Port-Royal Chocolatier SA (BE 0433.283.558, denominazione abbreviata registrale 'CPR CHOCOLATIER') e' controllata dal gruppo Neuhaus dal 2013: Neuhaus figura direttamente fra gli amministratori della societa'. Neuhaus (fatturato ~149 M EUR all'epoca dell'operazione, gruppo che possiede anche Jeff de Bruges) e' a sua volta parte di un gruppo belga quotato. La decisione di compliance EUDR si prende a livello di capogruppo Neuhaus: il lead cosi' com'e' (PMI indipendente da 8,8 M EUR) e' fuorviante.

**Evidenza:** https://www.pappers.be/fr/company/corne-port-royal-chocolatier-0433283558 — dirigeants: NEUHAUS, BELLEGRO (administrateur delegue), Valerie Paquot, Isabel Baert, nomine dal 05-12-2023. Frammento RTBF/RetailDetail: "Neuhaus rachete le chocolatier Corne Port-Royal" (https://www.rtbf.be/article/wavre-corne-port-royal-rachete-par-neuhaus-7994003); "Neuhaus Holding a rachete Corne Port-Royal au groupe Distripar, filiale de la CNP".

**Correzione proposta:** Dichiarare nel campo dimensione: controllata dal gruppo Neuhaus (Neuhaus SA amministratore) dal 2013; valutare l'esclusione del lead perche' la compliance e' decisa dalla capogruppo.

#### Dolfin SA — campo `dimensione`

Dato aziendale incompleto e ormai superato dagli eventi: nell'aprile 2026 Dolfin e' diventata azionista di maggioranza della Chocolaterie Galler (rilevata da un consorzio vallone insieme a Wallonie Entreprendre, investitori privati e Sebastien Desclee). Dolfin non e' piu' una micro-cioccolateria da ~6 M EUR ma la capogruppo di un insieme Dolfin+Galler che si avvicina alla soglia di esclusione. Il legame non e' dichiarato nel campo.

**Evidenza:** Frammento La Libre/QU4TRE: "le capital de la nouvelle societe Galler est desormais majoritairement dans les mains de la chocolaterie familiale Dolfin, basee a Nivelles" — https://www.qu4tre.be/infos/economie/des-actionnaires-wallons-reprennent-la-chocolaterie-galler/2014147 ; https://www.parismatch.be/actualites/societe/2026/04/23/la-chocolaterie-galler-reprise-par-un-consortium-wallon-70-licenciements-prevus-sur-les-170-employes-75IWTID2DVEGDN6O56R2JXHSQQ/

**Correzione proposta:** Dichiarare: dall'aprile 2026 Dolfin SA e' azionista di maggioranza della nuova Chocolaterie Galler; valutare il perimetro dimensionale del gruppo Dolfin+Galler.

#### Extremis NV — campo `referente`

Referente non aggiornato: Dirk Wynants e' oggi owner e chief designer, NON il vertice esecutivo. L'amministratore delegato in carica e' Valentine Batjoens, nominata CEO in successione a Yff Vandendriessche. Il campo attribuisce erroneamente a Wynants la funzione di vertice.

**Evidenza:** https://www.lovethatdesign.com/?post_type=news&p=378797 e https://www.linkedin.com/posts/extremis_meet-our-new-ceo-aka-captain-of-the-ship-activity-7046080915592069121-Z6QI - frammento: "Extremis appointed Valentine Batjoens as its new Chief Executive Officer... continue the course of outgoing CEO Yff Vandendriessche. However, Dirk Wynants remains as the owner and chief designer of Extremis"

**Correzione proposta:** Valentine Batjoens — CEO (Dirk Wynants resta fondatore/proprietario e chief designer)

#### La Chocolaterie Galler SA — campo `dimensione`

AZIENDA IN CRISI E CEDUTA. Galler era in procedura di riorganizzazione giudiziaria (PRJ 'silenziosa') ed e' stata rilevata nell'aprile 2026 da un consorzio vallone (chocolaterie Dolfin come azionista di maggioranza, Wallonie Entreprendre, investitori privati, Sebastien Desclee) tramite la costituzione di una 'nuova societa' Galler', con 70 licenziamenti su 170 dipendenti. Il record ne fa un cenno ma non ne trae le conseguenze: la societa' storica BE 0416.169.689 potrebbe non essere piu' l'entita' operativa (cessione di attivi a nuova entita'), il fatturato ~29,5-32 M EUR e i 194 dipendenti sono superati, e la compliance e' ora decisa dal nuovo azionariato (Dolfin). Lead da riqualificare o scartare; il numero d'impresa da usare va riverificato in KBO.

**Evidenza:** Frammento La Libre: "Un projet de relance d'un nouveau Galler entierement entre des mains belges permet d'eviter le choc d'une faillite frontale" (23-04-2026); "L'entreprise chocolatiere liegeoise Galler, qui avait ete placee en procedure de reorganisation judiciaire silencieuse, a ete reprise par des actionnaires entierement wallons ... le capital ... majoritairement dans les mains de la chocolaterie familiale Dolfin" — https://www.qu4tre.be/infos/economie/des-actionnaires-wallons-reprennent-la-chocolaterie-galler/2014147

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

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

#### Vincent Sheppard NV — campo `referente`

Referente errato: Brendan McCarthy risulta Managing Director di Vincent Sheppard USA / Sika Design USA (struttura distributiva statunitense nata nel 2021 con Design Holdings), non della NV belga. Il vertice della societa' belga e' Jos Destrooper, entrato come nuovo CEO e investitore (proveniente da Lotus Bakeries).

**Evidenza:** crunchbase.com/person/brendan-mccarthy: 'Managing Director @ Vincent Sheppard and Sika Design USA'; made-in.be/west-vlaanderen/nieuwe-ceo-en-investeerder-bij-vincent-sheppard: 'Jos Destrooper ... operationeel en als aandeelhouder (fifty-fifty) naast de familie Claeys'

**Correzione proposta:** Jos Destrooper — CEO / gedelegeerd bestuurder

#### Vincent Sheppard NV — campo `dimensione`

Assetto proprietario non dichiarato: dal 2002 la societa' e' controllata dalla famiglia Claeys tramite Cennini Holding e oggi il capitale e' 50/50 tra la famiglia Claeys e Jos Destrooper. Il fatturato 20.832.726 € e i 36,3 FTE sono invece confermati.

**Evidenza:** made-in.be 'Nieuwe CEO en investeerder bij Vincent Sheppard': 'In 2002 werd de familie Claeys (Cennini Holding) 100 procent eigenaar'; trendstop.knack.be/nl/detail/456646801: 'turnover of €20,832,726 ... 36.3 FTEs'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto


### Austria (1)

#### Tschurtschenthaler Gerberei GmbH — campo `email`

Nessuna e-mail pubblica reperibile (campo 'n.d.') e nessun sito web aziendale: il lead non e' contattabile per via digitale. Le fonti pubbliche (WKO, herold.at, cylex, yelp) riportano solo indirizzo e telefono.

**Evidenza:** https://firmen.wko.at/tschurtschenthaler-gerberei-gmbh/k%C3%A4rnten/ - la scheda WKO riporta solo indirizzo Bach 17, 9623 St. Stefan/Gailtal e telefono 04283 20..., nessuna e-mail ne' sito

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto


---

## 5. Casi di gravità MEDIA (154)

_Dato dubbio o obsoleto: da rinfrescare prima del contatto, non necessariamente errato._


### Italia (11)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| A. Brivio Compensati SpA | dimensione | Dato obsoleto: 15,41M€ è il 2023; il bilancio 2024 riporta ricavi per 12,24M€ (-20%) e una perdita di -365.141€, con 84 dipendenti. L'azienda resta in forbice ma in contrazione. | https://www.companyreports.it/a-brivio-compensati-spa-02109430153 — 'Fatturato € 12.241.471,00 (2024); Utile € -365.141,00 (2024); Dipendenti 84' | ≈12,2M€ (fatturato 2024, Registro Imprese) — perdita netta 2024 |
| Conceria 800 S.p.A. | dimensione | Fatturato indicato 11,4M€; il bilancio 2023 riporta 9,12M€ con perdita netta di -547.884€. Dato sovrastimato e società in perdita (20-49 dipendenti). | https://topaziende.quotidiano.net/toscana/pisa/fatturato-conceria-800-spa/ — 'ricavi 9.118.508 € (2023); utile netto -547.884 €; dipendenti 20-49' | ≈9,1M€ (bilancio 2023, Top Aziende) — perdita netta 2023 |
| Conceria Belvedere S.r.l. | dimensione | Fatturato indicato 14M€; i bilanci depositati riportano 11,78M€ (2023) e 11,28M€ (2022). Dato sovrastimato o riferito ad anno non dichiarato. | https://www.reportaziende.it/conceria_belvedere_srl_vi_03742800240 — 'ricavi 2023: 11.776.554 €; 2022: 11.280.042 €; dipendenti 20-49' | ≈11,8M€ (fatturato 2023, Registro Imprese/ReportAziende) |
| Conceria Beschin | denominazione | Manca la forma giuridica e c'è ambiguità di soggetto: al Registro risultano due entità distinte, 'Conceria Beschin S.n.c. di Graziano Beschin & C.' e 'Conceria Beschin S.r.l. (Unipersonale)', entrambe a Chiampo. Va identificato quale è l'operatore EU | https://www.reteimprese.it/concerie-tintorie-pellami-cuoio/chiampo/azienda/1239180 ('Conceria Beschin Snc') e https://www.reteimprese.it/concerie-tint |  |
| Conceria Beschin | dimensione | Campo 'n.d.': la S.n.c. (P.IVA 00594430241) non deposita bilancio pubblico e risulta avere 10-19 dipendenti, dimensione che rende probabile un fatturato SOTTO la forbice target 5-40M€. DA CONFERMARE prima di lavorare il lead. | https://www.reportaziende.it/conceria_beschin_snc_di_graziano_beschin_c_vi_00594430241 — 'dipendenti 10-19; ultimo bilancio depositato: ricavi **** (d |  |
| Conceria Daniela | denominazione | Manca la forma giuridica e il nome è ambiguo: al Registro esistono 'CONCERIA DANIELA S.R.L.' (P.IVA 03948180249) e 'CONCERIA DANIELA DI DAL MONTE GIULIANO E C. S.N.C.' (P.IVA 00601580244), entrambe ad Arzignano. Il sito conceriadaniela.com fa capo al | https://www.ufficiocamerale.it/9084/conceria-daniela-srl e https://www.ufficiocamerale.it/3712/conceria-daniela-di-dal-monte-giuliano-e-c-snc | Conceria Daniela S.r.l. |
| Conceria Daniela | dimensione | Campo 'n.d.': impossibile verificare la forbice target 5-40M€. DA CONFERMARE. | Nessun dato di fatturato nei frammenti; scheda https://www.ufficiocamerale.it/9084/conceria-daniela-srl senza cifre nei risultati |  |
| Conceria Emmedue | dimensione | Campo 'n.d.': il fatturato reale è ~4,2M€ (2025), quindi SOTTO la forbice target 5-40M€. Lead sottodimensionato, da declassare. | https://www.reportaziende.it/conceria_emmedue_srl_vi_00793250242 — 'fatturato 4,2 milioni di euro (2025), utile netto 231,6 mila €, +10,2% sull'anno p | ≈4,2M€ (fatturato 2025) — sotto forbice target |
| Conceria La Veneta S.p.A. | dimensione | Dato obsoleto: 12,9M€ è il fatturato 2024; nel 2025 i ricavi sono scesi a 8,68M€ (-32,7%), quindi al limite inferiore della forbice target. Calo rilevante da segnalare al commerciale. | https://registroaziende.it/azienda/conceria-la-veneta-spa-arzignano — 'ricavi 8.681.980 € (2025); 2024: 12,9 mln; 2022: 19.397.025 €; 63 dipendenti' | ≈8,7M€ (fatturato 2025, Registro Imprese) — era 12,9M€ nel 2024 |
| Conceria Lomar (Lomar Lavorazione Pelli S.r. | email | L'indirizzo 'lomar@concerialomar.it' non compare nelle fonti pubbliche reperite; le schede aziendali e la certificazione LWG riportano 'info@concerialomar.it'. DA CONFERMARE. | https://www.reportaziende.it/lomar_lavorazione_pelli_srl_vi_02002810246 — 'Email: info@concerialomar.it; Tel +39 0444625050; PEC lomar@pec-italia.it' | info@concerialomar.it |
| Cuoificio Bisonte S.p.A. | dimensione | Fatturato indicato 12,1M€: sottostimato/obsoleto. Il bilancio 2023 riporta ricavi per 15,25M€ e utile 428.879€ (20-49 dipendenti). | https://topaziende.quotidiano.net/toscana/pisa/fatturato-cuoificio-bisonte-spa/ — 'fatturato 2023: 15.247.239 €; utile 428.879 €; dipendenti 20-49; co | ≈15,2M€ (fatturato 2023, Top Aziende/Registro Imprese) |

### Germania (20)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Alder Sägewerk & Holzhandlung GmbH | dimensione | Campo privo di qualsiasi elemento dimensionale ('Umsatz/MA n.d.'): nessun tipo di dato, nessuna fonte, nessun anno. Segheria familiare (HRB 201958 Amtsgericht Stadthagen) verosimilmente molto sotto la forbice target 5-40 Mio EUR, senza segnalazione e | https://www.northdata.com/Alder%20S%C3%A4gewerk%20&%20Holzhandlung%20GmbH,%20Auhagen/Amtsgericht%20Stadthagen%20HRB%20201958 - scheda registro senza d |  |
| Christian Göbel Holzgroßhandlung GmbH & Co.  | email | L'Impressum ufficiale riporta l'indirizzo info@goebel-holz.com (dominio .com), non info@goebel-holz.de come indicato nel record. Il sito e invece www.goebel-holz.de. | https://www.goebel-holz.de/impressum/ - 'Telefon: 069 / 95 30 19-18 ... E-Mail: info@goebel-holz.com ... USt-IdNr.: DE112006391' | info@goebel-holz.com |
| Christian Göbel Holzgroßhandlung GmbH & Co.  | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d.'), sostituito da un elemento non dimensionale ('>85 anni'). Nessun fatturato ne numero addetti con fonte e anno. | https://www.wlw.com/en/company/christian-goebel-holzgrosshandlung-grosshandlung-mit-sperrholz-gmbh-co-kg-755264 e https://www.northdata.com/Christian% |  |
| E. Fuhlrott GmbH & Co. KG (HOLZFUHLROTT) | dimensione | Il dato '~20-49 MA (wlw.de)' e una fascia di portale senza anno di riferimento e senza alcun dato di fatturato ('Umsatz n.d.'). Non consente di collocare il lead nella forbice 5-40 Mio EUR. | https://www.wlw.de/de/firma/e-fuhlrott-gmbh-co-kg-kistenfabrik-und-holzhandel-483545 (fascia addetti, senza anno); https://www.invest-in-thuringia.de/ |  |
| Furnierwerk Bühl GmbH | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d.'). Le fonti danno indicazioni discordanti: classe di fatturato 10-50 Mio EUR ma totale di bilancio 2023 di soli 1,8 Mio EUR. Da riverificare prima di considerare il lead in forbice. | https://implisense.com/de/companies/furnierwerk-buehl-gmbh-buehl-DE7ZGDDBNO95 - 'Bilanzsumme 2023: 1,8 Mio EUR'; https://www.wer-zu-wem.de/firma/furni | Totale di bilancio 1,8 Mio EUR (2023, Bundesanzeiger via Implisense); classe di fatturato 10-50 Mio EUR (wer-zu-wem) - D |
| Gebr. Kilger, Lederfabrik Viechtach KG | dimensione | Il campo riporta solo '~20 MA, Umsatz n.d.' senza anno ne fonte. Il dato dipendenti e confermabile (fonte 2019) ma nessun dato di fatturato e disponibile; con ~20 addetti e 1.000-1.500 pelli/mese l'azienda e verosimilmente molto sotto la forbice targ | https://www.hogn.de/2019/07/02/1-da-hogn-geht-um/nachrichten-im-landkreis-regen/michael-kilger-viechtach-leder-manufaktur-guertel-schuhe-gerbung-satte | ~20 dipendenti (fonte: hogn.de, 2019); volumi 1.000-1.500 pelli/mese; fatturato non pubblicato (KG non tenuta al deposit |
| HOFA Holzimport GmbH | dimensione | 'Umsatz >2,5 Mio EUR (Firmenauskunft), cifra esatta n.d.' non e un dato dimensionale utilizzabile: soglia aperta, senza anno e senza fonte puntuale. Non permette di verificare la forbice target 5-40 Mio EUR. | https://firmeneintrag.creditreform.de/22145/2390205389/HOFA_HOLZIMPORT_GMBH - scheda Creditreform senza cifra di fatturato nei frammenti; https://www. |  |
| Hartmann Möbelwerke GmbH | dimensione | Fatturato di riferimento del 2017 (8 anni fa) e fascia addetti '~140-210' troppo ampia. Il dato piu recente disponibile e il totale di bilancio 2023 di 10 Mio EUR (+5,2% sull'anno precedente); gli addetti confermati sono 'oltre 140'. | https://implisense.com/en/companies/hartmann-moebelwerke-gmbh-beelen-DEZSR23ZJW75 - 'last published balance sheet total 2023: 10 M EUR, +5.2%'; https: | Totale di bilancio 10 Mio EUR (2023, Bundesanzeiger via Implisense); oltre 140 dipendenti (Die Glocke, 2024); fatturato  |
| Lederfabrik Josef Heinen GmbH & Co. KG (Hein | dimensione | Dato dimensionale obsoleto (2019/2020, 5+ anni) e in conflitto con le fonti: Creditreform/firmeneintrag colloca l'azienda in classe di fatturato 50-100 Mio EUR, non 20-35 Mio EUR. Va riverificato l'anno di riferimento. | https://firmeneintrag.creditreform.de/41844/5230009708/LEDERFABRIK_JOSEF_HEINEN_GMBH_CO_KG - classe di fatturato 50-100 Mio EUR; https://www.kfw.de/st | Fatturato 35 Mio EUR (2019, KfW Stories); classe di fatturato indicata da Creditreform 50-100 Mio EUR - anno piu recente |
| Lederfabrik Josef Heinen GmbH & Co. KG (Hein | esistenza_stato | DA CONFERMARE lo stato dell'azienda: Creditreform registra una variazione di bonita (Bonitaetsaenderung) datata 02.09.2025 il cui motivo non emerge dalle fonti aperte. Considerato che il settore concia tedesco ha gia registrato piu insolvenze, lo sta | https://firmeneintrag.creditreform.de/41844/5230009708/LEDERFABRIK_JOSEF_HEINEN_GMBH_CO_KG - 'Bonitaetsaenderung am 02.09.2025'; nessuna notizia di in |  |
| Max Cropp GmbH & Co. KG (Timber Im- & Export | email | Il campo email e valorizzato con 'n.d.' mentre l'indirizzo compare letteralmente nell'Impressum/contatti aziendali. | https://www.cropp-timber.com/de/kontakt/ e https://www.edelholzshop.de/de/service/about/ - 'Telefon: 040 - 766 235-0; E-Mail: info@cropp-timber.com' | info@cropp-timber.com |
| Max Cropp GmbH & Co. KG (Timber Im- & Export | dimensione | Il campo riporta '~13 MA' senza fonte ne anno e 'Umsatz n.d.'. Nessun elemento consente di verificare la forbice target 5-40 Mio EUR; l'ordine di grandezza (~13 addetti in un'attivita di import/commercio) resta indeterminato. | https://www.cropp-timber.com/de/unternehmen/ - azienda fondata nel 1919, nessuna cifra dimensionale pubblicata; https://www.cropp-timber.com/de/untern |  |
| Meisen Holzverarbeitung GmbH & Co. KG | dimensione | Il dato '~20-49 MA (Regiomanager)' e una fascia di portale priva di anno e non e accompagnato da alcun dato di fatturato ('Umsatz n.d.'): il campo non permette di collocare il lead nella forbice 5-40 Mio EUR. | https://www.regiomanager.de/koeln-bonn-aachen/unternehmen/meisen-holzverarbeitung-gmbh-und-co-kg/ (fascia addetti senza anno); https://firmeneintrag.c |  |
| PFT Holz in Form GmbH | dimensione | Il fatturato e indicato solo come classe '10-50 Mio EUR' senza anno di riferimento: fascia troppo ampia (copre sia il centro sia il limite superiore della forbice target). Anche il dato addetti (~35) e privo di anno. | https://www.wer-zu-wem.de/firma/formsperrholz.html e https://firmeneintrag.creditreform.de/96132/3410092585/PFT_HOLZ_IN_FORM_GMBH - classe di fatturat |  |
| Paletten Meyer | dimensione | Campo privo di qualsiasi elemento dimensionale ('Umsatz/MA n.d.'): nessun tipo di dato, nessuna fonte, nessun anno. Trattandosi di impresa individuale non soggetta a deposito di bilancio, il dato non e ricavabile dai registri e il lead non e collocab | https://www.regiomanager.de/suedwestfalen/unternehmen/meyer-palettenbau/ - profilo aziendale senza cifre; impresa individuale (Inh. Julian Meyer), nes |  |
| Parkett Herter GmbH & Co. KG | dimensione | Il fatturato e espresso come fascia aperta verso il basso ('fino a 10 Mio EUR') e senza anno di riferimento: compatibile anche con valori sotto la soglia minima della forbice target (5 Mio EUR). Anche '>30 MA' e privo di anno. | https://www.firmenwissen.de/az/firmeneintrag/72116/7270165223/PARKETT_HERTER_GMBH_CO_KG.html - 'Jahresumsatz bis 10 Mio EUR', 'mehr als 30 Mitarbeiter |  |
| RMW Wohnmöbel GmbH & Co. KG (Rietberger Möbe | dimensione | Il fatturato di ~20 Mio EUR e una STIMA di portale (Die Deutsche Wirtschaft) priva di anno di riferimento e non ricavata da bilancio depositato; non e affiancata da alcun dato addetti. Il campo non e verificabile. | https://die-deutsche-wirtschaft.de/unternehmen/rmw-wohnmoebel-gmbh-co-kg-rietberg/ - 'geschaetzter Umsatz 20 Mio EUR' (stima, senza esercizio) |  |
| Weinheimer Leder GmbH | dimensione | Campo privo di qualsiasi elemento dimensionale verificabile ('Umsatz/MA n.d.'): non dichiara ne tipo di dato, ne fonte, ne anno. Impossibile collocare il lead nella forbice target 5-40 Mio EUR. | https://www.firmenwissen.de/az/firmeneintrag/69469/7170220020/WEINHEIMER_LEDER_GMBH.html (scheda Firmenauskunft, HRB 432889 Mannheim) - nessun fattura |  |
| Weinheimer Leder GmbH | dimensione | Struttura di gruppo non dichiarata: Weinheimer Leder GmbH e collegata a Das Lederband GmbH (Weinheim, HRB 724382), con Uwe Holubeck Geschäftsführer di entrambe; le fonti aperte non chiariscono il verso del controllo. L'azienda e inoltre nata nel 2003 | https://www.northdata.de/Das%20Lederband%20GmbH,%20Weinheim/Amtsgericht%20Mannheim%20HRB%20724382 - collegamento societario con Weinheimer Leder GmbH, |  |
| ecopell GmbH | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d. (dal 1992)'). Le fonti disponibili indicano una micro-impresa: totale di bilancio 2023 pari a ~900 mila EUR (-20,1% sull'anno precedente), capitale sociale 265.000 EUR. E' quindi molto al di sotto del | https://implisense.com/en/companies/ecopell-gmbh-weitnau-seltmans-DE7L5HN3YI34 - 'last published balance sheet total of Ecopell GmbH in 2023 was 900k  | Totale di bilancio ~0,9 Mio EUR (2023, Bundesanzeiger via Implisense) - micro-impresa, fuori forbice target |

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

### Olanda (30)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Arco Meubelfabriek B.V. | referente | Referente da riconfermare: le fonti pubbliche indicano Jorre van Ast alla guida dell'azienda familiare dal 2011 come creative director, affiancato dal managing director Jan Tichelaar. 'F. van Ast' risulta solo dal dato Company.info (algemeen directeu | https://www.vno-ncw.nl/forum/meubelfabriek-arco-120-jaar-vallen-opstaan-en-weer-doorgaan - frammento: 'In 2011 kwam het familiebedrijf onder leiding v |  |
| BeBo Parket B.V. | dimensione | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dichiarata nel campo (solo il legame con BeBo Groep B. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'samen met investeerder Nobel Capital Partners' |  |
| BeBo Parket B.V. | dimensione | Il fatturato di ca. 20 M EUR e' datato 2024 nel record, ma il dato di 20 milioni compare nell'articolo sul passaggio generazionale del 2022 (riferito all'esercizio precedente). Anno del dato DA CONFERMARE. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Vorig jaar had Bebo Parket een omzet van 20 mil |  |
| BeBo Parket B.V. | linkedin | Il link LinkedIn e' il profilo personale di Frans Bolier (nl.linkedin.com/in/frans-bolier-b64b394a), non la pagina aziendale di BeBo Parket. Trattandosi di un ex titolare uscito nel 2022, il link non e' utilizzabile. | https://nl.linkedin.com/in/frans-bolier-b64b394a - titolo: 'Frans Bolier - directeur mede-eigenaar beboparket BV' |  |
| Beijleveld Houtimport B.V. | referente | Referente e ruolo assenti: il direttore statutario e' la persona giuridica Beyleveld Groep B.V. e nelle fonti aperte non emerge alcun nome fisico. Senza referente il lead non e' azionabile. DA CONFERMARE. | https://www.transfirm.nl/nl/organisatie/24136531-000016457986-beijleveld-houtimport-b.v. e https://drimble.nl/bedrijf/rotterdam/16457986/beijleveld-ho |  |
| Bruns B.V. | email | Il campo email riporta 'n.d.' ma esiste una casella nominativa pubblica del direttore: jan.burgmans@bruns.nl. Il record e' quindi ingiustificatamente privo di recapito operativo. | http://bergeijk.gevabiz.nl/company/bruns-bv-bergeijk.html - frammento: 'Managing director Jan Burgmans, e-mail: jan.burgmans@bruns.nl' | jan.burgmans@bruns.nl |
| De Leeuw Huidenhandel N.V. | referente | Referente e ruolo assenti. Il direttore statutario iscritto al KVK e' una persona giuridica (LHST B.V., algemeen directeur dal 2022): manca un nome fisico per il contatto commerciale. Nei frammenti pubblici compare solo Christian Hossu (chossu@deleeu | https://companyinfo.nl/organisatieprofiel/groothandel-in-huiden-en-vellen/de-leeuw-huidenhandel-n-v-winterswijk-08011164-000017531705 - frammento: 'LH |  |
| GWW Houtimport B.V. | dimensione | Controllata di gruppo: dal 01/01/2026 GWW Houtimport, GWW Agency e Van den Berg Hardhout confluiscono nella holding Van den Berg Houtgroep. Il legame e' gia' dichiarato correttamente nel campo, ma la compliance EUDR si decidera' a livello di capogrup | https://www.houtwereld.nl/nieuws/van-den-berg-en-gww-houtimport-gaan-samen/ - frammento: 'GWW Houtimport, GWW Agency en Van den Berg Hardhout uit Lopi |  |
| GWW Houtimport B.V. | dimensione | Il campo cita 'Secondo direttore citato: John Hoogendoorn': non trova riscontro. Il comunicato di riorganizzazione indica Arjan de Jong come algemeen directeur (confermato) e Bart van Meuwen come commercieel directeur; Albert Oudenaarden passa agli a | https://www.houtwereld.nl/nieuws/van-den-berg-en-gww-houtimport-gaan-samen/ - frammento: 'Arjan de Jong is benoemd tot algemeen directeur en Bart van  | Bart van Meuwen - commercieel directeur |
| Hardhouthandel Hotim B.V. | dimensione | Il campo dichiara 'n. KVK non reperito': il numero risulta invece pubblicato. Creditsafe riporta per Hotim B.V. il KvK-nummer 17051960. Da riconciliare con la denominazione esatta iscritta (Hotim B.V. / Hardhouthandel Hotim B.V.). | https://www.creditsafe.com/business-index/en-us/company/hotim-bv-nl00776206 - frammento: 'Hotim B.V. has KvK-nummer: 17051960' | KVK 17051960 (da riconciliare con la ragione sociale esatta) |
| Hardhouthandel Hotim B.V. | referente | Referente e ruolo assenti; nelle fonti aperte consultate non emerge il nome del directeur/eigenaar. DA CONFERMARE. | https://www.hotim.nl/contact/ (pubblica solo verkoop@hotim.nl e tel. 013 514 24 44, nessun nome) |  |
| Houthandel Jos Dennebos B.V. | dimensione | Il numero di dipendenti e' lasciato discordante (20-49 vs 2-5). La fonte aziendale scioglie il dubbio: circa 30 addetti nella produzione di pavimenti in legno a Raalte. Il record va aggiornato. | https://www.dennebosflooring.com/en/about-us/ - frammento: 'About 30 employees produce their wooden floors for various clients, both in and outside Eu | ca. 30 dipendenti (fonte dennebosflooring.com, 2025) |
| Houthandel Jos Dennebos B.V. | referente | Referente e ruolo assenti. Il socio unico e' la persona giuridica Jos Dennebos Exploitatie B.V.; il fondatore storico e' Jos Dennebos (attivo anche in Dennebos Suriname). Nome e carica del directeur attuale DA CONFERMARE. | https://companyinfo.nl/organisatieprofiel/groothandel-in-hout-en-plaatmateriaal/houthandel-jos-dennebos-b-v-raalte-05073894-000016548884 e https://www |  |
| Houtimport Reuver B.V. | dimensione | Anno di fondazione errato: il record indica 1987, ma l'azienda e' stata fondata il 1 aprile 1973 dai fratelli Jac e Wiel Schoolmeesters come commercio di pannelli truciolari. | https://www.houtimportreuver.nl/ - frammento: 'opgericht op 1 april 1973 door de gebroeders Jac en Wiel Schoolmeesters' | Fondata il 01/04/1973 |
| Houtimport Reuver B.V. | referente | Referente e ruolo assenti (algemeen directeur iscritto e' la persona giuridica Gebrs. Schoolmeesters Holding B.V.). Nelle fonti aperte compare Tim Schoolmeesters in relazione alla direzione dell'azienda: nome DA CONFERMARE come directeur attuale. | https://companyinfo.nl/organisatieprofiel/groothandel-in-hout-en-plaatmateriaal/houtimport-reuver-b-v-reuver-12024480-000019946104 e https://appartme. |  |
| Houtplex B.V. | dimensione | Controllata di gruppo estero: Houtplex appartiene al gruppo Wood United, con sede a Singapore; dal febbraio 2019 le quote sia di Houtplex sia di Wood United sono di Timothy Paul, che ha rilevato la partecipazione di Jan Kersten. Il legame di gruppo e | https://www.houtwereld.nl/nieuws/houtplex-en-wood-united-overgenomen/ - frammento: 'Timothy Paul heeft de aandelen in Houtplex (Haaksbergen) en Wood U |  |
| Houtplex B.V. | referente | Referente e ruolo assenti. Le fonti indicano Timothy Paul come titolare della gestione quotidiana di Houtplex dopo l'uscita del precedente directeur Koen Kersten (passato a Kegro Deuren); Ruud van Oene, commercieel directeur, e' andato in pensione. D | https://www.houtwereld.nl/nieuws/houtplex-en-wood-united-overgenomen/ - frammento: 'Timothy Paul heeft de dagelijkse leiding van Houtplex overgenomen. |  |
| M.S. Pallets B.V. | referente | Referente assente: il directeur statutario e una persona giuridica (Maso Onroerend B.V.), nessun nome fisico pubblicato. DA CONFERMARE il nome della persona fisica dietro la holding prima di usare il lead per un contatto nominale. | https://companyinfo.nl/organisatieprofiel/vervaardiging-van-houten-emballage/m-s-pallets-b-v-den-ham-05049728-000016563247 - il campo dimensione del r |  |
| Montis B.V. | dimensione | Legame di gruppo: Montis e uno dei sei marchi della Lande Groep (con Artifort, Lande, Portner, Zwaardvis, A Lott Of Space), che produce in NL, BE, DE e TR. Il legame e dichiarato nel campo ma senza precisare che la compliance EUDR si decide a livello | https://www.landefamily.nl/montis - 'Montis is one of six strong brands under the Lande Groep (along with A Lott Of Space, Artifort, Lande, Portner an |  |
| Montis B.V. | dimensione | Il fatturato indicato (ca. 24,6 M$ ~ 22 M€) proviene da stime RocketReach/Creditsafe, non da un bilancio depositato: il campo stesso ammette che il fatturato non e depositato. Dato da trattare come stima non verificata, non come fatturato. | https://www.creditsafe.com/business-index/en-ie/company/montis-bv-nl01008091 - il campo dichiara 'Fatturato esatto NON depositato pubblicamente (B.V.  |  |
| Montis B.V. | referente | Referente e ruolo assenti. DA CONFERMARE il directeur attuale della B.V.: le fonti pubbliche associano Montis alla direzione storica di Paul van den Berg (dal 1975) ma non confermano un vertice in carica oggi sotto Lande Groep. | https://www.landefamily.nl/montis - 'high-quality design furniture from its own factory in Dongen since 1975 under the leadership of Paul van den Berg |  |
| Origin Bridge (Barchem) | denominazione | Forma giuridica NON risolta dopo 3 ricerche: nessuna fonte pubblica indicizzata riporta la rechtsvorm né una denominazione legale con suffisso. Restano solo KVK 70878315 e P.IVA NL001587917B24 pubblicati dall'azienda stessa. La struttura del numero I | https://originbridge.coffee/legal-information/ e https://originbridge.coffee/contact/ - 'Heidehoflaan 2B, 7244AG Barchem, The Netherlands ... CoC: 708 |  |
| Origin Bridge (Barchem) | email | L'email del foglio (info@bridgetoorigin.com) NON è quella principale del sito ufficiale: la pagina di contatto di originbridge.coffee indica come recapito dell'entità olandese europe@originbridge.coffee, tel. +31 85 301 6984. info@bridgetoorigin.com  | https://originbridge.coffee/contact/ - 'Origin Bridge Netherlands, Heidehoflaan 2B, 7244AG Barchem ... +31 85 301 6984 ... europe@originbridge.coffee' | europe@originbridge.coffee |
| Rompa Tanneries B.V. | email | Email e sito legati al vecchio marchio (sales@rompa-tanneries.com / www.rompa-tanneries.com). Con la ridenominazione in Vitelco Leather il dominio di riferimento del gruppo e' vitelco.nl; il vecchio sito hulshof.com rimanda ancora a 'Rompa Tanneries' | http://www.hulshof.com/ (titolo pagina: 'Rompa Tanneries') e https://www.vitelco.nl/en/about-us |  |
| Rompa Tanneries B.V. | referente | Referente e ruolo vuoti. Le fonti stampa locali citano Twan de Bie come 'directeur leerlooierij' dello stabilimento di Lichtenvoorde. DA CONFERMARE la carica attuale dopo il passaggio a Vitelco Leather. | https://www.gld.nl/nieuws/2414011/directeur-leerlooierij-laat-de-wethouder-bellen-dan-lossen-we-het-als-volwassen-mensen-op - frammento: 'De directeur |  |
| Smeulders Interieurwerken B.V. | email | Email assente ('n.d.'): il lead non e contattabile via e-mail. Il campo dimensione cita j.mulder@smeulders-ig.nl trovata in directory, ma non e riportata nel campo email ne verificata come casella attiva. DA CONFERMARE una casella generica sul domini | https://smeulders-ig.nl/contact/ - pagina contatti del gruppo; il record stesso riporta 'Non risulta pubblicata una casella info@ generica' |  |
| Van Ierssel Houtimport B.V. | dimensione | Controllata di gruppo: Van Ierssel Houtimport e stata rilevata da Boogaerdt Hout nel 1986 e fa parte della Koninklijke Boogaerdt Groep. Il legame e dichiarato nel campo, ma il lead resta una controllata: la decisione di compliance EUDR si colloca a l | https://www.boogaerdthout.nl/en/2026/02/04/commercial-manager-member-of-ierssel-houtimport/ - 'In 1986 Van Ierssel Houtimport was taken over by Boogae |  |
| Van Ierssel Houtimport B.V. | referente | Fred Verver risulta confermato come directeur operativo di Van Ierssel (con werfmanager Ton van Oers), ma nelle fonti compare anche Oscar Smeets come 'Directeur Boogaerdt Hout - Van Ierssel Houtimport': verificare quale sia il vertice statutario dell | https://nl.linkedin.com/in/oscar-smeets-55856411 - 'Oscar Smeets - Directeur \| Boogaerdt Hout - Van Ierssel ...'; https://www.linkedin.com/in/fred-ve |  |
| Van den Berg Hardhout B.V. | email | Incoerenza di dominio: l'email e su .nl (info@vandenberghardhout.nl) mentre il sito ufficiale e le e-mail nominative del personale sono sul dominio .com (vandenberghardhout.com). Verificare quale dominio di posta sia realmente attivo. | https://rocketreach.co/albert-oudenaarden-email_99038923 - 'a******@vandenberghardhout.com'; https://www.vandenberghardhout.com/en/contact/ | info@vandenberghardhout.com (da confermare) |
| Van den Berg Hardhout B.V. | dimensione | Legame di gruppo dichiarato ma imminente: dal 01/01/2026 la societa e nella holding Van den Berg Houtgroep insieme a GWW Houtimport e GWW Agency. Con 6 dipendenti confermati e fatturato non pubblicato, l'azienda e sotto la forbice 5-40 M€ e la compli | https://rocketreach.co/van-den-berg-hardhout-bv-profile_b40aa59bff9a461e - 'Van den Berg Hardhout BV employs 6 people and is based in Lopik, Utrecht' |  |

### Belgio (50)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| A & A Chocolaterie NV | linkedin | NON E' UN DUPLICATO. Verificato il rilievo del controllo automatico: A & A Chocolaterie NV e Pralinart NV sono due societa' realmente distinte, con numeri d'impresa KBO diversi (BE 0892.388.320 vs BE 0450.589.051), sedi diverse (Mosten 16 vs Waasland | https://www.companyweb.be/en/0892388320/a-a-chocolaterie (A & A Chocolaterie, fondata 20-09-2007, sede Mosten 16, 9160 Lokeren, BE0892388320) e https: | Mantenere entrambi i record. Segnalare esplicitamente nel campo linkedin che la pagina https://be.linkedin.com/company/a |
| A & A Chocolaterie NV | sito | Il sito indicato (hamlet.be) e' il dominio della capogruppo/distributore Hamlet NV, non un dominio proprio di A & A Chocolaterie NV. Stesso valore assegnato anche a Pralinart NV: i due record condividono sito, LinkedIn ed email ('n.d.'), quindi nessu | https://www.hamlet.be/pagina/over-hamlet/productiesites-onze-merken-kerncijfers/ — le due societa' vi compaiono come siti produttivi del gruppo Hamlet |  |
| A & A Chocolaterie NV | referente | Referente e ruolo vuoti ed email 'n.d.': il lead non e' contattabile in modo diretto. L'unico nominativo emerso dalle fonti pubbliche e' Jeroen Van Overloop, indicato come COO di A&A Chocolaterie & Pralin'Art — ruolo operativo, non il titolo statutar | Frammento di ricerca: "Jeroen Van Overloop is the COO of A&A Chocolaterie & Pralin'Art" (https://be.linkedin.com/company/a&a-chocolaterie-pralin'art) |  |
| A & A Chocolaterie NV | dimensione | Il legame di gruppo e' correttamente dichiarato, ma va valutato l'effetto sul perimetro commerciale: A & A Chocolaterie (22,1 M€) e Pralinart (18,4 M€) sono entrambe controllate al 100% da Hamlet NV, quindi la decisione di compliance EUDR si prende v | https://www.hamlet.be/pagina/over-hamlet/productiesites-onze-merken-kerncijfers/ ; companyweb 0892388320 (22.087.972 €, 35,4 FTE, deposito 22-10-2025) |  |
| Belvas SA | referente | Il referente indicato (Thierry Noesen, fondatore) risulta tuttora amministratore, ma le fonti recenti indicano come CEO operativo Jean-David Couderc. Il vertice esecutivo attuale va riconfermato; inoltre la forma giuridica di Belvas compare in piu' f | Frammento di ricerca: "Thierry Noesens serves as the director of Belvas, with Jean-David Couderc as CEO"; https://hainaut-terredegouts.be/producteur/b |  |
| Bruyerre Chocolates SA | referente | Referente e ruolo vuoti. Le fonti pubbliche indicano Marc Delsemme come Administrateur Delegue di Bruyerre Chocolates (con Olivier de Macar, coacquirente della cioccolateria e cofondatore di Bruyerre Chocolates SA). Titolo coerente con una SA vallona | https://rocketreach.co/marc-delsemme-email_123029407 ("Marc Delsemme ... Bruyerre Chocolates Administrateur Delegue"); https://bruyerre.eu/en/history/ | referente: Marc Delsemme — ruolo: Administrateur delegue (DA CONFERMARE su KBO/NBB) |
| Bulo NV | referente | Referente probabilmente non aggiornato. Dirk Busschop risulta CEO in fonti risalenti (2009); l'azienda e' oggi guidata dalla terza generazione, Carlo e Louis Busschop, con Carlo Busschop indicato come Managing Director / CEO in fonti recenti. Da rico | https://www.bulo.com/third_generation/ e https://rocketreach.co/carlo-busschop-email_93406361 - frammento: "Carlo Busschop, based in Mechelen, BE, is  | Carlo Busschop — gedelegeerd bestuurder / Managing Director (DA CONFERMARE) |
| Buzzispace NV | email | Email 'n.d.': record privo di indirizzo di contatto nonostante il sito buzzi.space sia attivo. DA CONFERMARE. | https://www.buzzi.space/brand (sito attivo, nessun indirizzo e-mail nei frammenti) |  |
| Carlens NV | referente | Referente e ruolo assenti. Le fonti pubbliche citano 'Carl Carlens' in contesto gestionale, mentre il campo dimensione ipotizza 'Luc Carlens' da FinCheck: nomi discordanti, nessuno dei due confermato come gedelegeerd bestuurder. DA CONFERMARE su BCE/ | https://www.limoco-industries.be/referenties/240-houthandel-carlens-keuze-voor-leverancier-dicht-bij-huis - frammento: risultati che referenziano "Car |  |
| Chocolaterie Ickx NV | sito | Il dominio indicato (ickx.be) non e' quello aziendale. Il sito ufficiale della cioccolateria e' choc-ickx.be — coerente anche con l'email gia' censita nel record (avangastel@choc-ickx.be), che usa lo stesso dominio. | https://www.choc-ickx.be/ compare come sito ufficiale nei risultati per "Chocolaterie Ickx"; sede confermata Rijkmakerlaan 28, 2910 Essen, BE 0421.359 | https://www.choc-ickx.be/ |
| Chocolaterie Ickx NV | referente | Referente e ruolo vuoti. Emerge solo che nel 2016 Bas Huurman ha lasciato la responsabilita' operativa ai tre figli; i nomi degli attuali gedelegeerd bestuurders non sono esposti nei frammenti gratuiti (dati riservati agli abbonamenti premium di papp | Frammento: "In 2016, Bas Huurman stepped back from operational responsibility and delegated it to his three children" — https://trends.knack.be/econom |  |
| Confiserie De Bie - L'Abeille - Trefin NV | referente | Referente e ruolo vuoti. Le fonti registrali indicano come amministratori Bert Verriet e Lisette Lerno. Fatturato (11.404.101 €), FTE (34,4) e deposito (08-06-2026) risultano confermati. | Frammento FinCheck: "The directors of Confiserie Trefin are Bert Verriet and Lisette Lerno" — https://fincheck.be/nl/confiserie-trefin/0400.120.050/Lo | referente: Bert Verriet — ruolo: gedelegeerd bestuurder (DA CONFERMARE quale dei due amministratori sia il delegato) |
| Confiserie Vandenbulcke NV | referente | Referente e ruolo vuoti. La terza generazione e' al timone con Jelle Vandenbulcke come CEO, affiancato dai cugini Bert e Luk. Fatturato 13.332.120 € confermato (44° posto di settore). | Frammento Voka/Made-in: "the third generation is now in charge, with CEO Jelle Vandenbulcke and his cousins Bert and Luk at the helm"; https://trendst | referente: Jelle Vandenbulcke — ruolo: CEO / gedelegeerd bestuurder |
| Confortluxe NV | referente | Referente e ruolo assenti benche' gli amministratori siano pubblici e confermati (Jacqueline Pauwels, Jimmy Ollevier, Heidi Ollevier). Il fondatore Andre Ollevier, storico gedelegeerd bestuurder, e' deceduto: non usarlo come referente. Da attribuire  | https://fincheck.be/en/confortluxe/0412.863.078/Wervik/connections - frammento: "The current board members of Confortluxe are Jacqueline Pauwels, Jimm | Jimmy Ollevier — bestuurder (ruolo di gedelegeerd bestuurder DA CONFERMARE) |
| Corné Port-Royal Chocolatier SA | referente | Referente e ruolo vuoti ed email 'n.d.'. Dalle fonti registrali l'administrateur delegue e' la societa' di management BELLEGRO (persona fisica non esposta nei frammenti gratuiti); gli altri amministratori nominati il 05-12-2023 sono NEUHAUS SA, Valer | https://www.pappers.be/fr/company/corne-port-royal-chocolatier-0433283558 — "BELLEGRO ... Administrateur, Administrateur delegue ... depuis le 5 decem |  |
| Decolvenaere BV | dimensione | Fatturato fortemente sottostimato. Il campo riporta 'oltre 10 milioni di euro' (fonte giornalistica Sterck Magazine), ma i dati di bilancio piu' recenti indicano un fatturato totale di 38.585.036 EUR, con altre fonti che collocano l'azienda nella fas | Frammenti di ricerca su Decolvenaere BV (BE 0400.079.171): "The most recent financial statements show a total turnover of EUR 38,585,036.00" e "turnov | Fatturato ~38,6 M EUR (ultimo bilancio depositato NBB) — DA RICONFERMARE sulla fonte NBB primaria |
| Delafaille NV | referente | Il referente indicato (Paul Daems) e' esplicitamente uscente: le fonti sull'operazione Maestrani (23-06-2025) confermano che Daems, proprietario e CEO, resta solo 'per un periodo limitato' per accompagnare la transizione e che verra' nominato un nuov | Frammento just-food: "Paul Daems, Delafaille's current owner and CEO, [will] stay with the company for a 'limited period' as he aids the transition, b |  |
| Delafaille NV | dimensione | Il legame di gruppo e' dichiarato ma la conclusione tratta nel campo ('resta pero' PMI belga autonoma con obblighi EUDR propri') e' opinabile: Maestrani Schweizer Schokoladen ha acquisito il 100% delle azioni di Delafaille e della sua controllata cec | Frammento bpv Braun Partners: "Maestrani ... acquisition of Belgian chocolate manufacturer Delafaille with a major Czech subsidiary [Ostrapack]"; "Del |  |
| Dolfin SA | referente | Referente e ruolo vuoti ed email 'n.d.'. Le fonti pubbliche indicano Jean-Jacques de Gruben come proprietario e Directeur General di Dolfin SA (ha rilevato la cioccolateria nel 2007 insieme a Gilles van der Meerschen). | Frammento: "En 2007, Jean-Jacques de Gruben a repris les renes de la Chocolaterie Dolfin" (https://www.dolfin.be/en/who-are-we/); "Jean-Jacques de Gru | referente: Jean-Jacques de Gruben — ruolo: Administrateur delegue / Directeur general (DA CONFERMARE il titolo statutari |
| Extremis NV | dimensione | Fatturato potenzialmente obsoleto: il campo riporta 12.900.125 EUR e 24,8 FTE dall'ultimo bilancio, ma risulta gia' depositato un bilancio piu' recente (deposito 02-07-2026) i cui dati non sono riflessi nel record. DA AGGIORNARE. | https://www.companyweb.be/en/0434625128/extremis - frammento: "The most recent financial statements of Extremis were filed on 02-07-2026" |  |
| Houthandel Denis Luyten NV | referente | Referente e ruolo assenti; il campo dimensione dichiara esplicitamente che il nome del gestore non e' pubblicato. Nemmeno le ricerche mirate restituiscono il gedelegeerd bestuurder in carica (azienda alla 4a generazione della famiglia Luyten). DA CON | https://www.companyweb.be/en/0403778831/houthandel-denis-luyten - frammento: "At the time of its most recent financial statements, Houthandel Denis Lu |  |
| Hulpiau Hides BV | referente | Referente e ruolo assenti. Le fonti pubbliche citano Raimond Hulpiau come 'current senior manager' (fratello del fondatore Christiaan Hulpiau), ma il ruolo formale (zaakvoerder/gedelegeerd bestuurder) non e' pubblicato: DA CONFERMARE. | https://www.hulpiauhides.com/en/about-us/ - frammento: "Christiaan Hulpiau, brother of current senior manager Raimond Hulpiau, founded Hulpiau Hides" |  |
| Jori NV | referente | Referente e ruolo assenti e non ricostruibili dalle fonti pubbliche consultate: nessun nome di gedelegeerd bestuurder/CEO emerge per Jori NV (BE 0888.984.313). DA CONFERMARE. Fatturato 16.143.273 EUR, 106,8 FTE e sede Hoogweg 52, 8940 Wervik risultan | https://www.companyweb.be/en/0888984313/jori - frammento: "with a revenue of EUR 16.143.273, Jori from Wervik ranks 19th in the furniture manufacturin |  |
| Keukenontwerpers NV | filiera | Perimetro EUDR debole. L'azienda opera con l'insegna SieMatic Keukenontwerpers come rivenditore/installatore a valle di cucine prodotte dalla tedesca SieMatic: non e' l'operatore che immette per primo il prodotto in legno sul mercato UE (lo e' il fab | https://www.keukenontwerpers.com/ e https://trustlocal.be/antwerpen/geel/keukenbouwer/siematic-keukenontwerpers/ - frammento: "SieMatic Keukenontwerpe |  |
| Keukenontwerpers NV | referente | Referente e ruolo assenti; nessuna fonte pubblica restituisce il gedelegeerd bestuurder di Keukenontwerpers NV (BE 0472.648.534). L'email geel@keukenontwerpers.com non e' inoltre riscontrabile letteralmente nei frammenti. DA CONFERMARE entrambi. Fatt | https://trendstop.knack.be/nl/detail/472648534/keukenontwerpers.aspx - frammento: "With a turnover of 16,033,016 euros, Keukenontwerpers is ranked 7th |  |
| Klingele Chocolade NV | dimensione | Il fatturato di ~8 M€ non e' verificabile: nell'ultimo bilancio depositato alla NBB (24-08-2025) la societa' NON pubblica la cifra d'affari (schema abbreviato). L'unico dato pubblico e' il margine lordo di 3.568.803 €, 44a posizione nel settore 'Choc | jaarrekening.be/nl/KLINGELE-CHOCOLADE/0479.916.606: 'Op het moment van haar meest recente jaarrekening publiceerde Klingele Chocolade geen omzetcijfer |  |
| Koffiebranderij Or BV (OR Coffee Roasters) | dimensione | La societa' e' molto piu' piccola di quanto lasci intendere l'obiettivo dichiarato di ~6 M€: l'ultimo esercizio (2024) registra 5,00 FTE e nessuna cifra d'affari pubblicata. Con 5 dipendenti e un margine lordo di 785.594 € si tratta di una micro-impr | fincheck.be/nl/koffiebranderij-or/0473.952.589/Wetteren/overzicht: 'In 2024 had het bedrijf 5,00 voltijdse equivalenten (VTE) in dienst'; 'De jaaromze |  |
| Koffiebranderij Or BV (OR Coffee Roasters) | dimensione | Controllata di gruppo: dall'aprile 2024 la societa' e' stata acquisita da Anaerobic Holding (Anversa), gia' proprietaria di Mister Barish Beans & Machines. Il legame e' dichiarato nel campo, ma va tenuto presente che la decisione di compliance EUDR s | kmoinsider.be/finance/koffiebranderij-or-coffee-roasters-uit-wetteren-overgenomen: 'Anaerobic Holding (Antwerpen), moederbedrijf van koffieautomatenve |  |
| La Chocolaterie Galler SA | referente | Referente, ruolo, LinkedIn ed email tutti vuoti/'n.d.': il lead non e' contattabile. Dalle cronache dell'operazione 2026 emerge Sebastien Desclee, CEO ad interim di Chocolaterie Galler e ora anche fra gli azionisti della nuova societa'. DA CONFERMARE | Frammento: "Le consortium d'actionnaires est compose de la chocolaterie Dolfin, de Wallonie Entreprendre (WE), d'un groupe d'investisseurs prives et d | referente: Sebastien Desclee — ruolo: CEO (ad interim) / administrateur delegue (DA CONFERMARE) |
| Lavrijsen Houtbedrijf NV | dimensione | Fatturato obsoleto e indirizzo errato. Il campo riporta 12.763.339 EUR (dato trendstop), mentre l'ultimo bilancio depositato indica 14.093.447 EUR e 23,1 FTE (non '20-49 addetti'). Inoltre la sede legale registrata e' Koning-Albertstraat 123, 2440 Ge | https://www.companyweb.be/en/0407106030/houtbedrijf-lavrijsen - frammento: "Houtbedrijf Lavrijsen recorded a total turnover of EUR 14,093,447.00... Th | Fatturato 14.093.447 EUR e 23,1 FTE (ultimo bilancio NBB); sede Koning-Albertstraat 123, 2440 Geel |
| Le Cercle du Cacao SRL | dimensione | Micro-impresa di consulenza/sourcing fuori dalla forbice 5-40 M€ (fatturato non pubblicato, struttura sostanzialmente unipersonale attorno al fondatore). La limitazione e' dichiarata nel campo, ma il record non e' un lead commercialmente utilizzabile | lecercleducacao.be: 'Le Cercle du Cacao, sourcing, négoce et consultance en fèves de cacao'; 'Nico Regout est fondatrice, actionnaire principale et gé |  |
| Manutti BV | dimensione | Il fatturato 15.340.098 € e i 27,4 FTE (bilancio NBB depositato 17-06-2024) sono confermati. Non trova invece riscontro pubblico l'affermazione di uno 'stabilimento produttivo in Indonesia (circa 140 addetti)': le fonti presentano Manutti come design | companyweb.be/en/0476263070/manutti: 'Manutti recorded a total turnover of EUR 15,340,098.00 according to the most recent financial statements filed o |  |
| Manutti BV | dimensione | Legame di gruppo con Manutti Invest BV (BE 0478.148.434) dichiarato nel record: si tratta della holding familiare che controlla l'operativa. Segnalato come 'media' perche' gia' dichiarato; la decisione di compliance potrebbe collocarsi a livello di h | https://www.companyweb.be/en/0478148434/manutti-invest |  |
| Mecam NV | referente | Il referente indicato (Inge Meers, CFO) non e' il vertice della societa'. Il gedelegeerd bestuurder / CEO e' il fratello Luc Meers, che ha la direzione generale; Inge cura la parte finanziaria. | meubihome.be / sterck-magazine.be: 'CFO en bestuurder Inge Meers runt samen met haar broer Luc het bedrijf'; wonen360.nl: 'CEO Luc Meers'; trendstop:  | Luc Meers — Gedelegeerd bestuurder / CEO |
| Mecam NV | dimensione | Il record riporta 32.145.268 € e 111,6 FTE per la sola Mecam NV, mentre la stampa parla di 37 M€ cumulati e ~220 dipendenti per l'intero Mecam Group (Mecam + Neo-Style). Il legame di gruppo esiste ed e' accennato ma il perimetro del dato va esplicita | sterck-magazine.be: 'Mecam ... met een gecumuleerde omzet van 37 miljoen euro (2023)'; 'Raymond Meers richtte de Mecam Group op in 1978 ... vandaag we |  |
| Meubelfabriek Lievens NV | dimensione | Fatturato 19.952.978 € e 53,5 FTE confermati, ma il dato e' anteriore all'uscita dal mercato olandese (dal 31-01-2024 Lievens e Confortluxe hanno abbandonato i Paesi Bassi, con azzeramento del fatturato NL). Il fatturato futuro sara' verosimilmente i | interiorbusiness.nl 'Meubelfabrikanten Confortluxe en Lievens herorienteren zich en verlaten Nederlandse markt'; wonen360.nl 'Confortluxe en Meubelfab |  |
| Passe Partout NV | dimensione | Il record non segnala che la produzione non avviene in Belgio: Passe Partout produce in Ungheria dal 1999, mentre a Temse lavorano ~13 persone (coerente con gli 11,3 FTE). Elemento rilevante per qualificare il ruolo EUDR (immissione sul mercato di mo | interiorbusiness.nl: 'Passe Partout ... produceert sinds 1999 vanuit Hongarije ... kantoor in Temse waar 13 mensen werken' |  |
| Pralinart NV | dimensione | Il fatturato riportato (18.427.020 €) proviene da un bilancio depositato il 02-11-2023, quindi riferito all'esercizio 2022: dato di 3+ anni fa, mentre le consociate del blocco hanno depositi 2025/2026. Inoltre trendstop riporta per Pralinart una cifr | Frammento companyweb/trendstop: "The company has an omzet (turnover) of €25,223,632 and ranks 33rd in the Chocolate and confectionery sector"; "Pralin |  |
| Pralinart NV | linkedin | Stesso rilievo speculare ad A & A Chocolaterie NV: le due societa' sono distinte (KBO BE 0450.589.051 vs BE 0892.388.320, sedi diverse) ma condividono la medesima pagina LinkedIn congiunta e il medesimo sito di gruppo hamlet.be, con email 'n.d.' in e | https://www.companyweb.be/en/0450589051/pralinart — Pralinart NV, Waaslandlaan 32, 9160 Lokeren, BE 0450.589.051; pagina condivisa https://be.linkedin |  |
| Radermecker SRL | referente | Referente e ruolo assenti. La conceria e' stata rilevata nell'aprile 2016 da due ingegneri francesi, Loic Honore e Nicolas Quintin, che ne sono gli attuali gestori: candidati referenti (gerant / administrateur delegue) da confermare su fonte societar | https://www.lavenir.net/regions/wallonie-picarde/comines-warneton/2022/01/14/cuirs-selliers-la-specialite-de-la-tannerie-radermecker-a-comines-YLAPU6L |  |
| Radermecker SRL | email | Email 'n.d.': nessun indirizzo di contatto nel record. Il sito radermecker.com espone una pagina contatti, ma l'indirizzo non e' recuperabile via frammenti di ricerca. DA CONFERMARE. | https://www.radermecker.com/pages/on-parle-de-nous-dans-la-presse (sito attivo, indirizzo e-mail non estraibile dai frammenti) |  |
| Royal Botania NV | referente | Referente probabilmente superato/impreciso. Kris Van Puyvelde risulta 'hoofddesigner en zaakvoerder' e cofondatore, non CEO; il cofondatore Frank Boschman ha lasciato l'azienda intorno al 2018 e nelle interviste recenti l'azienda e' rappresentata da  | apbc.be/stories/awd-2-kris-van-puyvelde-royal-botania: 'Kris van Puyvelde is hoofddesigner en zaakvoerder van Royal Botania'; wonen360.nl/article/9224 |  |
| Sas NV (Sas Coffee) | referente | Herman Sas risulta ancora 'gedelegeerd bestuurder' negli estratti KBO pubblicati (pappers.be, insieme a Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HELFINCO), ma nessuna fonte post-cessione a Nimbus (05/2024) lo riconferma al vertice operati | https://www.pappers.be/nl/company/sas-0404190783 - 'Herman Sas is de gedelegeerd bestuurder; overige bestuurders: Dominic Sas, Danielle Vanden Eede, M |  |
| Sas NV (Sas Coffee) | email | L'email nel foglio (info@sas-koffie.be) NON e' quella pubblicata sul sito ufficiale sas-coffee.com: la pagina di contatto riporta CUSTOMERSERVICE@SAS-COFFEE.COM, tel. +32 14 61 12 00, indirizzo LILSEDIJK 36 - 2340 BEERSE. info@sas-koffie.be resta rep | https://sas-coffee.com/en/contact/ - 'CUSTOMERSERVICE@SAS-COFFEE.COM \| +32 14 61 12 00 \| LILSEDIJK 36 - 2340 BEERSE - BELGIUM' | customerservice@sas-coffee.com ; sede Lilsedijk 36, 2340 Beerse DA CONFERMARE |
| Silco NV | dimensione | Discordanza 4,8 vs 8,4 M€ NON risolta: le due banche dati continuano a riportare cifre diverse per lo stesso ultimo bilancio depositato (14-06-2024). Trendstop: EUR 8.358.215 (23a nel settore 'koffie en thee'); Companyweb/Fincheck: EUR 4.843.986. Sen | https://trendstop.knack.be/nl/detail/715792692/silco.aspx - 'omzet van 8.358.215 euro, 23e in de sector Koffie en thee'; https://www.companyweb.be/en/ |  |
| Tannerie Masure SA | email | Email 'n.d.'. Il sito masure.be ha una pagina contatti attiva ma l'indirizzo non e' verificabile dai frammenti. DA CONFERMARE. | https://www.masure.be/contact (pagina contatti esistente; indirizzo e-mail non presente nei frammenti) |  |
| VC Wood Zottegem NV | referente | Il record afferma che 'il nome del gestore non e' pubblicato in fonti verificabili': non e' vero. I zaakvoerders sono i fratelli Van Cauwenberge (terza generazione): Thomas, Tim e Bart Van Cauwenberge. | managermagazines.be 'Vc Wood Zottegem — Eenvoudig veelzijdig': 'Thomas Van Cauwenberge is een van de zaakvoerders, samen met zijn broers Tim en Bart' | Thomas Van Cauwenberge (con i fratelli Tim e Bart) — zaakvoerder/bestuurder |
| Vanerum Belgie NV | referente | Gert Van Erum e' il CEO della capogruppo i3-Group, non l'amministratore della sola Vanerum Belgie NV: il mandato esclude l'uso dell'amministratore di capogruppo come referente della controllata. Va individuato il responsabile della societa' belga. | trends.knack.be: 'Gert Van Erum (CEO i3 Group)'; cbinsights: 'i3-Group, formerly VANERUM Group, founded 1968, based in Diest' |  |
| Vanerum Belgie NV | dimensione | Il legame di gruppo e' dichiarato ma incompleto: i3-Group non e' piu' interamente familiare. WorxInvest ha acquistato circa il 25% per 10 M€ e nel novembre 2023 anche il gruppo americano Steelcase ha preso una partecipazione. La compliance EUDR si de | derijkstebelgen.be 'NIEUW – WorxInvest betaalt 10 miljoen euro voor kwart van Van Erum schoolborden'; holahageland.net 'Na WorxInvest neemt ook Amerik |  |
| Woodtex NV | dimensione | Dato di fatturato superato. Il record riporta 11.778.466 € (deposito 23-06-2025); l'ultimo bilancio depositato (01-06-2026) indica 12.131.554 € con 35 FTE. | companyweb.be/en/0413744194/woodtex: 'Woodtex recorded a total turnover of €12,131,554.00. The most recent financial statements were filed on 01-06-20 | Fatturato 12.131.554 € - 35 FTE (bilancio NBB depositato 01-06-2026) |

### Austria (10)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| BRAUN LOCKENHAUS GmbH | dimensione | Filiale di gruppo estero: la societa' e' controllata da SCHNEEWEISS AG / SCHNEEWEISS interior, con sede del gruppo a Kippenheim (Baden-Württemberg, DE), dal 2006. La decisione di compliance EUDR si assume a livello di capogruppo tedesca. Il legame e' | https://www.braunlockenhaus.at/en/imprint - frammento: "Geschäftsführer Jochen Joachims und Gesellschafter SCHNEEWEISS AG"; "Braun Lockenhaus is part  |  |
| Breitschopf Gesellschaft mbH & Co KG | referente | Il referente indicato (Martin Breitschopf) fa parte del 'Fuehrungstrio' familiare dal 2021 con delega a vendite/finanza/strategia, ma il Geschaeftsfuehrer iscritto dal 2001 risulta Dipl.-Ing. Johann Breitschopf. Il ruolo formale di Martin come GF non | https://www.meinbezirk.at/steyr-steyr-land/c-wirtschaft/breitschopf-kuechen-setzt-auf-fuehrungstrio_a6834711 - frammento: "Johann Breitschopf (Dipl.-I |  |
| Hrachowina Fenster & Türen GmbH | dimensione | Fatturato ca. 25 Mio EUR dichiarato come stima non ufficiale (die-deutsche-wirtschaft.de) e senza anno. Da segnalare inoltre il precedente di insolvenza 2019 della controllata produttiva H&W Holzfensterproduktions-GmbH (JV con Weinzetl), poi rilevata | https://www.holzkurier.com/holzprodukte/2019/06/hrachowina.html - frammento: "H&W Holzfensterproduktions-GmbH had to file for insolvency in late Febru |  |
| Jannach Lärchenholz GmbH | email | Campo e-mail vuoto ('n.d.'): l'Impressum offusca l'indirizzo in chiave anti-spam e nessuna fonte pubblica riporta letteralmente un recapito. Il lead resta contattabile solo via form/telefono. DA CONFERMARE. | https://jannach.com/kontakt/impressum.html - pagina Impressum senza indirizzo e-mail in chiaro; conferma GF: "Mag. (FH) Helmut Jannach is the manager  |  |
| Ludwig Reiter Schuhmanufaktur GmbH | email | L'indirizzo office@ludwig-reiter.com non compare nell'Impressum aziendale, che riporta reiter@ludwig-reiter.com come recapito di contatto. | https://www.ludwig-reiter.com/de/impressum - frammento: "telephone +43-1-2559300, fax +43-1-2559300-77, and email reiter@ludwig-reiter.com" | reiter@ludwig-reiter.com |
| Ludwig Reiter Schuhmanufaktur GmbH | dimensione | Il fatturato di ca. 15 Mio EUR e i ca. 60 dipendenti attribuiti a Wikipedia/AustriaWiki (2019-2023) non trovano riscontro: la voce Wikipedia riporta solo dati storici di organico (ca. 70 addetti nel 1919, ca. 130 nel 1966) e nessun dato di fatturato  | https://de.wikipedia.org/wiki/Ludwig_Reiter_Schuhmanufaktur - frammento: "In 1919, approximately 70 employees were employed, and in 1966, the company  |  |
| Mayr - Schulmöbel Gesellschaft m.b.H. | dimensione | Il fatturato di ca. 39,0 Mio EUR (stima Die Deutsche Wirtschaft) e' smentito dai dati di ricavo pubblicati dall'azienda/stampa locale: 21 Mio EUR nel 2013, 22,4 Mio EUR nel 2014, 23,1 Mio EUR nel 2016 (+5%). Cade quindi anche l'avvertenza 'AZIENDA DI | https://www.meinbezirk.at/salzkammergut/c-wirtschaft/50000-schueler-lernen-erfolgreich-auf-sesseln-von-mayr-schulmoebel_a824339 - frammento: "In 2013  | Fatturato ca. 23,1 Mio € (2016, ultimo dato pubblicato), ca. 145 dipendenti |
| Mayr - Schulmöbel Gesellschaft m.b.H. | dimensione | Il secondo Geschaeftsfuehrer indicato nel campo ('Ing. Florian Huemer') non e' riscontrato: le fonti riportano come coppia di GF Franz Josef Wiener (referente del record, corretto) e Maximilian Auinger. | https://newsroom.kommhaus.com/qualitaetsschulmoebel-made-in-austria/ - frammento: "The two managing directors of Mayr Schulmoebel are Franz Josef Wien | Secondo Geschäftsführer: Maximilian Auinger |
| Tschurtschenthaler Gerberei GmbH | sito | Sito aziendale assente ('n.d.'): nessun dominio proprio individuato nelle fonti pubbliche, solo schede di directory (herold, cylex, europages). | https://www.herold.at/gelbe-seiten/st-stefan-im-gailtal/RZ2RJ/tschurtschenthaler-gerberei-gmbh/ - scheda senza URL aziendale |  |
| Waldviertler Werkstätten GmbH | dimensione | Dato di fatturato datato (2016-2019) e non riconciliato: le fonti citano 31 Mio EUR di ricavi 2016 riferiti all'universo GEA e, per la controllante Heinrich Staudinger GmbH, un totale di bilancio 2024 di 5,45 Mio EUR. Il perimetro societario del dato | https://www.firmenabc.at/heinrich-staudinger-gmbh-gea-waldviertler_NTLA - frammento: "balance sheet total of EUR 5.454.811,76 as of December 31, 2024" |  |

---

## 6. Casi di gravità BASSA (85)

_Refusi formali e incoerenze di stile._


### Italia (14)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| 3C Lavorazione Pelli S.r.l. | denominazione | Ragione sociale al Registro Imprese riportata come '3 C - LAVORAZIONE PELLI S.R.L.' (con spazio e trattino), non '3C Lavorazione Pelli S.r.l.' | https://www.europages.it/3-C-LAVORAZIONE-PELLI-SRL/SEAC000597361-002.html — '3 C - LAVORAZIONE PELLI SRL a Arzignano, Conceria'; idem https://www.pagi | 3 C - Lavorazione Pelli S.r.l. |
| A. Brivio Compensati SpA | denominazione | Forma giuridica scritta in modo non conforme: al Registro Imprese la ragione sociale è 'A. BRIVIO COMPENSATI S.P.A.' (non 'SpA'). | https://www.ufficiocamerale.it/1666/a-brivio-compensati-spa — 'A. BRIVIO COMPENSATI S.P.A., Partita IVA: 02109430153 ... Forma giuridica: SOCIETA' PER | A. Brivio Compensati S.p.A. |
| Conceria Ambassador S.p.A. | linkedin | Campo vuoto: la pagina LinkedIn aziendale esiste ed è riscontrata. | https://it.linkedin.com/company/conceria-ambassador-spa — 'CONCERIA AMBASSADOR SPA \| LinkedIn' | https://it.linkedin.com/company/conceria-ambassador-spa |
| Conceria Cilp | denominazione | Manca la forma giuridica: la ragione sociale attuale al Registro Imprese è 'CONCERIA CILP S.R.L.' (P.IVA 00190610501), ex 'Conceria Cilp S.n.c. di Poggetti Riccardo e Davide'. | https://www.ufficiocamerale.it/9423/conceria-cilp-snc-di-poggetti-riccardo-e-davide — 'CONCERIA CILP S.R.L., Partita IVA: 00190610501' | Conceria CILP S.r.l. |
| Conceria Emmedue | denominazione | Manca la forma giuridica: al Registro Imprese la ragione sociale è 'CONCERIA EMMEDUE S.R.L.' (P.IVA 00793250242). | https://www.ufficiocamerale.it/1739/conceria-emmedue-srl — 'CONCERIA EMMEDUE SRL, Partita IVA: 00793250242' | Conceria Emmedue S.r.l. |
| Conceria Ferrari S.r.l. | dimensione | Manca l'anno di riferimento; il dato aggiornato di bilancio 2023 è 20,52M€ (utile 1,15M€, 20-49 dipendenti), non 19,9M€. | https://registroaziende.it/azienda/conceria-ferrari-srl-chiampo — 'fatturato 2023: 20,52 milioni; utile 1,15 milioni (-28%)'; https://www.aziende.it/c | ≈20,5M€ (fatturato 2023, Registro Imprese) |
| Conceria Italia S.p.A. | fonte | L'URL indicato (www.conceriaitalia.com/contatti) non risulta essere la pagina contatti del sito: la pagina CONTATTI pubblicata è /nuova-pagina. Link probabilmente non valido. | Risultato di ricerca: 'CONTATTI — Conceria Italia' → https://www.conceriaitalia.com/nuova-pagina | https://www.conceriaitalia.com/nuova-pagina |
| Conceria Lomar (Lomar Lavorazione Pelli S.r. | dimensione | Valore corretto (6,2M€, bilancio 2024) ma manca l'anno di riferimento nel campo; è comunque il record più vicino al limite inferiore della forbice 5-40M€. | https://www.ufficiocamerale.it/1740/lomar-lavorazione-pelli-srl — 'ultimo bilancio depositato 2024: ricavi 6.199.639 €; 20-49 dipendenti' | ≈6,2M€ (fatturato 2024, Registro Imprese) |
| Conceria Nuova Impala S.r.l. | dimensione | Valore confermato (22,25M€, bilancio 2024, in calo del 5,39%) ma manca l'anno nel campo. | https://www.reportaziende.it/conceria_nuova_impala_srl_pi — 'ultimo bilancio 2024: ricavi 22.248.620 €, -5,39% sul precedente' | ≈22,2M€ (fatturato 2024, Registro Imprese) |
| Conceria Nuova Impala S.r.l. | referente | Campo vuoto. Le fonti pubbliche indicano come figure apicali Gianfranco Caponi (direttore tecnico) e Mauro Vannucci (direttore amministrativo), seconda generazione dei fondatori: non è però confermato chi sia l'amministratore unico/legale rappresenta | https://www.nuovaimpala.com/ — 'fondata oltre 35 anni fa da Mario Caponi e dal cugino Orlando Vannucci, passata poi ai rispettivi figli, Gianfranco e  |  |
| Conceria Tolio S.p.A. | dimensione | Il numero di dipendenti indicato (~50-249, da Europages) è errato: il Registro Imprese riporta una fascia 20-49 dipendenti. Il fatturato 16,2M€ è confermato ma è del 2023 (utile 91.705€, molto sottile). | https://www.ufficiocamerale.it/5218/conceria-tolio-spa — 'fatturato 16.201.421 € (2023); utile 91.705 €; dipendenti 20-49; costo del personale 2.460.3 | ≈16,2M€ (fatturato 2023) / 20-49 dipendenti (Registro Imprese) |
| Conceria Tolio S.p.A. | referente | Campo vuoto: il vertice attuale è identificabile con certezza dalle fonti di distretto. | https://www.distrettovenetodellapelle.it/soci-distretto-veneto-pelle/concia/conceria-tolio-spa/ — 'Conceria Tolio nasce nel 1962 da un'idea imprendito | Mario Tolio — Presidente |
| Fonpelli S.p.A. | denominazione | Forma giuridica errata: al Registro Imprese la società è 'FONPELLI - S.R.L.' (P.IVA 01705980249), non S.p.A. Anche il sito e le schede camerali riportano S.r.l. | https://www.ufficiocamerale.it/2684/fonpelli-spa — 'FONPELLI - S.R.L., Partita IVA: 01705980249'; https://xrayfinance.it/fonpelli-s-p-a — 'FONPELLI S. | Fonpelli S.r.l. |
| Fonpelli S.p.A. | dimensione | Valore confermato (15,32M€) ma manca l'anno: è il bilancio 2024, chiuso però in perdita (-203.123€) con 35 dipendenti. Elemento da segnalare al commerciale. | https://xrayfinance.it/fonpelli-s-p-a — 'Fatturato: € 15.322.593,00 (2024); Utile: € -203.123,00 (2024); Dipendenti: 35 (2025)' | ≈15,3M€ (fatturato 2024, Registro Imprese) — esercizio in perdita |

### Germania (8)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Christian Göbel Holzgroßhandlung GmbH & Co.  | denominazione | Ragione sociale incompleta: la denominazione registrata e 'Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG' (HRA 15605 Amtsgericht Frankfurt/Main). | https://www.goebel-holz.de/impressum/ - 'Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG, Anton-Schlüter-Straße 2, 60437 Fr | Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG |
| E. Fuhlrott GmbH & Co. KG (HOLZFUHLROTT) | denominazione | Denominazione registrata completa: 'E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel' (HRA 400107). Esistono inoltre societa collegate del medesimo gruppo familiare (FUHLROTT Paletten Verpackungen & Logistik GmbH, HRB 510714; Fuhlrott Produktio | https://www.unternehmen24.info/Firmeninformationen/Deutschland/Firma/164652 - 'E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel, HRA 400107'; ht | E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel |
| Gebr. Kilger, Lederfabrik Viechtach KG | dimensione | L'inciso 'marchio Rendenbach' non trova riscontro: Rendenbach (J. Rendenbach jr.) e una conceria di Trier, non risulta alcun legame con Kilger nei risultati di ricerca. DA CONFERMARE. | Ricerca '"Lederfabrik Kilger Viechtach Rendenbach"': nessun risultato collega Kilger a Rendenbach; kilger.de/en/about-us/ descrive solo il marchio pro |  |
| H. Heitz Furnierkantenwerk GmbH & Co. KG | referente | Referente CONFERMATO ma di nomina recente: Jürgen Cirkel e subentrato come Geschäftsführer dopo il pensionamento del precedente GF Stefan Wernecke; nelle banche dati compare ancora anche Ralf Heitz come GF. Verificare che l'anagrafica sia aggiornata. | https://www.h-heitz.de/aktuelles/presse/ - 'Juergen Cirkel wurde zum neuen Geschaeftsfuehrer bestellt ... nach dem Ausscheiden des langjaehrigen Gesch |  |
| Hartmann Möbelwerke GmbH | referente | Compagine della Geschäftsführung incompleta: oltre a Katharina Hartmann e Holger Hanhardt ne fa parte anche Bernhard Hartmann, che ha ceduto la guida alla figlia ma resta in Geschäftsführung. | https://www.die-glocke.de/lokalnachrichten/katharina-hartmann-uebernimmt-beelener-moebelhersteller-1709910613 - 'Katharina Hartmann ist in die Geschae | Katharina Hartmann, Bernhard Hartmann, Holger Hanhardt |
| PFT Holz in Form GmbH | sede | La sede legale (Sitz) iscritta a registro e Schlüsselfeld, con iscrizione presso l'Amtsgericht Stendal (HRB 26378); Mertendorf OT Görschen (Südring 7) e la sede operativa/stabilimento. Il campo non distingue i due livelli. | https://www.northdata.com/PFT%20Holz%20in%20Form%20GmbH,%20Schl%C3%BCsselfeld/Amtsgericht%20Stendal%20HRB%2026378 - 'PFT Holz in Form GmbH, Schlüsself | Stabilimento: Mertendorf OT Görschen (Sachsen-Anhalt); sede legale: Schlüsselfeld (Bayern), HRB 26378 AG Stendal |
| Paletten Meyer | denominazione | 'Paletten Meyer' e solo il nome commerciale/dominio. La ditta e iscritta come 'Josef Meyer Palettenbau Inh. Julian Meyer' (impresa individuale, non societa di capitali): la forma giuridica va esplicitata perche incide sulla figura del contraente EUDR | https://www.europages.de/JOSEF-MEYER-PALETTENBAU-INH-JULIAN-MEYER/00000005396426-001.html e https://www.wlw.de/de/firma/josef-meyer-palettenbau-inh-ju | Josef Meyer Palettenbau Inh. Julian Meyer (Paletten Meyer) |
| RMW Wohnmöbel GmbH & Co. KG (Rietberger Möbe | referente | Geschäftsführung incompleta: oltre a Rudolf Eikenkötter risulta Geschäftsführer anche Volker Klocke (RMW Wohnmöbel Verwaltungs GmbH, HRB 6744 AG Gütersloh, socio accomandatario). | https://www.northdata.com/RMW%20Wohnm%C3%B6bel%20Verwaltungs%20GmbH,%20Rietberg/Amtsgericht%20G%C3%BCtersloh%20HRB%206744 e https://www.rmw-wohnmoebel | Rudolf Eikenkötter, Volker Klocke |

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

### Olanda (9)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Bangma Verpakking B.V. | sito | Il sito indicato nel foglio (https://www.bangma.nl) non è il dominio istituzionale usato oggi dall'azienda, che pubblica i propri contenuti su bangmaverpakking.nl (pagina 'Historie Bangma Verpakking'). DA CONFERMARE quale dei due sia il dominio attiv | https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - pagina istituzionale corrente dell'azienda | https://bangmaverpakking.nl/ (DA CONFERMARE) |
| Beijleveld Houtimport B.V. | sito | Il dominio ufficiale indicato nelle fonti di registro e' www.beyleveld.com (coerente con l'email info@beyleveld.com); beyleveldhoutimport.com risulta un secondo dominio attivo. Verificare quale sia il sito primario. | https://www.telefoonboek.nl/bedrijven/t2585787/rotterdam/beijleveld-houtimport-b.v./ - frammento: 'Email: info@beyleveld.com - Website: www.beyleveld. |  |
| Bruns B.V. | sede | Indirizzo discordante: il record indica Riethovensedijk 20, 5571 CR Bergeijk, mentre l'anagrafica di settore riporta Stokskesweg 11, 5571 TJ Bergeijk. Il comune (Bergeijk, Noord-Brabant) e' comunque corretto. Indirizzo civico DA CONFERMARE. | http://bergeijk.gevabiz.nl/company/bruns-bv-bergeijk.html - frammento: 'Stokskesweg 11, NL-5571TJ Bergeijk' |  |
| Gras Wood Wide B.V. | dimensione | Anno di fondazione errato: il record indica 1921, mentre azienda e stampa di settore datano la fondazione al 1868 (sesta generazione familiare, coerente). Il 1921 corrisponde semmai a una successiva iscrizione societaria. | https://www.houtwereld.nl/bedrijven/gras-wood-wide-b-v/ e https://www.graswoodwide.com/over-ons/ - frammento: 'founded in 1868' | Fondata nel 1868 |
| Gras Wood Wide B.V. | linkedin | Campo LinkedIn vuoto benche' esista la pagina aziendale ufficiale. | https://nl.linkedin.com/company/graswoodwide - titolo: 'Gras Wood Wide \| LinkedIn' | https://nl.linkedin.com/company/graswoodwide |
| Houtimport Lekkerkerker B.V. | dimensione | Il campo deduce la fascia 10-20 M EUR dal volume (ca. 200.000 m3/anno) senza alcuna fonte di fatturato: la stima non e' sostenuta e va marcata come tale. Il volume in se' e' l'unico dato dichiarato con tipo e fonte. | https://www.houtimportlekkerkerker.nl/ e https://www.creditsafe.com/business-index/en-us/company/houtimport-lekkerkerker-bv-nl01698016 (nessun fattura |  |
| Smeulders Interieurwerken B.V. | referente | Referente riportato con la sola iniziale ('A. Smeulders'). Il nome completo pubblicato e Anton Smeulders, alla guida dell'azienda dal 1992; la proprieta fa capo a Holding Smeulders B.V. | https://smeulders-ig.nl/over-ons/ - 'Anton Smeulders ... leidt het bedrijf sinds 1992'; proprieta Holding Smeulders B.V. | Anton Smeulders |
| Van de Stadt Houtimport B.V. | dimensione | Indirizzo di sede indicato nel campo ('sede portuale Noorder IJ- en Zeeweg') non coincide con quello registrato oggi: KVK/Drimble e il sito riportano Rijshoutweg 31, 1505 HL Zaandam. Dato di sede obsoleto. | https://drimble.nl/bedrijf/zaandam/15832708/van-de-stadt-houtimport-bv.html - 'Van de Stadt Houtimport B.V. Rijshoutweg'; https://www.telefoonboek.nl/ | Rijshoutweg 31, 1505 HL Zaandam |
| Van den Berg Hardhout B.V. | linkedin | URL LinkedIn probabilmente errato: la pagina aziendale reperibile e /company/van-den-berg-hardhout-bv---lopik, non /company/vandenberghardhout. | https://nl.linkedin.com/company/van-den-berg-hardhout-bv---lopik - 'Van den Berg Hardhout BV \| LinkedIn' | https://nl.linkedin.com/company/van-den-berg-hardhout-bv---lopik |

### Belgio (20)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Belignum NV | dimensione | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato il 02-07-2024 (esercizio 2023). La cifra di EUR 16. | https://trendstop.knack.be/nl/detail/405348449/belignum.aspx - 'omzet van 14.746.642 euro, 40e in de sector houthandel... laatst neergelegde jaarreken | Fatturato EUR 14.746.642, esercizio 2023 (bilancio depositato 02-07-2024), 10,8 FTE - eliminare il riferimento a 16.075. |
| Bruyerre Chocolates SA | linkedin | Campo LinkedIn vuoto: esiste una pagina aziendale belga attiva. Da verificare se copra la sola Bruyerre Chocolates SA o l'intero marchio Bruyerre (che include anche Bruyerre SA distribuzione, BE 0431.703.151). | https://be.linkedin.com/company/bruyerre | https://be.linkedin.com/company/bruyerre (DA CONFERMARE la corrispondenza con l'entita' 0688.794.525) |
| Buzzispace NV | dimensione | Il campo indica la produzione 'in Kempen' (implicitamente Belgio): le fonti aziendali collocano lo stabilimento produttivo a Bladel, nei Paesi Bassi. La sede sociale ad Anversa resta corretta, ma l'attivita' manifatturiera non e' belga; l'azienda ha  | https://officeinsight.com/officenewswire/buzzispace-appoints-new-ceo-announces-new-role-for-former-ceo-and-founder/ - frammento: "showrooms in Antwerp |  |
| Callens NV (Callens African Woods) | referente | Thierry Maelfait risulta confermato alla guida, ma dal 2021-2022 e' entrata in azienda la figlia Sam Maelfait, indicata dalle fonti come zaakvoerster/marketingverantwoordelijke: verificare chi sia oggi il rappresentante legale. Nota formale: per una  | https://www.voka.be/nieuws/west-vlaanderen-ondernemers-2024-19/callens-african-woods-heeft-productiefaciliteiten-kameroen - frammento: "Sam Maelfait,  |  |
| Chocolaterie Ickx NV | dimensione | Fatturato confermato nell'ordine di grandezza ma con cifra leggermente diversa dalla fonte: trendstop/pappers riportano 32.272.193 € (27° posto di settore) contro i 32.746.626 € del record. FTE 139,7 e deposito 26-03-2026 confermati. | Frammento: "With a turnover of 32,272,193 euros, Chocolaterie Ickx is ranked 27th in the chocolate and confectionery sector" — https://www.pappers.be/ |  |
| Confiserie Vandenbulcke NV | denominazione | La denominazione registrale in KBO/trendstop e' 'Vandenbulcke Confiserie NV' (ordine invertito rispetto al record); il marchio commerciale e' 'Chocolatier Vandenbulcke'. Il sito indicato e' corretto (vandenbulcke.com). | https://trendstop.knack.be/nl/detail/417738319/vandenbulcke-confiserie.aspx — "Vandenbulcke Confiserie NV - BE 0417.738.319 - Heule (8501)" | Vandenbulcke Confiserie NV |
| Corné Port-Royal Chocolatier SA | denominazione | La denominazione registrale completa e' 'CORNE PORT-ROYAL CHOCOLATIER, en abrege CPR CHOCOLATIER'; companyweb indicizza l'impresa come 'CPR CHOCOLATIER (SA)'. Refuso formale: nel record manca la sigla registrale. | https://www.companyweb.be/en/0433283558/corne-port-royal-chocolatier — titolo "CPR CHOCOLATIER (SA) - Wavre (1300) - BE0433283558"; https://trademarks | Corne Port-Royal Chocolatier SA (in abbreviato CPR Chocolatier SA) |
| Decadt Houthandel NV | ruolo | Stefaan Decadt e' confermato al vertice, ma il ruolo pubblicato e' 'bedrijfsleider' (LinkedIn) e non 'Algemeen directeur'; per una NV il titolo statutario sarebbe 'gedelegeerd bestuurder'. Inoltre coesistono due siti web riferiti a Decadt a Vlamertin | https://be.linkedin.com/in/stefaan-decadt-8b8144113 - frammento: "Stefaan Decadt - bedrijfsleider bij decadt houthandel nv"; siti concorrenti https:// | Ruolo: Bedrijfsleider / gedelegeerd bestuurder |
| Decadt Houthandel NV | dimensione | Data di fondazione discordante: il campo indica 01-01-1975 (data di costituzione della NV) mentre le fonti aziendali datano l'attivita' al 1927. Fatturato 13.460.408 EUR confermato. | https://trendstop.knack.be/nl/detail/415284714/decadt-houthandel.aspx - frammento: "With a turnover of 13,460,408 euros, Decadt Houthandel is ranked 4 |  |
| Denderwood NV | dimensione | Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta indeterminata e potenzialmente sotto la soglia dei 5 M EUR. Il campo lo dichiara ('TAGLIA DA VERIFICARE'), ma il dato non e' riscontrabile su NBB. Resto del record | https://www.atibt.org/en/members/24/denderwood e https://www.denderwood.com/over-ons/ - frammento: "Denderwood is located at J. Cardijnstraat, 3 B-942 |  |
| Hulpiau Hides BV | dimensione | Il campo usa come proxy dimensionale il margine lordo (2.284.726 EUR) di UN'ALTRA entita' giuridica (Hulpiau BV, BE 0429.082.864), non della societa' target BE 0777.875.662, che deposita a schema abbreviato e non pubblica il fatturato. Dato confermat | https://www.companyweb.be/en/0777875662/hulpiau-hides - frammento: "There are 6.1 FTEs working at Hulpiau Hides according to staff figures in the most |  |
| Klingele Chocolade NV | referente | Referente confermato (Koen Klingele, cofondatore 1995) ma incompleto: la societa' e' co-gestita dalla moglie Eline Blanchaert, indicata dalle fonti come zaakvoerder alla pari. Da notare che le fonti usano 'zaakvoerder', titolo proprio della BV, mentr | vrt.be/vrtnws/nl/2025/11/05: 'Koen Klingele en Eline Blanchaert, zaakvoerders van Klingele Chocolade'; jaarrekening.be/nl/KLINGELE-CHOCOLADE/0479.916. | Koen Klingele (con Eline Blanchaert) — gedelegeerd bestuurder |
| Lavrijsen Houtbedrijf NV | ruolo | Jan e Bert Lavrijsen sono confermati alla guida dell'azienda, ma per una NV il titolo statutario corretto e' 'gedelegeerd bestuurder / bestuurder', non 'zaakvoerder' (termine proprio delle BV). | https://lavrijsen.be/over-ons/ - frammento: "Jan and Bert Lavrijsen are at the helm of the company with secured succession" | Bestuurders / gedelegeerd bestuurders |
| Le Cercle du Cacao SRL | sede | Sede incoerente con la fonte aziendale: il sito ufficiale indica Rue des Sables 16, boite 4, 1000 Bruxelles (Bruxelles-Ville), non Schaerbeek 1030. DA CONFERMARE quale sia la sede sociale attuale iscritta alla BCE. | lecercleducacao.be/contact/: 'Le Cercle du Cacao est situé Rue des Sables 16, Boite 4 - 1000 Bruxelles' | Bruxelles-Ville (1000) — Regione di Bruxelles-Capitale |
| Meubelfabriek Lievens NV | ruolo | Lieven Decoene e' confermato come 'general manager' operativo, ma il mandato statutario della NV e' esercitato da Telinfra (VA Telifra) con rappresentante permanente Andre Ollevier. Il ruolo indicato non e' quello statutario belga (gedelegeerd bestuu | pappers.be/nl/company/meubelfabriek-lievens-0413666990: 'VA Telifra — Andre Ollevier, vaste vertegenwoordiger/zaakvoerder'; wonen360.nl: 'general mana | Lieven Decoene — General Manager (rappresentante legale: Telinfra, rappr. perm. Andre Ollevier) |
| Passe Partout NV | ruolo | Il titolo 'Zaakvoerder' e' proprio delle BV; per una NV il titolo statutario corretto e' gedelegeerd bestuurder / bestuurder. Dirk Steenbeke e' comunque confermato come fondatore e vertice attuale. | wonen360.nl 'Dirk Steenbeke van Passe Partout' (fondatore/CEO); verhouden.nl/ontwerpers/dirk-steenbeke | Gedelegeerd bestuurder |
| Radermecker SRL | dimensione | Discordanza sugli addetti: il record indica 9,1 FTE (bilancio BNB), mentre la scheda Europages dichiara 20-49 dipendenti. Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta non verificabile. | https://www.europages.fr/TANNERIE-RADERMECKER/BEL069426-000019048001.html - frammento: "The company employs between 20 and 49 people" |  |
| Royal Botania NV | ruolo | 'CEO e cofondatore' non e' un titolo statutario belga; per una NV il titolo corretto e' gedelegeerd bestuurder / bestuurder (le fonti usano 'zaakvoerder', incoerente con la forma NV). | https://www.apbc.be/stories/awd-2-kris-van-puyvelde-royal-botania | Gedelegeerd bestuurder |
| Silco NV | sito | Nessun sito web proprio reperito per Silco NV in 3 ricerche: l'azienda compare solo su banche dati societarie (trendstop, companyweb, fincheck, northdata, staatsbladmonitor). Coerente con la struttura a 1 FTE. Il campo vuoto e' quindi corretto, ma va | https://www.northdata.com/Silco%20N.V.,%20Antwerpen/KBO%200715.792.692 - solo scheda registro; nessun dominio aziendale nei risultati | n.d. (nessun sito web aziendale) |
| VC Wood Zottegem NV | linkedin | L'URL LinkedIn indicato (company/vc-wood-zottegem) non corrisponde alla pagina che emerge dalle ricerche, che e' company/vc-wood. DA CONFERMARE quale delle due sia attiva. | https://be.linkedin.com/company/vc-wood (risultato di ricerca per 'VC Wood Zottegem houthandel') | https://be.linkedin.com/company/vc-wood |

### Austria (4)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| HOLZBAU MAIER GmbH & Co KG | dimensione | Il fatturato di ca. 35,0 Mio EUR e' una stima non ufficiale di die-deutsche-wirtschaft.de e non riporta l'anno di riferimento, come richiesto per i dati dimensionali. Confermati invece FN 525501x/LG Salzburg e la co-GF Hildegund Maier. | https://www.maier.at/de/impressum.html - frammento: "Geschaeftsfuehrer: Hildegund Maier (representing since 07.04.2005) and Dipl.Ing Birgit Maier (07. |  |
| Holzindustrie Schafler GmbH & Co KG | ruolo | Il ruolo riportato ('Gewerberechtlicher Geschaeftsfuehrer') sottostima la posizione: l'Impressum aziendale indica Bernd (Christoph) Schafler come Geschaeftsfuehrer e proprietario, quarta generazione familiare. | https://www.schafler-holz.at/impressum - frammento: "Geschaeftsfuehrer: Bernd Schafler... current managing director and owner Bernd Christoph Schafler | Geschäftsführer / Inhaber |
| Karnische Massiv Möbel GmbH | denominazione | Ragione sociale a Firmenbuch: 'Karnische-Massiv-Moebel Gesellschaft m.b.H.' (con trattini), FN 094638z, LG Klagenfurt; 'Karnische Massiv Moebel GmbH' e' il nome commerciale. Refuso formale. Confermati invece GF Werner Hohenwarter (fratello Otto Proku | https://www.firmenabc.at/karnische-massiv-moebel-gesellschaft-m-b-h_Xyc e https://www.northdata.de/Karnische-Massiv-M%C3%B6bel%20GmbH,%20Kirchbach/094 | Karnische-Massiv-Möbel Gesellschaft m.b.H. |
| MAFI Naturholzboden GmbH | dimensione | Il fatturato di 22,3 Mio EUR e' datato al 2017 nel record, ma la fonte (die-deutsche-wirtschaft.de) lo presenta come dato piu' recente disponibile con crescita del 2,8% rispetto a una stima precedente di 20,0 Mio EUR. Anno di riferimento da riconferm | https://die-deutsche-wirtschaft.de/famu_top/oesterreich-mafi-naturholzboden-gmbh-schneegattern-umsatz-mitarbeiterzahl/ - frammento: "The most recent a |  |

### (tutti) (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| (controllo di rientro) | denominazione | nessuna delle 7 aziende rimosse e' rientrata nei fogli. Controllo eseguito su _records.json (742 record, tutti i fogli) cercando in ogni campo, con radici tolleranti alle varianti: 'getama', 'dragsb', 'pacorini', 'immobra', 'lavazza', 'segafredo', 'k | Verifica programmatica su _myeudr_build/verifica/_records.json: per ciascuna delle 7 radici, 0 corrispondenze nel campo 'denominazione' su tutti i 742 |  |
