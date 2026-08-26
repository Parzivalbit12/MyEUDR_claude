# REPORT DI VERIFICA — MyEUDR Lead Mapping

> Controllo qualità **record per record** del censimento lead (**738 aziende, 8 fogli**), alla ricerca di refusi, attribuzioni errate e ogni altro errore introdotto durante la raccolta. Non è una ricerca di nuove aziende.


## Come leggere questo report

La verifica si è svolta in due fasi, con budget e coperture diverse:

| Fase | Metodo | Copertura |
|---|---|---|
| **A — controlli deterministici** | 26 controlli automatici offline su tutti i JSON di build e sul workbook | **100%** dei 738 record |
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


## 0-bis. Correzioni già applicate al workbook (59)

Applicate **solo le correzioni certe**, secondo il mandato: refusi formali, entità HTML, forme giuridiche, filiere fuori Allegato I, aziende cessate. Tutto il resto resta come rilievo aperto in questo report.

Ogni correzione di campo è stata applicata con un **controllo di guardia**: lo script verifica che il valore attuale del campo coincida esattamente con quello atteso, altrimenti salta la correzione, così lo script è rieseguibile senza rischi. Dopo l'applicazione le righe sono **740** (due rimozioni motivate, vedi sotto) e l'ordine dei fogli è ripristinato (Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria).


### Record rimossi dal censimento (4)

Sono le uniche righe **tolte** dai fogli. Ciascuna rientra in una categoria che il mandato autorizza a correggere — filiere fuori Allegato I, aziende cessate — e in ogni caso il progetto aveva già applicato lo stesso criterio a un caso analogo, che viene citato nella motivazione.

**Helvoet Rubber & Plastic Technologies NV** — foglio Belgio  
FUORI PERIMETRO EUDR: la gamma elastomeri dichiarata dall'azienda stessa (helvoet.com/rubber) comprende solo polimeri sintetici — IIR, CR, EPDM, NBR, AEM/ACM, AU, VMQ/FMVQ, FKM, HNBR, FFKM — piu' termoplastici e silicone LSR. La gomma naturale non compare. Nessuna commodity dell'Allegato I: stesso criterio gia' applicato a RICO Elastomere (silicone) in Austria e a Immobra (olio di lino) in Belgio. E' inoltre filiale del gruppo olandese Helvoet (Hydratec 2015, poi RF Plast 09/2024), non una PMI belga indipendente.

**Marine Olie Handel Maatschappij B.V.** — foglio Olanda  
FUORI PERIMETRO EUDR: la filiera dichiarata è «Olio di palma», ma le fonti descrivono un trader di sottoprodotti alimentari e olio da frittura usato (UCO) destinati ai biocarburanti — è la motivazione stessa dell'acquisizione da parte di STX Group, che opera nei biofuels. UCO e biodiesel sono fuori dall'Allegato I: stesso criterio già applicato a Münzer/ABID (biodiesel da colza e oli esausti) in Austria. Due motivi concordanti: il bilancio 2022 riporta quasi 400 M€ — dieci volte il tetto della forbice 5-40 M€, e il campo Dimensione affermava invece che il fatturato «non è pubblicato» (stesso caso di Dragsbæk, rimossa a ~255 M€) — ed è stata acquisita da STX Group con closing 01/12/2024, quindi non più indipendente.

**Weissengruber Möbelmanufaktur GmbH** — foglio Austria  
AZIENDA IN INSOLVENZA: Sanierungsverfahren ohne Eigenverwaltung aperto al Landesgericht Linz il 13 gennaio, curatore René Lindner, prosecuzione con Massekredit e voto dei creditori il 29 aprile (fonti: registro insolvenze KSV, EUWID Holz, Nachrichten.at). Il progetto applica gia' questo criterio: escluse HAKA Küche, KAPO Möbel, ADA e Schletterer per insolvenza in corso, mentre Franz Hauswirth e' stata mantenuta proprio perche' risanata. Qui la procedura e' aperta. Si aggiunge che l'entita' operativa risulta «WEISSENGRUBER Möbelproduktion e.U.», non la GmbH censita.

**ODENSE SEGLMÆRKEFABRIK A/S** — foglio Danimarca  
SOCIETÀ ESTINTA: il CVR 17620487 risulta «opløst efter fusion» (sciolta a seguito di fusione); l'attività è oggi un sito di Optimum Group Nordic (OG Nordic ApS, gruppo olandese) e nel 2025 è stata trasferita da Odense ad Ans By per condividere lo stabilimento con la consociata Etiflex. La persona giuridica censita non esiste più e il lead non è più un'impresa danese autonoma: stesso criterio già applicato a Getama Danmark (non più produttore autonomo), Magnus Olesen (fallita) e Bent Krogh (cessata). Fonti: ownr.dk e profiler.dk su CVR 17620487; signprintpack.dk 14.07.2025.

Il totale del censimento passa quindi da **742 a 738 aziende** (Belgio 95→94, Olanda 100→99, Austria 93→92).


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

### Refusi formali (32)

| Foglio | Azienda | Campo | Correzione | Motivo |
|---|---|---|---|---|
| Danimarca | NPI (Nordic Panel Import) | denominazione | «NPI (Nordic Panel Import)» → «NPI A/S (Nordic Panel Import)» | forma giuridica mancante: al CVR 37418730 la societa' è registrata come NPI A/S (proff.dk) |
| Olanda | Rompa Tanneries B.V. | denominazione | «Rompa Tanneries B.V.» → «Vitelco Leather B.V. (già Rompa Tanneries B.V.)» | denominazione obsoleta: sciolta la joint venture, Vitelco è socio unico al 100% e la societa' è stata ridenomi |
| Austria | Karnische Massiv Möbel GmbH | denominazione | «Karnische Massiv Möbel GmbH» → «Karnische-Massiv-Möbel Gesellschaft m.b.H.» | ragione sociale a Firmenbuch FN 094638z (LG Klagenfurt); «Karnische Massiv Möbel GmbH» è il nome commerciale |
| Belgio | Confiserie Vandenbulcke NV | denominazione | «Confiserie Vandenbulcke NV» → «Vandenbulcke Confiserie NV» | ordine dei termini invertito rispetto alla denominazione registrale KBO |
| Germania | Paletten Meyer | denominazione | «Paletten Meyer» → «Josef Meyer Palettenbau Inh. Julian Meyer (Paletten Meyer)» | «Paletten Meyer» è il solo nome commerciale: la ditta è iscritta come impresa individuale Josef Meyer Paletten |
| Austria | Storebest Ladeneinrichtungen Gmb | denominazione | «Storebest Ladeneinrichtungen GmbH» → «"Storebest" Ladeneinrichtungen Gesellschaft m.b.H.» | ragione sociale a Firmenbuch FN 117692b (firmenabc.at, WKO); «Storebest Ladeneinrichtungen GmbH» è il nome com |
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
| Germania | 97 | 2 | 0 | 4 | 34 | 35% |
| Finlandia | 84 | 1 | 0 | 4 | 17 | 20% |
| Danimarca | 88 | 3 | 0 | 2 | 54 | 61% |
| Svezia | 89 | 1 | 1 | 3 | 33 | 37% |
| Olanda | 99 | 2 | 0 | 4 | 34 | 34% |
| Belgio | 94 | 3 | 0 | 2 | 57 | 61% |
| Austria | 92 | 2 | 0 | 3 | 38 | 41% |
| **TOTALE** | **738** | **15** | **1** | **26** | **286** | **39%** |

_Un blocco è contato **completo** solo se l'agente ha confermato di aver verificato tutti i record. I **blocchi parziali** sono quelli ancora in corso o interrotti dal limite di sessione: i rilievi già salvati sono validi e inclusi nel report, ma la copertura è conteggiata al ribasso (solo le aziende che compaiono fra i rilievi). Il salvataggio incrementale ogni 3-4 record è ciò che ha evitato di perdere quel lavoro._

> La Fase A copre invece il **100%** dei 738 record: è un controllo offline e non dipende dal budget di ricerca.


_A questi si aggiunge la verifica mirata dei **13 punti già noti** lasciati aperti dalla raccolta, condotta separatamente e riportata per intero più sotto._


## 2. Rilievi per foglio

**Totale rilievi Fase B: 460** — alta 66 · media 259 · bassa 135.

| Foglio | Rilievi | alta | media | bassa | Aziende toccate |
|---|--:|--:|--:|--:|--:|
| Italia | 25 | 0 | 11 | 14 | 17 |
| Germania | 56 | 3 | 38 | 15 | 34 |
| Finlandia | 23 | 6 | 11 | 6 | 15 |
| Danimarca | 74 | 19 | 36 | 19 | 49 |
| Svezia | 58 | 10 | 28 | 20 | 32 |
| Olanda | 74 | 9 | 50 | 15 | 33 |
| Belgio | 115 | 15 | 68 | 32 | 57 |
| Austria | 34 | 4 | 17 | 13 | 25 |
| _(tutti)_ | 1 | 0 | 0 | 1 | 1 |
| **TOTALE** | **460** | **66** | **259** | **135** | **263** |

### Rilievi per campo

| Campo | Rilievi | di cui alta |
|---|--:|--:|
| dimensione | 222 | 36 |
| referente | 102 | 14 |
| denominazione | 35 | 9 |
| email | 28 | 2 |
| linkedin | 19 | 0 |
| sede | 13 | 1 |
| filiera | 13 | 4 |
| ruolo | 12 | 0 |
| sito | 11 | 0 |
| fonte | 4 | 0 |
| esistenza_stato | 1 | 0 |

---

## 3. Tema trasversale — legami di gruppo (75 rilievi)

È il problema **più diffuso e meno atteso** emerso dalla verifica: non era fra i 13 punti noti dell'handoff. Numerose aziende del censimento sono controllate di gruppi, spesso esteri o quotati. Per il criterio già applicato dal progetto — che aveva rimosso Lavazza Kaffee, Segafredo Zanetti Austria e Kaffee Partner Austria perché *«la compliance si decide a livello di gruppo, non nella filiale»* — sono **lead di valore dubbio**.

La tabella distingue i due casi, che non hanno la stessa gravità:

- **DICHIARATO** — il campo `Dimensione` del foglio già segnala il legame. Non è un errore di dato: la raccolta ha fatto quel che le regole chiedevano (*«segnalare sempre i legami di gruppo»*). È una **decisione di selezione** che spetta al cliente.

- **NON DICHIARATO / ERRATO** — il legame manca del tutto, oppure la capogruppo indicata è sbagliata. Questo **è** un errore di dato.

| Foglio | Azienda | Stato nel foglio | Rilievo |
|---|---|---|---|
| Austria | BRAUN LOCKENHAUS GmbH | **dichiarato** | Filiale di gruppo estero: la societa' e' controllata da SCHNEEWEISS AG / SCHNEEWEISS interior, con sede del gruppo a Kippenheim (Baden-Württemberg, DE), dal 2006. La decisione di compliance EUDR si as |
| Austria | Schösswender Möbel Gesellschaft m.b.H. | **dichiarato** | Il solo dato di fatturato citato e' quello di gruppo del 2012 (28 M€): 13 anni di anzianita', inutilizzabile per il dimensionamento. La stima 15-25 M€ per la sola societa' mobili resta non confermata. |
| Austria | Storebest Ladeneinrichtungen GmbH | **NON dichiarato** | FILIALE DI GRUPPO ESTERO NON DICHIARATA. STOREBEST Österreich e' parte della Kesseböhmer Holding KG di Bad Essen (Germania), gruppo con ca. 3.500 dipendenti su dodici siti; esiste anche la consorella  |
| Belgio | A & A Chocolaterie NV | **dichiarato** | Il legame di gruppo e' correttamente dichiarato, ma va valutato l'effetto sul perimetro commerciale: A & A Chocolaterie (22,1 M€) e Pralinart (18,4 M€) sono entrambe controllate al 100% da Hamlet NV,  |
| Belgio | Accent NV | **dichiarato** | La descrizione del legame di gruppo e' rovesciata e fuorviante. Accent non e' la 'capofila' del gruppo Asteria: dal 2018 la famiglia Declerck ha ceduto la MAGGIORANZA al fondo Waterland (prima 18 M€,  |
| Belgio | Allbox NV | **NON dichiarato** | Assetto proprietario NON dichiarato. Il record presenta Allbox come 'azienda familiare', ma il controllo integrale della NV e' stato acquisito da KBC Investco (capitale di rischio) insieme al manageme |
| Belgio | Autajon Packaging Belgium SA | **dichiarato** | Controllata di gruppo estero: la societa' e' una filiale del gruppo familiare francese Autajon (guidato da Gerard Autajon), che in Belgio ha due siti (Anderlecht e Arlon). Il legame e' dichiarato nel  |
| Belgio | Corné Port-Royal Chocolatier SA | **NON dichiarato** | LEGAME DI GRUPPO NON DICHIARATO. Corne Port-Royal Chocolatier SA (BE 0433.283.558, denominazione abbreviata registrale 'CPR CHOCOLATIER') e' controllata dal gruppo Neuhaus dal 2013: Neuhaus figura dir |
| Belgio | Delafaille NV | **dichiarato** | Il legame di gruppo e' dichiarato ma la conclusione tratta nel campo ('resta pero' PMI belga autonoma con obblighi EUDR propri') e' opinabile: Maestrani Schweizer Schokoladen ha acquisito il 100% dell |
| Belgio | Dolfin SA | **NON dichiarato** | Dato aziendale incompleto e ormai superato dagli eventi: nell'aprile 2026 Dolfin e' diventata azionista di maggioranza della Chocolaterie Galler (rilevata da un consorzio vallone insieme a Wallonie En |
| Belgio | Gudrun Commercial NV | **dichiarato** | Legame di gruppo dichiarato ma incompleto e con conseguenze non tratte: Natra ha acquisito il 100% di Gudrun (annuncio ottobre 2024) dal fondo Down2Earth Capital, e Natra e' a sua volta partecipata da |
| Belgio | Hannecard Benelux NV | **NON dichiarato** | LEGAME DI GRUPPO NON DICHIARATO. Hannecard Benelux NV (BE 0694.906.812) non e' una societa' indipendente: e' l'entita' Benelux del Gruppo Hannecard, che fa capo a Hannecard NV (BE 0892.311.512, stessa |
| Belgio | Hannecard Benelux NV | **NON dichiarato** | Il LinkedIn indicato (linkedin.com/company/hannecard-nv) e' la pagina del gruppo Hannecard, non della sola Hannecard Benelux NV: coerente con il rilievo sul legame di gruppo. Non e' un errore grave ma |
| Belgio | Helvoet Rubber & Plastic Technologies NV | **NON dichiarato** | LEGAME DI GRUPPO NON DICHIARATO. La societa' di Lommel e' la filiale belga del gruppo olandese Helvoet (Helvoet Holding B.V., fondata 1939 a Hellevoetsluis, siti in NL, DE, BE, IN, PL), acquisito da H |
| Belgio | Koffiebranderij Or BV (OR Coffee Roaster | **dichiarato** | Controllata di gruppo: dall'aprile 2024 la societa' e' stata acquisita da Anaerobic Holding (Anversa), gia' proprietaria di Mister Barish Beans & Machines. Il legame e' dichiarato nel campo, ma va ten |
| Belgio | Manufacture Belge de Chocolats SRL | **NON dichiarato** | LEGAME DI GRUPPO NON DICHIARATO. MBC non e' una PMI belga indipendente: e' lo stabilimento di produzione bruxellese di Godiva ceduto nel giugno 2019 al fondo MBK Partners insieme alle attivita' Godiva |
| Belgio | Manutti BV | **dichiarato** | Legame di gruppo con Manutti Invest BV (BE 0478.148.434) dichiarato nel record: si tratta della holding familiare che controlla l'operativa. Segnalato come 'media' perche' gia' dichiarato; la decision |
| Belgio | Mecam NV | **NON dichiarato** | Il record riporta 32.145.268 € e 111,6 FTE per la sola Mecam NV, mentre la stampa parla di 37 M€ cumulati e ~220 dipendenti per l'intero Mecam Group (Mecam + Neo-Style). Il legame di gruppo esiste ed  |
| Belgio | Sas NV (Sas Coffee) | **dichiarato** | CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elen |
| Belgio | Silco NV | **NON dichiarato** | RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui president |
| Belgio | Tannerie Masure SA | **NON dichiarato** | Societa' non indipendente: dal 2014 Tannerie Masure fa parte del Groupe Saturne insieme alla francese Tannerie Fortier-Beaulieu (Roanne). Il referente indicato, Olivier Lesage, risulta anche dirigente |
| Belgio | Vanerum Belgie NV | **dichiarato** | Il legame di gruppo e' dichiarato ma incompleto: i3-Group non e' piu' interamente familiare. WorxInvest ha acquistato circa il 25% per 10 M€ e nel novembre 2023 anche il gruppo americano Steelcase ha  |
| Belgio | Vincent Sheppard NV | **NON dichiarato** | Assetto proprietario non dichiarato: dal 2002 la societa' e' controllata dalla famiglia Claeys tramite Cennini Holding e oggi il capitale e' 50/50 tra la famiglia Claeys e Jos Destrooper. Il fatturato |
| Danimarca | BØJSØ DØRE & VINDUER A/S | **dichiarato** | Lead non indipendente: dal 2017 la società è controllata da INWIDO DENMARK A/S, parte del gruppo quotato svedese Inwido AB (fatturato di gruppo ~9 mld SEK nel 2025). Secondo il mandato una controllata |
| Danimarca | Copenhagen Coffee Lab ApS | **NON dichiarato** | Assetto proprietario non dichiarato: la societa' fa parte di un gruppo di 6 societa' con capogruppo Copenhagen Coffee Lab Holding ApS; il 70% e' stato rilevato dagli investitori danesi Steen Skallebae |
| Danimarca | DANSK KAFFE ApS | **NON dichiarato** | Assetto proprietario non dichiarato: DANSK KAFFE ApS fa parte di un gruppo di 2 societa' con capogruppo KAFFEA ApS. Manca inoltre la data di costituzione (27.11.2013), utile a qualificare la micro-imp |
| Danimarca | HVIDBJERG VINDUET A/S | **dichiarato** | Assetto proprietario errato e lead non indipendente: il campo indica come controllante "Hvidbjerg i A/S", ma la società è controllata dal gruppo ACO Nordic, a sua volta parte del gruppo tedesco ACO (f |
| Danimarca | JKE DESIGN A/S | **dichiarato** | Lead non indipendente: la società appartiene al gruppo BALLINGSLÖV INTERNATIONAL DANMARK A/S / Ballingslöv International AB (gruppo svedese, Stena Adactum), con presidente del CdA e consigliere espres |
| Danimarca | KLS PUREPRINT A/S | **dichiarato** | Il legame di gruppo e' dichiarato correttamente ma va aggiornato e pesato come criterio di esclusione del lead: F. E. Bording A/S ha rilevato la quota di Knud Erik Larsen a fine 2024/inizio 2025, per  |
| Danimarca | KRYDSFINER-HANDELEN A/S | **dichiarato** | Controllata di gruppo estero: dall'autunno 2023 la societa' e' stata venduta da Carsten Rittig a Fritzoe Nordic Holding AS (Norvegia), che ne detiene il controllo. Il record lo accenna in forma dubita |
| Danimarca | KVIST INDUSTRIES A/S | **NON dichiarato** | Assetto proprietario non dichiarato: la societa' figura nel portafoglio del fondo di private equity danese Dansk Ejerkapital ed e' controllata tramite KVIST HOLDING A/S (CVR 21746886, Esbjerg). Il cam |
| Danimarca | LILLEHEDEN A/S | **dichiarato** | Controllata di gruppo: la societa' fa parte di Nordic Wood Industries A/S (CVR 37385603), che dal 12.05.2025 ha un nuovo adm. direktor di gruppo (Holger Carsten Hansen). Il legame e' gia' correttament |
| Danimarca | MULTIFORM A/S | **dichiarato** | Controllata di gruppo: capogruppo BALLINGSLOV INTERNATIONAL DANMARK A/S (gruppo svedese Ballingslov International / Stena Adactum). Il legame e' gia' dichiarato correttamente nel record, quindi il ril |
| Danimarca | Naturli' Foods | **dichiarato** | RILIEVO EMERSO DAL CONTROLLO DI RIENTRO. Il record dichiara esso stesso che Naturli' Foods e' 'parte del gruppo Dragsbaek/Orkla': e' quindi una controllata del gruppo norvegese quotato Orkla ASA, per  |
| Danimarca | SKJERN PAPER A/S (già Skjern Papirfabrik | **NON dichiarato** | ASSETTO PROPRIETARIO FALSO. Il campo dichiara 'Proprieta' Buur Invest A/S + dirigenti operativi (indipendente danese dal 2005)'. In realta' Skjern Paper A/S e' stata acquisita dal gruppo statunitense  |
| Danimarca | SKJERN PAPER A/S (già Skjern Papirfabrik | **NON dichiarato** | Il nome e la data sono corretti (Nikolaj Bjerre Thybo, adm. direktoer dal 2020) ma, essendo la societa' controllata da Sonoco dal 2022, il referente non e' il decisore finale sulla compliance EUDR. Se |
| Danimarca | Skagerak Denmark A/S | **NON dichiarato** | Referente errato e legame di gruppo non dichiarato: Skagerak Denmark A/S e' stata acquisita da Fritz Hansen A/S nel dicembre 2021 ed e' oggi il marchio 'Skagerak by Fritz Hansen'. Josef Theodor Kaiser |
| Danimarca | TIMBERMAN DENMARK A/S | **dichiarato** | Assetto proprietario errato/obsoleto: il record indica solo 'controllata da Timberman Holding ApS ... azionariato nordico'. In realta' nel dicembre 2024 la societa' e' stata acquistata dal gruppo indu |
| Danimarca | TJOERNEHOEJ MOELLE A/S | **NON dichiarato** | LEAD NON VALIDO. A/S Tjoernehoej Moelle (CVR 34175012) NON e' un'impresa indipendente: e' stata acquistata da DLG nel 1989 dal mugnaio Sander Petersen ed e' oggi una controllata della cooperativa DLG  |
| Finlandia | CWP Coloured Wood Products Oy | **NON dichiarato** | Azienda ACQUISITA: l'intero capitale è stato rilevato da Auroora Yhtiöt Oyj (serial acquirer finlandese, 131 M€ di fatturato, oltre 20 PMI). Il legame di gruppo non è dichiarato nel record; la decisio |
| Finlandia | I.S. Mäkinen Oy (MAKINEN) | **NON dichiarato** | Appartenenza a gruppo non dichiarata: I.S. Makinen Oy fa parte del gruppo MAKINEN (il nuovo CEO Mikko Makinen e' indicato come parte della proprieta' del gruppo). La decisione di compliance EUDR si pr |
| Germania | Die Pharmadrucker GmbH | **NON dichiarato** | Appartenenza a gruppo dichiarata ma da qualificare: la società è controllata dalla Bernecker-Gruppe (Druckerei Bernecker GmbH, stessa sede) dal 2016; la decisione di compliance EUDR si prende a livell |
| Germania | H. Heitz Furnierkantenwerk GmbH & Co. KG | **NON dichiarato** | CONTROLLO DI GRUPPO NON DICHIARATO: dal 2016 Heitz e societa del gruppo INDUS Holding AG (holding industriale quotata, Bergisch Gladbach). Il record non riporta alcun legame di gruppo: la decisione di |
| Germania | Weinheimer Leder GmbH | **NON dichiarato** | Struttura di gruppo non dichiarata: Weinheimer Leder GmbH e collegata a Das Lederband GmbH (Weinheim, HRB 724382), con Uwe Holubeck Geschäftsführer di entrambe; le fonti aperte non chiariscono il vers |
| Olanda | BeBo Parket B.V. | **dichiarato** | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dich |
| Olanda | GWW Houtimport B.V. | **dichiarato** | Controllata di gruppo: dal 01/01/2026 GWW Houtimport, GWW Agency e Van den Berg Hardhout confluiscono nella holding Van den Berg Houtgroep. Il legame e' gia' dichiarato correttamente nel campo, ma la  |
| Olanda | Houthandel Jos Dennebos B.V. | **NON dichiarato** | Referente e ruolo assenti. Il socio unico e' la persona giuridica Jos Dennebos Exploitatie B.V.; il fondatore storico e' Jos Dennebos (attivo anche in Dennebos Suriname). Nome e carica del directeur a |
| Olanda | Houtplex B.V. | **dichiarato** | Controllata di gruppo estero: Houtplex appartiene al gruppo Wood United, con sede a Singapore; dal febbraio 2019 le quote sia di Houtplex sia di Wood United sono di Timothy Paul, che ha rilevato la pa |
| Olanda | Kargro Banden B.V. | **dichiarato** | Legame di gruppo confermato e piu ampio di quanto dichiarato: oltre a Kargro International e Lintire, il gruppo comprende Banden Plan Europa BV (Montfoort) e Tyre Plan Europe (Kalmthout, BE) sotto Kar |
| Olanda | Marine Olie Handel Maatschappij B.V. | **dichiarato** | AZIENDA ACQUISITA: Marine Olie e stata acquisita da STX Group (Amsterdam); l'operazione, approvata dalla Commissione europea, si e chiusa il 01/12/2024. La societa non e piu indipendente e la decision |
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
| Svezia | Horreds Möbel Aktiebolag | **dichiarato** | Legame di gruppo indicato solo genericamente («Fa parte di un gruppo di 3 società») senza nominare la capogruppo. Allabolag indica Horreds Holding AB come società madre e Horreds Möbel Utvecklings AB  |
| Svezia | Kvänum Kök AB | **dichiarato** | Controllata di gruppo: capogruppo Vedena AB, gruppo di 5 società con 350 dipendenti e 1 135,0 MSEK di fatturato. Il legame è già dichiarato correttamente nel foglio, ma la decisione di compliance EUDR |
| Svezia | Lammhults Möbel Aktiebolag | **dichiarato** | Controllata del gruppo quotato Lammhults Design Group AB: legame già dichiarato correttamente nel foglio, ma il lead è una controllata di gruppo quotato e la compliance EUDR si decide a livello di cap |
| Svezia | N K Lundströms Trävaror Aktiebolag | **dichiarato** | Controllata di gruppo: capogruppo KGL Trä Aktiebolag, gruppo di 2 società con 34 dipendenti e 203,0 MSEK di fatturato. Il legame è già dichiarato correttamente nel foglio; resta una questione di selez |
| Svezia | Nordanå Trä Aktiebolag | **dichiarato** | Legame di gruppo dichiarato (controllata di Green Wood Sverige AB) e confermato da allabolag, ma Ratsit riporta l'azienda come NON appartenente ad alcun koncern: informazione discordante fra le fonti, |
| Svezia | Rödins Trä AB | **dichiarato** | Il valore riportato (380 291 KSEK ≈ 33,7 M€, 2025) è il fatturato CONSOLIDATO di gruppo: Rödins Trä AB è koncernmoderbolag con la controllata Ålsta Sågverk Nord AB, e il gruppo di 2 società fattura 37 |
| Svezia | Rörvikshus Sweden AB | **dichiarato** | Controllata di gruppo: capogruppo Munio Sweden Aktiebolag (org.nr 556509-3449), gruppo di 4 società con 52 dipendenti e 229,0 MSEK di fatturato. Legame già dichiarato correttamente nel foglio: resta u |
| Svezia | Sjöbergs Workbenches AB | **dichiarato** | Il legame di gruppo è dichiarato (capogruppo Idun Woodcraft AB, acquisizione 2018) ma ne è sottostimata la portata: allabolag indica che l'azienda appartiene a un gruppo di 74 società facente capo a I |
| Svezia | Tärnsjö Garveri Aktiebolag | **NON dichiarato** | Legame di gruppo NON dichiarato: il record definisce l'azienda 'la principale conceria indipendente attiva', ma allabolag indica come moderbolag Axel Bodéns Handels Aktiebolag. L'affermazione di indip |

---

## 4. Casi di gravità ALTA (66)

_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, oppure fuori dal perimetro dell'Allegato I EUDR._


### Germania (3)

#### Die Pharmadrucker GmbH — campo `referente`

Referente errato: «Ingo Hofmeier» non risulta Geschäftsführer della società. L'Impressum attuale indica Felix Fischer e Alexander Storck (una pagina più vecchia riportava Conrad Fischer).

**Evidenza:** https://www.diepharmadrucker.de/impressum/ — «Geschäftsführer: Felix Fischer, Alexander Storck», Unter dem Schöneberg 1, 34212 Melsungen, AG Fritzlar HRB 12160

**Correzione proposta:** Felix Fischer, Alexander Storck

#### H. Heitz Furnierkantenwerk GmbH & Co. KG — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: dal 2016 Heitz e societa del gruppo INDUS Holding AG (holding industriale quotata, Bergisch Gladbach). Il record non riporta alcun legame di gruppo: la decisione di compliance EUDR si colloca a livello di capogruppo, quindi il lead ha valore dubbio. Manca inoltre qualsiasi dato dimensionale ('Umsatz/MA n.d.').

**Evidenza:** https://www.h-heitz.de/aktuelles/presse/ - 'Seit 2016 gehoert Heitz zur INDUS, einem weltweit agierenden Unternehmen, das Beteiligungen an mittelstaendischen Hidden Champions haelt'

**Correzione proposta:** Controllata di INDUS Holding AG (gruppo quotato) dal 2016; dato dimensionale da integrare con fonte e anno

#### Hausberger GmbH & Co. KG — campo `dimensione`

Campo senza alcun dato («Umsatz/MA n.d.»), ma le fonti disponibili indicano una micro-impresa da 1-4 dipendenti: sarebbe di un ordine di grandezza fuori dalla forbice 5-40 Mio €. Va inoltre verificato il perimetro: la società opera anche come Vertriebs-KG di Wellkisten e materiale d'imballaggio (rivendita), e un puro rivenditore di cartone già immesso sul mercato UE non è l'operatore che immette per primo la commodity. Se confermato, il lead va escluso.

**Evidenza:** https://www.wlw.de/de/firma/hausberger-gmbh-co-kg-382731 — «1-4 Mitarbeiter»; ragione sociale collegata: «Hausberger GmbH & Co. Vertriebs-KG, Wellkisten und Verpackungsmaterial, Oberasbach» (https://firmeneintrag.creditreform.de/90522/8190035516/HAUSBERGER_GMBH_CO_VERTRIEBS_KG_WELLKISTEN_UND_VERPACKUNGSMATERIAL)

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto


### Finlandia (6)

#### Akonkosken Saha Oy — campo `email`

L'indirizzo akonkoskensaha@akonkoskensaha.fi non compare in nessuna fonte pubblica: le fonti (Finder/Fonecta/yrityshakemisto) riportano un dominio di posta diverso (netikka.fi), dominio storico dell'azienda distinto dal sito web.

**Evidenza:** https://www.finder.fi/Puutavara/Akonkosken+saha+Oy/T%C3%B6ys%C3%A4/yhteystiedot/124414 — frammento: "Email (Sähköposti): akonkoskensaha@netikka.fi; Puhelin: 020 773 8585; Ähtärintie 23, 63600 Töysä"

**Correzione proposta:** akonkoskensaha@netikka.fi (da riconfermare sulla pagina https://www.akonkoskensaha.fi/kontakti.html)

#### CWP Coloured Wood Products Oy — campo `dimensione`

Azienda ACQUISITA: l'intero capitale è stato rilevato da Auroora Yhtiöt Oyj (serial acquirer finlandese, 131 M€ di fatturato, oltre 20 PMI). Il legame di gruppo non è dichiarato nel record; la decisione di compliance EUDR passa alla capogruppo.

**Evidenza:** https://auroora.com/en/auroora-yhtiot-acquires-cwp-coloured-wood-products-a-manufacturer-of-coloured-veneer-materials/ — frammento: "Auroora Yhtiöt Oyj has acquired the entire share capital of CWP Coloured Wood Products Oy"

**Correzione proposta:** Controllata di Auroora Yhtiöt Oyj (Tampere) — riqualificare il lead sulla capogruppo o scartare

#### Elega Oy — campo `referente`

Referente errato: Kaj Pellinen non e' il toimitusjohtaja ma il talouspaallikko (direttore amministrativo/finanziario). Il toimitusjohtaja in carica e' Pauli Niinikoski, confermato anche dopo il riassetto azionario.

**Evidenza:** https://elega.fi/ajankohtaista/elegan-osakkaiksi-elegalaisia-avainhenkiloita/ e https://www.asiakastieto.fi/yritykset/fi/elega-oy/24968649/paattajat — frammento: "Pauli Niinikoski continues in his role as CEO and as a shareholder alongside other members of the entrepreneur team... Kaj Pellinen serves as the finance director (talouspaallikko)"

**Correzione proposta:** Pauli Niinikoski — Toimitusjohtaja (CEO)

#### I.S. Mäkinen Oy (MAKINEN) — campo `dimensione`

Appartenenza a gruppo non dichiarata: I.S. Makinen Oy fa parte del gruppo MAKINEN (il nuovo CEO Mikko Makinen e' indicato come parte della proprieta' del gruppo). La decisione di compliance EUDR si prende a livello di capogruppo.

**Evidenza:** https://navigatormagazine.fi/uutiset/nimitykset/i-s-makinen-oyn-toimitusjohtaja-vaihtuu/ — frammento: "Jaakko Makikalli left his position as CEO on May 9, 2025, and was replaced by Mikko Makinen, who is part of the MAKINEN group's ownership"

**Correzione proposta:** Segnalare l'appartenenza al gruppo MAKINEN e verificare la capogruppo

#### Jet-Puu Oy — campo `dimensione`

Appartenenza a gruppo NON dichiarata: JET-Puu Oy fa parte di JETTA-Korporaatio (gruppo Jetta-Talo, case prefabbricate). Lead da riqualificare sulla capogruppo. Inoltre il fatturato riportato (8,4 M€ 2024) e' superato: 10,7 M€ e 27 dip. nel 2025.

**Evidenza:** https://vainu.io/company/jet-puu-oy-taloustiedot-ja-liikevaihto/183735/yritystiedot — frammento: "The company is part of the JETTA-Korporaatio group and operates as a sawmill and wood processing facility in Perho... In 2025, JET-Puu Oy had a revenue of 10.7 million euros and employed 27 people. In 2024, the company's revenue was 8.4 million euros"

**Correzione proposta:** Liikevaihto 10,7 M€ / 27 dip. (2025); parte di JETTA-Korporaatio (Jetta-Talo)

#### Kiilax Oy — campo `referente`

Referente errato/superato: il toimitusjohtaja in carica e' Jouni Kontkanen (imprenditore di Joensuu che ha rilevato e rilanciato l'azienda, gia' nota come Palavaneri). Jani Olkkonen non risulta amministratore delegato attuale.

**Evidenza:** https://vainu.io/company/kiilax-oy-taloustiedot-ja-liikevaihto/256569/yritystiedot e https://www.karjalainen.fi/paikalliset/7656099 — frammento: "The company's managing director (toimitusjohtaja) is Jouni Kontkanen"; "Tuore joensuulainen yrittaja Jouni Kontkanen on pistanyt aiemmin Palavanerina tunnettua Kiilaxia iskukuntoon"

**Correzione proposta:** Jouni Kontkanen — Toimitusjohtaja (CEO)


### Danimarca (19)

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

#### KAILOW A/S — campo `referente`

REFERENTE SUPERATO. Joergen Kailow non e' piu' al vertice operativo: dal 1 aprile 2025 l'administrerende direktoer di KAILOW A/S e' Per Puch Holm-Larsen, mentre Joergen Kailow e' passato a presidente del consiglio (bestyrelsesformand) dalla stessa data. Il ruolo indicato ('Direktoer della capogruppo') non e' inoltre il vertice della societa' target.

**Evidenza:** https://lasso.dk/firmaer/15945672/ny-administrerende-direktr-i-kailow-as/... 'Ny administrerende direktoer i KAILOW A/S' (evento 01.04.2025); estatistik.dk/virksomhed/kailow-as/15945672/roller - 'Per Puch Holm-Larsen, administrerende direktoer siden 1. april 2025; Joergen Kailow, bestyrelsesformand siden 1. april 2025'

**Correzione proposta:** Per Puch Holm-Larsen — Adm. direktør (dal 01.04.2025)

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

#### ODENSE SEGLMÆRKEFABRIK A/S — campo `dimensione`

AZIENDA NON PIU' AUTONOMA. Il CVR 17620487 risulta con stato 'oploest efter fusion' (sciolta a seguito di fusione) e la capogruppo e' OG NORDIC ApS, ossia Optimum Group Nordic, braccio nordico del gruppo olandese Optimum Group. Il record la presenta invece come unita' produttiva indipendente: e' un lead da decidere a livello di capogruppo estera, non locale.

**Evidenza:** https://ownr.dk/companies/public-profile/17620487 e https://profiler.dk/17620487/stamdata - CVR 17620487, stato 'oploest efter fusion', 'del af en koncern med OG Nordic ApS som moderselskab'; https://optimumgroup-printing.com/sites/optimum-group-odense-seglmaerke/ - 'Odense Seglmaerke \| Optimum Group'

**Correzione proposta:** Odense Seglmærke — sito produttivo di Optimum Group Nordic (OG NORDIC ApS), gruppo Optimum Group (NL). CVR 17620487 sciolto per fusione. Lead da valutare a livello di capogruppo.

#### ODENSE SEGLMÆRKEFABRIK A/S — campo `sede`

Sede superata: nel 2025 Optimum Group Nordic ha deciso di trasferire Odense Seglmaerke da Odense ad Ans By (tra Bjerringbro e Silkeborg, Midtjylland) per condividere lo stabilimento con la consociata Etiflex; il trasferimento e' previsto entro fine 2025.

**Evidenza:** https://signprintpack.dk/2025/07/14/odense-seglmaerke-forlader-odense/ - 'Odense Seglmaerke forlader Odense' (14.07.2025)

**Correzione proposta:** Ans By (Silkeborg, Midtjylland) dal 2025 — DA CONFERMARE la data effettiva del trasferimento

#### SKJERN PAPER A/S (già Skjern Papirfabrik A/S) — campo `dimensione`

ASSETTO PROPRIETARIO FALSO. Il campo dichiara 'Proprieta' Buur Invest A/S + dirigenti operativi (indipendente danese dal 2005)'. In realta' Skjern Paper A/S e' stata acquisita dal gruppo statunitense SONOCO Products Company (NYSE: SON) con accordo annunciato il 28.09.2022 per ~88 mio USD / 675 mio DKK, closing nel Q4 2022. Non e' un'azienda indipendente danese: la decisione EUDR si colloca presso la capogruppo USA.

**Evidenza:** https://www.globenewswire.com/news-release/2022/09/28/2524051/26553/en/Sonoco-to-Expand-European-Manufacturing-with-the-Acquisition-of-Skjern-Paper-in-Denmark.html e https://denmark.dlapiper.com/en/news/dla-piper-advises-sonoco-its-acquisition-skjern-paper - 'DLA Piper advises Sonoco on its acquisition of Skjern Paper'; dbrs.dk 'Skjern Paper solgt for 675 millioner kroner'

**Correzione proposta:** Controllata di Sonoco Products Company (USA) dal Q4 2022 (acquisizione ~675 mio DKK). Produzione ~75.000 t/anno di cartoncino da riciclo. Lead da escludere o da trattare a livello di capogruppo Sonoco.

#### SKOVS KORN A/S. KORN- OG FODERSTOFAGENTUR — campo `filiera`

Perimetro EUDR dubbio: la societa' si qualifica pubblicamente come broker/agenzia di intermediazione internazionale ('brokers indenfor international handel med korn, foderstoffer og oliefro' dal 1987) e la ragione sociale stessa e' 'Korn- og Foderstofagentur'. Un agente che non acquista in proprio non immette la commodity sul mercato UE e quindi non e' operatore ai sensi EUDR (analogia con gli operatori di sola logistica). Inoltre le commodity trattate (cereali, mangimi, semi oleosi) ricadono in Allegato I solo per la parte soia, non verificata. Il modesto bruttofortjeneste (12 M DKK ~1,6 M€) e' coerente con un'attivita' di pura intermediazione.

**Evidenza:** http://skovskorn.dk/ - 'Skovs Korn A/S har siden 1987 opereret som brokers indenfor international handel med korn, foderstoffer og oliefro' ; https://www.proff.dk/firma/skovs-korn-as.-korn-og-foderstofagentur/vejle/jordbrugsr%C3%A5varer-levende-dyr-tekstilr%C3%A5varer-og-indsatsvarer-agentur/064Z69I10OL (settore: agentur)

**Correzione proposta:** Escludere o declassare il lead salvo verifica che la societa' operi anche in conto proprio su soia (import fisico nell'UE)

#### STOK EMBALLAGE K/S — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO E FUORI FORBICE. Il campo indica solo la capogruppo formale STOK Denmark ApS senza dire chi la controlla: dal 30.04.2024 STOK e' partecipata in maggioranza dal fondo di private equity statunitense A&M Capital Europe (Alvarez & Marsal Capital), dopo la morte improvvisa del proprietario e una cessione da ~700 mio DKK. Inoltre il fatturato e' pubblicato ed e' fuori forbice: 686,73 mio DKK nel 2025 (~92 M€), risultato 32,9 mio DKK — non 'verosimilmente >50 M€' come stimato.

**Evidenza:** https://www.a-mcapital.com/am-capital-europe-announces-majority-investment-in-stok-emballage/ - 'A&M Capital Europe Announces Majority Investment in STOK Emballage'; https://kapwatch.dk/nyheder/kapitalfonde/article17008882.ece - 'Dansk familievirksomhed solgt til amerikansk kapitalfond'; https://www.proff.dk/firma/stok-emballage-ks/langeskov/producenter/GL8Z7BI016D - 'omsaetning 686.730 t.DKK, resultat 32.895 t.DKK (2025)'; koncern di 11 societa' con STOK Denmark ApS capogruppo

**Correzione proposta:** Fatturato 686,7 mio DKK nel 2025 (~92 M€) — FUORI FORBICE (>40 M€). Controllata di maggioranza del fondo statunitense A&M Capital Europe dal 30.04.2024 tramite STOK Denmark ApS (gruppo di 11 societa'). Lead da escludere o da trattare a livello di capogruppo. Adm. direktør Martin Frederiksen confermato in carica.

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


### Svezia (10)

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

#### Johanson Design Aktiebolag — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: Johanson Design Aktiebolag fa parte di un gruppo di 5 società la cui capogruppo è Johanson Design Invest Aktiebolag (org.nr 556691-6457, stessa sede a Markaryd); la stessa Johanson Design AB ha 3 controllate. Il foglio non ne fa menzione. Attenuante: Dan Mikael Johansson è VD e ordförande della società operativa e ordförande anche della holding, quindi il referente indicato resta il decisore corretto. Dati confermati: 251 117 KSEK = 22,2 M€ (2024), 70 dipendenti, conversione KSEK corretta.

**Evidenza:** https://www.allabolag.se/5563585206/koncern — «Johanson Design Aktiebolag is part of a group with a total of 5 companies, with Johanson Design Invest Aktiebolag as the parent company ... Johanson Design Aktiebolag has 3 subsidiaries»

**Correzione proposta:** Aggiungere: capogruppo Johanson Design Invest Aktiebolag (org.nr 556691-6457), gruppo di 5 società; 3 controllate dirette

#### NC Nordic Care AB — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: la capogruppo di NC Nordic Care AB è Materia Group AB. Il foglio presenta l'azienda come autonoma e non menziona alcun legame societario. Ai fini EUDR la compliance si decide a livello di capogruppo: il lead va riqualificato o riassegnato a Materia Group AB.

**Evidenza:** https://www.allabolag.se/foretag/nc-nordic-care-ab/valdemarsvik/m%C3%B6bler/2JZRNU1I5YGJV — «The parent company (moderbolaget) is Materia Group AB»

**Correzione proposta:** Aggiungere: capogruppo Materia Group AB (gruppo di arredo); lead da valutare a livello di capogruppo

#### Nola Industrier AB — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: Nola Industrier AB fa parte di un gruppo di 3 società la cui capogruppo è Sentensen Aktiebolag (22 dipendenti, 88,0 MSEK di fatturato consolidato). Il foglio non ne fa menzione. Dati economici confermati (86 155 KSEK ≈ 7,6 M€, 2024; 22 dipendenti): conversione KSEK corretta.

**Evidenza:** https://www.allabolag.se/foretag/nola-industrier-ab/stockholm/kontorsinredningar/2JZIK3UI5YF48 — «Nola Industrier AB ingår i en koncern med totalt 3 bolag, där moderbolaget är Sentensen Aktiebolag»

**Correzione proposta:** Aggiungere: capogruppo Sentensen Aktiebolag (gruppo di 3 società, 88,0 MSEK)

#### Nydala Trävaru Aktiebolag — campo `dimensione`

CONTROLLO DI GRUPPO NON DICHIARATO: Nydala Trävaru Aktiebolag fa parte di un gruppo di 2 società la cui capogruppo è Nydala Trä Holding AB. Il foglio la presenta come «segheria familiare» senza indicare la holding. Rilevante per EUDR: la compliance si decide a livello di capogruppo.

**Evidenza:** https://www.allabolag.se/organisation/nydala-trc3a4varu-aktiebolag/vrigstad/sc3a5gverk/2JYQ8C9I5YHTM — «The parent company is Nydala Trä Holding AB. Nydala Trävaru Aktiebolag is part of a group with a total of 2 companies»

**Correzione proposta:** Aggiungere: capogruppo Nydala Trä Holding AB (gruppo di 2 società)

#### Tärnsjö Garveri Aktiebolag — campo `dimensione`

Legame di gruppo NON dichiarato: il record definisce l'azienda 'la principale conceria indipendente attiva', ma allabolag indica come moderbolag Axel Bodéns Handels Aktiebolag. L'affermazione di indipendenza è falsa e la compliance EUDR si deciderebbe alla capogruppo.

**Evidenza:** allabolag.se (556474-7797): «Tärnsjö Garveri Aktiebolag har 46 anställda och dess moderbolag är Axel Bodéns Handels Aktiebolag» — https://www.allabolag.se/foretag/t%C3%A4rnsj%C3%B6-garveri-aktiebolag/t%C3%A4rnsj%C3%B6/producenter/2K13UVPI63IK3

**Correzione proposta:** Sostituire 'principale conceria indipendente attiva' con: 'controllata di Axel Bodéns Handels Aktiebolag (moderbolag)'


### Olanda (9)

#### Bangma Verpakking B.V. — campo `dimensione`

LEAD NON VALIDO — aggravamento rispetto a quanto annotato. Non solo De Jong Verpakking ha acquisito Bangma (closing 30-07-2020), ma nel 2023 l'INTERO De Jong Packaging Group è stato acquisito da STORA ENSO (multinazionale finlandese quotata). Bangma Verpakking opera oggi 'as part of the De Jong Verpakking and Stora Enso family': non è più un'entità autonoma sotto il profilo decisionale e la compliance EUDR si determina a livello di capogruppo Stora Enso, che ha già un proprio programma EUDR di gruppo. Da rimuovere dalla lista lead.

**Evidenza:** https://dejongverpakking.com/en/news/de-jong-packaging-completes-acquisition-of-bangma-verpakking/ ; https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - 'in 2023 werd De Jong Packaging Group overgenomen door Stora Enso ... vandaag maakt Bangma Verpakking deel uit van de De Jong Verpakking en Stora Enso familie'; https://www.agf.nl/article/9238854/de-jong-verpakking-neemt-bangma-verpakking-over/

**Correzione proposta:** Rimuovere il lead (controllata Stora Enso via De Jong Packaging Group dal 2023)

#### BeBo Parket B.V. — campo `referente`

Referente obsoleto: Frans Bolier e Johan van de Beek (fondatori 2006) hanno ceduto l'azienda nel 2022 alla seconda generazione. La direzione e' oggi di Kees van de Beek e Marielle Zwolsman.

**Evidenza:** https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Kees van de Beek en Marielle Zwolsman maakten al deel uit van het management van Bebo en blijven het bedrijf leiden na de overdracht'

**Correzione proposta:** Kees van de Beek / Marielle Zwolsman - Directeur

#### Kargro Banden B.V. — campo `filiera`

DUBBIO DI PERIMETRO EUDR: l'attivita e la raccolta e lavorazione circolare di carcasse di pneumatici gia usati per la loro ricostruzione (loopvlakvernieuwing). Non si tratta dell'immissione per la prima volta sul mercato UE di gomma naturale o di pneumatici nuovi: il materiale ha gia concluso il proprio ciclo di vita e sarebbe altrimenti rifiuto, fattispecie esclusa dall'ambito EUDR. Il ruolo di operatore va dimostrato, altrimenti e un errore di perimetro come per gli operatori di sola logistica.

**Evidenza:** https://www.kargrogroep.nl/kargro-banden/ - 'Kargro Group Holding ... circulaire verwerking van gedemonteerde vrachtwagen- en personenautobanden'; https://kargrorecycling.com/nl/over/kargro-groep/ - 'goedgekeurde karkassen voorzien van een nieuw loopvlak'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### L. Verhoeven's Emballagefabriek en Houthandel B.V. — campo `dimensione`

Appartenenza a gruppo non dichiarata: l'azienda opera in gruppo con la consociata Zagerij Verhoeven (Harskamp) e con Kist&Co (Ridderkerk) e Harskamp Timber (Harskamp). Il campo la presenta come singola azienda familiare: la struttura di gruppo incide sia sul perimetro EUDR (segheria a monte) sia sul dimensionamento.

**Evidenza:** https://verhoeven-emballage.nl/en/about-us/ - frammento: 'works closely with sister company Zagerij Verhoeven in Harskamp; the group also includes Kist&Co in Ridderkerk and Harskamp Timber in Harskamp'

**Correzione proposta:** Gruppo Verhoeven: Zagerij Verhoeven (Harskamp), Kist&Co (Ridderkerk), Harskamp Timber (Harskamp)

#### Marine Olie Handel Maatschappij B.V. — campo `dimensione`

DATO FALSO: il campo afferma che il fatturato non e pubblicato. Il bilancio 2022 riporta un fatturato di quasi 400 M€, cioe dieci volte il tetto della forbice target 5-40 M€. Il lead e completamente fuori dalla fascia dimensionale del cliente.

**Evidenza:** https://mena.nl/artikel/handelshuis-sfx-krijgt-eigen-olie-door-overname - 'Volgens het jaarverslag over 2022 had Marine Olie een omzet van bijna 400 miljoen euro'

**Correzione proposta:** Fatturato ca. 400 M€ (bilancio 2022) - FUORI FORBICE

#### Marine Olie Handel Maatschappij B.V. — campo `denominazione`

AZIENDA ACQUISITA: Marine Olie e stata acquisita da STX Group (Amsterdam); l'operazione, approvata dalla Commissione europea, si e chiusa il 01/12/2024. La societa non e piu indipendente e la decisione di compliance EUDR si colloca in STX Group. Lead da scartare o da riferire alla capogruppo.

**Evidenza:** https://stxgroup.com/media-release/stx-group-expands-its-biofuels-business-with-strategic-acquisition-of-marine-olie/ - acquisizione annunciata a dicembre 2024, closing 1 dicembre 2024; https://www.maverick-law.com/nl/zaken/maverick-advocaten-begeleidt-marine-olie-bij-goedkeuring-van-europese-commissie-voor-overname-door-stx.html

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Marine Olie Handel Maatschappij B.V. — campo `filiera`

DUBBIO DI PERIMETRO: la filiera dichiarata e 'Olio di palma', ma le fonti descrivono un trader di oli che sono in prevalenza sottoprodotti e scarti alimentari (sottoprodotti dell'olio d'oliva, olio da frittura usato/UCO) destinati ai biocarburanti - proprio la motivazione dell'acquisizione da parte di STX Group, che opera nei biofuels. UCO e biodiesel sono fuori Allegato I. L'esposizione a olio di palma non e dimostrata da alcuna fonte.

**Evidenza:** https://mena.nl/artikel/handelshuis-sfx-krijgt-eigen-olie-door-overname - 'handelt in diverse olien die vaak reststromen uit voeding zijn, van bijproducten van olijfolie tot gebruikt frituurvet'; https://fd.nl/bedrijfsleven/1538504/ - 'STX Group koopt Marine Olie om te groeien in handel van biobrandstoffen'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Rompa Tanneries B.V. — campo `denominazione`

Denominazione obsoleta: la societa' e' stata ridenominata VITELCO LEATHER B.V. Vitelco (gruppo PALI) ha rilevato le quote di Rompa Leather sciogliendo la joint venture ed e' oggi socio unico al 100%. Anche la pagina LinkedIn indicata (nl.linkedin.com/company/rompa-tanneries) si presenta ora come 'Vitelco Leather'.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco and Rompa Leder however decided to dissolve this joint venture and Vitelco took over the Rompa Tanneries shares from Rompa Leder. Vitelco is now 100% owner of the tannery and changes its name to Vitelco Leather B.V.'

**Correzione proposta:** Vitelco Leather B.V.

#### Rompa Tanneries B.V. — campo `dimensione`

Assetto proprietario dichiarato errato: il campo indica ancora 'Soci: PALI Group (Den Bosch, vitello) e Rompa Leather (Rijen)', ma la JV e' stata sciolta e Vitelco (PALI Group) e' socio unico al 100%. La societa' e' quindi una controllata integrale di gruppo (PALI Group, 's-Hertogenbosch): la compliance EUDR si decide a livello di capogruppo, il lead va riqualificato o scartato.

**Evidenza:** https://www.paligroup.nl/uk/news/rompa-tanneries-becomes-vitelco-leather/ - frammento: 'Vitelco is now 100% owner of the tannery'

**Correzione proposta:** Controllata al 100% di Vitelco B.V. (PALI Group), 's-Hertogenbosch


### Belgio (15)

#### Accent NV — campo `dimensione`

La descrizione del legame di gruppo e' rovesciata e fuorviante. Accent non e' la 'capofila' del gruppo Asteria: dal 2018 la famiglia Declerck ha ceduto la MAGGIORANZA al fondo Waterland (prima 18 M€, poi 52 M€ di capitale fresco) e Accent e' oggi una societa' operativa dentro The Asteria Group, che con 17 acquisizioni in tre anni ha raggiunto un fatturato consolidato di 492 M€. Le decisioni di compliance EUDR si prendono a livello di gruppo, non a Gullegem: il record non e' un lead autonomo.

**Evidenza:** derijkstebelgen.be 'Asteria wil tegen 2030 met Waterland Europees leider worden': 'In 2018 haalde de West-Vlaamse familie Declerck durfkapitalist Waterland binnen als nieuwe meerderheidsaandeelhouder in hun bedrijf Accent'; 'De eerste geconsolideerde jaarrekening van The Asteria Group toont een omzet van 492 miljoen euro'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Allbox NV — campo `dimensione`

Assetto proprietario NON dichiarato. Il record presenta Allbox come 'azienda familiare', ma il controllo integrale della NV e' stato acquisito da KBC Investco (capitale di rischio) insieme al management familiare, che ha mantenuto solo una partecipazione di minoranza significativa e la direzione operativa. La decisione di compliance EUDR non e' quindi interamente in mano alla famiglia.

**Evidenza:** dvo.be/artikel/14427-allbox-nv: 'KBC Investco, verschaffer van risicokapitaal, heeft samen met het familiale management de integrale controle over Allbox N.V. verworven. Het familiale management, dat een belangrijke minderheidsparticipatie in Allbox verwerft, blijft de operationele leiding van de onderneming behouden'

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

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

#### Hannecard Benelux NV — campo `dimensione`

LEGAME DI GRUPPO NON DICHIARATO. Hannecard Benelux NV (BE 0694.906.812) non e' una societa' indipendente: e' l'entita' Benelux del Gruppo Hannecard, che fa capo a Hannecard NV (BE 0892.311.512, stessa sede di Ronse) e il cui capitale e' entrato nel febbraio 2022 in BNP Paribas Fortis Private Equity. Il gruppo opera a livello mondiale con piu' societa': la decisione di compliance EUDR si prende a livello di gruppo, non della societa' Benelux.

**Evidenza:** https://www.bnpparibasfortis.be/en/public/article/bnp-paribas-fortis-private-equity-participates-in-hannecard — "In February 2022, BNP Paribas Fortis Private Equity acquired [a stake in] Hannecard NV"; https://fincheck.be/nl/hannecard/0892.311.512/Ronse/bestuurders (entita' distinta Hannecard NV, Ronse); "the Hannecard Group stands as a worldwide leader in industrial roller coverings" (https://www.hannecard.com/en/company/)

**Correzione proposta:** Dichiarare: societa' del Gruppo Hannecard (capogruppo Hannecard NV, BE 0892.311.512, Ronse), partecipato da BNP Paribas Fortis Private Equity dal febbraio 2022.

#### Helvoet Rubber & Plastic Technologies NV — campo `filiera`

ERRORE DI PERIMETRO EUDR. Helvoet non lavora gomma naturale: la gamma elastomeri dichiarata dall'azienda comprende esclusivamente polimeri sintetici — butile (IIR), cloroprene (CR), EPDM, nitrile (NBR), acrilico (AEM/ACM), poliuretano (AU), siliconi e fluorosiliconi (VMQ/FMVQ), FKM, HNBR, FFKM — oltre a termoplastici e LSR. Il sito di Lommel e' descritto dall'azienda stessa come hub per componenti termoindurenti, termoplastici ad alte prestazioni e silicone liquido (LSR), per automotive/e-mobility/medicale. Caso analogo a RICO Elastomere (Austria), gia' scartata: fuori Allegato I EUDR.

**Evidenza:** https://helvoet.com/rubber/ — "Engineering Elastomers including Butyl Rubber (IIR), Chloroprene Rubber (CR), EPDM and Nitrile Rubber (NBR) ... Acrylate Rubber (AEM, ACM), Polyurethane (AU), Silicone and Fluorosilicone Rubber (VMQ, FMVQ), Fluor rubber (FKM), HNBR and Perfluor Elastomers (FFKM)"; https://helvoet.com/news/helvoet-strengthens-position-in-high-performance-plastics/ — "Helvoet's Lommel site serves as a fully integrated hub for thermoset, high-performance thermoplastic and liquid silicone rubber (LSR) components". Nessuna menzione di gomma naturale (NR).

**Correzione proposta:** Scartare il lead per fuori perimetro EUDR (solo elastomeri sintetici e silicone), salvo prova documentale di impiego di gomma naturale.

#### Helvoet Rubber & Plastic Technologies NV — campo `dimensione`

LEGAME DI GRUPPO NON DICHIARATO. La societa' di Lommel e' la filiale belga del gruppo olandese Helvoet (Helvoet Holding B.V., fondata 1939 a Hellevoetsluis, siti in NL, DE, BE, IN, PL), acquisito da Hydratec Industries NV nel luglio 2015 e successivamente passato a RF Plast (settembre 2024). Non e' una PMI belga indipendente e la compliance si decide a livello di capogruppo. Inoltre il dato di 17,48 M EUR non e' accompagnato da FTE: l'ultimo bilancio (giugno 2025) indica 78,4 FTE.

**Evidenza:** https://pitchbook.com/profiles/company/40839-13 ("Helvoet Rubber & Plastic Technologies was acquired on September 1, 2024 by RF Plast"); https://mergr.com/hydratec-industries-nv-acquires-helvoet-holding-bv (Hydratec Industries acquisisce Helvoet Holding BV, 08-07-2015); https://www.companyweb.be/en/0867662822/helvoet-rubber-plastic-technologies ("78.4 FTEs ... most recent financial statements filed in June 2025"); https://nl.wikipedia.org/wiki/Helvoet_Rubber

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### La Chocolaterie Galler SA — campo `dimensione`

AZIENDA IN CRISI E CEDUTA. Galler era in procedura di riorganizzazione giudiziaria (PRJ 'silenziosa') ed e' stata rilevata nell'aprile 2026 da un consorzio vallone (chocolaterie Dolfin come azionista di maggioranza, Wallonie Entreprendre, investitori privati, Sebastien Desclee) tramite la costituzione di una 'nuova societa' Galler', con 70 licenziamenti su 170 dipendenti. Il record ne fa un cenno ma non ne trae le conseguenze: la societa' storica BE 0416.169.689 potrebbe non essere piu' l'entita' operativa (cessione di attivi a nuova entita'), il fatturato ~29,5-32 M EUR e i 194 dipendenti sono superati, e la compliance e' ora decisa dal nuovo azionariato (Dolfin). Lead da riqualificare o scartare; il numero d'impresa da usare va riverificato in KBO.

**Evidenza:** Frammento La Libre: "Un projet de relance d'un nouveau Galler entierement entre des mains belges permet d'eviter le choc d'une faillite frontale" (23-04-2026); "L'entreprise chocolatiere liegeoise Galler, qui avait ete placee en procedure de reorganisation judiciaire silencieuse, a ete reprise par des actionnaires entierement wallons ... le capital ... majoritairement dans les mains de la chocolaterie familiale Dolfin" — https://www.qu4tre.be/infos/economie/des-actionnaires-wallons-reprennent-la-chocolaterie-galler/2014147

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Manufacture Belge de Chocolats SRL — campo `dimensione`

LEGAME DI GRUPPO NON DICHIARATO. MBC non e' una PMI belga indipendente: e' lo stabilimento di produzione bruxellese di Godiva ceduto nel giugno 2019 al fondo MBK Partners insieme alle attivita' Godiva di Giappone, Corea del Sud e Oceania, e ribattezzato 'Manufacture Belge de Chocolats'. La societa' fa parte del gruppo Godiva Japan (CEO di gruppo Jerome Chouchan). La decisione di compliance EUDR si prende a livello di Godiva Japan/MBK Partners: il lead va riqualificato o scartato.

**Evidenza:** Frammento mbcchocolates.be/theorg: "Manufacture Belge de Chocolats is a company being part of Godiva Japan"; "In June 2019, MBK Partners acquired Godiva Japan, along with operations in South Korea, Oceania, and the Brussels production plant. The factory is renamed Manufacture Belge de Chocolats (MBC), becoming part of the Godiva Japan Group" — https://www.mbcchocolates.be/en/about-us ; https://www.prnewswire.com/news-releases/godiva-chocolatier-owned-by-yildiz-holding-completes-the-sale-of-select-godiva-assets-to-mbk-partners-300860576.html

**Correzione proposta:** Dichiarare: controllata del gruppo Godiva Japan (MBK Partners) dal 2019, ex stabilimento Godiva di Bruxelles.

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


### Austria (4)

#### Storebest Ladeneinrichtungen GmbH — campo `denominazione`

FILIALE DI GRUPPO ESTERO NON DICHIARATA. STOREBEST Österreich e' parte della Kesseböhmer Holding KG di Bad Essen (Germania), gruppo con ca. 3.500 dipendenti su dodici siti; esiste anche la consorella tedesca STOREbest GmbH & Co. KG di Lübeck. La compliance EUDR si decide alla capogruppo tedesca: lead da declassare o rimuovere secondo il criterio gia' applicato a Segafredo Zanetti Austria / Lavazza Kaffee / BRAUN LOCKENHAUS.

**Evidenza:** https://www.storebest.at/unternehmen/ ('STOREBEST Österreich ist Teil der inhabergeführten, international tätigen Kesseböhmer Holding KG mit Sitz in Bad Essen'; 'rund 3.500 Mitarbeiter an zwölf Standorten'); https://www.handelsverband.at/mitglieder/unsere-partner/detail/storebest-ladeneinrichtungen-gmbh/

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Tschurtschenthaler Gerberei GmbH — campo `email`

Nessuna e-mail pubblica reperibile (campo 'n.d.') e nessun sito web aziendale: il lead non e' contattabile per via digitale. Le fonti pubbliche (WKO, herold.at, cylex, yelp) riportano solo indirizzo e telefono.

**Evidenza:** https://firmen.wko.at/tschurtschenthaler-gerberei-gmbh/k%C3%A4rnten/ - la scheda WKO riporta solo indirizzo Bach 17, 9623 St. Stefan/Gailtal e telefono 04283 20..., nessuna e-mail ne' sito

**Correzione proposta:** — nessun valore certo: rilievo lasciato aperto

#### Weissengruber Möbelmanufaktur GmbH — campo `denominazione`

AZIENDA IN INSOLVENZA. Il produttore di mobili Weissengruber (Niederzirking 89, Ried in der Riedmark, ca. 55-60 dipendenti) ha presentato istanza di insolvenza (Sanierungsverfahren ohne Eigenverwaltung) al Landesgericht Linz il 13 gennaio; curatore René Lindner, prosecuzione con Massekredit e voto dei creditori sul piano di risanamento il 29 aprile. Caso identico a HAKA Küche / KAPO Möbel / ADA / Schletterer gia' esclusi. Inoltre l'entita' attiva risulta 'WEISSENGRUBER Möbelproduktion e.U.' (non la GmbH): denominazione e forma giuridica del record non corrispondono.

**Evidenza:** https://www.ksv.at/insolvenzfaelle/weissengruber-moebelproduktion-eu-198251 ; https://www.euwid-holz.de/news/moebel/wohn-und-objektmoebelhersteller-weissengruber-ist-insolvent-140125/ ; https://www.nachrichten.at/wirtschaft/insolvenz-bei-moebelhersteller-weissengruber-fortfuehrung-mit-massekredit;art15,4020792 ; https://firmen.wko.at/weissengruber-m%C3%B6belproduktion-eu/ober%C3%B6sterreich/

**Correzione proposta:** RIMUOVERE il lead (insolvenza in corso)

#### Wittmann Möbelwerkstätten GmbH — campo `referente`

REFERENTE OBSOLETO DI DUE PASSAGGI. Heinz Hofer-Wittmann non e' piu' alla guida: gli e' subentrato Bo Thuesen come CEO, uscito dopo circa un anno e mezzo su sua richiesta, e oggi la Geschäftsführung e' di Alice Wittmann (39 anni, pro-pronipote del fondatore), con responsabilita' su marketing, prodotto e vendite. In Firmenbuch risultano inoltre iscritti Alexander Sova e Ron Vorona.

**Evidenza:** https://www.noen.at/krems/wechsel-ururenkelin-von-firmengruender-neu-an-spitze-von-etsdorfer-unternehmen-508632071 ; https://moebel-guide.at/news/generationswechsel-bei-wittmann-alice-wittmann-ubernimmt-geschaftsfuhrung ; https://www.moebelfertigung.com/branche/bo-thuesen-ist-der-neue-ceo ; https://www.firmenabc.at/wittmann-moebelwerkstaetten-gmbh_NVdS

**Correzione proposta:** Alice Wittmann — Geschäftsführerin


---

## 5. Casi di gravità MEDIA (259)

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

### Germania (38)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Alder Sägewerk & Holzhandlung GmbH | dimensione | Campo privo di qualsiasi elemento dimensionale ('Umsatz/MA n.d.'): nessun tipo di dato, nessuna fonte, nessun anno. Segheria familiare (HRB 201958 Amtsgericht Stadthagen) verosimilmente molto sotto la forbice target 5-40 Mio EUR, senza segnalazione e | https://www.northdata.com/Alder%20S%C3%A4gewerk%20&%20Holzhandlung%20GmbH,%20Auhagen/Amtsgericht%20Stadthagen%20HRB%20201958 - scheda registro senza d |  |
| Büttenpapierfabrik Gmund GmbH & Co. KG | email | Il campo è vuoto («n.d.») pur essendo l'indirizzo pubblicato letteralmente nell'Impressum del sito aziendale, obbligatorio per legge in Germania. | https://de.gmund.com/impressum.html/ — Mangfallstr. 5, 83703 Gmund a. Tegernsee; Tel. +49 8022 7500-0; E-Mail: info@gmund.com; AG München HRB 114639,  | info@gmund.com |
| Christian Göbel Holzgroßhandlung GmbH & Co.  | email | L'Impressum ufficiale riporta l'indirizzo info@goebel-holz.com (dominio .com), non info@goebel-holz.de come indicato nel record. Il sito e invece www.goebel-holz.de. | https://www.goebel-holz.de/impressum/ - 'Telefon: 069 / 95 30 19-18 ... E-Mail: info@goebel-holz.com ... USt-IdNr.: DE112006391' | info@goebel-holz.com |
| Christian Göbel Holzgroßhandlung GmbH & Co.  | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d.'), sostituito da un elemento non dimensionale ('>85 anni'). Nessun fatturato ne numero addetti con fonte e anno. | https://www.wlw.com/en/company/christian-goebel-holzgrosshandlung-grosshandlung-mit-sperrholz-gmbh-co-kg-755264 e https://www.northdata.com/Christian% |  |
| Die Pharmadrucker GmbH | dimensione | Appartenenza a gruppo dichiarata ma da qualificare: la società è controllata dalla Bernecker-Gruppe (Druckerei Bernecker GmbH, stessa sede) dal 2016; la decisione di compliance EUDR si prende a livello di capogruppo, quindi il lead va indirizzato lì. | https://www.diepharmadrucker.de/unternehmen/ — società del gruppo Bernecker dal 2016, stessa sede di Druckerei Bernecker GmbH (Unter dem Schöneberg 1, | «Controllata di Bernecker-Gruppe (Melsungen) dal 2016; 50-99 dipendenti (wlw.com, senza anno) — fatturato non pubblicato |
| Druckerei Siepmann GmbH | dimensione | Campo inutilizzabile: «KMU; Umsatz/MA n.d.», nessun dato quantitativo, nessuna fonte, nessun anno. Il numero di dipendenti è invece pubblicato dall'azienda (~65). | https://siepmanndruck.de/ — «ein Team von rund 65 Mitarbeitern»; AG Hamburg HRB 25539 | «~65 dipendenti (sito aziendale, 2025); fatturato non pubblicato (GmbH, deposito abbreviato) — DA CONFERMARE su Bundesan |
| Druckerei Siepmann GmbH | filiera | La filiera è dichiarata «Verpackungsdruck/Faltschachteln», ma l'azienda si presenta come tipografia commerciale generalista di Amburgo (stampati, cataloghi), non come produttore di astucci pieghevoli. Va inoltre valutato il perimetro EUDR: un tipogra | https://siepmanndruck.de/ — «Druckerei Siepmann \| Ihre Hamburger Druckerei»; https://www.wer-zu-wem.de/firma/siepmanndruck.html |  |
| E. Fuhlrott GmbH & Co. KG (HOLZFUHLROTT) | dimensione | Il dato '~20-49 MA (wlw.de)' e una fascia di portale senza anno di riferimento e senza alcun dato di fatturato ('Umsatz n.d.'). Non consente di collocare il lead nella forbice 5-40 Mio EUR. | https://www.wlw.de/de/firma/e-fuhlrott-gmbh-co-kg-kistenfabrik-und-holzhandel-483545 (fascia addetti, senza anno); https://www.invest-in-thuringia.de/ |  |
| EGGER Druck + Medien GmbH | referente | Elenco Geschäftsführer incompleto: l'Impressum indica tre amministratori, il record ne riporta due (manca Axel Schreiner). | https://www.eggerdruck.de/impressum.html — «Geschäftsführer: Franz Xaver Egger, Josef Maximilian Egger, Axel Schreiner»; AG Augsburg HRB 9915 | Franz Xaver Egger, Josef Maximilian Egger, Axel Schreiner |
| EGGER Druck + Medien GmbH | email | L'e-mail indicata (service@madika.de) è quella del negozio online madika.de, non l'indirizzo aziendale dell'Impressum di EGGER Druck + Medien. Per un contatto commerciale B2B è preferibile l'indirizzo societario. | https://www.eggerdruck.de/impressum.html — Lechwiesenstraße 23, D-86899 Landsberg am Lech, Tel. +49 8191 9180-0, E-Mail: egger@eggerdruck.de | egger@eggerdruck.de |
| EGGER Druck + Medien GmbH | dimensione | Campo privo di qualsiasi dato («Umsatz/MA n.d.»). Le fonti disponibili indicano 11-50 dipendenti: con questa dimensione l'azienda è verosimilmente SOTTO la soglia minima di 5 Mio € della forbice cliente, e il record andrebbe riqualificato o escluso.  | https://firmeneintrag.creditreform.de/86899/8030017156/EGGER_DRUCK_MEDIEN_GMBH e https://www.wer-zu-wem.de/firma/egger-druck-medien.html — 11-50 Mitar | «11-50 dipendenti (Creditreform / wer-zu-wem, 2025); fatturato non pubblicato — probabile sotto-soglia rispetto alla for |
| Ebro Color GmbH | dimensione | Campo senza fonte, senza anno e senza dato di fatturato («~40 MA, familiengeführt; Umsatz n.d.»). È invece disponibile il bilancio 2023 depositato: totale di bilancio 5 Mio €, in calo del 20,2% sull'anno precedente — informazione rilevante anche perc | https://www.northdata.com/Ebro%20Color%20GmbH,%20Albstadt/Amtsgericht%20Stuttgart%20HRB%20400380 — «Bilanzsumme 2023: 5 Mio EUR (-20,2%)»; https://www | «Totale di bilancio 5 Mio € (2023, Bundesanzeiger via Northdata, -20,2% a/a); ~40 dipendenti; fatturato non pubblicato ( |
| FMS AG | dimensione | Il campo riporta solo una fascia di portale senza anno e senza fatturato («>60 MA (wer-zu-wem); Umsatz n.d.»). Il numero è confermato dal sito aziendale ma resta impossibile collocare l'azienda nella forbice 5-40 Mio €. Trattandosi di una AG con regi | https://fmsag.de/ihre-fms/ — «über 60 Mitarbeiterinnen, Mitarbeiter und Auszubildende»; https://www.northdata.com/FMS%20AG%20-%20Druck,%20Verpackungen | «>60 dipendenti (sito aziendale, 2025); fatturato non pubblicato — DA CONFERMARE su Bundesanzeiger, AG Ansbach HRB 5384» |
| Falt Schachtel Hamburg dyecut GmbH | dimensione | Campo inutilizzabile: «KMU; Umsatz/MA n.d.», nessun dato, nessuna fonte, nessun anno. Referente (Martin Lemcke), e-mail e sede risultano invece corretti da Impressum. | https://www.faltschachtelhamburg.de/impressum/ — Wördemanns Weg 58, 22527 Hamburg; Geschäftsführer Martin Lemcke; info@faltschachtelhamburg.de; AG Ham |  |
| Furnierwerk Bühl GmbH | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d.'). Le fonti danno indicazioni discordanti: classe di fatturato 10-50 Mio EUR ma totale di bilancio 2023 di soli 1,8 Mio EUR. Da riverificare prima di considerare il lead in forbice. | https://implisense.com/de/companies/furnierwerk-buehl-gmbh-buehl-DE7ZGDDBNO95 - 'Bilanzsumme 2023: 1,8 Mio EUR'; https://www.wer-zu-wem.de/firma/furni | Totale di bilancio 1,8 Mio EUR (2023, Bundesanzeiger via Implisense); classe di fatturato 10-50 Mio EUR (wer-zu-wem) - D |
| Gebr. Kilger, Lederfabrik Viechtach KG | dimensione | Il campo riporta solo '~20 MA, Umsatz n.d.' senza anno ne fonte. Il dato dipendenti e confermabile (fonte 2019) ma nessun dato di fatturato e disponibile; con ~20 addetti e 1.000-1.500 pelli/mese l'azienda e verosimilmente molto sotto la forbice targ | https://www.hogn.de/2019/07/02/1-da-hogn-geht-um/nachrichten-im-landkreis-regen/michael-kilger-viechtach-leder-manufaktur-guertel-schuhe-gerbung-satte | ~20 dipendenti (fonte: hogn.de, 2019); volumi 1.000-1.500 pelli/mese; fatturato non pubblicato (KG non tenuta al deposit |
| Graphische Betriebe Kip GmbH + Co. KG | dimensione | Dato dipendenti obsoleto (2020, sei anni fa) e nessun dato di fatturato. Le fonti attuali indicano oltre 100 dipendenti a tempo pieno / fascia 51-200 (LinkedIn), quindi il campo non consente di collocare l'azienda nella forbice 5-40 Mio €. | https://www.emsachse.de/unternehmen/graphische-betriebe-kip-gmbh-co-kg — azienda familiare fondata nel 1951, «mehr als 100 Vollzeitbeschäftigte», prod | «>100 dipendenti a tempo pieno (2025, emsachse.de); fatturato non pubblicato (GmbH & Co. KG, AG Osnabrück HRA 130316) —  |
| H.-J. Dres GmbH | dimensione | Dato gravemente obsoleto: «~19 MA (2010, lieferanten.de)» ha 16 anni ed è tratto da un portale di elenchi, non da bilancio. Inoltre, se il dato fosse ancora attuale, con ~19 addetti l'azienda sarebbe ampiamente SOTTO la soglia minima di 5 Mio € della | https://www.lieferanten.de/lieferant-8453-h-j-dres-gmbh.html (dato 2010: 19 dipendenti); https://www.northdata.com/H%C2%B7-J%C2%B7%20Dres%20GmbH,%20Sp | «~19 dipendenti (2010, lieferanten.de) — dato non aggiornato; fatturato non pubblicato. Verificare l'attuale dimensione: |
| HOFA Holzimport GmbH | dimensione | 'Umsatz >2,5 Mio EUR (Firmenauskunft), cifra esatta n.d.' non e un dato dimensionale utilizzabile: soglia aperta, senza anno e senza fonte puntuale. Non permette di verificare la forbice target 5-40 Mio EUR. | https://firmeneintrag.creditreform.de/22145/2390205389/HOFA_HOLZIMPORT_GMBH - scheda Creditreform senza cifra di fatturato nei frammenti; https://www. |  |
| Hannoversche Kartonagenfabrik GmbH & Co. KG | dimensione | Campo privo di dati verificabili («Umsatz/MA n.d.»). Le fonti indicano ~30 dipendenti: con questa dimensione l'azienda è al limite inferiore o sotto la forbice 5-40 Mio €, elemento che il campo deve rendere esplicito. | https://www.wer-zu-wem.de/firma/hannoversche-karton.html — «mittelständisches Familienunternehmen, gegründet 1958, rund 30 Mitarbeiter»; AG Hannover H | «~30 dipendenti (wer-zu-wem.de, 2025); fatturato non pubblicato (GmbH & Co. KG, AG Hannover HRA 26344) — verosimilmente  |
| Hartmann Möbelwerke GmbH | dimensione | Fatturato di riferimento del 2017 (8 anni fa) e fascia addetti '~140-210' troppo ampia. Il dato piu recente disponibile e il totale di bilancio 2023 di 10 Mio EUR (+5,2% sull'anno precedente); gli addetti confermati sono 'oltre 140'. | https://implisense.com/en/companies/hartmann-moebelwerke-gmbh-beelen-DEZSR23ZJW75 - 'last published balance sheet total 2023: 10 M EUR, +5.2%'; https: | Totale di bilancio 10 Mio EUR (2023, Bundesanzeiger via Implisense); oltre 140 dipendenti (Die Glocke, 2024); fatturato  |
| Horn Verpackung GmbH | dimensione | Campo privo di dati («Mittelstand; Umsatz/MA n.d.») nonostante sia disponibile il bilancio depositato 2023: totale di bilancio 10 Mio €, in calo dell'8,2% sull'anno precedente. | https://www.northdata.com/Horn%20Verpackung%20GmbH,%20Winnenden/Amtsgericht%20Stuttgart%20HRB%20263833 — «Bilanzsumme 2023: 10 Mio EUR (-8,2%)»; AG St | «Totale di bilancio 10 Mio € (2023, Bundesanzeiger via Northdata, -8,2% a/a); fatturato non pubblicato (deposito abbrevi |
| Lederfabrik Josef Heinen GmbH & Co. KG (Hein | dimensione | Dato dimensionale obsoleto (2019/2020, 5+ anni) e in conflitto con le fonti: Creditreform/firmeneintrag colloca l'azienda in classe di fatturato 50-100 Mio EUR, non 20-35 Mio EUR. Va riverificato l'anno di riferimento. | https://firmeneintrag.creditreform.de/41844/5230009708/LEDERFABRIK_JOSEF_HEINEN_GMBH_CO_KG - classe di fatturato 50-100 Mio EUR; https://www.kfw.de/st | Fatturato 35 Mio EUR (2019, KfW Stories); classe di fatturato indicata da Creditreform 50-100 Mio EUR - anno piu recente |
| Lederfabrik Josef Heinen GmbH & Co. KG (Hein | esistenza_stato | DA CONFERMARE lo stato dell'azienda: Creditreform registra una variazione di bonita (Bonitaetsaenderung) datata 02.09.2025 il cui motivo non emerge dalle fonti aperte. Considerato che il settore concia tedesco ha gia registrato piu insolvenze, lo sta | https://firmeneintrag.creditreform.de/41844/5230009708/LEDERFABRIK_JOSEF_HEINEN_GMBH_CO_KG - 'Bonitaetsaenderung am 02.09.2025'; nessuna notizia di in |  |
| Max Cropp GmbH & Co. KG (Timber Im- & Export | email | Il campo email e valorizzato con 'n.d.' mentre l'indirizzo compare letteralmente nell'Impressum/contatti aziendali. | https://www.cropp-timber.com/de/kontakt/ e https://www.edelholzshop.de/de/service/about/ - 'Telefon: 040 - 766 235-0; E-Mail: info@cropp-timber.com' | info@cropp-timber.com |
| Max Cropp GmbH & Co. KG (Timber Im- & Export | dimensione | Il campo riporta '~13 MA' senza fonte ne anno e 'Umsatz n.d.'. Nessun elemento consente di verificare la forbice target 5-40 Mio EUR; l'ordine di grandezza (~13 addetti in un'attivita di import/commercio) resta indeterminato. | https://www.cropp-timber.com/de/unternehmen/ - azienda fondata nel 1919, nessuna cifra dimensionale pubblicata; https://www.cropp-timber.com/de/untern |  |
| Meisen Holzverarbeitung GmbH & Co. KG | dimensione | Il dato '~20-49 MA (Regiomanager)' e una fascia di portale priva di anno e non e accompagnato da alcun dato di fatturato ('Umsatz n.d.'): il campo non permette di collocare il lead nella forbice 5-40 Mio EUR. | https://www.regiomanager.de/koeln-bonn-aachen/unternehmen/meisen-holzverarbeitung-gmbh-und-co-kg/ (fascia addetti senza anno); https://firmeneintrag.c |  |
| PFT Holz in Form GmbH | dimensione | Il fatturato e indicato solo come classe '10-50 Mio EUR' senza anno di riferimento: fascia troppo ampia (copre sia il centro sia il limite superiore della forbice target). Anche il dato addetti (~35) e privo di anno. | https://www.wer-zu-wem.de/firma/formsperrholz.html e https://firmeneintrag.creditreform.de/96132/3410092585/PFT_HOLZ_IN_FORM_GMBH - classe di fatturat |  |
| Paletten Meyer | dimensione | Campo privo di qualsiasi elemento dimensionale ('Umsatz/MA n.d.'): nessun tipo di dato, nessuna fonte, nessun anno. Trattandosi di impresa individuale non soggetta a deposito di bilancio, il dato non e ricavabile dai registri e il lead non e collocab | https://www.regiomanager.de/suedwestfalen/unternehmen/meyer-palettenbau/ - profilo aziendale senza cifre; impresa individuale (Inh. Julian Meyer), nes |  |
| Parkett Herter GmbH & Co. KG | dimensione | Il fatturato e espresso come fascia aperta verso il basso ('fino a 10 Mio EUR') e senza anno di riferimento: compatibile anche con valori sotto la soglia minima della forbice target (5 Mio EUR). Anche '>30 MA' e privo di anno. | https://www.firmenwissen.de/az/firmeneintrag/72116/7270165223/PARKETT_HERTER_GMBH_CO_KG.html - 'Jahresumsatz bis 10 Mio EUR', 'mehr als 30 Mitarbeiter |  |
| RMW Wohnmöbel GmbH & Co. KG (Rietberger Möbe | dimensione | Il fatturato di ~20 Mio EUR e una STIMA di portale (Die Deutsche Wirtschaft) priva di anno di riferimento e non ricavata da bilancio depositato; non e affiancata da alcun dato addetti. Il campo non e verificabile. | https://die-deutsche-wirtschaft.de/unternehmen/rmw-wohnmoebel-gmbh-co-kg-rietberg/ - 'geschaetzter Umsatz 20 Mio EUR' (stima, senza esercizio) |  |
| Schmidt & Thürmer Holzhandlung, Säge- und Ho | dimensione | Campo inutilizzabile: fatturato dichiarato come «~5 Mio € (stima)» senza fonte né anno, e numero dipendenti superato. Il sito aziendale e Die Deutsche Wirtschaft indicano 130 dipendenti, non ~100. Con 130 addetti e 5 sedi un fatturato di 5 Mio € è im | https://die-deutsche-wirtschaft.de/unternehmen/schmidt-thuermer-holzhandlung-saege-und-hobelwerk-gmbh-co-kg-behrenhoff/ — «betreibt seit 30 Jahren ein | «~130 dipendenti (2024, Die Deutsche Wirtschaft / sito aziendale); fatturato non pubblicato (GmbH & Co. KG, nessun bilan |
| Schorn & Groh GmbH | dimensione | Campo privo di anno e di fatturato: «~80 MA (Creditreform); Umsatz n.d.». Il sito aziendale indica ~85 dipendenti. Nessun elemento consente di collocare l'azienda nella forbice 5-40 Mio €. Attenzione: alcuni aggregatori (RocketReach) riportano «14,2  | https://www.sg-veneers.com/unternehmen/ueber-uns.html — «in zweiter Generation geführt, beschäftigt rund 85 Mitarbeiter, seit mehreren Jahren PEFC- un | «~85 dipendenti (sito aziendale, 2025); fatturato non pubblicato — DA CONFERMARE su Bundesanzeiger (HRB 103479, AG Mannh |
| Weinheimer Leder GmbH | dimensione | Campo privo di qualsiasi elemento dimensionale verificabile ('Umsatz/MA n.d.'): non dichiara ne tipo di dato, ne fonte, ne anno. Impossibile collocare il lead nella forbice target 5-40 Mio EUR. | https://www.firmenwissen.de/az/firmeneintrag/69469/7170220020/WEINHEIMER_LEDER_GMBH.html (scheda Firmenauskunft, HRB 432889 Mannheim) - nessun fattura |  |
| Weinheimer Leder GmbH | dimensione | Struttura di gruppo non dichiarata: Weinheimer Leder GmbH e collegata a Das Lederband GmbH (Weinheim, HRB 724382), con Uwe Holubeck Geschäftsführer di entrambe; le fonti aperte non chiariscono il verso del controllo. L'azienda e inoltre nata nel 2003 | https://www.northdata.de/Das%20Lederband%20GmbH,%20Weinheim/Amtsgericht%20Mannheim%20HRB%20724382 - collegamento societario con Weinheimer Leder GmbH, |  |
| Wimmer Wohnkollektionen GmbH | dimensione | Il dato «~40 Mio € Umsatz, ~60 MA» è privo di anno: risale a una fonte del 2018 (8 anni fa). Inoltre 60 dipendenti per 40 Mio € è un rapporto anomalo, mentre LinkedIn indica oggi 51-200 dipendenti. Essendo il valore al limite superiore della forbice  | https://www.moebelindustrie.de/presse/2336/wimmer-wohnkollektionen-tritt-massivholzverband-bei.html — «Das Unternehmen produziert mit seinen 60 Mitarb | «~40 Mio € fatturato e ~60 dipendenti (2018, moebelindustrie.de) — dato da aggiornare» |
| Winter & Freis GmbH & Co. KG | dimensione | Campo privo di qualsiasi dato verificabile: «Umsatz/MA n.d.». Non è possibile stabilire se l'azienda rientri nella forbice 5-40 Mio €. Inoltre l'anno di fondazione indicato (1927) non coincide con le fonti aziendali, che riportano 1926. | https://holzkiste-palette.de/wir-sind-winter-freis/ — «1926 in Bayern gegründet ... seit über 90 Jahren in Familienbesitz, heute in dritter und vierte | «Impresa familiare fondata nel 1926, imballaggi in legno/casse da export; fatturato e dipendenti non pubblicati (GmbH &  |
| ecopell GmbH | dimensione | Campo privo di dato dimensionale ('Umsatz/MA n.d. (dal 1992)'). Le fonti disponibili indicano una micro-impresa: totale di bilancio 2023 pari a ~900 mila EUR (-20,1% sull'anno precedente), capitale sociale 265.000 EUR. E' quindi molto al di sotto del | https://implisense.com/en/companies/ecopell-gmbh-weitnau-seltmans-DE7L5HN3YI34 - 'last published balance sheet total of Ecopell GmbH in 2023 was 900k  | Totale di bilancio ~0,9 Mio EUR (2023, Bundesanzeiger via Implisense) - micro-impresa, fuori forbice target |

### Finlandia (11)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Aureskosken Jalostetehdas Oy | dimensione | Società appartenente a Tammisto-Yhtiöt (gruppo): il legame è già dichiarato nel campo, ma la compliance EUDR si decide a livello di capogruppo — lead da riqualificare sulla holding Tammisto (stesso CEO di Lapuan Saha). | https://www.asiakastieto.fi/yritykset/fi/aureskosken-jalostetehdas-oy/25116026/yleiskuva — frammento: "Aureskosken Jalostetehdas Oy ... kuuluu Tammist |  |
| CWP Coloured Wood Products Oy | dimensione | Fatturato 3,4 M€ (2024, in calo da 4,6 M€ 2022 e 4,1 M€ 2023): sotto la soglia minima tollerabile di 5 M€, senza che il campo lo segnali. | https://www.asiakastieto.fi/yritykset/fi/cwp-coloured-wood-products-oy/18959252/taloustiedot — frammento: "revenue was 3.4 million euros in 2024; 4.1  | Liikevaihto 3,4 M€ (2024) — FUORI FORBICE (sotto i 5 M€) |
| E J Hiipakka Oy | sito | Il sito ufficiale dell'azienda e' www.hiipakka.net (tutte le pagine yhteystiedot/henkilomme/tietosuojaseloste sono su quel dominio); ejh.fi risulta usato solo come dominio di posta. Il valore indicato nel campo 'sito' non e' il sito istituzionale. | https://www.hiipakka.net/kodin-kalusteet/yhteystiedot/ e https://investkurikka.fi/yrityshakemisto/e-j-hiipakka-oy/ — frammento: "Website: https://www. | https://www.hiipakka.net |
| Esan Levykaluste Oy | dimensione | Il campo segnala 'sotto sweet spot' ma il valore (3,62 M€; 3,7 M€ e 23 dip. nel 2025) e' sotto anche la soglia minima tollerabile di 5 M€: lead fuori forbice, non solo fuori sweet spot. Manca inoltre anno e fonte del dato riportato. | https://search.vainu.com/company/esan-levykaluste-oy-taloustiedot-ja-liikevaihto/FI04807872/yritystiedot — frammento: "The company's revenue was 3.7 m | Liikevaihto 3,7 M€ / 23 dip. (2025, Vainu) — FUORI FORBICE (sotto i 5 M€) |
| FM Timber Oy | dimensione | Il campo definisce il dato 'fascia alta, vicino al limite', ma 44 M€ e' gia' SOPRA il tetto di 40 M€ della forbice tollerabile (2025: 42,9 M€, 48 dip. — sempre fuori). Inoltre FM Timber e' capogruppo con tre stabilimenti (Pihtipudas, Pyhanta, Kiihtel | https://vainu.io/company/fm-timber-oy-taloustiedot-ja-liikevaihto/157555/yritystiedot e https://fmtimber.fi/konserni/ — frammento: "revenue was 44 MEU | Liikevaihto 42,9 M€ / 48 dip. (2025) — FUORI FORBICE (sopra i 40 M€); gruppo con 3 stabilimenti |
| I.S. Mäkinen Oy (MAKINEN) | email | Email assente ('n.d.'): il lead non e' contattabile via posta elettronica. Nessun indirizzo reperito nei frammenti pubblici consultati. | https://www.finder.fi/Laivasisustus/I+S+M%C3%A4kinen+Oy/Vanhalinna/yhteystiedot/138719 — la scheda contatti non espone un indirizzo email nei framment |  |
| I.S. Mäkinen Oy (MAKINEN) | filiera | Perimetro EUDR da verificare: l'attivita' principale (laivasisustus) e' allestimento/installazione di interni per navi da crociera, cioe' contract di installazione con pannelli e componenti acquistati gia' sul mercato UE. Non e' detto che l'azienda i | https://vainu.io/company/is-makinen-oy-taloustiedot-ja-liikevaihto/362542/yritystiedot — frammento: "the company operates in ship interior design... s |  |
| Jet-Puu Oy | email | Email assente ('n.d.'): lead non contattabile via posta elettronica. Esiste una pagina contatti pubblica (jet-puu.fi/en/contacts/) da cui estrarre un indirizzo, ma il dato non e' emerso nei frammenti. | https://www.jet-puu.fi/en/contacts/ — pagina contatti esistente; nessun indirizzo email nei frammenti di ricerca. DA CONFERMARE |  |
| Kensa Oy | email | Email assente ('n.d.'): lead non contattabile via posta elettronica. Nessun indirizzo emerso dai frammenti pubblici (Finder/Asiakastieto/Nordicnet). | https://www.finder.fi/Keitti%C3%B6kalusteet/Kensa+Oy/Himanka/yhteystiedot/3311123 — frammento con indirizzo e attivita' ("Targantie 9, 68100 Himanka.. |  |
| Kiilax Oy | dimensione | Il campo dichiara 'liikevaihto n.d.' ma il dato e' pubblicamente disponibile: 6,7 M€ nell'esercizio chiuso a 03/2025, utile 514 k€, 24 dipendenti, fatturato in calo del 6,8%. Valore al limite inferiore della forbice. | https://www.asiakastieto.fi/yritykset/fi/kiilax-oy/14857945/taloustiedot — frammento: "For the fiscal year ending in 2025/03, Kiilax Oy's revenue was  | Liikevaihto 6,7 M€ / 24 dip. (esercizio chiuso 03/2025, Asiakastieto) |
| Kiilax Oy | filiera | Descrizione parziale: l'attivita' principale e' la produzione di botole/portelli d'ispezione (tarkastusluukut) e il commercio specializzato di prodotti in compensato, non la produzione di compensato di betulla o di pannelli lamellari. Da riformulare  | https://vainu.io/company/kiilax-oy-taloustiedot-ja-liikevaihto/256569/yritystiedot — frammento: "Kiilax was founded in 1993 and manufactures inspectio | Legno/Arredo — botole d'ispezione e prodotti in compensato (produzione + rivendita specializzata) |

### Danimarca (36)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| ALL CREATIVE A/S | dimensione | Il campo non contiene alcun dato economico: non riporta ne' fatturato ne' bruttofortjeneste ne' anno di riferimento, ma solo una fascia di dipendenti '11-50' presa da LinkedIn e priva di data. La collocazione nella forbice target 5-40 M€ resta quindi | https://www.proff.dk/firma/all-creative-as/r%C3%B8dovre/producenter/GSG8C7I016D (scheda regnskab della societa', CVR 21124796) |  |
| BUCHS A/S | dimensione | Il campo non riporta alcun dato di bilancio verificato ma solo una stima ('fascia stimata 5-15 M€'). Il dato pubblicato e' il bruttofortjeneste: 14.746.681 DKK nel 2024 (16.092.571 DKK nel 2023), ~2,0 M€ di margine lordo, con 28 dipendenti. Con quest | https://www.krak.dk/buchs+as+randers+sv/67226095/firma - 'bruttofortjeneste 14.746.681 DKK i 2024, mod 16.092.571 DKK i 2023 ... 28 ansatte' | Bruttofortjeneste 14,75 mio DKK nel 2024 (~2,0 M€ di margine lordo), 28 dipendenti (krak.dk/proff.dk, CVR 29845646). Fat |
| CAFÉU DENMARK ApS | referente | Campo vuoto: il vertice e' pubblicato e coincide con il titolare della holding gia' citata nel campo dimensione. Steffan Noergaard Tobiesen e' fondatore e direktoer di CaféU Denmark ApS (capogruppo STEFFAN TOBIESEN HOLDING ApS). | https://cvrapi.dk/virksomhed/dk/cafeu-denmark-aps/33243537 e https://www.proff.dk/firma/caf%C3%A9u-denmark-aps/esbjerg-n/n%C3%A6rings-og-nydelsesmidle | Steffan Nørgård Tobiesen — Direktør (fondatore) |
| COPENHAGEN CHOCOLATE FACTORY ApS | email | L'email pubblicata come recapito ufficiale nelle condizioni di vendita e sulle schede societarie e' kundeservice@simplychocolate.dk (tel. +45 3634 0070). info@simplychocolate.dk, riportata nel foglio, non e' stata ritrovata letteralmente in nessuna f | https://www.simplychocolate.dk/pages/handelsbetingelser e https://www.proff.dk/firma/copenhagen-chocolate-factory-aps/kastrup/producenter/0JI778I016D  | kundeservice@simplychocolate.dk |
| Copenhagen Coffee Lab ApS | dimensione | Assetto proprietario non dichiarato: la societa' fa parte di un gruppo di 6 societa' con capogruppo Copenhagen Coffee Lab Holding ApS; il 70% e' stato rilevato dagli investitori danesi Steen Skallebaek e Ole Kristoffersen, mentre i fondatori Allan Kr | https://nordic9.com/news/steen-skallebk-and-ole-kristoffersen-acquire-70-of-copenhagen-coffee-lab-news8170860302/ - 'Steen Skallebaek and Ole Kristoff | Aggiungere: capogruppo Copenhagen Coffee Lab Holding ApS (gruppo di 6 societa'); 70% Steen Skallebæk e Ole Kristoffersen |
| DANSK KAFFE ApS | dimensione | Assetto proprietario non dichiarato: DANSK KAFFE ApS fa parte di un gruppo di 2 societa' con capogruppo KAFFEA ApS. Manca inoltre la data di costituzione (27.11.2013), utile a qualificare la micro-impresa. Corretta invece la segnalazione 'SOTTO IL TA | https://proff.dk/firma/dansk-kaffe-aps/odense-c/kaffe-og-te-agentur-og-engros/0EXL1KI0Z8T - 'CVR 25081544, Filosofgangen 9 5, 5000 Odense C, stiftet 2 | Aggiungere: capogruppo KAFFEA ApS (gruppo di 2 societa'), societa' costituita il 27.11.2013. Micro-impresa MOLTO SOTTO S |
| EMBALLAGEFABRIKKEN THY PAP | dimensione | Il campo e' 'n.d.'. La verifica mostra che si tratta di THY PAP, enkeltmandsvirksomhed (ditta individuale) con CVR 25352769, registrata in Morsoe Kommune (proff.dk la colloca a Nykoebing M) con unita' produttiva a Industrivej 19 B, 7700 Thisted. Una  | https://www.proff.dk/firma/thy-pap/nyk%C3%B8bing-m/producenter/GNWOAAI016D e https://estatistik.dk/virksomhed/thy-pap/25352769 - 'enkeltmandsvirksomhe | CVR 25352769 (THY PAP, enkeltmandsvirksomhed). Fatturato e addetti non pubblicati per forma giuridica; micro-impresa AMP |
| EMBALLAGEFABRIKKEN THY PAP | referente | DA CONFERMARE: il nome 'Carsten Boye Steen' come indehaver non e' stato ritrovato in nessuna fonte pubblica raggiungibile (proff, estatistik, degulesider, krak, sito aziendale). Trattandosi di ditta individuale il titolare e' il decisore unico: il da | Ricerche '"Thy Pap" "Carsten" indehaver ejer' e '"Thy Pap" Thisted CVR indehaver': nessun frammento riporta il nome del titolare; le fonti si fermano  |  |
| Estate Coffee Copenhagen A/S | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: il CVR 18179407 e' oggi registrato come Smage-Compagniet A/S, Holmevej 10, 5683 Haarby. La cronologia e' ricostruita dall'azienda stessa: fondata nei primi anni '90 (tra i fondatori Claus Meyer) come Chokolade  | https://smage-compagniet.dk/estate-coffee/ - 'Virksomhedens historie gaar tilbage til starten af 1990'erne, hvor den blev grundlagt af blandt andre Cl | Smage-Compagniet A/S (CVR 18179407) - gia' Estate Coffee Copenhagen A/S / Chokolade Compagniet |
| Estate Coffee Copenhagen A/S | dimensione | Dati di bilancio obsoleti di cinque anni: il campo cita 'bruttofortjeneste 10 mio DKK (bilancio 2021)' e '10-20 dipendenti', mentre le fonti aggiornate danno bruttofortjeneste 11 mio DKK nel 2023 e 15 mio DKK nel 2024 (~2,0 M€ di margine lordo) e una | https://www.proff.dk/firma/smage-compagniet-as/haarby/n%C3%A6rings-og-nydelsesmidler/GLOZ6AI116S - 'I 2023 viste regnskabet en bruttofortjeneste paa 1 | Bruttofortjeneste 15 mio DKK nel 2024 (~2,0 M€ di margine lordo; 11 mio DKK nel 2023), 20-50 dipendenti; fatturato non p |
| H. EMBALLAGE ApS | dimensione | Il campo scrive 'ricavi/margine lordo dichiarati 9,211 mio DKK' senza dichiarare di quale dato si tratti: per una ApS il bilancio in forma ridotta pubblica il bruttofortjeneste, non il fatturato. La formula ambigua rende non interpretabile il dato (9 | https://www.proff.dk/firma/h.-emballage-aps/glamsbjerg/producenter/GWNSLZI016D - CVR 38528742, 'Papirvarefabrikker og kartonnagefabrikker', Hoejrupvej | Bruttofortjeneste 9,211 mio DKK (~1,2 M€ di margine lordo), 21 dipendenti; fatturato non pubblicato (ApS, bilancio in fo |
| IKAST ETIKET A/S | referente | Il campo e' vuoto e il campo dimensione afferma che 'nessun adm. direktoer pubblicato': e' falso. Ulrik Lauritsen risulta direktoer della societa' dal 2003 (oltre che membro del consiglio). | https://www.proff.dk/firma/ikast-etiket-as/ikast/engroshandel-annet/GJF022I10N6 - 'Ikast Etiket A/S blev grundlagt i 1986 og har vaeret ledet af Ulrik | Ulrik Lauritsen — Direktør |
| IKAST ETIKET A/S | dimensione | Dati non allineati alle fonti: il campo riporta 'risultato netto 7,62 mio DKK' e 12 dipendenti, mentre il bilancio 2024 pubblicato indica un bruttofortjeneste di 16 mio DKK e 14 dipendenti. Non e' inoltre dichiarata la capogruppo UL HOLDING IKAST ApS | https://www.proff.dk/firma/ikast-etiket-as/ikast/engroshandel-annet/GJF022I10N6 - 'I 2024 viste regnskabet en bruttofortjeneste paa 16 mio. DKK ... 14 | Bruttofortjeneste 16 mio DKK nel 2024 (~2,1 M€ di margine lordo), 14 dipendenti; fatturato non pubblicato. Capogruppo UL |
| INNOVATION LIVING A/S (già Innovation Rander | dimensione | Dato obsoleto: il campo cita il bruttofortjeneste 2023 (47,3 M DKK) mentre l'ultimo bilancio disponibile (2025) riporta 40 M DKK, quindi in calo. Anche la composizione del gruppo è imprecisa: INNOVATION HOLDING A/S conta 10 società, non 8. | https://www.proff.dk/firma/innovation-living-as/randers-n%C3%B8/m%C3%B8bler/13462KI015G — frammento: "In 2025, the company reported a gross profit of  | Bruttofortjeneste 40 mio DKK (~5,4 M€) nel 2025 (proff.dk, CVR 65699516); fatturato non pubblicato; gruppo INNOVATION HO |
| JKE DESIGN A/S | dimensione | Dato obsoleto: il campo riporta il bruttofortjeneste 2023 (55,6 M DKK) mentre il bilancio 2024 depositato indica 50 M DKK, in ulteriore calo rispetto al 2022 (58,7 M DKK). La stima ricavi "~20-27 M€" resta non verificata. | https://regnskaber.cvrapi.dk/21017236/ (Årsrapport 2024 JKE DESIGN A/S, Gl Klæstrupvej 75, 9740 Jerslev J) — frammento: "In 2024, the company showed a | Bruttofortjeneste 50 mio DKK (~6,7 M€) nel 2024 (årsrapport 2024, CVR 63271012); fatturato non pubblicato |
| JOHNSEN GRAPHIC SOLUTIONS A/S (oggi anche Jo | referente | Campo vuoto: il vertice e' pubblicato. Steen Johnsen risulta adm. direktoer del CVR 18624141 (Sune Johnsen co-direttore; Peter Bager presidente del consiglio). | https://cvrapi.dk/virksomhed/dk/johnsen-graphic-solutions-as/18624141 - 'CVR: 18624141, adm. dir: Steen Johnsen'; proff.dk roller: 'Steen Johnsen og S | Steen Johnsen — Adm. direktør |
| JOHNSEN GRAPHIC SOLUTIONS A/S (oggi anche Jo | dimensione | Numero di addetti superato (92 contro 111 nel 2024) e stima di fatturato '10-20 M€' priva di fonte, mentre il dato pubblicato e' disponibile: bruttofortjeneste 51 mio DKK nel 2024 (~6,8 M€ di margine lordo). | https://www.proff.dk/firma/johnsen-print-digital-media-as/grenaa/b%C3%B8ger-aviser-og-blader-engros/GLGJZEI10MF - 'I 2024 viste regnskabet en bruttofo | 111 dipendenti (2024); bruttofortjeneste 51 mio DKK 2024 (~6,8 M€ di margine lordo); fatturato non pubblicato. Capogrupp |
| Just Coffee | denominazione | Ragione sociale CVR ora VERIFICATA: non e' ne' ApS ne' A/S ne' amba, e' un INTERESSENTSKAB. Denominazione legale 'Just Coffee I/S', CVR 35492380, costituita il 01-01-2014, sede Frederiksborgvej 551, 4000 Roskilde; soci illimitatamente responsabili Ma | https://cvrapi.dk/virksomhed/dk/just-coffee-is/35492380 e https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Just Coffee I/ | Just Coffee I/S - CVR 35492380 (forma giuridica: interessentskab) |
| KLS PUREPRINT A/S | dimensione | Il legame di gruppo e' dichiarato correttamente ma va aggiornato e pesato come criterio di esclusione del lead: F. E. Bording A/S ha rilevato la quota di Knud Erik Larsen a fine 2024/inizio 2025, per cui KLS PurePrint e' oggi controllata integralment | https://signprintpack.dk/2025/01/06/bording-oger-ejerandelen-af-kls-pureprint-og-knud-erik-larsen-takker-af/ - 'Bording koeber Knud Erik Larsen ud af  | Controllata (oggi integralmente) di F. E. BORDING A/S dopo il riacquisto della quota di Knud Erik Larsen a fine 2024. Le |
| KRYDSFINER-HANDELEN A/S | dimensione | Controllata di gruppo estero: dall'autunno 2023 la societa' e' stata venduta da Carsten Rittig a Fritzoe Nordic Holding AS (Norvegia), che ne detiene il controllo. Il record lo accenna in forma dubitativa ('riconducibile a proprieta' nordica/scandina | https://fritzoenordic.no/en/selskap/krydsfiner-handelen-a-s/ ; https://www.wood-supply.dk/article/view/1053393/nordmaend_kober_95_ar_gammelt_dansk_fam | Dichiarare in modo esplicito: controllata al 100% da Fritzoe Nordic Holding AS (NO) dall'autunno 2023 |
| KVIST INDUSTRIES A/S | dimensione | Assetto proprietario non dichiarato: la societa' figura nel portafoglio del fondo di private equity danese Dansk Ejerkapital ed e' controllata tramite KVIST HOLDING A/S (CVR 21746886, Esbjerg). Il campo dimensione non menziona il legame di gruppo/par | https://www.danskejerkapital.dk/portefoelje/kvist-industries/ ; https://www.proff.dk/firma/kvist-industries-as/esbjerg/hovedkontortjenester/GMGAWAI10N | Aggiungere: controllata da KVIST HOLDING A/S, partecipata dal fondo Dansk Ejerkapital; fatturato non pubblicato (bilanci |
| LILLEHEDEN A/S | dimensione | Controllata di gruppo: la societa' fa parte di Nordic Wood Industries A/S (CVR 37385603), che dal 12.05.2025 ha un nuovo adm. direktor di gruppo (Holger Carsten Hansen). Il legame e' gia' correttamente dichiarato nel campo, quindi non e' un errore di | https://nowi.dk/limtraesproducent-styrker-produktionen-markant/ ; https://www.proff.dk/firma/nordic-wood-industries-as/hampen/investeringsselskaper/0M | Aggiornare il bruttofortjeneste all'ultimo esercizio disponibile e valutare il lead a livello di Nordic Wood Industries  |
| MULTIFORM A/S | dimensione | Controllata di gruppo: capogruppo BALLINGSLOV INTERNATIONAL DANMARK A/S (gruppo svedese Ballingslov International / Stena Adactum). Il legame e' gia' dichiarato correttamente nel record, quindi il rilievo riguarda la validita' del lead (compliance EU | https://www.proff.dk/firma/multiform-as/kib%C3%A6k/producenter/GLGFCDI016D - 'Multiform er en del af en koncern, hvor modervirksomheden er BALLINGSLOV |  |
| NPI (Nordic Panel Import) | referente | Campo referente vuoto pur essendo il direktor reperibile nelle fonti pubbliche: risulta Theis Graves Larsen (uno dei due fondatori, 2002). | https://www.proff.dk/firma/npi-as/l%C3%B8sning/t%C3%B8mmer-tr%C3%A6last-og-byggevarer-agentur-og-engros/0MA0H6I10LA - direktor: Theis Graves Larsen ;  | Theis Graves Larsen, Direktor (da riconfermare al primo contatto) |
| ODENSE SEGLMÆRKEFABRIK A/S | sito | Il dominio segl.dk non e' piu' il sito operativo: i contenuti sono confluiti su ogn.dk (Optimum Group Nordic), che ospita la pagina di contatto dedicata 'Kontakt_OdenseSeglmaerke'. Di conseguenza anche l'email um@segl.dk va riconfermata sulla nuova p | https://www.ogn.dk/kontaktodenseseglmaerke - pagina 'Kontakt_OdenseSeglmaerke' di Optimum Group Nordic | https://www.ogn.dk/ (pagina contatti: https://www.ogn.dk/kontaktodenseseglmaerke) |
| SCANLUX PACKAGING A/S | dimensione | Dato di bilancio obsoleto (esercizio 2023, oltre tre anni) e numero di addetti lasciato indeterminato ('28-38, fonti divergenti'). Si chiude invece il dubbio di perimetro sollevato nel campo: Scanlux e' certificata FSC (C126290) e la gamma e' prevale | https://scanlux-packaging.com/sustainability-at-scanlux/ - 'FSC certified (C126290)'; https://scanlux-packaging.com/ - 'gift paper, boxes, ribbons, wi | Aggiornare al bilancio piu' recente disponibile e fissare il numero di addetti; confermato il perimetro EUDR (carta/cart |
| SIKA DESIGN A/S | dimensione | Dato di bilancio obsoleto: l'utile lordo di 29 M DKK e' riferito al 2021 (cinque esercizi fa) e la stima ricavi '~8-10 M€' non e' verificata. Anche il numero di addetti e' disallineato: le fonti aggiornate riportano 19 dipendenti / 17 FTE a novembre  | https://www.paqle.dk/p/sika-design-a-s/330977 (19 ansatte, 17 FTE nov. 2025) ; https://ownr.dk/companies/public-profile/31476712 | Aggiornare bruttofortjeneste e addetti all'ultimo bilancio disponibile |
| SKJERN PAPER A/S (già Skjern Papirfabrik A/S | referente | Il nome e la data sono corretti (Nikolaj Bjerre Thybo, adm. direktoer dal 2020) ma, essendo la societa' controllata da Sonoco dal 2022, il referente non e' il decisore finale sulla compliance EUDR. Segnalato per coerenza con il rilievo sull'assetto p | https://dbrs.dk/artikel/skjern-paper-ny-direktør-overtager-en-solid-grøn-virksomhed e https://www.tvmidtvest.dk/fast-arbejde/papirfabrikken-i-skjern-l |  |
| SOFTLINE A/S | dimensione | Dato di margine lordo riferito al 2023 e stima ricavi '~12-18 M€' non verificata: la collocazione nella forbice target 5-40 M€ resta non dimostrata. DA CONFERMARE su bilancio piu' recente. Referente Finn Herluf Sorensen e stato 'Normal' della societa | https://ownr.dk/companies/public-profile/27266355 (status Normal) ; https://folketidende.dk/erhverv/produktudvikling-er-krumtappen-hos-softline-a-s (' |  |
| SOMMER-SAVEX A/S | dimensione | Il campo dichiara 'fatturato non verificato / dati di bilancio non accessibili', ma i dati esistono e sono pubblici: bruttofortjeneste 13,06 M DKK nel 2024 (~1,75 M€) contro 14,82 M DKK nel 2023, con esercizio 2024-25 chiuso in perdita (-1,37 M DKK). | https://ownr.dk/companies/public-profile/13923795 ; https://vismarating.dk/firma/13923795-sommer-savex-as - 'bruttofortjeneste i 2024 pa 13.059.301 DK | Bruttofortjeneste 13,06 M DKK (2024, ~1,75 M€), risultato 2024-25 negativo; fatturato non pubblicato (classe B). Taglia  |
| STIBO COMPLETE A/S (già Rosendahls A/S - Pri | dimensione | Il dato '150 dipendenti; fatturato ~200 mio DKK' e' privo di anno e di fonte verificabile ed e' smentito dalle fonti: paqle classifica Stibo Complete A/S nella fascia 200-500 dipendenti e l'esercizio 2025 (chiusura 30 aprile) e' stato in perdita per  | https://www.paqle.dk/p/stibo-complete-a-s/182143 - 'Stibo Complete A/S · 200-500 ansatte'; https://www.proff.dk/firma/stibo-complete-as/horsens/tryker | 200-500 dipendenti (paqle 2025); esercizio 2025 (1.5.2024-30.4.2025) chiuso con perdita di 33,5 mio DKK; fatturato non p |
| STIBO COMPLETE A/S (già Rosendahls A/S - Pri | sede | La sede legale del CVR 37120928 e' Saturnvej 65, 8700 Horsens; Esbjerg N (Lammefjordsvej 2) e' una delle unita' operative, come Soeborg. Il campo indica solo Esbjerg N. Inoltre l'URL in 'fonte' punta ancora alla scheda proff della denominazione super | https://virmo.dk/firma/37120928-stibo-complete-as - 'Stibo Complete A/S (37120928) - Saturnvej 65, 8700 Horsens'; schede proff.dk distinte per Esbjerg | Sede legale: Horsens (Saturnvej 65, Midtjylland); unita' operative a Esbjerg N e Søborg. Fonte da aggiornare a https://w |
| Skagerak Denmark A/S | dimensione | Dati economici obsoleti: utile lordo 53,7 M DKK riferito al 2021 e addetti al dicembre 2022, cioe' antecedenti o coevi all'acquisizione da parte di Fritz Hansen. La stima ricavi '~15-22 M€' non e' verificata e non e' piu' rappresentativa dell'assetto | https://estatistik.dk/virksomhed/skagerak-denmark-as/28855990 ; https://www.dezeen.com/2021/12/15/fritz-hansen-acquires-skagerak/ |  |
| SØRENSEN LÆDER A/S (Sorensen Leather) | dimensione | Dato obsoleto e non allineato alla fonte: il record indica bruttofortjeneste 23,85 mio DKK (2022) e ca. 20 dipendenti, mentre la scheda proff.dk attuale (CVR 50828514) riporta bruttofortjeneste 13.056 tkr (13,06 mio DKK ≈ 1,75 M€) e 16 dipendenti. In | https://www.proff.dk/regnskab/s%C3%B8rensen-l%C3%A6der-as/lystrup/skind-l%C3%A6der-og-pels/GKJEN4I07RD — frammento: "Bruttofortjeneste: 13.056 tkr ... | Bruttofortjeneste 13,06 mio DKK (~1,75 M€) e 16 dipendenti — proff.dk, CVR 50828514 (ultimo bilancio disponibile); fattu |
| TJOERNEHOEJ MOELLE A/S | dimensione | Fatturato recente NON reperito: il dato del foglio resta quello del 2003 (80 M DKK). In 3 ricerche l'unico bilancio individuato e' il PDF dell'esercizio 2011 su regnskaber.cvrapi.dk e menzioni di dati fino al 2014; nessuna cifra 2023-2025 emerge dall | https://regnskaber.cvrapi.dk/21057143/Y3ZyLmRrOi8vcGRmcy8zNDE3NTAxMjtBL1M1MDg2MTsyMDExMDEwMTsyMDExMTIzMTtSO1I.pdf - bilancio 01-01-2011/31-12-2011; ht |  |
| VESTJYSK SPECIALFODER ApS | filiera | Perimetro EUDR DA CONFERMARE: l'oggetto sociale registrato e' generico ('handelsvirksomhed inden for specialfoder'), classificato proff.dk come 'engroshandel - annet'. Nessuna fonte pubblica conferma l'impiego di soia (unica commodity EUDR plausibile | https://royalfireworks.dk/forhandler/vestjysk-specialfoder-aps/ - scheda rivenditore fuochi d'artificio a Vemb; https://www.proff.dk/firma/vestjysk-sp |  |

### Svezia (28)

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
| Horreds Möbel Aktiebolag | dimensione | Dato di fatturato obsoleto (esercizio 2022, 103 MSEK). L'ultimo bilancio disponibile su allabolag/bolagsfakta indica 93 384 KSEK = 93,4 MSEK ≈ 8,3 M€ (2023, -9,7%) e ~92,9 MSEK nell'ultimo esercizio, con 50 dipendenti. L'azienda resta dentro la fasci | https://www.bolagsfakta.se/5563651974-Horreds_Mobel_Aktiebolag — «Horreds Möbel Aktiebolag had a turnover of 93,384 KSEK in 2023 ... revenue decline o | Fatturato 93 384 KSEK = 93,4 MSEK ≈ 8,3 M€ (2023, -9,7%); 50 dipendenti; org.nr 556365-1974 – fonte allabolag.se/bolagsf |
| Horreds Möbel Aktiebolag | dimensione | Legame di gruppo indicato solo genericamente («Fa parte di un gruppo di 3 società») senza nominare la capogruppo. Allabolag indica Horreds Holding AB come società madre e Horreds Möbel Utvecklings AB (org.nr 559016-3324) come capogruppo del gruppo. R | https://www.allabolag.se/5563651974/koncern — «Horreds Möbel AB is part of a group with 3 companies, where Horreds Holding AB is the parent company an | Aggiungere: capogruppo Horreds Holding AB / Horreds Möbel Utvecklings AB (org.nr 559016-3324), gruppo di 3 società |
| Kvänum Kök AB | dimensione | Controllata di gruppo: capogruppo Vedena AB, gruppo di 5 società con 350 dipendenti e 1 135,0 MSEK di fatturato. Il legame è già dichiarato correttamente nel foglio, ma la decisione di compliance EUDR si prende a livello Vedena AB: si tratta di una q | https://www.allabolag.se/foretag/kv%C3%A4num-k%C3%B6k-ab/kv%C3%A4num/m%C3%B6bler/2JZHGJBI5YGJV — «Kvänum Kök Aktiebolag is a subsidiary that is part o |  |
| Kvänum Kök AB | dimensione | Numero di dipendenti discordante: il foglio riporta 127 dipendenti, mentre allabolag/bolagsfakta registrano 0 dipendenti sull'ultimo esercizio a fronte di 297 420 KSEK di fatturato (2025). Verosimilmente il personale è impiegato in altra società del  | https://www.bolagsfakta.se/5562023159-Kvanum_Kok_Aktiebolag — «Kvänum Kök Aktiebolag had 0 employees and achieved a result of 6,307 KSEK with revenue  |  |
| Lammhults Möbel Aktiebolag | referente | Beatrice Kortner Henriksson è stata nominata VD ad interim (tillförordnad) dopo l'uscita di Åsa van Drumpt dal gruppo il 17 giugno 2024, arrivando dalla posizione di CSO di Lammhults Design Group. Allabolag la riporta tuttora come VD, ma la natura in | https://lammhultsdesigngroup.com/tidings/forandringar-i-vd-positionen-i-lammhults-mobel-ab/ ; https://www.allabolag.se/5560582602/lammhults-mobel-akti |  |
| Lammhults Möbel Aktiebolag | dimensione | Controllata del gruppo quotato Lammhults Design Group AB: legame già dichiarato correttamente nel foglio, ma il lead è una controllata di gruppo quotato e la compliance EUDR si decide a livello di capogruppo (questione di selezione del lead). Dati 20 | https://www.bolagsfakta.se/5560582602-Lammhults_Mobel_Aktiebolag — «For the full year 2024, Lammhults Möbel Aktiebolag had 41 employees and achieved a |  |
| Lars Carlsson Trävaru Aktiebolag | referente | Referente e ruolo assenti: il record non è contattabile a livello nominativo. Allabolag indica Anders Carlsson come styrelseordförande e Olof Carlsson come styrelseledamot; non risulta un VD registrato distinto. Dati dimensionali confermati (70 552 K | https://www.allabolag.se/foretag/lars-carlsson-tr%C3%A4varu-aktiebolag/%C3%A4lmeboda/s%C3%A5gverk/2JYU2DYI5YHTM — «14 employees ... omsättning of 70,5 | Anders Carlsson – styrelseordförande (DA CONFERMARE l'esistenza di un VD) |
| N K Lundströms Trävaror Aktiebolag | dimensione | Controllata di gruppo: capogruppo KGL Trä Aktiebolag, gruppo di 2 società con 34 dipendenti e 203,0 MSEK di fatturato. Il legame è già dichiarato correttamente nel foglio; resta una questione di selezione del lead, perché la decisione EUDR si prende  | https://www.allabolag.se/5561078154/n-k-lundstroms-travaror-aktiebolag — «N K Lundströms Trävaror Aktiebolag is part of a group with a total of 2 comp |  |
| Nordanå Trä Aktiebolag | dimensione | Legame di gruppo dichiarato (controllata di Green Wood Sverige AB) e confermato da allabolag, ma Ratsit riporta l'azienda come NON appartenente ad alcun koncern: informazione discordante fra le fonti, da riconfermare. In ogni caso, se il controllo Gr | https://www.allabolag.se/organisation/nordan%C3%A5-tr%C3%A4-aktiebolag/alfta/s%C3%A5gverk/2JZ2XUFI5YHTM — «Allabolag indicates that the parent company |  |
| Nordanå Trä Aktiebolag | dimensione | Il dato 2025 (117 660/117,7 MSEK ≈ 10,4 M€) è confermato ma è in calo del 52% sull'esercizio precedente, con un risultato di 40,7 MSEK sproporzionato rispetto al fatturato: forte indizio di esercizio di durata anomala o di operazione straordinaria (c | https://www.allabolag.se/bokslut/nordan%C3%A5-tr%C3%A4-aktiebolag/alfta/s%C3%A5gverk/2JZ2XUFI5YHTM — «Under 2025 the company had a turnover of 117.7 M |  |
| Nydala Trävaru Aktiebolag | dimensione | Dato di fatturato fermo all'esercizio 2023 (323 425 KSEK ≈ 28,6 M€, 41 dipendenti), mentre l'årsredovisning 2024 risulta già depositata e disponibile su allabolag. Il valore va aggiornato: l'azienda è sulla fascia alta del range tollerabile e un'ulte | https://www.allabolag.se/5560752825/bokslut — «Nydala Trävaru Aktiebolag had 41 employees and made a result of 14,794 KSEK with a turnover of 323,425  |  |
| Rörvikshus Sweden AB | dimensione | Controllata di gruppo: capogruppo Munio Sweden Aktiebolag (org.nr 556509-3449), gruppo di 4 società con 52 dipendenti e 229,0 MSEK di fatturato. Legame già dichiarato correttamente nel foglio: resta una questione di selezione del lead, perché la deci | https://www.bolagsfakta.se/5566220926-Rorvikshus_Sweden_AB — «Rörvikshus Sweden AB had 49 employees and achieved a result of 1,195 KSEK with a turnove | Fatturato 154 918 KSEK ≈ 13,7 M€ (2024, -30,8%); 49 dipendenti; capogruppo Munio Sweden Aktiebolag (gruppo di 4 società, |
| Sjöbergs Workbenches AB | dimensione | Il legame di gruppo è dichiarato (capogruppo Idun Woodcraft AB, acquisizione 2018) ma ne è sottostimata la portata: allabolag indica che l'azienda appartiene a un gruppo di 74 società facente capo a Idun Woodcraft AB (piattaforma legno del gruppo ind | https://www.allabolag.se/organisation/sj%C3%B6bergs-workbenches-ab/stockaryd/tr%C3%A4varor-produktion/2JYSCQ9I63IL3 — «Sjöbergs Workbenches AB is part | Aggiungere: gruppo Idun Woodcraft AB, 74 società (gruppo Idun) |

### Olanda (50)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Arco Meubelfabriek B.V. | referente | Referente da riconfermare: le fonti pubbliche indicano Jorre van Ast alla guida dell'azienda familiare dal 2011 come creative director, affiancato dal managing director Jan Tichelaar. 'F. van Ast' risulta solo dal dato Company.info (algemeen directeu | https://www.vno-ncw.nl/forum/meubelfabriek-arco-120-jaar-vallen-opstaan-en-weer-doorgaan - frammento: 'In 2011 kwam het familiebedrijf onder leiding v |  |
| Ascot Amsterdam B.V. | referente | Referente e ruolo assenti: risulta pubblicamente Merijn Bruinse come Managing Director di Ascot Amsterdam B.V. | https://rocketreach.co/merijn-bruinse-email_50707800 - 'Merijn Bruinse ... Ascot Amsterdam BV Managing Director' | Merijn Bruinse - Managing Director (da riconfermare su fonte KVK) |
| Ascot Amsterdam B.V. | dimensione | Dipendenza estera dichiarata ma sostanziale: Ascot Amsterdam e l'ufficio vendite della Cocoa Abrabopa Association (cooperativa ghanese). La decisione di compliance EUDR e il potere d'acquisto stanno in Ghana, non ad Amsterdam: lead da riqualificare. | https://ascot-amsterdam.com/sales-office/ - 'Ascot Amsterdam \| Sales Office Cocoa Abrabopa Association Ghana' |  |
| BeBo Parket B.V. | dimensione | Assetto proprietario incompleto: dal 2022 l'azienda e' partecipata dall'investitore Nobel Capital Partners insieme al management di seconda generazione. La partecipazione di private equity non e' dichiarata nel campo (solo il legame con BeBo Groep B. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'samen met investeerder Nobel Capital Partners' |  |
| BeBo Parket B.V. | dimensione | Il fatturato di ca. 20 M EUR e' datato 2024 nel record, ma il dato di 20 milioni compare nell'articolo sul passaggio generazionale del 2022 (riferito all'esercizio precedente). Anno del dato DA CONFERMARE. | https://www.vloerenbusiness.nl/vloerenspecialist-bebo-overgenomen-door-tweede-generatie/ - frammento: 'Vorig jaar had Bebo Parket een omzet van 20 mil |  |
| BeBo Parket B.V. | linkedin | Il link LinkedIn e' il profilo personale di Frans Bolier (nl.linkedin.com/in/frans-bolier-b64b394a), non la pagina aziendale di BeBo Parket. Trattandosi di un ex titolare uscito nel 2022, il link non e' utilizzabile. | https://nl.linkedin.com/in/frans-bolier-b64b394a - titolo: 'Frans Bolier - directeur mede-eigenaar beboparket BV' |  |
| Beijleveld Houtimport B.V. | referente | Referente e ruolo assenti: il direttore statutario e' la persona giuridica Beyleveld Groep B.V. e nelle fonti aperte non emerge alcun nome fisico. Senza referente il lead non e' azionabile. DA CONFERMARE. | https://www.transfirm.nl/nl/organisatie/24136531-000016457986-beijleveld-houtimport-b.v. e https://drimble.nl/bedrijf/rotterdam/16457986/beijleveld-ho |  |
| Bruns B.V. | email | Il campo email riporta 'n.d.' ma esiste una casella nominativa pubblica del direttore: jan.burgmans@bruns.nl. Il record e' quindi ingiustificatamente privo di recapito operativo. | http://bergeijk.gevabiz.nl/company/bruns-bv-bergeijk.html - frammento: 'Managing director Jan Burgmans, e-mail: jan.burgmans@bruns.nl' | jan.burgmans@bruns.nl |
| CocoaSupply B.V. | dimensione | Nessun dato dimensionale verificabile: fatturato, dipendenti e numero KVK restano non reperiti anche dopo ricerca mirata. Il record non permette di collocare l'azienda nella forbice 5-40 M€. DA CONFERMARE. | https://cocoasupply.eu/pages/contact-us - la pagina contatti pubblica indirizzo (van Nelleweg 1, unit 1.H8A, 3044 BC Rotterdam), telefono +31 10 20057 |  |
| CocoaSupply B.V. | sito | Rischio di confusione con omonima estera: esiste cocoasupply.com (Cocoa Supply, gruppo con base in Ecuador/USA) accanto al cocoasupply.eu della B.V. olandese. Il dominio .eu usato nel record e quello corretto, ma la relazione fra le due entita va chi | https://cocoasupply.com/about-us/ - 'Empowering Direct Trade: CocoaSupply's Commitment...' (sito distinto da https://cocoasupply.eu/) |  |
| Daarnhouwer & Co B.V. | email | Email indicata come 'n.d.' mentre sono pubblicate caselle attive: cocoa@daarnhouwer.nl (reparto cacao) e caselle nominative @daarnhouwer.nl. Nota: le e-mail sono sul dominio .nl mentre il sito e .com. | https://daarnhouwer.com/cocoa/ - 'cocoa@daarnhouwer.nl'; contatto alternativo 'W.VANGINKEL@DAARNHOUWER.NL' | cocoa@daarnhouwer.nl |
| Daarnhouwer & Co B.V. | referente | Referente e ruolo assenti. Il sito pubblica una pagina 'Meet our team' ma nessuna fonte consultata identifica il directeur statutario. DA CONFERMARE. | https://daarnhouwer.com/cocoa-stories/meet-our-team/ - pagina team pubblicata, nessun ruolo di directeur esplicitato nei frammenti |  |
| De Leeuw Huidenhandel N.V. | referente | Referente e ruolo assenti. Il direttore statutario iscritto al KVK e' una persona giuridica (LHST B.V., algemeen directeur dal 2022): manca un nome fisico per il contatto commerciale. Nei frammenti pubblici compare solo Christian Hossu (chossu@deleeu | https://companyinfo.nl/organisatieprofiel/groothandel-in-huiden-en-vellen/de-leeuw-huidenhandel-n-v-winterswijk-08011164-000017531705 - frammento: 'LH |  |
| Dietz Cacao Trading B.V. | ruolo | Il referente indicato non e il vertice statutario: Jordy Kuijpers e Sales Director (sales & purchase), non directeur/bestuurder della B.V. Per un contatto di compliance EUDR serve il directeur statutario, non reperito nelle fonti pubbliche consultate | https://rocketreach.co/jordy-kuijpers-email_222834060 - 'Jordy Kuijpers ... DIETZ CACAO TRADING Sales Director'; https://nl.linkedin.com/in/jcjkuijper |  |
| Facta International B.V. | referente | Referente da riconfermare: Ben Dekker risulta effettivamente Director di Facta International BV, ma la scheda FCC/Kompass indica come MD/Chief Operating Officer il sig. A.A. Molenaar. Va chiarito chi sia il bestuurder statutario prima del contatto. | https://gb.kompass.com/c/facta-international-b-v/nl507577/ - 'Mr A.A. Molenaar - MD/Chief Operating Officer'; https://www.linkedin.com/in/ben-dekker-9 |  |
| Facta International B.V. | email | Email indicata come 'n.d.' mentre e pubblicata una casella nominativa attiva sul dominio aziendale: a.molenaar@facta-international.com. Il lead e quindi contattabile. | https://gb.kompass.com/c/facta-international-b-v/nl507577/ - 'a.molenaar@facta-international.com'; telefono +31 (0)75 681 80 40 | a.molenaar@facta-international.com |
| GWW Houtimport B.V. | dimensione | Controllata di gruppo: dal 01/01/2026 GWW Houtimport, GWW Agency e Van den Berg Hardhout confluiscono nella holding Van den Berg Houtgroep. Il legame e' gia' dichiarato correttamente nel campo, ma la compliance EUDR si decidera' a livello di capogrup | https://www.houtwereld.nl/nieuws/van-den-berg-en-gww-houtimport-gaan-samen/ - frammento: 'GWW Houtimport, GWW Agency en Van den Berg Hardhout uit Lopi |  |
| GWW Houtimport B.V. | dimensione | Il campo cita 'Secondo direttore citato: John Hoogendoorn': non trova riscontro. Il comunicato di riorganizzazione indica Arjan de Jong come algemeen directeur (confermato) e Bart van Meuwen come commercieel directeur; Albert Oudenaarden passa agli a | https://www.houtwereld.nl/nieuws/van-den-berg-en-gww-houtimport-gaan-samen/ - frammento: 'Arjan de Jong is benoemd tot algemeen directeur en Bart van  | Bart van Meuwen - commercieel directeur |
| Gaia Cacao B.V. | sede | Sede incoerente: il record indica Amsterdam / Duivendrecht (Noord-Holland), ma il registro riporta anche Gaia Cacao B.V. a Nieuwegein (Utrecht) sotto lo stesso KVK 78049636. Possibile trasferimento di sede non recepito. | https://www.northdata.com/Gaia%20Cacao%20B%C2%B7V%C2%B7,%20Nieuwegein/KVK%2078049636 - 'Gaia Cacao B.V., Nieuwegein, Netherlands - KVK 78049636' |  |
| Gaia Cacao B.V. | referente | Referente e ruolo assenti; nessuna fonte pubblica accessibile via ricerca identifica il directeur/bestuurder. DA CONFERMARE. | https://us.kompass.com/c/gaia-cacao-b-v/nlc0730826/ - profilo societario senza indicazione di dirigenti |  |
| Hardhouthandel Hotim B.V. | dimensione | Il campo dichiara 'n. KVK non reperito': il numero risulta invece pubblicato. Creditsafe riporta per Hotim B.V. il KvK-nummer 17051960. Da riconciliare con la denominazione esatta iscritta (Hotim B.V. / Hardhouthandel Hotim B.V.). | https://www.creditsafe.com/business-index/en-us/company/hotim-bv-nl00776206 - frammento: 'Hotim B.V. has KvK-nummer: 17051960' | KVK 17051960 (da riconciliare con la ragione sociale esatta) |
| Hardhouthandel Hotim B.V. | referente | Referente e ruolo assenti; nelle fonti aperte consultate non emerge il nome del directeur/eigenaar. DA CONFERMARE. | https://www.hotim.nl/contact/ (pubblica solo verkoop@hotim.nl e tel. 013 514 24 44, nessun nome) |  |
| Houthandel Jos Dennebos B.V. | dimensione | Il numero di dipendenti e' lasciato discordante (20-49 vs 2-5). La fonte aziendale scioglie il dubbio: circa 30 addetti nella produzione di pavimenti in legno a Raalte. Il record va aggiornato. | https://www.dennebosflooring.com/en/about-us/ - frammento: 'About 30 employees produce their wooden floors for various clients, both in and outside Eu | ca. 30 dipendenti (fonte dennebosflooring.com, 2025) |
| Houthandel Jos Dennebos B.V. | referente | Referente e ruolo assenti. Il socio unico e' la persona giuridica Jos Dennebos Exploitatie B.V.; il fondatore storico e' Jos Dennebos (attivo anche in Dennebos Suriname). Nome e carica del directeur attuale DA CONFERMARE. | https://companyinfo.nl/organisatieprofiel/groothandel-in-hout-en-plaatmateriaal/houthandel-jos-dennebos-b-v-raalte-05073894-000016548884 e https://www |  |
| Houtimport Reuver B.V. | dimensione | Anno di fondazione errato: il record indica 1987, ma l'azienda e' stata fondata il 1 aprile 1973 dai fratelli Jac e Wiel Schoolmeesters come commercio di pannelli truciolari. | https://www.houtimportreuver.nl/ - frammento: 'opgericht op 1 april 1973 door de gebroeders Jac en Wiel Schoolmeesters' | Fondata il 01/04/1973 |
| Houtimport Reuver B.V. | referente | Referente e ruolo assenti (algemeen directeur iscritto e' la persona giuridica Gebrs. Schoolmeesters Holding B.V.). Nelle fonti aperte compare Tim Schoolmeesters in relazione alla direzione dell'azienda: nome DA CONFERMARE come directeur attuale. | https://companyinfo.nl/organisatieprofiel/groothandel-in-hout-en-plaatmateriaal/houtimport-reuver-b-v-reuver-12024480-000019946104 e https://appartme. |  |
| Houtplex B.V. | dimensione | Controllata di gruppo estero: Houtplex appartiene al gruppo Wood United, con sede a Singapore; dal febbraio 2019 le quote sia di Houtplex sia di Wood United sono di Timothy Paul, che ha rilevato la partecipazione di Jan Kersten. Il legame di gruppo e | https://www.houtwereld.nl/nieuws/houtplex-en-wood-united-overgenomen/ - frammento: 'Timothy Paul heeft de aandelen in Houtplex (Haaksbergen) en Wood U |  |
| Houtplex B.V. | referente | Referente e ruolo assenti. Le fonti indicano Timothy Paul come titolare della gestione quotidiana di Houtplex dopo l'uscita del precedente directeur Koen Kersten (passato a Kegro Deuren); Ruud van Oene, commercieel directeur, e' andato in pensione. D | https://www.houtwereld.nl/nieuws/houtplex-en-wood-united-overgenomen/ - frammento: 'Timothy Paul heeft de dagelijkse leiding van Houtplex overgenomen. |  |
| Kargro Banden B.V. | referente | Referente assente. Le fonti indicano Jan Driessen come directeur di Kargro (gruppo di Montfoort); il nome va confermato come bestuurder della singola B.V. Kargro Banden e non della sola holding. | https://www.utrechtbusiness.nl/magazine/artikel/579/12352/de-circulaire-ambities-van-marktleider-kargro - 'Kargro-directeur Jan Driessen' |  |
| Kargro Banden B.V. | dimensione | Legame di gruppo confermato e piu ampio di quanto dichiarato: oltre a Kargro International e Lintire, il gruppo comprende Banden Plan Europa BV (Montfoort) e Tyre Plan Europe (Kalmthout, BE) sotto Kargro Group Holding. La compliance si deciderebbe a  | https://kargrorecycling.com/nl/over/kargro-groep/ - 'Lintire in Vianen ... Banden Plan Europa in Montfoort ... Tyre Plan Europe, Kalmthout (Belgie)' |  |
| M.S. Pallets B.V. | referente | Referente assente: il directeur statutario e una persona giuridica (Maso Onroerend B.V.), nessun nome fisico pubblicato. DA CONFERMARE il nome della persona fisica dietro la holding prima di usare il lead per un contatto nominale. | https://companyinfo.nl/organisatieprofiel/vervaardiging-van-houten-emballage/m-s-pallets-b-v-den-ham-05049728-000016563247 - il campo dimensione del r |  |
| Montis B.V. | dimensione | Legame di gruppo: Montis e uno dei sei marchi della Lande Groep (con Artifort, Lande, Portner, Zwaardvis, A Lott Of Space), che produce in NL, BE, DE e TR. Il legame e dichiarato nel campo ma senza precisare che la compliance EUDR si decide a livello | https://www.landefamily.nl/montis - 'Montis is one of six strong brands under the Lande Groep (along with A Lott Of Space, Artifort, Lande, Portner an |  |
| Montis B.V. | dimensione | Il fatturato indicato (ca. 24,6 M$ ~ 22 M€) proviene da stime RocketReach/Creditsafe, non da un bilancio depositato: il campo stesso ammette che il fatturato non e depositato. Dato da trattare come stima non verificata, non come fatturato. | https://www.creditsafe.com/business-index/en-ie/company/montis-bv-nl01008091 - il campo dichiara 'Fatturato esatto NON depositato pubblicamente (B.V.  |  |
| Montis B.V. | referente | Referente e ruolo assenti. DA CONFERMARE il directeur attuale della B.V.: le fonti pubbliche associano Montis alla direzione storica di Paul van den Berg (dal 1975) ma non confermano un vertice in carica oggi sotto Lande Groep. | https://www.landefamily.nl/montis - 'high-quality design furniture from its own factory in Dongen since 1975 under the leadership of Paul van den Berg |  |
| Nijsen company B.V. | dimensione | Fatturato obsoleto: il dato di ca. 30 M€ risale a un'intervista del 2013 (13 anni fa) e non e stato riconfermato da alcuna fonte recente. Confermati invece 'oltre 100 collaboratori' e volumi di oltre 100.000 t/anno. | https://nijsen.co/en/nijsen/about-nijsen/ - 'over 100 colleagues ... over 100,000 tons of foodstuffs'; nessuna fonte pubblica recente riporta l'omzet |  |
| Nijsen company B.V. | filiera | DUBBIO DI PERIMETRO da chiarire: il modello attuale dell'azienda e il concetto Food-for-Feed, cioe la trasformazione di flussi residui dell'industria alimentare in mangimi circolari, non l'import di soia. L'esposizione alla soia (Allegato I) derivere | https://nijsen.co/en/nijsen/about-nijsen/ - 'Food-for-Feed concept, processing high-quality products from the food industry into ... raw materials for |  |
| OTR Oiltrade B.V. | referente | Referente e ruolo assenti: risulta pubblicamente Lars Schipper come directeur di OTR Oiltrade B.V. | https://www.transfirm.nl/nl/organisatie/24464899-000000435155-otr-oiltrade-b.v. - 'Lars Schipper is directeur'; KVK 24464899, Dieplood 40, 4251 LV Wer | Lars Schipper - Directeur |
| OTR Oiltrade B.V. | filiera | Esposizione all'olio di palma non dimostrata: le fonti pubbliche descrivono OTR Oiltrade come fornitore di 'plantaardige olien voor de voedingsindustrie' senza specificare la palma. Il campo la deduce dai grassi da frittura. DA CONFERMARE la presenza | https://www.oiltrade.nl/over-ons/ e https://nl.kompass.com/c/otr-oiltrade-b-v/nl821699/ - descrizione come fornitore di oli vegetali per l'industria a |  |
| Origin Bridge (Barchem) | denominazione | Forma giuridica NON risolta dopo 3 ricerche: nessuna fonte pubblica indicizzata riporta la rechtsvorm né una denominazione legale con suffisso. Restano solo KVK 70878315 e P.IVA NL001587917B24 pubblicati dall'azienda stessa. La struttura del numero I | https://originbridge.coffee/legal-information/ e https://originbridge.coffee/contact/ - 'Heidehoflaan 2B, 7244AG Barchem, The Netherlands ... CoC: 708 |  |
| Origin Bridge (Barchem) | email | L'email del foglio (info@bridgetoorigin.com) NON è quella principale del sito ufficiale: la pagina di contatto di originbridge.coffee indica come recapito dell'entità olandese europe@originbridge.coffee, tel. +31 85 301 6984. info@bridgetoorigin.com  | https://originbridge.coffee/contact/ - 'Origin Bridge Netherlands, Heidehoflaan 2B, 7244AG Barchem ... +31 85 301 6984 ... europe@originbridge.coffee' | europe@originbridge.coffee |
| PaBrEm B.V. | fonte | Fonte non pertinente: l'URL indicato e la pagina di categoria 'Cocoa Netherlands' di Europages, un elenco generico di fornitori, non una scheda della societa. Non sostiene alcun dato del record. | https://www.europages.co.uk/companies/netherlands/cocoa.html - pagina di elenco B2B per categoria, non profilo aziendale | https://pabrem.com/product/cocoa-mass (oppure una scheda KVK/company.info della societa) |
| PaBrEm B.V. | dimensione | Nessun dato dimensionale reperibile (fatturato, dipendenti e KVK restano ignoti dopo ricerca mirata) e forti indizi di micro-impresa: unico recapito pubblicato e un numero di cellulare (+31 653354279). Il record e ben sotto la forbice 5-40 M€ e non e | https://www.openpr.com/news/4338347/pabrem-b-v-emerges-as-a-trusted-fresh-fruits-vegetables-cocoa - 'Rollemastate 11, 8925 DA Leeuwarden ... +31 65335 |  |
| PaBrEm B.V. | filiera | DUBBIO DI PERIMETRO: le fonti descrivono PaBrEm come esportatore/grossista che porta prodotti agricoli 'dai Paesi Bassi verso i mercati mondiali', non come importatore che immette per primo il cacao sul mercato UE. L'obbligo EUDR come operatore va ve | https://www.openpr.com/news/4338347/pabrem-b-v-emerges-as-a-trusted-fresh-fruits-vegetables-cocoa - 'trusted exporter, supplier and wholesaler bringin |  |
| Rompa Tanneries B.V. | email | Email e sito legati al vecchio marchio (sales@rompa-tanneries.com / www.rompa-tanneries.com). Con la ridenominazione in Vitelco Leather il dominio di riferimento del gruppo e' vitelco.nl; il vecchio sito hulshof.com rimanda ancora a 'Rompa Tanneries' | http://www.hulshof.com/ (titolo pagina: 'Rompa Tanneries') e https://www.vitelco.nl/en/about-us |  |
| Rompa Tanneries B.V. | referente | Referente e ruolo vuoti. Le fonti stampa locali citano Twan de Bie come 'directeur leerlooierij' dello stabilimento di Lichtenvoorde. DA CONFERMARE la carica attuale dopo il passaggio a Vitelco Leather. | https://www.gld.nl/nieuws/2414011/directeur-leerlooierij-laat-de-wethouder-bellen-dan-lossen-we-het-als-volwassen-mensen-op - frammento: 'De directeur |  |
| Smeulders Interieurwerken B.V. | email | Email assente ('n.d.'): il lead non e contattabile via e-mail. Il campo dimensione cita j.mulder@smeulders-ig.nl trovata in directory, ma non e riportata nel campo email ne verificata come casella attiva. DA CONFERMARE una casella generica sul domini | https://smeulders-ig.nl/contact/ - pagina contatti del gruppo; il record stesso riporta 'Non risulta pubblicata una casella info@ generica' |  |
| Van Ierssel Houtimport B.V. | dimensione | Controllata di gruppo: Van Ierssel Houtimport e stata rilevata da Boogaerdt Hout nel 1986 e fa parte della Koninklijke Boogaerdt Groep. Il legame e dichiarato nel campo, ma il lead resta una controllata: la decisione di compliance EUDR si colloca a l | https://www.boogaerdthout.nl/en/2026/02/04/commercial-manager-member-of-ierssel-houtimport/ - 'In 1986 Van Ierssel Houtimport was taken over by Boogae |  |
| Van Ierssel Houtimport B.V. | referente | Fred Verver risulta confermato come directeur operativo di Van Ierssel (con werfmanager Ton van Oers), ma nelle fonti compare anche Oscar Smeets come 'Directeur Boogaerdt Hout - Van Ierssel Houtimport': verificare quale sia il vertice statutario dell | https://nl.linkedin.com/in/oscar-smeets-55856411 - 'Oscar Smeets - Directeur \| Boogaerdt Hout - Van Ierssel ...'; https://www.linkedin.com/in/fred-ve |  |
| Van den Berg Hardhout B.V. | email | Incoerenza di dominio: l'email e su .nl (info@vandenberghardhout.nl) mentre il sito ufficiale e le e-mail nominative del personale sono sul dominio .com (vandenberghardhout.com). Verificare quale dominio di posta sia realmente attivo. | https://rocketreach.co/albert-oudenaarden-email_99038923 - 'a******@vandenberghardhout.com'; https://www.vandenberghardhout.com/en/contact/ | info@vandenberghardhout.com (da confermare) |
| Van den Berg Hardhout B.V. | dimensione | Legame di gruppo dichiarato ma imminente: dal 01/01/2026 la societa e nella holding Van den Berg Houtgroep insieme a GWW Houtimport e GWW Agency. Con 6 dipendenti confermati e fatturato non pubblicato, l'azienda e sotto la forbice 5-40 M€ e la compli | https://rocketreach.co/van-den-berg-hardhout-bv-profile_b40aa59bff9a461e - 'Van den Berg Hardhout BV employs 6 people and is based in Lopik, Utrecht' |  |

### Belgio (68)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| A & A Chocolaterie NV | linkedin | NON E' UN DUPLICATO. Verificato il rilievo del controllo automatico: A & A Chocolaterie NV e Pralinart NV sono due societa' realmente distinte, con numeri d'impresa KBO diversi (BE 0892.388.320 vs BE 0450.589.051), sedi diverse (Mosten 16 vs Waasland | https://www.companyweb.be/en/0892388320/a-a-chocolaterie (A & A Chocolaterie, fondata 20-09-2007, sede Mosten 16, 9160 Lokeren, BE0892388320) e https: | Mantenere entrambi i record. Segnalare esplicitamente nel campo linkedin che la pagina https://be.linkedin.com/company/a |
| A & A Chocolaterie NV | sito | Il sito indicato (hamlet.be) e' il dominio della capogruppo/distributore Hamlet NV, non un dominio proprio di A & A Chocolaterie NV. Stesso valore assegnato anche a Pralinart NV: i due record condividono sito, LinkedIn ed email ('n.d.'), quindi nessu | https://www.hamlet.be/pagina/over-hamlet/productiesites-onze-merken-kerncijfers/ — le due societa' vi compaiono come siti produttivi del gruppo Hamlet |  |
| A & A Chocolaterie NV | referente | Referente e ruolo vuoti ed email 'n.d.': il lead non e' contattabile in modo diretto. L'unico nominativo emerso dalle fonti pubbliche e' Jeroen Van Overloop, indicato come COO di A&A Chocolaterie & Pralin'Art — ruolo operativo, non il titolo statutar | Frammento di ricerca: "Jeroen Van Overloop is the COO of A&A Chocolaterie & Pralin'Art" (https://be.linkedin.com/company/a&a-chocolaterie-pralin'art) |  |
| A & A Chocolaterie NV | dimensione | Il legame di gruppo e' correttamente dichiarato, ma va valutato l'effetto sul perimetro commerciale: A & A Chocolaterie (22,1 M€) e Pralinart (18,4 M€) sono entrambe controllate al 100% da Hamlet NV, quindi la decisione di compliance EUDR si prende v | https://www.hamlet.be/pagina/over-hamlet/productiesites-onze-merken-kerncijfers/ ; companyweb 0892388320 (22.087.972 €, 35,4 FTE, deposito 22-10-2025) |  |
| Accent NV | referente | Ives Declerck e' il CEO della capogruppo The Asteria Group, non l'amministratore della sola Accent NV: il mandato esclude di usare l'amministratore di capogruppo come referente della controllata. Va individuato il responsabile del sito di Gullegem. | asteriagroup.eu/asteria-group-interview-with-ives-declerck/ 'The Asteria Group: Interview with CEO Ives Declerck'; linkedin.com/in/ives-declerck-55b38 |  |
| Accent NV | dimensione | Il fatturato di 33.126.981 € attribuito ad Accent NV e' da riverificare: la crescita del gruppo e' stata rapidissima (da 20 M€ a ~500 M€ in poco piu' di sei anni) e la stampa cita 170 M€ per Asteria gia' prima delle ultime acquisizioni. Il perimetro  | made-in.be 'Asteria groeit aan hysterisch tempo'; derijkstebelgen.be: 'CEO Ives Declerck bouwde de verpakkingsgroep in iets meer dan zes jaar van 20 m |  |
| Allbox NV | referente | Referente e ruolo assenti: il record non e' utilizzabile per un contatto nominale. Le fonti pubbliche indicano come amministratori le societa' Y CORR NV (rappr. perm. Yves Vanquaethem) e JC WIBO NV (rappr. perm. Jean-Charles Wibo) piu' Caroline Brouw | fincheck.be/nl/allbox/0417.348.339/Harelbeke/bestuurders: 'Y CORR NV (Yves Vanquaethem), JC WIBO NV (Jean-Charles Wibo), Caroline Brouwers' (situazion |  |
| Autajon Packaging Belgium SA | dimensione | Controllata di gruppo estero: la societa' e' una filiale del gruppo familiare francese Autajon (guidato da Gerard Autajon), che in Belgio ha due siti (Anderlecht e Arlon). Il legame e' dichiarato nel campo, ma la decisione di compliance EUDR si collo | autajon.com/en/locations/packaging-belgium-bruxelles/; pappers.be/fr/company/autajon-packaging-belgium-0402682929: amministratori 'ROMAN AUTAJON, GERA |  |
| Autajon Packaging Belgium SA | referente | Referente e ruolo assenti. Le fonti pubbliche indicano come amministratori della SA belga Roman Autajon, Gerard Autajon e Jean-Pierre Wilhelm: quest'ultimo e' l'unico non appartenente alla famiglia proprietaria e verosimilmente il riferimento operati | pappers.be/fr/company/autajon-packaging-belgium-0402682929: 'Les dirigeants de Autajon Packaging Belgium sont ROMAN AUTAJON, GERARD AUTAJAN et Jean-Pi |  |
| Belvas SA | referente | Il referente indicato (Thierry Noesen, fondatore) risulta tuttora amministratore, ma le fonti recenti indicano come CEO operativo Jean-David Couderc. Il vertice esecutivo attuale va riconfermato; inoltre la forma giuridica di Belvas compare in piu' f | Frammento di ricerca: "Thierry Noesens serves as the director of Belvas, with Jean-David Couderc as CEO"; https://hainaut-terredegouts.be/producteur/b |  |
| Bruyerre Chocolates SA | referente | Referente e ruolo vuoti. Le fonti pubbliche indicano Marc Delsemme come Administrateur Delegue di Bruyerre Chocolates (con Olivier de Macar, coacquirente della cioccolateria e cofondatore di Bruyerre Chocolates SA). Titolo coerente con una SA vallona | https://rocketreach.co/marc-delsemme-email_123029407 ("Marc Delsemme ... Bruyerre Chocolates Administrateur Delegue"); https://bruyerre.eu/en/history/ | referente: Marc Delsemme — ruolo: Administrateur delegue (DA CONFERMARE su KBO/NBB) |
| Bulo NV | referente | Referente probabilmente non aggiornato. Dirk Busschop risulta CEO in fonti risalenti (2009); l'azienda e' oggi guidata dalla terza generazione, Carlo e Louis Busschop, con Carlo Busschop indicato come Managing Director / CEO in fonti recenti. Da rico | https://www.bulo.com/third_generation/ e https://rocketreach.co/carlo-busschop-email_93406361 - frammento: "Carlo Busschop, based in Mechelen, BE, is  | Carlo Busschop — gedelegeerd bestuurder / Managing Director (DA CONFERMARE) |
| Buzzispace NV | email | Email 'n.d.': record privo di indirizzo di contatto nonostante il sito buzzi.space sia attivo. DA CONFERMARE. | https://www.buzzi.space/brand (sito attivo, nessun indirizzo e-mail nei frammenti) |  |
| Carlens NV | referente | Referente e ruolo assenti. Le fonti pubbliche citano 'Carl Carlens' in contesto gestionale, mentre il campo dimensione ipotizza 'Luc Carlens' da FinCheck: nomi discordanti, nessuno dei due confermato come gedelegeerd bestuurder. DA CONFERMARE su BCE/ | https://www.limoco-industries.be/referenties/240-houthandel-carlens-keuze-voor-leverancier-dicht-bij-huis - frammento: risultati che referenziano "Car |  |
| Cartonnages Delsaux SA | email | Il campo e' valorizzato 'n.d.', ma un indirizzo e-mail aziendale esiste ed e' pubblicato sui repertori camerali (CCI Wapi) e su Europages/Kompass insieme al telefono 056/33.12.78; nei risultati di ricerca compare mascherato. DA CONFERMARE l'indirizzo | catalogue.cciwapi.be/entreprises/cartonnages-delsaux/ e fr.kompass.com/c/cartonnages-delsaux/be0007444/: 'Boulevard du Textile 13, 7700 Mouscron, tel. |  |
| Cartonnages Delsaux SA | dimensione | Conferma del sospetto gia' annotato nel campo: con 20-49 collaboratori dichiarati e un margine lordo di 2.828.246 € (113a nel settore Emballage), il fatturato — non pubblicato nel bilancio abbreviato — e' verosimilmente sotto i 5 M€, quindi FUORI dal | fr.kompass.com/c/cartonnages-delsaux/be0007444/: 'effectif de 20 à 49 employés'; trendstop.levif.be/fr/detail/401231293/cartonnages-delsaux.aspx: marg |  |
| Chocolaterie Ickx NV | sito | Il dominio indicato (ickx.be) non e' quello aziendale. Il sito ufficiale della cioccolateria e' choc-ickx.be — coerente anche con l'email gia' censita nel record (avangastel@choc-ickx.be), che usa lo stesso dominio. | https://www.choc-ickx.be/ compare come sito ufficiale nei risultati per "Chocolaterie Ickx"; sede confermata Rijkmakerlaan 28, 2910 Essen, BE 0421.359 | https://www.choc-ickx.be/ |
| Chocolaterie Ickx NV | referente | Referente e ruolo vuoti. Emerge solo che nel 2016 Bas Huurman ha lasciato la responsabilita' operativa ai tre figli; i nomi degli attuali gedelegeerd bestuurders non sono esposti nei frammenti gratuiti (dati riservati agli abbonamenti premium di papp | Frammento: "In 2016, Bas Huurman stepped back from operational responsibility and delegated it to his three children" — https://trends.knack.be/econom |  |
| Confiserie De Bie - L'Abeille - Trefin NV | referente | Referente e ruolo vuoti. Le fonti registrali indicano come amministratori Bert Verriet e Lisette Lerno. Fatturato (11.404.101 €), FTE (34,4) e deposito (08-06-2026) risultano confermati. | Frammento FinCheck: "The directors of Confiserie Trefin are Bert Verriet and Lisette Lerno" — https://fincheck.be/nl/confiserie-trefin/0400.120.050/Lo | referente: Bert Verriet — ruolo: gedelegeerd bestuurder (DA CONFERMARE quale dei due amministratori sia il delegato) |
| Confiserie Vandenbulcke NV | referente | Referente e ruolo vuoti. La terza generazione e' al timone con Jelle Vandenbulcke come CEO, affiancato dai cugini Bert e Luk. Fatturato 13.332.120 € confermato (44° posto di settore). | Frammento Voka/Made-in: "the third generation is now in charge, with CEO Jelle Vandenbulcke and his cousins Bert and Luk at the helm"; https://trendst | referente: Jelle Vandenbulcke — ruolo: CEO / gedelegeerd bestuurder |
| Confortluxe NV | referente | Referente e ruolo assenti benche' gli amministratori siano pubblici e confermati (Jacqueline Pauwels, Jimmy Ollevier, Heidi Ollevier). Il fondatore Andre Ollevier, storico gedelegeerd bestuurder, e' deceduto: non usarlo come referente. Da attribuire  | https://fincheck.be/en/confortluxe/0412.863.078/Wervik/connections - frammento: "The current board members of Confortluxe are Jacqueline Pauwels, Jimm | Jimmy Ollevier — bestuurder (ruolo di gedelegeerd bestuurder DA CONFERMARE) |
| Corné Port-Royal Chocolatier SA | referente | Referente e ruolo vuoti ed email 'n.d.'. Dalle fonti registrali l'administrateur delegue e' la societa' di management BELLEGRO (persona fisica non esposta nei frammenti gratuiti); gli altri amministratori nominati il 05-12-2023 sono NEUHAUS SA, Valer | https://www.pappers.be/fr/company/corne-port-royal-chocolatier-0433283558 — "BELLEGRO ... Administrateur, Administrateur delegue ... depuis le 5 decem |  |
| Corpack NV | dimensione | Il campo dichiara il dato 'NON REPERITO', ma parte dell'informazione e' pubblica: l'ultimo bilancio depositato alla NBB (17-07-2026) riporta 44,3 FTE, e i repertori d'impresa collocano Corpack nella fascia di fatturato 10-25 M€ con 20-49 addetti. Man | companyweb.be/en/0452991978/corpack: 'The most recent financial statements of Corpack were filed on 17-07-2026 ... 44.3 FTEs'; be.kompass.com/c/corpac | N. impresa BE 0452.991.978. 44,3 FTE (bilancio NBB depositato 17-07-2026); fatturato non pubblicato, stimato 10-25 M€ (K |
| Corpack NV | referente | Referente e ruolo assenti: il record non e' utilizzabile per un contatto nominale. Ne' trendstop, ne' companyweb, ne' bizzy.org pubblicano il nome del gedelegeerd bestuurder della NV. DA CONFERMARE tramite Moniteur belge / BCE. | Ricerche 'Corpack 0452.991.978 bestuurders/gedelegeerd bestuurder' su trendstop.knack.be/nl/detail/452991978, companyweb.be/en/0452991978/corpack, biz |  |
| Decolvenaere BV | dimensione | Fatturato fortemente sottostimato. Il campo riporta 'oltre 10 milioni di euro' (fonte giornalistica Sterck Magazine), ma i dati di bilancio piu' recenti indicano un fatturato totale di 38.585.036 EUR, con altre fonti che collocano l'azienda nella fas | Frammenti di ricerca su Decolvenaere BV (BE 0400.079.171): "The most recent financial statements show a total turnover of EUR 38,585,036.00" e "turnov | Fatturato ~38,6 M EUR (ultimo bilancio depositato NBB) — DA RICONFERMARE sulla fonte NBB primaria |
| Delafaille NV | referente | Il referente indicato (Paul Daems) e' esplicitamente uscente: le fonti sull'operazione Maestrani (23-06-2025) confermano che Daems, proprietario e CEO, resta solo 'per un periodo limitato' per accompagnare la transizione e che verra' nominato un nuov | Frammento just-food: "Paul Daems, Delafaille's current owner and CEO, [will] stay with the company for a 'limited period' as he aids the transition, b |  |
| Delafaille NV | dimensione | Il legame di gruppo e' dichiarato ma la conclusione tratta nel campo ('resta pero' PMI belga autonoma con obblighi EUDR propri') e' opinabile: Maestrani Schweizer Schokoladen ha acquisito il 100% delle azioni di Delafaille e della sua controllata cec | Frammento bpv Braun Partners: "Maestrani ... acquisition of Belgian chocolate manufacturer Delafaille with a major Czech subsidiary [Ostrapack]"; "Del |  |
| Dolfin SA | referente | Referente e ruolo vuoti ed email 'n.d.'. Le fonti pubbliche indicano Jean-Jacques de Gruben come proprietario e Directeur General di Dolfin SA (ha rilevato la cioccolateria nel 2007 insieme a Gilles van der Meerschen). | Frammento: "En 2007, Jean-Jacques de Gruben a repris les renes de la Chocolaterie Dolfin" (https://www.dolfin.be/en/who-are-we/); "Jean-Jacques de Gru | referente: Jean-Jacques de Gruben — ruolo: Administrateur delegue / Directeur general (DA CONFERMARE il titolo statutari |
| Extremis NV | dimensione | Fatturato potenzialmente obsoleto: il campo riporta 12.900.125 EUR e 24,8 FTE dall'ultimo bilancio, ma risulta gia' depositato un bilancio piu' recente (deposito 02-07-2026) i cui dati non sono riflessi nel record. DA AGGIORNARE. | https://www.companyweb.be/en/0434625128/extremis - frammento: "The most recent financial statements of Extremis were filed on 02-07-2026" |  |
| Gudrun Commercial NV | dimensione | Legame di gruppo dichiarato ma incompleto e con conseguenze non tratte: Natra ha acquisito il 100% di Gudrun (annuncio ottobre 2024) dal fondo Down2Earth Capital, e Natra e' a sua volta partecipata dal fondo di private equity britannico CapVest. Gudr | https://www.just-food.com/news/capvest-backed-natra-buys-chocolate-peer-gudrun/ ; https://www.capvest.com/news/gudrun ("Natra acquired 100% of Gudrun  | Integrare: acquisita al 100% da Natra (gruppo partecipato da CapVest) nell'ottobre 2024; venditore Down2Earth Capital. |
| Hannecard Benelux NV | referente | Referente e ruolo vuoti, e il quadro dirigenziale e' in transizione: il gedelegeerd bestuurder storico di Hannecard Benelux (Rik De Jo..., in carica dal 1984) risulta pensionato dal 2025. Il CEO di gruppo e' Dirk Vidts — vertice del gruppo, non neces | https://rocketreach.co/de-jo-rik-email_483835577 — "De Jo Rik ... HANNECARD Gepensioneerd", "Gedelegeerd Bestuurder at Hannecard Benelux 1984-2025"; " |  |
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
| Libeert NV | ruolo | Il referente indicato (Lily Libeert, 'Co-directrice') non e' il vertice statutario. Il gedelegeerd bestuurder di Libeert e' Ignace Libeert; Lily Libeert risulta Co-CEO per Sales & Marketing e Pieter Libeert e' fra i proprietari. Per una NV/SA il tito | https://www.linkedin.com/in/ignace-libeert-ba44b8113/ — "Ignace Libeert - gedelegeerd bestuurder - LIBEERT - Belgian Chocolate Creators"; frammento: " | referente: Ignace Libeert — ruolo: gedelegeerd bestuurder (mantenere eventualmente Lily Libeert come secondo contatto co |
| Manutti BV | dimensione | Il fatturato 15.340.098 € e i 27,4 FTE (bilancio NBB depositato 17-06-2024) sono confermati. Non trova invece riscontro pubblico l'affermazione di uno 'stabilimento produttivo in Indonesia (circa 140 addetti)': le fonti presentano Manutti come design | companyweb.be/en/0476263070/manutti: 'Manutti recorded a total turnover of EUR 15,340,098.00 according to the most recent financial statements filed o |  |
| Manutti BV | dimensione | Legame di gruppo con Manutti Invest BV (BE 0478.148.434) dichiarato nel record: si tratta della holding familiare che controlla l'operativa. Segnalato come 'media' perche' gia' dichiarato; la decisione di compliance potrebbe collocarsi a livello di h | https://www.companyweb.be/en/0478148434/manutti-invest |  |
| Mecam NV | referente | Il referente indicato (Inge Meers, CFO) non e' il vertice della societa'. Il gedelegeerd bestuurder / CEO e' il fratello Luc Meers, che ha la direzione generale; Inge cura la parte finanziaria. | meubihome.be / sterck-magazine.be: 'CFO en bestuurder Inge Meers runt samen met haar broer Luc het bedrijf'; wonen360.nl: 'CEO Luc Meers'; trendstop:  | Luc Meers — Gedelegeerd bestuurder / CEO |
| Mecam NV | dimensione | Il record riporta 32.145.268 € e 111,6 FTE per la sola Mecam NV, mentre la stampa parla di 37 M€ cumulati e ~220 dipendenti per l'intero Mecam Group (Mecam + Neo-Style). Il legame di gruppo esiste ed e' accennato ma il perimetro del dato va esplicita | sterck-magazine.be: 'Mecam ... met een gecumuleerde omzet van 37 miljoen euro (2023)'; 'Raymond Meers richtte de Mecam Group op in 1978 ... vandaag we |  |
| Meubelfabriek Lievens NV | dimensione | Fatturato 19.952.978 € e 53,5 FTE confermati, ma il dato e' anteriore all'uscita dal mercato olandese (dal 31-01-2024 Lievens e Confortluxe hanno abbandonato i Paesi Bassi, con azzeramento del fatturato NL). Il fatturato futuro sara' verosimilmente i | interiorbusiness.nl 'Meubelfabrikanten Confortluxe en Lievens herorienteren zich en verlaten Nederlandse markt'; wonen360.nl 'Confortluxe en Meubelfab |  |
| Oxfam Fair Trade CV | referente | Referente e ruolo vuoti e LinkedIn vuoto. L'unico nominativo emerso e' Luc Van Haute, presentato come direttore generale di Oxfam-Wereldwinkels/Oxfam Fair Trade, ma la fonte risale al 2017: non riconfermato per il 2025-2026. DA CONFERMARE. Fatturato  | https://www.otheo.be/nieuws/luc-haute-nieuwe-directeur-oxfam-wereldwinkels (2017); https://trendstop.knack.be/nl/detail/453066016/oxfam-fairtrade.aspx |  |
| Passe Partout NV | dimensione | Il record non segnala che la produzione non avviene in Belgio: Passe Partout produce in Ungheria dal 1999, mentre a Temse lavorano ~13 persone (coerente con gli 11,3 FTE). Elemento rilevante per qualificare il ruolo EUDR (immissione sul mercato di mo | interiorbusiness.nl: 'Passe Partout ... produceert sinds 1999 vanuit Hongarije ... kantoor in Temse waar 13 mensen werken' |  |
| Pierre Marcolini Group SA | referente | Referente, ruolo, LinkedIn ed email tutti vuoti/'n.d.': il lead non e' contattabile. L'administrateur-delegue della societa' e' Pierre Marcolini stesso (BE 0461.740.982, Rue du Bassin Collecteur 4, 1130 Bruxelles). | https://www.pappers.be/fr/company/pierre-marcolini-group-0461740982 — "Pierre Marcolin[i] est Administrateur-delegue"; sede Rue du Bassin Collecteur 4 | referente: Pierre Marcolini — ruolo: Administrateur delegue |
| Pierre Marcolini Group SA | dimensione | Fatturato non aggiornato: il record riporta 19.300.806 EUR, mentre l'ultimo bilancio depositato (16-10-2025) indica 21.606.032 EUR con 118,1 FTE. Inoltre l'azionariato non e' dichiarato: nel capitale figurano investitori finanziari (NEO Investment Pa | https://www.companyweb.be/en/0461740982/pierre-marcolini-group — "total turnover of EUR 21,606,032.00 ... financial statements filed on October 16, 20 | Fatturato 21.606.032 EUR e 118,1 FTE (bilancio NBB depositato 16-10-2025); aggiungere la composizione dell'azionariato f |
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
| Van De Wiele Rubber NV | filiera | Perimetro EUDR dubbio. L'azienda si presenta come specialista di 'rubber and plastic extrusion and injection molding' e il suo parco macchine comprende la co-estrusione di kunststof (materie plastiche): non esiste evidenza pubblica che lavori gomma N | rubber-groothandel.be/machinepark: 'kunststof co-extrusie \| matrijzenmakerij \| Van De Wiele Rubber \| Kluisbergen'; vandewiele-gummi.de/rubber.html: |  |
| Van De Wiele Rubber NV | referente | Referente e ruolo assenti: il record non e' utilizzabile per un contatto commerciale nominale. Le ricerche su fonti pubbliche (trendstop, companyweb, jaarrekening.be, LinkedIn aziendale) non restituiscono il nome del gedelegeerd bestuurder della NV.  | Ricerche 'Van De Wiele Rubber bestuurder/directeur' su trendstop.knack.be/nl/detail/405713386, companyweb.be/en/0405713386/van-de-wiele-rubber e be.li |  |
| Van De Wiele Rubber NV | dimensione | Il campo non qualifica la societa' rispetto alla forbice target 5-40 M€. Con 28,4 FTE e un margine lordo di 3.331.259 € (22a nel settore 'rubber en banden'), il fatturato — non pubblicato in bilancio (schema abbreviato, ultimo deposito 03-03-2025) —  | companyweb.be/en/0405713386/van-de-wiele-rubber: 'the most recent financial statements were filed on 03-03-2025 ... 28.4 FTEs ... Van De Wiele Rubber  |  |
| Vanerum Belgie NV | referente | Gert Van Erum e' il CEO della capogruppo i3-Group, non l'amministratore della sola Vanerum Belgie NV: il mandato esclude l'uso dell'amministratore di capogruppo come referente della controllata. Va individuato il responsabile della societa' belga. | trends.knack.be: 'Gert Van Erum (CEO i3 Group)'; cbinsights: 'i3-Group, formerly VANERUM Group, founded 1968, based in Diest' |  |
| Vanerum Belgie NV | dimensione | Il legame di gruppo e' dichiarato ma incompleto: i3-Group non e' piu' interamente familiare. WorxInvest ha acquistato circa il 25% per 10 M€ e nel novembre 2023 anche il gruppo americano Steelcase ha preso una partecipazione. La compliance EUDR si de | derijkstebelgen.be 'NIEUW – WorxInvest betaalt 10 miljoen euro voor kwart van Van Erum schoolborden'; holahageland.net 'Na WorxInvest neemt ook Amerik |  |
| Woodtex NV | dimensione | Dato di fatturato superato. Il record riporta 11.778.466 € (deposito 23-06-2025); l'ultimo bilancio depositato (01-06-2026) indica 12.131.554 € con 35 FTE. | companyweb.be/en/0413744194/woodtex: 'Woodtex recorded a total turnover of €12,131,554.00. The most recent financial statements were filed on 01-06-20 | Fatturato 12.131.554 € - 35 FTE (bilancio NBB depositato 01-06-2026) |

### Austria (17)

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
| Meiberger Holzbau GmbH | dimensione | Il totale di bilancio 11,33 Mio EUR (31.01.2025) e' confermato, ma non sostiene la stima di fatturato 10-15 Mio EUR: la voce e' composta per 8,67 Mio EUR da immobilizzazioni (Anlagevermögen), con patrimonio netto 3,36 Mio EUR. Trattandosi di una Zimm | https://www.firmenabc.at/meiberger-holzbau-gmbh_cXK ('Bilanzsumme 11.328.315,08 EUR; Eigenkapital 3.358.529,11 EUR; Anlagevermögen 8.673.136,11 EUR',  | Totale di bilancio 11,33 Mio EUR (31.01.2025, firmenabc.at), di cui 8,67 Mio EUR immobilizzazioni; fatturato non pubblic |
| Meyer Parkett GmbH | sede | La sede non e' piu' Kalsdorf bei Graz: Firmenbuch, herold e firmenabc indicano Sternweg 2, 8141 Premstaetten (Graz-Umgebung). Trasferimento oggetto di Kundmachung comunale 2024. | https://www.evi.gv.at/f/226133z (titolo: 'Meyer Parkett GmbH 8141 Premstaetten \| Firmenbuch'); https://www.herold.at/gelbe-seiten/premst%C3%A4tten/qS | Premstätten (Steiermark) |
| Rauchenzauner Möbel GmbH | dimensione | Il fatturato di 18,8 M€ e' una stima Die Deutsche Wirtschaft, non un dato firmenabc: la fonte e' attribuita male. L'unico dato di bilancio reale e' il totale attivo 4.454.624,41 EUR al 31.03.2025. La societa' e' inoltre di costituzione recente (FN 61 | https://www.evi.gv.at/f/611446k ('Bilanz zum 31.03.2025, Bilanzsumme 4.454.624,41 EUR'; iscritta 06.09.2023; GF Gerhard Rauchenzauner e Sabine Rauchen | Totale di bilancio 4,45 Mio EUR (31.03.2025, Firmenbuch); 50-99 dipendenti (firmenabc); fatturato non pubblicato (18,8 M |
| Schösswender Möbel Gesellschaft m.b.H. | dimensione | Il solo dato di fatturato citato e' quello di gruppo del 2012 (28 M€): 13 anni di anzianita', inutilizzabile per il dimensionamento. La stima 15-25 M€ per la sola societa' mobili resta non confermata. Va inoltre tenuto presente il legame di gruppo (S | https://www.firmenabc.at/schoesswender-moebel-gesellschaft-m-b-h_jQF ; https://www.northdata.com/Sch%C3%B6sswender%20M%C3%B6bel%20GmbH,%20Franking/035 |  |
| Speedmaster GmbH | dimensione | Il campo dichiara 'fatturato e dipendenti non pubblicati', ma entrambi i dati sono pubblici: ca. 29 Mio EUR di fatturato annuo e ca. 300 dipendenti nella sede di Eberstalzell, piu' un secondo stabilimento produttivo a Steinsfeld (Germania). L'azienda | https://www.meinbezirk.at/wels-wels-land/c-wirtschaft/stelzer-bei-speedmaster-in-eberstalzell_a5975977 ('erwirtschaftet einen Jahresumsatz von 29 Mill | Fatturato ca. 29 Mio EUR/anno e ca. 300 dipendenti (meinbezirk.at, Landeshauptmann-Besuch); secondo stabilimento a Stein |
| Storebest Ladeneinrichtungen GmbH | referente | Gernot Karlsböck risulta Prokurist (authorized signatory) della '"Storebest" Ladeneinrichtungen Gesellschaft m.b.H.', mentre come Geschäftsführer e' indicato Martin Klapka. Il referente dichiarato non e' quindi il vertice statutario. DA CONFERMARE su | https://www.firmenabc.at/storebest-ladeneinrichtungen-gesellschaft-m-b-h_um ('Gernot Karlsböck (Dkfm.) ... Prokurist; Martin Klapka ... Geschäftsführe |  |
| Tschurtschenthaler Gerberei GmbH | sito | Sito aziendale assente ('n.d.'): nessun dominio proprio individuato nelle fonti pubbliche, solo schede di directory (herold, cylex, europages). | https://www.herold.at/gelbe-seiten/st-stefan-im-gailtal/RZ2RJ/tschurtschenthaler-gerberei-gmbh/ - scheda senza URL aziendale |  |
| Waldviertler Werkstätten GmbH | dimensione | Dato di fatturato datato (2016-2019) e non riconciliato: le fonti citano 31 Mio EUR di ricavi 2016 riferiti all'universo GEA e, per la controllante Heinrich Staudinger GmbH, un totale di bilancio 2024 di 5,45 Mio EUR. Il perimetro societario del dato | https://www.firmenabc.at/heinrich-staudinger-gmbh-gea-waldviertler_NTLA - frammento: "balance sheet total of EUR 5.454.811,76 as of December 31, 2024" |  |
| Wittmann Möbelwerkstätten GmbH | dimensione | Conferma dell'incoerenza gia' segnalata: la stima Die Deutsche Wirtschaft di 45,0 Mio EUR e' riferita al 2023, mentre il totale di bilancio 2024 e' 9.611.765,78 EUR. Nessun fatturato ufficiale pubblicato. Esiste inoltre una seconda 'Wittmann Möbelwer | https://die-deutsche-wirtschaft.de/famu_top/oesterreich-wittmann-moebelwerkstaetten-gmbh-etsdorf-am-kamp-umsatz-mitarbeiterzahl/ (stima 45,0 Mio EUR,  |  |

---

## 6. Casi di gravità BASSA (135)

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

### Germania (15)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Büttenpapierfabrik Gmund GmbH & Co. KG | dimensione | Il dato è datato 2022 (4 anni) e proviene da un portale aggregatore (wer-zu-wem.de), non da bilancio depositato. Va riconfermato o sostituito con il dato più recente. | https://www.wer-zu-wem.de/firma/buettenpapierfabrik.html (dato 2022: ~120 MA, ~20 Mio € Umsatz) |  |
| Christian Göbel Holzgroßhandlung GmbH & Co.  | denominazione | Ragione sociale incompleta: la denominazione registrata e 'Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG' (HRA 15605 Amtsgericht Frankfurt/Main). | https://www.goebel-holz.de/impressum/ - 'Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG, Anton-Schlüter-Straße 2, 60437 Fr | Christian Göbel Holzgroßhandlung, Großhandlung mit Sperrholz GmbH & Co. KG |
| E. Fuhlrott GmbH & Co. KG (HOLZFUHLROTT) | denominazione | Denominazione registrata completa: 'E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel' (HRA 400107). Esistono inoltre societa collegate del medesimo gruppo familiare (FUHLROTT Paletten Verpackungen & Logistik GmbH, HRB 510714; Fuhlrott Produktio | https://www.unternehmen24.info/Firmeninformationen/Deutschland/Firma/164652 - 'E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel, HRA 400107'; ht | E. Fuhlrott GmbH & Co. KG, Kistenfabrik und Holzhandel |
| Falt Schachtel Hamburg dyecut GmbH | denominazione | Refuso nella ragione sociale: la denominazione registrata è «Faltschachtel Hamburg dyecut GmbH» (una parola), non «Falt Schachtel». | https://www.northdata.com/Faltschachtel%20Hamburg%20dyecut%20GmbH,%20Hamburg/HRB%2096405 e https://www.faltschachtelhamburg.de/impressum/ — AG Hamburg | Faltschachtel Hamburg dyecut GmbH |
| Gebr. Kilger, Lederfabrik Viechtach KG | dimensione | L'inciso 'marchio Rendenbach' non trova riscontro: Rendenbach (J. Rendenbach jr.) e una conceria di Trier, non risulta alcun legame con Kilger nei risultati di ricerca. DA CONFERMARE. | Ricerca '"Lederfabrik Kilger Viechtach Rendenbach"': nessun risultato collega Kilger a Rendenbach; kilger.de/en/about-us/ descrive solo il marchio pro |  |
| H. Heitz Furnierkantenwerk GmbH & Co. KG | referente | Referente CONFERMATO ma di nomina recente: Jürgen Cirkel e subentrato come Geschäftsführer dopo il pensionamento del precedente GF Stefan Wernecke; nelle banche dati compare ancora anche Ralf Heitz come GF. Verificare che l'anagrafica sia aggiornata. | https://www.h-heitz.de/aktuelles/presse/ - 'Juergen Cirkel wurde zum neuen Geschaeftsfuehrer bestellt ... nach dem Ausscheiden des langjaehrigen Gesch |  |
| H.-J. Dres GmbH | referente | Referenti (Jürgen e Petra Dres) confermati dall'Impressum, ma si segnala il passaggio generazionale in corso: Nathalie Dres (dal 2018) e Christoph Dres (dal 2018) sono operativi in azienda. Verificare prima del contatto se la rappresentanza legale si | https://www.dres-faltschachteln.de/impressum.html — «vertreten durch die Geschäftsführer Jürgen Dres und Petra Dres»; https://www.dres-faltschachteln. |  |
| Hartmann Möbelwerke GmbH | referente | Compagine della Geschäftsführung incompleta: oltre a Katharina Hartmann e Holger Hanhardt ne fa parte anche Bernhard Hartmann, che ha ceduto la guida alla figlia ma resta in Geschäftsführung. | https://www.die-glocke.de/lokalnachrichten/katharina-hartmann-uebernimmt-beelener-moebelhersteller-1709910613 - 'Katharina Hartmann ist in die Geschae | Katharina Hartmann, Bernhard Hartmann, Holger Hanhardt |
| Horn Verpackung GmbH | referente | Ferdinand Horn è indicato come Geschäftsführer: la nomina a secondo amministratore risulta da un comunicato aziendale, ma l'Impressum e i portali continuano a riportarlo come «Assistenz der Geschäftsleitung / Prokurist» e indicano un solo Geschäftsfü | https://www.horn-verpackung.de/ferdinand-horn-wird-zusatzlicher-geschaftsfuhrer-starkung-fur-kontinuitat-und-zukunft (comunicato) vs. https://www.horn |  |
| Josef Schulte GmbH | dimensione | Il dato (116 dipendenti, ~36 Mio € di fatturato) è confermato dalla fonte citata, ma il campo non riporta l'anno di riferimento: è l'unico elemento mancante per un record altrimenti utilizzabile. Il valore è al limite superiore della forbice cliente  | https://www.wirtschaftsforum.de/news/josef-schulte-gmbh/hochwertig-und-nachhaltig — «beschäftigt derzeit 116 Mitarbeiter ... mehr als 3.500 Kunden ... | «~36 Mio € di fatturato e 116 dipendenti (wirtschaftsforum.de) — aggiungere l'anno del servizio; verificare l'aggiorname |
| Josef Schulte GmbH | denominazione | La ragione sociale iscritta al registro è «Josef Schulte Gesellschaft mit beschränkter Haftung»; «Josef Schulte GmbH» è la forma d'uso. Refuso formale, non bloccante. | https://firmeneintrag.creditreform.de/33129/4290014288/JOSEF_SCHULTE_GESELLSCHAFT_MIT_BESCHRAENKTER_HAFTUNG e https://www.companyhouse.de/en/Josef-Sch | Josef Schulte Gesellschaft mit beschränkter Haftung |
| PFT Holz in Form GmbH | sede | La sede legale (Sitz) iscritta a registro e Schlüsselfeld, con iscrizione presso l'Amtsgericht Stendal (HRB 26378); Mertendorf OT Görschen (Südring 7) e la sede operativa/stabilimento. Il campo non distingue i due livelli. | https://www.northdata.com/PFT%20Holz%20in%20Form%20GmbH,%20Schl%C3%BCsselfeld/Amtsgericht%20Stendal%20HRB%2026378 - 'PFT Holz in Form GmbH, Schlüsself | Stabilimento: Mertendorf OT Görschen (Sachsen-Anhalt); sede legale: Schlüsselfeld (Bayern), HRB 26378 AG Stendal |
| Paletten Meyer | denominazione | 'Paletten Meyer' e solo il nome commerciale/dominio. La ditta e iscritta come 'Josef Meyer Palettenbau Inh. Julian Meyer' (impresa individuale, non societa di capitali): la forma giuridica va esplicitata perche incide sulla figura del contraente EUDR | https://www.europages.de/JOSEF-MEYER-PALETTENBAU-INH-JULIAN-MEYER/00000005396426-001.html e https://www.wlw.de/de/firma/josef-meyer-palettenbau-inh-ju | Josef Meyer Palettenbau Inh. Julian Meyer (Paletten Meyer) |
| RMW Wohnmöbel GmbH & Co. KG (Rietberger Möbe | referente | Geschäftsführung incompleta: oltre a Rudolf Eikenkötter risulta Geschäftsführer anche Volker Klocke (RMW Wohnmöbel Verwaltungs GmbH, HRB 6744 AG Gütersloh, socio accomandatario). | https://www.northdata.com/RMW%20Wohnm%C3%B6bel%20Verwaltungs%20GmbH,%20Rietberg/Amtsgericht%20G%C3%BCtersloh%20HRB%206744 e https://www.rmw-wohnmoebel | Rudolf Eikenkötter, Volker Klocke |
| Schmidt & Thürmer Holzhandlung, Säge- und Ho | referente | Elenco dei Geschäftsführer incompleto: l'Impressum ne indica due, il record ne riporta uno solo. Da valutare anche Peter-Uwe Winkel, nominato Geschäftsführer nel 2019 (EUWID): verificare se sia ancora in carica. | https://www.schmidt-thuermer.de/impressum/ — Geschäftsführer: Mathias Mörke, Andreas Helmrich; cfr. https://www.euwid-holz.de/news/handel/winkel-neuer | Mathias Mörke, Andreas Helmrich |

### Finlandia (6)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Aureskosken Jalostetehdas Oy | dimensione | Fatturato riportato (15,8 M€ 2024) superato dal bilancio 2025: 18,9 M€ e 52 dipendenti. | https://vainu.io/company/aureskosken-jalostetehdas-oy-taloustiedot-ja-liikevaihto/128104/yritystiedot — frammento: "In 2025, the company had a revenue | Liikevaihto 18,9 M€ / 52 dip. (2025, Vainu/Asiakastieto) |
| Elega Oy | dimensione | Fatturato impreciso e senza fonte/anno certo ('~8,8 M€ 2023-24'): il dato di bilancio 2024 e' 9,5 M€ con 56 dipendenti, in calo del 17,5%. | https://vainu.io/company/elega-oy-taloustiedot-ja-liikevaihto/542365/yritystiedot — frammento: "Elega Oy's revenue was 9.5 million euros in 2024 and e | Liikevaihto 9,5 M€ / 56 dip. (2024, Asiakastieto/Vainu) |
| Hakola Huonekalu Oy | dimensione | Dato di fatturato non aggiornato (4,82 M€ 2023): il bilancio 2024 riporta 5,0 M€ e 30 dipendenti. Resta comunque al limite inferiore della forbice (5 M€). | https://vainu.io/company/hakola-huonekalu-oy-taloustiedot-ja-liikevaihto/163895/yritystiedot — frammento: "Hakola Huonekalu Oy's revenue was 5 million | Liikevaihto 5,0 M€ / 30 dip. (2024, Asiakastieto/Vainu) — limite inferiore forbice |
| Hoisko CLT (CLT Finland Oy) | dimensione | Dati anagrafici e finanziari confermati (5,0 M€ 2024, 25 dip., toimitusjohtaja Tero Yli-Sikkila), ma il campo non segnala la fragilita' patrimoniale: omavaraisuusaste (equity ratio) 9% e margine operativo 3,3%. Fatturato al limite inferiore della for | https://www.asiakastieto.fi/yritykset/fi/clt-finland-oy/27245892/taloustiedot — frammento: "turnover of 5 MEUR in 2024 and employed 25 people... opera |  |
| Hollolan Viilu ja Laminaatti Oy (HVL) | dimensione | Il valore 5,4 M€ (2025) e' confermato ma la serie storica e' bassa (4,47 M€ nel 2023, 4,7 M€ nell'esercizio precedente): l'azienda oscilla intorno alla soglia minima di 5 M€ della forbice. Da valutare come lead marginale. | https://search.vainu.com/company/hollolan-viilu-ja-laminaatti-oy-taloustiedot-ja-liikevaihto/FI09821550/yritystiedot — frammento: "2025: 5.4 million e |  |
| Kankarin Kaluste Oy | dimensione | Serie storica incoerente con le fonti: il record indica 18,8 M€ per il 2024, mentre le fonti riportano oltre 23 M€ nel 2023 e 22 M€ nel 2025 (69 dip.). Il dato 2025 e' corretto; il dato intermedio 2024 va riverificato. | https://puumieslehti.fi/kuukauden-juttu/kankarin-kaluste-oy-kiintokalusteita-kihniosta-40-vuoden-kokemuksella/ e https://vainu.io/company/kankarin-kal | Liikevaihto 22,0 M€ / 69 dip. (2025) — rimuovere o riverificare il valore 18,8 M€ (2024) |

### Danimarca (19)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| ALL CREATIVE A/S | referente | Nome del referente incompleto: l'adm. direktor registrato e' Mette Juhl Christensen. Email info@allcreative.dk e sede (vendite Islevdalvej 214, Rodovre; produzione Tulipvej 3, Vejle) risultano confermate. | https://www.proff.dk/firma/all-creative-as/r%C3%B8dovre/papir-og-papirprodukter-produktion/GSG8C7I10K1 (adm. direktor Mette Juhl Christensen) ; https: | Mette Juhl Christensen, Adm. direktor |
| BØJSØ DØRE & VINDUER A/S | dimensione | Organico non allineato: le fonti reperite indicano 43 dipendenti, il record ne indica 41. Inoltre il campo non riporta alcun dato economico verificato (né fatturato né bruttofortjeneste): la collocazione in forbice 5-40 M€ resta una stima non verific | https://www.proff.dk/firma/b%C3%B8js%C3%B8-d%C3%B8re-vinduer-as/vorbasse/producenter/GJL0QJI016D — frammento: "Bøjsø doors and windows was founded in  | 43 dipendenti (proff.dk, CVR 12224494); dato economico da recuperare a bilancio |
| CAFÉU DENMARK ApS | dimensione | Il bruttofortjeneste di 7,3 mio DKK e' riportato senza anno di riferimento ('ultimo bilancio disponibile'): il mandato richiede tipo di dato + fonte + anno. Corretta invece la segnalazione 'SOTTO IL TARGET' (7,3 mio DKK di margine lordo ~1,0 M€). | https://www.proff.dk/firma/caf%C3%A9u-denmark-aps/esbjerg-n/n%C3%A6rings-og-nydelsesmidler/GT4AIYI116S - CVR 33243537, NACE 463700 'engroshandel med k | Indicare l'anno di bilancio del bruttofortjeneste di 7,3 mio DKK — DA CONFERMARE su regnskab |
| COLOR LABEL A/S | ruolo | Ruolo generico e non conforme alla nomenclatura danese. Erik Groenning risulta effettivamente in carica ma con il titolo di adm. direktoer. | https://www.colorlabel.dk/om-color-label - 'Color Label ... etableret af Erik Groenning, der fortsat leder virksomheden'; proff.dk CVR 15136901 riport | Adm. direktør (fondatore) |
| COLOR LABEL A/S | dimensione | Anno di fondazione discordante: il campo indica 'fondata 1991', il sito aziendale indica la fondazione nel 1980 da parte di Erik Groenning (1991 e' verosimilmente la data di registrazione dell'attuale CVR 15136901). | https://www.colorlabel.dk/om-color-label - azienda 'etableret' nel 1980 da Erik Groenning | fondata nel 1980 (attuale CVR 15136901 registrato nel 1991) — DA CONFERMARE |
| COPENHAGEN CHOCOLATE FACTORY ApS | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: CVR 32761844, Amager Landevej 123, 2770 Kastrup, costituita il 26-01-2010, ApS; opera con i binavne 'Simply Chocolate Copenhagen' e www.simplychocolate.dk; direttore Niels Ostenkaer; capogruppo SOLSTRA INVESTME | https://cvrapi.dk/virksomhed/dk/copenhagen-chocolate-factory-aps/32761844 ; https://www.simplychocolate.dk/pages/handelsbetingelser - 'www.simplychoco |  |
| FREDERICIA FURNITURE A/S | dimensione | Refuso nell'unità di misura: "risultato ante imposte 6,5 M€ DKK" mescola euro e corone danesi. Il valore va espresso in una sola valuta. | Testo del campo dimensione del record stesso: "risultato ante imposte 6,5 M€ DKK" | risultato ante imposte 6,5 mio DKK (~0,87 M€) |
| Farstrup Furniture A/S | ruolo | DA CONFERMARE: i registri elencano due direktør (Jan Andersen e Steen Cederholm-Johansen) senza qualificare esplicitamente Cederholm-Johansen come administrerende direktør. Il ruolo indicato non è riconfermato. | https://www.proff.dk/firma/farstrup-furniture-as/s%C3%B8nders%C3%B8/producenter/GKF1OMI016D — frammento: "The directors are Jan Andersen and Steen Ced |  |
| INNOVATION LIVING A/S (già Innovation Rander | linkedin | URL LinkedIn con prefisso di locale tedesco (de.linkedin.com) per una società danese. Non è un errore di pagina ma è incoerente con lo standard del dataset (dk. o www.). | Valore del record: https://de.linkedin.com/company/innovation-living-a-s | https://dk.linkedin.com/company/innovation-living-a-s |
| JOHNSEN GRAPHIC SOLUTIONS A/S (oggi anche Jo | denominazione | La ragione sociale attuale del CVR 18624141 e' JOHNSEN PRINT & DIGITAL MEDIA A/S; 'Johnsen Graphic Solutions A/S' e' la denominazione precedente, non un secondo nome in uso. La formulazione del campo inverte nome storico e nome attuale. | https://virmo.dk/firma/18624141-johnsen-print-digital-media-as e https://cvrapi.dk/virksomhed/dk/johnsen-graphic-solutions-as/18624141 - 'JOHNSEN PRIN | JOHNSEN PRINT & DIGITAL MEDIA A/S (già Johnsen Graphic Solutions A/S) — CVR 18624141 |
| Just Coffee | sede | La sede registrata al CVR e' Frederiksborgvej 551, 4000 Roskilde, non Jyllinge: il riferimento a Jyllinge deriva dal testo promozionale del sito ('risteriet ligger paa en gaard i Jyllinge lige uden for Roskilde'). Il comune e' comunque Roskilde, Regi | https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Frederiksborgvej 551, 4000 Roskilde'; https://estatistik.dk/virksomhed/j | Frederiksborgvej 551, 4000 Roskilde, Regione Sjaelland |
| MC EMBALLAGE A/S | dimensione | Il dato di bilancio e' riportato senza anno di riferimento (mandato: tipo di dato + fonte + anno). Il bruttofortjeneste di 110 mio DKK e il risultato di 48,257 mio DKK si riferiscono all'esercizio 2025; gli addetti sono 87 (non '79-87'). Confermati i | https://www.proff.dk/firma/mc-emballage-as/hinnerup/engroshandel-andet/06HCM2I10N6 - 'I 2025 viste regnskabet en bruttofortjeneste paa 110 mio. DKK .. | Bruttofortjeneste 110 mio DKK (esercizio 2025, ~14,7 M€ di margine lordo), risultato 48,3 mio DKK, 87 dipendenti (proff. |
| N. EILERSEN A/S | fonte | Il CVR corretto della societa' e' 35118519 (non indicato nel record, che non riporta il numero) e nel registro esiste anche una omonima 'Eilersen A/S' CVR 42555932: rischio di confusione tra le due entita' in fase di contatto/verifica. | https://ownr.dk/companies/public-profile/35118519 ; https://virmo.dk/firma/42555932-eilersen-as | Indicare esplicitamente CVR 35118519 per N. EILERSEN A/S |
| NIELAUS A/S | dimensione | Numero di dipendenti non allineato alla fonte citata: la scheda proff.dk (CVR 35480943) riporta 19 addetti, il record ne indica 11. | https://www.proff.dk/firma/nielaus-as/bramming/m%C3%B8bler/GUJZBOI015G — frammento: "NIELAUS A/S is a furniture production company located at Vejrup S | 19 dipendenti (proff.dk, CVR 35480943) — verificare l'anno di riferimento |
| NIELAUS A/S | email | DA CONFERMARE: l'indirizzo info@nielaus.dk non compare letteralmente in nessuna fonte pubblica reperita; la pagina Kontakt del sito ufficiale protegge l'indirizzo dagli spambot e non lo espone in chiaro nei frammenti. | https://www.nielaus.dk/da/om-os/kontakt — frammento: "Email: Available on their website (protected against spambots)" |  |
| NPI (Nordic Panel Import) | denominazione | Ragione sociale imprecisa: la societa' e' registrata al CVR 37418730 come 'NPI A/S' (forma giuridica A/S, non ApS). Il record lascia il punto come non verificato. | https://www.proff.dk/firma/npi-as/l%C3%B8sning/t%C3%B8mmer-tr%C3%A6last-og-byggevarer-agentur-og-engros/0MA0H6I10LA (NPI A/S - CVR-nr 37418730 - Losni | NPI A/S (Nordic Panel Import) |
| ONECOLLECTION A/S (House of Finn Juhl) | fonte | DA CONFERMARE: l'ID proff nell'URL citato (GXS757I015G) non coincide con quello della scheda ONECOLLECTION A/S CVR 29787786 reperita (GQYY8HI016D). L'URL potrebbe puntare a una scheda diversa/obsoleta. | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D — titolo: "ONECOLLECTION A/S - CVR-nr 29787786 - Ringkøbing" | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D |
| Skagerak Denmark A/S | linkedin | Il link LinkedIn punta alla vecchia denominazione 'trip-trap-denmark-a-s'; il marchio comunica oggi come Skagerak (by Fritz Hansen). DA CONFERMARE quale pagina sia quella ufficiale attiva. | https://www.linkedin.com/company/trip-trap-denmark-a-s (denominazione storica) ; https://www.dezeen.com/2021/12/15/fritz-hansen-acquires-skagerak/ |  |
| VERMUND LARSEN A/S (VELA / VERMUND) | sito | Disallineamento tra i canali: il sito indicato (vermund.eu) e' quello del solo marchio di design 'Vermund', mentre il sito istituzionale della societa' e del marchio principale e' vela.dk (coerente con l'email mail@vela.dk e con la pagina LinkedIn 'v | https://www.vela.dk/om-vela ; https://estatistik.dk/virksomhed/vermund-larsen-as/52796628/roller - 'Ny Vela Holding ApS tiltradte som ejer 100% af vir | https://www.vela.dk/ (con vermund.eu come sito del marchio design) |

### Svezia (20)

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
| NC Nordic Care AB | sede | Indirizzo operativo/registrato discordante: allabolag colloca l'azienda a Grännäs, 615 95 Valdemarsvik (Östergötlands län), con indirizzo postale Box 30, 573 21 Tranås e säte formale a Tranås. Il foglio riporta solo «Tranås, Jönköpings län». Da preci | https://www.allabolag.se/foretag/nc-nordic-care-ab/valdemarsvik/m%C3%B6bler/2JZRNU1I5YGJV — «NC Nordic Care AB is located at Grännäs, 615 95 Valdemars | Tranås, Jönköpings län (säte); stabilimento/indirizzo Grännäs, Valdemarsvik, Östergötlands län |
| Nola Industrier AB | referente | Il nome completo registrato è Claes Henrik Edlund, ma le fonti pubbliche e aziendali lo indicano come Henrik Edlund (VD dal 2019, subentrato alla zia Agneta Stake). Il dato non è errato ma va usato nella forma d'uso corrente nei contatti. | https://sv.wikipedia.org/wiki/Nola_Industrier — «Agneta Stake lämnade över vd-skapet till systersonen Henrik Edlund år 2019»; allabolag: «VD för Nola  | Henrik Edlund (Claes Henrik Edlund) |
| Norrgavel AB | dimensione | Dato aggiornabile: il foglio riporta l'esercizio 2024 (127 986 KSEK ≈ 11,3 M€, 62 dipendenti), mentre è già disponibile il 2025 con 135 118 KSEK ≈ 12,0 M€ e 59 dipendenti. L'azienda resta pienamente in target e la conversione KSEK del foglio è corret | https://www.bolagsfakta.se/5564913381-Norrgavel_AB — «The 2025 revenue is 135,118 thousand SEK ... The company has 59 employees»; email e co-CEO: http | Fatturato 135 118 KSEK = 135,1 MSEK ≈ 12,0 M€ (2025); 59 dipendenti |
| Norrlands Trä Aktiebolag | dimensione | Lieve scostamento sul fatturato 2025: il foglio riporta 275 049 KSEK, allabolag/bolagsfakta riportano 274 677 KSEK (≈24,3 M€, +7,6%, risultato 17 561 KSEK, 41 dipendenti). Differenza marginale, ma il valore va allineato alla fonte. Confermati VD Jan  | https://www.bolagsfakta.se/5560924077-Norrlands_Tra_Aktiebolag — «omsättning of 274,677 KSEK during 2025 ... 41 employees ... result of 17,561 KSEK .. | ≈24,3 M€ / 41 dip. (allabolag 2025: 274 677 KSEK, +7,6%) |
| Rödins Trä AB | dimensione | Il valore riportato (380 291 KSEK ≈ 33,7 M€, 2025) è il fatturato CONSOLIDATO di gruppo: Rödins Trä AB è koncernmoderbolag con la controllata Ålsta Sågverk Nord AB, e il gruppo di 2 società fattura 370,0 MSEK con 37 dipendenti. Il campo non specifica | https://allabolag.se/organisation/rc3b6dins-trc3a4-ab/svenstavik/sc3a5gverk/2K092UXI5YHTM — «Rödins Trä AB är ett koncernmoderbolag med ett dotterbola | ≈33,7 M€ consolidato di gruppo (allabolag 2025: 380,3 MSEK koncern, +3%); capogruppo essa stessa, controllata Ålsta Sågv |
| Tärnsjö Garveri Aktiebolag | dimensione | Numero dipendenti non allineato alla fonte: il record indica 43 dipendenti (2024), allabolag riporta 46. | allabolag.se: «Tärnsjö Garveri Aktiebolag har 46 anställda». Fatturato 51,9 MSEK 2024 (+6%) confermato. | 46 dipendenti |

### Olanda (15)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Ascot Amsterdam B.V. | dimensione | Il campo dichiara 'numero KVK non reperito': il dato e invece pubblico. KVK 55089666, P.IVA NL85156137B01. Da integrare. | https://ascot-amsterdam.com/contact/ - 'Chamber of Commerce: 55089666 - VAT number: NL 85156137B01' | KVK 55089666, P.IVA NL85156137B01 |
| Bangma Verpakking B.V. | sito | Il sito indicato nel foglio (https://www.bangma.nl) non è il dominio istituzionale usato oggi dall'azienda, che pubblica i propri contenuti su bangmaverpakking.nl (pagina 'Historie Bangma Verpakking'). DA CONFERMARE quale dei due sia il dominio attiv | https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - pagina istituzionale corrente dell'azienda | https://bangmaverpakking.nl/ (DA CONFERMARE) |
| Beijleveld Houtimport B.V. | sito | Il dominio ufficiale indicato nelle fonti di registro e' www.beyleveld.com (coerente con l'email info@beyleveld.com); beyleveldhoutimport.com risulta un secondo dominio attivo. Verificare quale sia il sito primario. | https://www.telefoonboek.nl/bedrijven/t2585787/rotterdam/beijleveld-houtimport-b.v./ - frammento: 'Email: info@beyleveld.com - Website: www.beyleveld. |  |
| Bruns B.V. | sede | Indirizzo discordante: il record indica Riethovensedijk 20, 5571 CR Bergeijk, mentre l'anagrafica di settore riporta Stokskesweg 11, 5571 TJ Bergeijk. Il comune (Bergeijk, Noord-Brabant) e' comunque corretto. Indirizzo civico DA CONFERMARE. | http://bergeijk.gevabiz.nl/company/bruns-bv-bergeijk.html - frammento: 'Stokskesweg 11, NL-5571TJ Bergeijk' |  |
| Daarnhouwer & Co B.V. | linkedin | URL LinkedIn malformato: contiene '&' e un punto finale (/company/daarnhouwer-&-co.), che non e uno slug LinkedIn valido. Da riscrivere con lo slug reale. | valore nel record: 'https://www.linkedin.com/company/daarnhouwer-&-co.' |  |
| Daarnhouwer & Co B.V. | sede | Indirizzo di sede da precisare: le fonti riportano Korte Hogendijk 18, 1506 MA Zaandam (Panjiva indica anche 1511 Oostzaan). Il campo sede generico 'Zaandam / Zaanstad' e corretto ma non verificato all'indirizzo. | https://es.panjiva.com/Daarnhouwer-Co-B-V/34001367 - 'Daarnhouwer & Co B.V., Zaandam, 1511 Oostzaan, Netherlands'; indirizzo pubblicato Korte Hogendij |  |
| Dietz Cacao Trading B.V. | dimensione | Azienda sotto la forbice target: 5 dipendenti, fatturato non pubblicato (deposito abbreviato). Il campo dichiara esplicitamente il limite ('Sotto la fascia ideale per organico'), quindi il rilievo e solo di conferma: nessun dato consente di collocarl | https://www.oozo.nl/bedrijven/heerlen/heerlen-centrum/heerlen-centrum/171578/dietz-cacao-trading-b-v |  |
| Gaia Cacao B.V. | dimensione | Il campo dichiara 'n. dipendenti non pubblicato': il dato e invece disponibile (ca. 8 dipendenti, Creditsafe/Kompass) e conferma la costituzione nel 2020. Resta comunque un'azienda sotto la forbice 5-40 M€, come gia segnalato nel campo. | https://www.creditsafe.com/business-index/en-gb/company/gaia-cacao-bv-nl05437910 - 'Gaia Cacao has approximately 8 employees'; https://us.kompass.com/ | ca. 8 dipendenti (Creditsafe, 2025); costituita nel 2020 |
| Gras Wood Wide B.V. | dimensione | Anno di fondazione errato: il record indica 1921, mentre azienda e stampa di settore datano la fondazione al 1868 (sesta generazione familiare, coerente). Il 1921 corrisponde semmai a una successiva iscrizione societaria. | https://www.houtwereld.nl/bedrijven/gras-wood-wide-b-v/ e https://www.graswoodwide.com/over-ons/ - frammento: 'founded in 1868' | Fondata nel 1868 |
| Gras Wood Wide B.V. | linkedin | Campo LinkedIn vuoto benche' esista la pagina aziendale ufficiale. | https://nl.linkedin.com/company/graswoodwide - titolo: 'Gras Wood Wide \| LinkedIn' | https://nl.linkedin.com/company/graswoodwide |
| Houtimport Lekkerkerker B.V. | dimensione | Il campo deduce la fascia 10-20 M EUR dal volume (ca. 200.000 m3/anno) senza alcuna fonte di fatturato: la stima non e' sostenuta e va marcata come tale. Il volume in se' e' l'unico dato dichiarato con tipo e fonte. | https://www.houtimportlekkerkerker.nl/ e https://www.creditsafe.com/business-index/en-us/company/houtimport-lekkerkerker-bv-nl01698016 (nessun fattura |  |
| PaBrEm B.V. | linkedin | Campo LinkedIn vuoto e nessuna pagina aziendale reperita: il lead non ha canale social verificabile. DA CONFERMARE. | nessun risultato LinkedIn per PaBrEm B.V. nelle ricerche effettuate |  |
| Smeulders Interieurwerken B.V. | referente | Referente riportato con la sola iniziale ('A. Smeulders'). Il nome completo pubblicato e Anton Smeulders, alla guida dell'azienda dal 1992; la proprieta fa capo a Holding Smeulders B.V. | https://smeulders-ig.nl/over-ons/ - 'Anton Smeulders ... leidt het bedrijf sinds 1992'; proprieta Holding Smeulders B.V. | Anton Smeulders |
| Van de Stadt Houtimport B.V. | dimensione | Indirizzo di sede indicato nel campo ('sede portuale Noorder IJ- en Zeeweg') non coincide con quello registrato oggi: KVK/Drimble e il sito riportano Rijshoutweg 31, 1505 HL Zaandam. Dato di sede obsoleto. | https://drimble.nl/bedrijf/zaandam/15832708/van-de-stadt-houtimport-bv.html - 'Van de Stadt Houtimport B.V. Rijshoutweg'; https://www.telefoonboek.nl/ | Rijshoutweg 31, 1505 HL Zaandam |
| Van den Berg Hardhout B.V. | linkedin | URL LinkedIn probabilmente errato: la pagina aziendale reperibile e /company/van-den-berg-hardhout-bv---lopik, non /company/vandenberghardhout. | https://nl.linkedin.com/company/van-den-berg-hardhout-bv---lopik - 'Van den Berg Hardhout BV \| LinkedIn' | https://nl.linkedin.com/company/van-den-berg-hardhout-bv---lopik |

### Belgio (32)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Antilope De Bie NV | dimensione | Refuso sull'anno del bilancio: il fatturato 15.593.574 € e i 72,1 FTE sono confermati, ma l'ultimo bilancio e' stato depositato il 10-07-2025, non nel 2024 come indicato. Da segnalare inoltre che l'azienda dichiara alla stampa 85 collaboratori (grupp | fincheck.be/nl/antilope-de-bie/0414.535.339/Duffel/overzicht: 'de meest recente jaarrekening werd neergelegd op 10-07-2025 ... 72,1 VTE'; made-in.be:  | Fatturato 15.593.574 € - 72,1 FTE (bilancio NBB depositato 10-07-2025) |
| Antilope De Bie NV | referente | Referente confermato (Bart De Bie, CEO, quarta generazione) ma incompleto: la direzione e' condivisa con il fratello Johan De Bie, che ha rilevato la drukkerij insieme a lui nel 1996. Segnalazione puramente formale. | made-in.be/mechelen/bart-de-bie-ceo-antilope-de-bie: 'Bart De Bie (CEO Antilope De Bie) ... Hij en zijn broer Johan zijn de vierde generatie van drukk | Bart De Bie (con il fratello Johan De Bie) — CEO / gedelegeerd bestuurder |
| Autajon Packaging Belgium SA | email | L'e-mail contact@autajon.com e il sito www.autajon.com sono il recapito e il dominio generici della capogruppo francese, non della societa' belga: un contatto inviato li' non raggiunge lo stabilimento di Anderlecht. Esiste una pagina dedicata alla se | https://www.autajon.com/en/locations/packaging-belgium-bruxelles/ (scheda della sede di Bruxelles del gruppo Autajon) |  |
| Belignum NV | dimensione | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato il 02-07-2024 (esercizio 2023). La cifra di EUR 16. | https://trendstop.knack.be/nl/detail/405348449/belignum.aspx - 'omzet van 14.746.642 euro, 40e in de sector houthandel... laatst neergelegde jaarreken | Fatturato EUR 14.746.642, esercizio 2023 (bilancio depositato 02-07-2024), 10,8 FTE - eliminare il riferimento a 16.075. |
| Bruyerre Chocolates SA | linkedin | Campo LinkedIn vuoto: esiste una pagina aziendale belga attiva. Da verificare se copra la sola Bruyerre Chocolates SA o l'intero marchio Bruyerre (che include anche Bruyerre SA distribuzione, BE 0431.703.151). | https://be.linkedin.com/company/bruyerre | https://be.linkedin.com/company/bruyerre (DA CONFERMARE la corrispondenza con l'entita' 0688.794.525) |
| Buzzispace NV | dimensione | Il campo indica la produzione 'in Kempen' (implicitamente Belgio): le fonti aziendali collocano lo stabilimento produttivo a Bladel, nei Paesi Bassi. La sede sociale ad Anversa resta corretta, ma l'attivita' manifatturiera non e' belga; l'azienda ha  | https://officeinsight.com/officenewswire/buzzispace-appoints-new-ceo-announces-new-role-for-former-ceo-and-founder/ - frammento: "showrooms in Antwerp |  |
| Callens NV (Callens African Woods) | referente | Thierry Maelfait risulta confermato alla guida, ma dal 2021-2022 e' entrata in azienda la figlia Sam Maelfait, indicata dalle fonti come zaakvoerster/marketingverantwoordelijke: verificare chi sia oggi il rappresentante legale. Nota formale: per una  | https://www.voka.be/nieuws/west-vlaanderen-ondernemers-2024-19/callens-african-woods-heeft-productiefaciliteiten-kameroen - frammento: "Sam Maelfait,  |  |
| Cartonnages Delsaux SA | ruolo | 'Amministratore' non e' un titolo statutario belga. Per una SA vallona il titolo corretto e' administrateur delegue (o administrateur). La co-direzione familiare con Charles e Sylvie Delsaux e' confermata dalle fonti. | ccimag.be/2019/05/28/cartonnages-delsaux-cartons-pousser-fleurs/: 'Christophe Delsaux et Charles Delsaux, avec leur soeur Sylvie, dirigent l'entrepris | Administrateur delegue |
| Chocolaterie Ickx NV | dimensione | Fatturato confermato nell'ordine di grandezza ma con cifra leggermente diversa dalla fonte: trendstop/pappers riportano 32.272.193 € (27° posto di settore) contro i 32.746.626 € del record. FTE 139,7 e deposito 26-03-2026 confermati. | Frammento: "With a turnover of 32,272,193 euros, Chocolaterie Ickx is ranked 27th in the chocolate and confectionery sector" — https://www.pappers.be/ |  |
| Confiserie Vandenbulcke NV | denominazione | La denominazione registrale in KBO/trendstop e' 'Vandenbulcke Confiserie NV' (ordine invertito rispetto al record); il marchio commerciale e' 'Chocolatier Vandenbulcke'. Il sito indicato e' corretto (vandenbulcke.com). | https://trendstop.knack.be/nl/detail/417738319/vandenbulcke-confiserie.aspx — "Vandenbulcke Confiserie NV - BE 0417.738.319 - Heule (8501)" | Vandenbulcke Confiserie NV |
| Corné Port-Royal Chocolatier SA | denominazione | La denominazione registrale completa e' 'CORNE PORT-ROYAL CHOCOLATIER, en abrege CPR CHOCOLATIER'; companyweb indicizza l'impresa come 'CPR CHOCOLATIER (SA)'. Refuso formale: nel record manca la sigla registrale. | https://www.companyweb.be/en/0433283558/corne-port-royal-chocolatier — titolo "CPR CHOCOLATIER (SA) - Wavre (1300) - BE0433283558"; https://trademarks | Corne Port-Royal Chocolatier SA (in abbreviato CPR Chocolatier SA) |
| Corpack NV | sede | Denominazione del comune superata: dopo la fusione del 2025 la sede legale risulta registrata come Doornpark 20, 9120 Beveren-Kruibeke-Zwijndrecht (non piu' 'Beveren-Waas'). Refuso puramente formale, l'indirizzo e la provincia (Oost-Vlaanderen) sono  | companyweb.be/en/0452991978/corpack: 'Corpack (NV) - Beveren-Kruibeke-Zwijndrecht (9120)'; trendstop: 'Doornpark(BEV) 20, 9120 Beveren-Kruibeke-Zwijnd | Beveren-Kruibeke-Zwijndrecht (ex Beveren-Waas), Provincia di Fiandre Orientali (Fiandre) |
| Decadt Houthandel NV | ruolo | Stefaan Decadt e' confermato al vertice, ma il ruolo pubblicato e' 'bedrijfsleider' (LinkedIn) e non 'Algemeen directeur'; per una NV il titolo statutario sarebbe 'gedelegeerd bestuurder'. Inoltre coesistono due siti web riferiti a Decadt a Vlamertin | https://be.linkedin.com/in/stefaan-decadt-8b8144113 - frammento: "Stefaan Decadt - bedrijfsleider bij decadt houthandel nv"; siti concorrenti https:// | Ruolo: Bedrijfsleider / gedelegeerd bestuurder |
| Decadt Houthandel NV | dimensione | Data di fondazione discordante: il campo indica 01-01-1975 (data di costituzione della NV) mentre le fonti aziendali datano l'attivita' al 1927. Fatturato 13.460.408 EUR confermato. | https://trendstop.knack.be/nl/detail/415284714/decadt-houthandel.aspx - frammento: "With a turnover of 13,460,408 euros, Decadt Houthandel is ranked 4 |  |
| Denderwood NV | dimensione | Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta indeterminata e potenzialmente sotto la soglia dei 5 M EUR. Il campo lo dichiara ('TAGLIA DA VERIFICARE'), ma il dato non e' riscontrabile su NBB. Resto del record | https://www.atibt.org/en/members/24/denderwood e https://www.denderwood.com/over-ons/ - frammento: "Denderwood is located at J. Cardijnstraat, 3 B-942 |  |
| Hannecard Benelux NV | linkedin | Il LinkedIn indicato (linkedin.com/company/hannecard-nv) e' la pagina del gruppo Hannecard, non della sola Hannecard Benelux NV: coerente con il rilievo sul legame di gruppo. Non e' un errore grave ma va segnalato che il contatto porta alla capogrupp | https://www.linkedin.com/company/hannecard-nv — pagina unica del gruppo; https://trendstop.knack.be/nl/detail/694906812/hannecard-benelux.aspx (entita |  |
| Hercorub NV | dimensione | Il numero di addetti e' riportato come forbice generica ('ca. 67-95 dipendenti, fonte aziendale') invece che come dato NBB: va sostituito con il dato FTE dell'ultimo bilancio depositato. Fatturato (15.240.806 EUR) e numero d'impresa confermati. Da ag | https://trendstop.knack.be/nl/detail/421767381/hercorub.aspx — "Hercorub recorded a total turnover of EUR 15,240,806.00"; https://www.hercorub.be/p/ho |  |
| Hercorub NV | referente | Il referente indicato (Patrick Lenaerts, afgevaardigd bestuurder) e' confermato, ma la societa' ha due gedelegeerd bestuurders: Patrick Lenaerts e Suzy Hermans. Nessun errore, solo integrazione. Confermato anche l'uso di gomma naturale (NR) nelle mes | https://www.hercorub.be/p/geschiedenis.html — "Patrick Lenaerts en Suzy Hermans werden gedelegeerd bestuurders van Hercorub"; https://www.hercorub.be/ |  |
| Hulpiau Hides BV | dimensione | Il campo usa come proxy dimensionale il margine lordo (2.284.726 EUR) di UN'ALTRA entita' giuridica (Hulpiau BV, BE 0429.082.864), non della societa' target BE 0777.875.662, che deposita a schema abbreviato e non pubblica il fatturato. Dato confermat | https://www.companyweb.be/en/0777875662/hulpiau-hides - frammento: "There are 6.1 FTEs working at Hulpiau Hides according to staff figures in the most |  |
| Klingele Chocolade NV | referente | Referente confermato (Koen Klingele, cofondatore 1995) ma incompleto: la societa' e' co-gestita dalla moglie Eline Blanchaert, indicata dalle fonti come zaakvoerder alla pari. Da notare che le fonti usano 'zaakvoerder', titolo proprio della BV, mentr | vrt.be/vrtnws/nl/2025/11/05: 'Koen Klingele en Eline Blanchaert, zaakvoerders van Klingele Chocolade'; jaarrekening.be/nl/KLINGELE-CHOCOLADE/0479.916. | Koen Klingele (con Eline Blanchaert) — gedelegeerd bestuurder |
| Lavrijsen Houtbedrijf NV | ruolo | Jan e Bert Lavrijsen sono confermati alla guida dell'azienda, ma per una NV il titolo statutario corretto e' 'gedelegeerd bestuurder / bestuurder', non 'zaakvoerder' (termine proprio delle BV). | https://lavrijsen.be/over-ons/ - frammento: "Jan and Bert Lavrijsen are at the helm of the company with secured succession" | Bestuurders / gedelegeerd bestuurders |
| Le Cercle du Cacao SRL | sede | Sede incoerente con la fonte aziendale: il sito ufficiale indica Rue des Sables 16, boite 4, 1000 Bruxelles (Bruxelles-Ville), non Schaerbeek 1030. DA CONFERMARE quale sia la sede sociale attuale iscritta alla BCE. | lecercleducacao.be/contact/: 'Le Cercle du Cacao est situé Rue des Sables 16, Boite 4 - 1000 Bruxelles' | Bruxelles-Ville (1000) — Regione di Bruxelles-Capitale |
| Libeert NV | sede | Refuso formale: la sede registrale e' Avenue des Chateaux 107A, 7780 Comines-Warneton; il record scrive la forma giuridica come NV mentre companyweb indicizza l'impresa come SA (societa' vallona francofona). Coerenza da sistemare fra denominazione (L | https://www.companyweb.be/en/0407026747/libeert — "Libeert (SA) - Comines-Warneton (7780) - BE0407026747" | Libeert SA |
| Manufacture Belge de Chocolats SRL | referente | Il ruolo 'CEO' attribuito ad Arnaud Verwilghen e' confermato da un'intervista del giugno 2026, ma altre fonti professionali lo indicano come Supply Chain & Finance Director e affiancano un secondo CEO (Jerome Chouchan, vertice di Godiva Japan). Titol | https://businessfocusmagazine.com/2026/06/03/manufacture-belge-de-chocolats-belgian-tradition-interview-with-ceo-arnaud-verwilghen/ ; https://www.apol |  |
| Manufacture Belge de Chocolats SRL | linkedin | Campo LinkedIn vuoto: esiste la pagina aziendale belga. | https://be.linkedin.com/company/manufacture-belge-de-chocolats | https://be.linkedin.com/company/manufacture-belge-de-chocolats |
| Meubelfabriek Lievens NV | ruolo | Lieven Decoene e' confermato come 'general manager' operativo, ma il mandato statutario della NV e' esercitato da Telinfra (VA Telifra) con rappresentante permanente Andre Ollevier. Il ruolo indicato non e' quello statutario belga (gedelegeerd bestuu | pappers.be/nl/company/meubelfabriek-lievens-0413666990: 'VA Telifra — Andre Ollevier, vaste vertegenwoordiger/zaakvoerder'; wonen360.nl: 'general mana | Lieven Decoene — General Manager (rappresentante legale: Telinfra, rappr. perm. Andre Ollevier) |
| Oxfam Fair Trade CV | linkedin | Campo LinkedIn vuoto: esiste la pagina aziendale belga. | https://be.linkedin.com/company/oxfam-fair-trade | https://be.linkedin.com/company/oxfam-fair-trade |
| Passe Partout NV | ruolo | Il titolo 'Zaakvoerder' e' proprio delle BV; per una NV il titolo statutario corretto e' gedelegeerd bestuurder / bestuurder. Dirk Steenbeke e' comunque confermato come fondatore e vertice attuale. | wonen360.nl 'Dirk Steenbeke van Passe Partout' (fondatore/CEO); verhouden.nl/ontwerpers/dirk-steenbeke | Gedelegeerd bestuurder |
| Radermecker SRL | dimensione | Discordanza sugli addetti: il record indica 9,1 FTE (bilancio BNB), mentre la scheda Europages dichiara 20-49 dipendenti. Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta non verificabile. | https://www.europages.fr/TANNERIE-RADERMECKER/BEL069426-000019048001.html - frammento: "The company employs between 20 and 49 people" |  |
| Royal Botania NV | ruolo | 'CEO e cofondatore' non e' un titolo statutario belga; per una NV il titolo corretto e' gedelegeerd bestuurder / bestuurder (le fonti usano 'zaakvoerder', incoerente con la forma NV). | https://www.apbc.be/stories/awd-2-kris-van-puyvelde-royal-botania | Gedelegeerd bestuurder |
| Silco NV | sito | Nessun sito web proprio reperito per Silco NV in 3 ricerche: l'azienda compare solo su banche dati societarie (trendstop, companyweb, fincheck, northdata, staatsbladmonitor). Coerente con la struttura a 1 FTE. Il campo vuoto e' quindi corretto, ma va | https://www.northdata.com/Silco%20N.V.,%20Antwerpen/KBO%200715.792.692 - solo scheda registro; nessun dominio aziendale nei risultati | n.d. (nessun sito web aziendale) |
| VC Wood Zottegem NV | linkedin | L'URL LinkedIn indicato (company/vc-wood-zottegem) non corrisponde alla pagina che emerge dalle ricerche, che e' company/vc-wood. DA CONFERMARE quale delle due sia attiva. | https://be.linkedin.com/company/vc-wood (risultato di ricerca per 'VC Wood Zottegem houthandel') | https://be.linkedin.com/company/vc-wood |

### Austria (13)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| HOLZBAU MAIER GmbH & Co KG | dimensione | Il fatturato di ca. 35,0 Mio EUR e' una stima non ufficiale di die-deutsche-wirtschaft.de e non riporta l'anno di riferimento, come richiesto per i dati dimensionali. Confermati invece FN 525501x/LG Salzburg e la co-GF Hildegund Maier. | https://www.maier.at/de/impressum.html - frammento: "Geschaeftsfuehrer: Hildegund Maier (representing since 07.04.2005) and Dipl.Ing Birgit Maier (07. |  |
| Holzindustrie Schafler GmbH & Co KG | ruolo | Il ruolo riportato ('Gewerberechtlicher Geschaeftsfuehrer') sottostima la posizione: l'Impressum aziendale indica Bernd (Christoph) Schafler come Geschaeftsfuehrer e proprietario, quarta generazione familiare. | https://www.schafler-holz.at/impressum - frammento: "Geschaeftsfuehrer: Bernd Schafler... current managing director and owner Bernd Christoph Schafler | Geschäftsführer / Inhaber |
| Karnische Massiv Möbel GmbH | denominazione | Ragione sociale a Firmenbuch: 'Karnische-Massiv-Moebel Gesellschaft m.b.H.' (con trattini), FN 094638z, LG Klagenfurt; 'Karnische Massiv Moebel GmbH' e' il nome commerciale. Refuso formale. Confermati invece GF Werner Hohenwarter (fratello Otto Proku | https://www.firmenabc.at/karnische-massiv-moebel-gesellschaft-m-b-h_Xyc e https://www.northdata.de/Karnische-Massiv-M%C3%B6bel%20GmbH,%20Kirchbach/094 | Karnische-Massiv-Möbel Gesellschaft m.b.H. |
| MAFI Naturholzboden GmbH | dimensione | Il fatturato di 22,3 Mio EUR e' datato al 2017 nel record, ma la fonte (die-deutsche-wirtschaft.de) lo presenta come dato piu' recente disponibile con crescita del 2,8% rispetto a una stima precedente di 20,0 Mio EUR. Anno di riferimento da riconferm | https://die-deutsche-wirtschaft.de/famu_top/oesterreich-mafi-naturholzboden-gmbh-schneegattern-umsatz-mitarbeiterzahl/ - frammento: "The most recent a |  |
| Mühlbauer Holz GmbH | sede | Himberg e' la sede operativa (Franz-Lehn-Gasse 7, 2325 Himberg), ma la sede legale iscritta al Firmenbuch e' 1080 Wien, Laudongasse 47/52 (anche l'iscrizione WKO e' su Vienna). | https://www.evi.gv.at/f/283235y (titolo: 'Mühlbauer Holz GmbH 1080 Wien \| Firmenbuch'); https://firmen.wko.at/m%C3%BChlbauer-holz-gmbh/wien/ | Himberg (Niederösterreich) — sede operativa; sede legale 1080 Wien |
| Mühlbauer Holz GmbH | referente | Referente corretto ma recentissimo e da datare: DI Joe Mühlbauer-Elbl e' iscritto come Geschäftsführer dal 04.02.2025, dopo la morte del titolare/GF Ing. Franz Mühlbauer (febbraio 2025). Diverse fonti (incl. l'Impressum aziendale indicizzato) riporta | https://www.holzkurier.com/content/holz/holzkurier/de/holzprodukte/2025/02/franz-muehlbauer-verstorben-.html ; https://www.wirtschaft.at/u/283235y ('v |  |
| SCHAFFER SÄGEWERK-HOLZEXPORT GmbH | ruolo | Markus Schaffer risulta Geschäftsführer a tutti gli effetti dal 01.06.2016 nel Firmenbuch (non solo 'gewerberechtlicher'). Nell'Impressum del sito compare invece come 'Prok. Schaffer Markus'. Il ruolo indicato va semplificato in Geschäftsführer. E-ma | https://www.evi.gv.at/f/137937z ('Markus Schaffer ... seit 01.06.2016'); https://www.schafferholz.com/en/legal-information/ ('Prok. Schaffer Markus, F | Geschäftsführer |
| Speedmaster GmbH | referente | La societa' ha due Geschäftsführer: Dipl.-Ing. (FH) Hermann Huber e Günther Schweiger (Prokurist: Dr. Philipp Waechter). Hermann Huber e' corretto, ma va indicata la co-gestione con Schweiger, coerente con la nota di scissione da Schweiger GmbH ripor | https://www.evi.gv.at/f/262852y ; https://www.wirtschaft.at/u/262852y (GF: Hermann Huber, Günther Schweiger; Prok. Philipp Waechter) |  |
| Storebest Ladeneinrichtungen GmbH | denominazione | Ragione sociale esatta a Firmenbuch: '"Storebest" Ladeneinrichtungen Gesellschaft m.b.H.' (FN 117692b); 'Storebest Ladeneinrichtungen GmbH' e' il nome commerciale. | https://www.firmenabc.at/storebest-ladeneinrichtungen-gesellschaft-m-b-h_um ; https://firmen.wko.at/%22storebest%22-ladeneinrichtungen-gesellschaft-mb | "Storebest" Ladeneinrichtungen Gesellschaft m.b.H. |
| Wallner Holzhandel GmbH | referente | Gerhard Wallner e' Geschäftsführer a pieno titolo (non solo 'gewerberechtlicher') e la gestione e' condivisa con Mag. Hans-Christian Riegler, BWL, secondo Geschäftsführer indicato nell'Impressum aziendale. | https://www.holz-wallner.at/de/impressum ('Geschäftsführung: Gerhard Wallner, Mag. Hans-Christian Riegler BWL; FN 267061m, HG St. Pölten'); https://ww | Geschäftsführer (con Mag. Hans-Christian Riegler) |
| Wallner Holzhandel GmbH | dimensione | L'organico dichiarato (80 dipendenti da WKO/herold) e' inferiore al dato pubblicato dall'azienda: 90 dipendenti. Il fatturato resta non pubblicato, quindi la fascia stimata 20-30 Mio EUR e' priva di riscontro documentale. | https://www.holz-wallner.at/de/impressum / https://www.holz-wallner.at/de/home ('90 Mitarbeiter', Holzgroß- und -einzelhandel, sedi Porschestraße 13 S | 90 dipendenti (holz-wallner.at); fatturato non pubblicato |
| steininger.designers gmbh | referente | Dato corretto ma incompleto: la Geschäftsführung e' collegiale. Nell'Impressum figurano Mag. Martin Steininger (GF dal 14.10.2008) e Arch. DI Harrytasch Ahmadian. Nessun rilievo su e-mail, sito e sede, tutti confermati (Weinleiten 1, 4113 St. Martin  | https://www.steiningerdesigners.com/impressum-agbs ('Geschäftsführer: Arch. DI Harrytasch Ahmadian, Mag. Martin Steininger; FN 317900a, Landesgericht  |  |
| weinberger-holz gmbh | dimensione | Il tribunale del registro e' errato: il Firmenbuch di weinberger-holz gmbh (FN 119447h) e' tenuto dal Bezirksgericht Wolfsberg, non dal 'LG Wolfsberg'. Inoltre anche qui il totale di bilancio (16,77 Mio EUR) non e' un fatturato: il dato di ricavi non | https://www.weinberger-holz.at/en/impressum/ ('FN 119447h, Bezirksgericht Wolfsberg'; gewerberechtliche Geschäftsführung Dipl.Ing. Johann Alfred Weinb | Totale di bilancio 16,77 Mio EUR (31.12.2024, firmenabc.at); fatturato non pubblicato. FN 119447h, BG Wolfsberg |

### (tutti) (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| (controllo di rientro) | denominazione | nessuna delle 7 aziende rimosse e' rientrata nei fogli. Controllo eseguito su _records.json (742 record, tutti i fogli) cercando in ogni campo, con radici tolleranti alle varianti: 'getama', 'dragsb', 'pacorini', 'immobra', 'lavazza', 'segafredo', 'k | Verifica programmatica su _myeudr_build/verifica/_records.json: per ciascuna delle 7 radici, 0 corrispondenze nel campo 'denominazione' su tutti i 742 |  |
