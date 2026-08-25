# REPORT DI VERIFICA — MyEUDR Lead Mapping

Verifica record per record del censimento (742 aziende, 8 fogli). Fase A: controlli deterministici offline. Fase B: riscontro sul web, record per record.

**Totale rilievi Fase B: 66** (alta 14 · media 29 · bassa 23).


## Sintesi per foglio

| Foglio | Rilievi | alta | media | bassa | Aziende toccate |
|---|--:|--:|--:|--:|--:|
| Italia | 0 | 0 | 0 | 0 | 0 |
| Germania | 0 | 0 | 0 | 0 | 0 |
| Finlandia | 0 | 0 | 0 | 0 | 0 |
| Danimarca | 26 | 9 | 8 | 9 | 17 |
| Svezia | 3 | 0 | 1 | 2 | 2 |
| Olanda | 4 | 1 | 2 | 1 | 2 |
| Belgio | 32 | 4 | 18 | 10 | 19 |
| Austria | 0 | 0 | 0 | 0 | 0 |
| (tutti) | 1 | 0 | 0 | 1 | 1 |
| **TOTALE** | **66** | **14** | **29** | **23** | **41** |

## Rilievi per campo

| Campo | Rilievi | alta |
|---|--:|--:|
| dimensione | 23 | 5 |
| referente | 15 | 4 |
| denominazione | 11 | 5 |
| email | 7 | 0 |
| ruolo | 3 | 0 |
| sito | 2 | 0 |
| filiera | 2 | 0 |
| sede | 1 | 0 |
| fonte | 1 | 0 |
| linkedin | 1 | 0 |

---

## Casi di gravità ALTA (14)

_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, oppure fuori dal perimetro dell'Allegato I EUDR._


### Danimarca (9)

**AUBO PRODUCTION A/S** — campo `referente`  
Referente non attuale: Torben Andersen è il PREDECESSORE. La carica di administrerende direktør è passata a Torben Paulin (ingresso registrato 22.01.2026 secondo lasso.dk). Contattare Torben Andersen come vertice attuale è un dato falso.  
*Evidenza:* https://lasso.dk/firmaer/28854846/ny-administrerende-direktr-i-aubo-production-as/ — titolo "Ny administrerende direktør i AUBO PRODUCTION A/S"; frammento: "Torben Paulin overtook the position of administrerende direktør (CEO) at AUBO PRODUCTION A/S from Torben Andersen"  
*Correzione proposta:* Torben Paulin — Adm. direktør

**BØJSØ DØRE & VINDUER A/S** — campo `denominazione`  
Lead non indipendente: dal 2017 la società è controllata da INWIDO DENMARK A/S, parte del gruppo quotato svedese Inwido AB (fatturato di gruppo ~9 mld SEK nel 2025). Secondo il mandato una controllata di un gruppo estero non è un lead valido, perché la due diligence EUDR viene decisa a livello di capogruppo. Il campo dimensione lo segnala ma il record resta classificato come lead.  
*Evidenza:* https://www.proff.dk/firma/b%C3%B8js%C3%B8-d%C3%B8re-vinduer-as/vorbasse/producenter/GJL0QJI016D — frammento: "Bøjsø Døre & Vinduer A/S has INWIDO DENMARK A/S as its parent company. Since 2017, Bøjsø has been part of the listed company Inwido"  
*Correzione proposta:* Escludere o riclassificare il lead: indirizzare il contatto alla capogruppo Inwido Denmark A/S

**HVIDBJERG VINDUET A/S** — campo `referente`  
Referente errato: Claus Arberg non risulta l'administrerende direktør attuale. Il vertice esecutivo è Morten Filtenborg Mortensgaard (pagina Kontakt del sito ufficiale, aprile 2026).  
*Evidenza:* https://www.hvidbjergvinduet.dk/kontakt/ — frammento: "Morten F. Mortensgaard is the managing director (based on their contact page from April 2026)"; "Morten Filtenborg Mortensgaard is the Managing Director (Administrerende direktør)"  
*Correzione proposta:* Morten Filtenborg Mortensgaard — Adm. direktør

**HVIDBJERG VINDUET A/S** — campo `dimensione`  
Assetto proprietario errato e lead non indipendente: il campo indica come controllante "Hvidbjerg i A/S", ma la società è controllata dal gruppo ACO Nordic, a sua volta parte del gruppo tedesco ACO (famiglia Ahlmann), dal rilevamento del gruppo Plastmo nel 1995. Controllata di gruppo estero: la due diligence EUDR si decide a livello di capogruppo.  
*Evidenza:* https://da.wikipedia.org/wiki/Hvidbjerg_Vinduet — frammento: "is a subsidiary of ACO Nordic Group, which is part of the German ACO Group, owned by Thomas Iver Ahlmann. In 1995, ACO Group took over the Danish company Plastmo Group, which consisted of Plastmo A/S and Hvidbjerg Vinduet A/S"; cfr. https://www.aco.dk/aco/aco-nordic  
*Correzione proposta:* Controllata del gruppo tedesco ACO (via ACO Nordic) — escludere o riclassificare il lead, contatto a livello di capogruppo

**HØRNING PARKET A/S** — campo `referente`  
Referente e ruolo errati: Peter (Christian Saaby) Mathiasen è presidente del consiglio di amministrazione (bestyrelsesformand), non adm. direktør. Il vertice esecutivo della società è Peter Vissing, direktør/adm. direktør e co-proprietario dal 2016.  
*Evidenza:* https://www.proff.dk/firma/h%C3%B8rning-parket-as/skanderborg/producenter/GTM41UI016D — frammento: "a director named Peter Vissing and board chairman Peter Christian Saaby Mathiasen ... has 24 employees"; https://rocketreach.co/peter-vissing-email_99791140 — "Peter Vissing ... CEO and Partner at Hørning Parket A/S"  
*Correzione proposta:* Peter Vissing — Adm. direktør

**JKE DESIGN A/S** — campo `denominazione`  
Lead non indipendente: la società appartiene al gruppo BALLINGSLÖV INTERNATIONAL DANMARK A/S / Ballingslöv International AB (gruppo svedese, Stena Adactum), con presidente del CdA e consigliere espressi dalla capogruppo (Björn Friedrich Hauber, Magnus Hegdal). Secondo il mandato una controllata di un gruppo estero non è un lead valido: la due diligence EUDR si decide a livello di capogruppo.  
*Evidenza:* https://ballingslovinternational.se/en/businesses/jke-design/ e https://www.proff.dk/firma/jke-design-as/jerslev-j/producenter/GKNXIBI016D — frammento: "The company is part of the Ballingslöv International Danmark A/S and Ballingslöv International AB group ... Björn Friedrich Hauber serves as board chairman and Magnus Hegdal is a board member"  
*Correzione proposta:* Escludere o riclassificare il lead: contatto a livello di capogruppo Ballingslöv International AB

**Naturli' Foods** — campo `dimensione`  
RILIEVO EMERSO DAL CONTROLLO DI RIENTRO. Il record dichiara esso stesso che Naturli' Foods e' 'parte del gruppo Dragsbaek/Orkla': e' quindi una controllata del gruppo norvegese quotato Orkla ASA, per la stessa ragione per cui Dragsbaek era stata rimossa dalla raccolta. Non e' un rientro formale (denominazione diversa) ma sostanzialmente reintroduce nel foglio un'entita' dello stesso gruppo: la compliance EUDR si decide a livello di capogruppo Orkla, quindi il lead non e' valido. Si aggiunge che la dimensione e' 'n.d.' (nessun dato di fatturato o dipendenti) e che la filiera dichiarata e' 'Olio di palma' sulla base di una FAQ del sito che dichiara solo l'uso di olio di palma RSPO in parte della gamma: perimetro EUDR marginale e non quantificato.  
*Evidenza:* Record _records.json, foglio Danimarca riga 86, campo dimensione: 'parte del gruppo Dragsbaek/Orkla (CVR 25476573)'; fonte del record https://www.naturli-foods.com/faq/oils/  
*Correzione proposta:* Rimuovere il lead (controllata Dragsbaek/Orkla, stessa motivazione della rimozione di Dragsbaek)

**TJOERNEHOEJ MOELLE A/S** — campo `dimensione`  
LEAD NON VALIDO. A/S Tjoernehoej Moelle (CVR 34175012) NON e' un'impresa indipendente: e' stata acquistata da DLG nel 1989 dal mugnaio Sander Petersen ed e' oggi una controllata della cooperativa DLG (25.000 agricoltori danesi), che la elenca esplicitamente tra le proprie societa' insieme a Vitfoss e Dangroent; la produzione e' commercializzata sotto il marchio Equsana, brand DLG dal 2012. Coerentemente, la sede legale registrata risulta a Koebenhavn V (sede DLG) e non a Hedehusene (dove resta lo stabilimento, Tingstedvej 47, 2640 Hedehusene). La compliance EUDR si decide a livello di capogruppo DLG.  
*Evidenza:* https://equsana.dk/om-equsana/tjoernehoej-moelle/ e https://www.dlg.dk/Energy-and-Retail/Retail/Equsana-alt-til-hest - 'DLG ejer datterselskaberne Tjoernehoej Moelle, Vitfoss og Dangroent'; 'Tjoernehoej Moelle blev koebt af DLG i 1989 af moeller Sander Petersen'; https://lasso.dk/firmaer/34175012/as-tjrnehj-mlle - 'A/S TJOERNEHOEJ MOELLE - Koebenhavn V'  
*Correzione proposta:* Rimuovere il lead (controllata del gruppo DLG) oppure riqualificarlo come stabilimento del gruppo DLG

**VESTJYSK SPECIALFODER ApS** — campo `denominazione`  
Ambiguita' PARZIALMENTE risolta: il fallimento riguarda l'omonima 'VestjyDsk Specialfoder ApS' CVR 39680718 (konkurs decretato dallo Skifteretten di Holstebro il 26-02-2020, curatore avv. Michael Joergensen, Bliddal & Holmstroem, Videbaek), NON la societa' del foglio. Resta pero' un'incoerenza nel record stesso: il campo dimensione indica CVR 38786709 mentre il campo fonte cita anche lasso.dk/firmaer/42242993 (un TERZO numero CVR) per la stessa denominazione. Esiste inoltre la ditta individuale omonima CVR 86607514. Quale delle entita' 'Vestjysk' sia quella operativa e attiva oggi resta DA CONFERMARE.  
*Evidenza:* https://konkurser.dk/konkurs/?id=102386 e https://www.proff.dk/firma/vestjydsk-specialfoder-aps-under-konkurs/vemb/n%C3%A6rings-og-nydelsesmidler/GXIFOUI116S/ - 'Vestjydsk Specialfoder ApS Under Konkurs - 39680718 ... ved dekret af 26. februar 2020 tog Skifteretten i Holstebro Vestjydsk Specialfoder ApS under konkursbehandling'; https://www.proff.dk/firma/vestjysk-specialfoder-aps/vemb/engroshandel-annet/GYZVKCI10N6/ - 'Vestjysk Specialfoder ApS, CVR 38786709, Industrivej 2, 7570 Vemb, startdato 11-07-2017'; https://lasso.dk/firmaer/42242993/vestjysk-specialfoder-aps  
*Correzione proposta:* Allineare il record a un unico CVR (38786709 secondo proff.dk) ed eliminare il riferimento a lasso.dk/42242993 se non pertinente


### Olanda (1)

**Bangma Verpakking B.V.** — campo `dimensione`  
LEAD NON VALIDO — aggravamento rispetto a quanto annotato. Non solo De Jong Verpakking ha acquisito Bangma (closing 30-07-2020), ma nel 2023 l'INTERO De Jong Packaging Group è stato acquisito da STORA ENSO (multinazionale finlandese quotata). Bangma Verpakking opera oggi 'as part of the De Jong Verpakking and Stora Enso family': non è più un'entità autonoma sotto il profilo decisionale e la compliance EUDR si determina a livello di capogruppo Stora Enso, che ha già un proprio programma EUDR di gruppo. Da rimuovere dalla lista lead.  
*Evidenza:* https://dejongverpakking.com/en/news/de-jong-packaging-completes-acquisition-of-bangma-verpakking/ ; https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - 'in 2023 werd De Jong Packaging Group overgenomen door Stora Enso ... vandaag maakt Bangma Verpakking deel uit van de De Jong Verpakking en Stora Enso familie'; https://www.agf.nl/article/9238854/de-jong-verpakking-neemt-bangma-verpakking-over/  
*Correzione proposta:* Rimuovere il lead (controllata Stora Enso via De Jong Packaging Group dal 2023)


### Belgio (4)

**Extremis NV** — campo `referente`  
Referente non aggiornato: Dirk Wynants e' oggi owner e chief designer, NON il vertice esecutivo. L'amministratore delegato in carica e' Valentine Batjoens, nominata CEO in successione a Yff Vandendriessche. Il campo attribuisce erroneamente a Wynants la funzione di vertice.  
*Evidenza:* https://www.lovethatdesign.com/?post_type=news&p=378797 e https://www.linkedin.com/posts/extremis_meet-our-new-ceo-aka-captain-of-the-ship-activity-7046080915592069121-Z6QI - frammento: "Extremis appointed Valentine Batjoens as its new Chief Executive Officer... continue the course of outgoing CEO Yff Vandendriessche. However, Dirk Wynants remains as the owner and chief designer of Extremis"  
*Correzione proposta:* Valentine Batjoens — CEO (Dirk Wynants resta fondatore/proprietario e chief designer)

**Sas NV (Sas Coffee)** — campo `dimensione`  
CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elenca come societa' di portafoglio con 'complete repositioning and rebranding'. Le decisioni di compliance EUDR si prendono a livello di gruppo/fondo: lead NON valido come impresa familiare indipendente.  
*Evidenza:* https://nimbus.com/ - 'Sas Coffee, a specialist in private label coffee, recently became part of the Nimbus portfolio'; https://www.made-in.be/kempen/kempens-koffiebedrijf-miko-blijft-achter-met-financiele-kater-van-20-miljoen-euro-na-verkoop-sas-koffie/ ; https://fd.nl/bedrijfsleven/1517530/investeerder-nimbus-koopt-belgische-koffiebrander-sas  
*Correzione proposta:* Segnalare nel campo dimensione: 'controllata di Nimbus Investments (NL) dal 24-05-2024 - non indipendente' oppure rimuovere il lead

**Silco NV** — campo `denominazione`  
RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui presidente e' Philippe Van Gestel e che e' controllata dalla famiglia Van Gestel (Noord Natie). L'amministratore di Silco indicato nel foglio e' 'Philip Van Gestel'. Forte indizio che Silco sia un veicolo del gruppo Efico/Van Gestel e non una trading house indipendente: in tal caso la compliance EUDR si deciderebbe a livello di capogruppo e il lead non sarebbe valido. DA CONFERMARE il legame societario.  
*Evidenza:* https://www.tendata.com/en/buyer/efico-nv-italielei-181-2000-antwerp-belgium-BELN376bec4ab92398acd7b73f7696701f41.html - 'EFICO NV. ITALIELEI 181. 2000 ANTWERP BELGIUM'; https://www.companyweb.be/en/0431096011/efico ; frammento: 'Philippe Van Gestel is the chairman of Efico... Noord Natie (the Van Gestel family) has control over Efico'  
*Correzione proposta:* — (nessun valore certo: rilievo aperto)

**Tannerie Masure SA** — campo `denominazione`  
Societa' non indipendente: dal 2014 Tannerie Masure fa parte del Groupe Saturne insieme alla francese Tannerie Fortier-Beaulieu (Roanne). Il referente indicato, Olivier Lesage, risulta anche dirigente della holding francese FINANCIERE SATURNE: le decisioni di compliance EUDR si giocano a livello di capogruppo francese, non sulla controllata belga.  
*Evidenza:* https://groupe-saturne.com/en/saturne-group/ - frammento: "In 2014, Fortier-Beaulieu associated with the Masure tannery in Estaimbourg (Belgium) to form the independent Groupe Saturne"; https://www.societe.com/manager/Olivier.LESAGE.s8sT-HgWTfO.html (Olivier LESAGE - FINANCIERE SATURNE)  
*Correzione proposta:* Valutare il lead a livello di capogruppo Groupe Saturne / Financiere Saturne (FR): la societa' belga non e' un centro decisionale autonomo per la compliance EUDR


---

## Casi di gravità MEDIA (29)


### Danimarca (8)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| COPENHAGEN CHOCOLATE FACTORY ApS | email | L'email pubblicata come recapito ufficiale nelle condizioni di vendita e sulle schede societarie e' kundeservice@simplychocolate.dk (tel. +45 3634 0070). info@simplychocolate.dk, riportata nel foglio, non e' stata ritrovata letter | https://www.simplychocolate.dk/pages/handelsbetingelser e https://www.proff.dk/firma/copenhagen-chocolate-factory-aps/kastrup/producenter/0JI778I016D - 'kundeservice@simp | kundeservice@simplychocolate.dk |
| Estate Coffee Copenhagen A/S | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: il CVR 18179407 e' oggi registrato come Smage-Compagniet A/S, Holmevej 10, 5683 Haarby. La cronologia e' ricostruita dall'azienda stessa: fondata nei primi anni '90 (tra i fondatori Claus Me | https://smage-compagniet.dk/estate-coffee/ - 'Virksomhedens historie gaar tilbage til starten af 1990'erne, hvor den blev grundlagt af blandt andre Claus Meyer og hed Cho | Smage-Compagniet A/S (CVR 18179407) - gia' Estate Coffee Copenhagen A/S / Chokolade Compagniet |
| INNOVATION LIVING A/S (già Innovation Randers | dimensione | Dato obsoleto: il campo cita il bruttofortjeneste 2023 (47,3 M DKK) mentre l'ultimo bilancio disponibile (2025) riporta 40 M DKK, quindi in calo. Anche la composizione del gruppo è imprecisa: INNOVATION HOLDING A/S conta 10 societ | https://www.proff.dk/firma/innovation-living-as/randers-n%C3%B8/m%C3%B8bler/13462KI015G — frammento: "In 2025, the company reported a gross profit of DKK 40 million ... p | Bruttofortjeneste 40 mio DKK (~5,4 M€) nel 2025 (proff.dk, CVR 65699516); fatturato non pubblicato; gruppo INNOVATION HO |
| JKE DESIGN A/S | dimensione | Dato obsoleto: il campo riporta il bruttofortjeneste 2023 (55,6 M DKK) mentre il bilancio 2024 depositato indica 50 M DKK, in ulteriore calo rispetto al 2022 (58,7 M DKK). La stima ricavi "~20-27 M€" resta non verificata. | https://regnskaber.cvrapi.dk/21017236/ (Årsrapport 2024 JKE DESIGN A/S, Gl Klæstrupvej 75, 9740 Jerslev J) — frammento: "In 2024, the company showed a gross profit of DKK | Bruttofortjeneste 50 mio DKK (~6,7 M€) nel 2024 (årsrapport 2024, CVR 63271012); fatturato non pubblicato |
| Just Coffee | denominazione | Ragione sociale CVR ora VERIFICATA: non e' ne' ApS ne' A/S ne' amba, e' un INTERESSENTSKAB. Denominazione legale 'Just Coffee I/S', CVR 35492380, costituita il 01-01-2014, sede Frederiksborgvej 551, 4000 Roskilde; soci illimitatam | https://cvrapi.dk/virksomhed/dk/just-coffee-is/35492380 e https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Just Coffee I/S ... CVR-nr 3549238 | Just Coffee I/S - CVR 35492380 (forma giuridica: interessentskab) |
| SØRENSEN LÆDER A/S (Sorensen Leather) | dimensione | Dato obsoleto e non allineato alla fonte: il record indica bruttofortjeneste 23,85 mio DKK (2022) e ca. 20 dipendenti, mentre la scheda proff.dk attuale (CVR 50828514) riporta bruttofortjeneste 13.056 tkr (13,06 mio DKK ≈ 1,75 M€) | https://www.proff.dk/regnskab/s%C3%B8rensen-l%C3%A6der-as/lystrup/skind-l%C3%A6der-og-pels/GKJEN4I07RD — frammento: "Bruttofortjeneste: 13.056 tkr ... Number of employees | Bruttofortjeneste 13,06 mio DKK (~1,75 M€) e 16 dipendenti — proff.dk, CVR 50828514 (ultimo bilancio disponibile); fattu |
| TJOERNEHOEJ MOELLE A/S | dimensione | Fatturato recente NON reperito: il dato del foglio resta quello del 2003 (80 M DKK). In 3 ricerche l'unico bilancio individuato e' il PDF dell'esercizio 2011 su regnskaber.cvrapi.dk e menzioni di dati fino al 2014; nessuna cifra 2 | https://regnskaber.cvrapi.dk/21057143/Y3ZyLmRrOi8vcGRmcy8zNDE3NTAxMjtBL1M1MDg2MTsyMDExMDEwMTsyMDExMTIzMTtSO1I.pdf - bilancio 01-01-2011/31-12-2011; https://erhvervplus.dk |  |
| VESTJYSK SPECIALFODER ApS | filiera | Perimetro EUDR DA CONFERMARE: l'oggetto sociale registrato e' generico ('handelsvirksomhed inden for specialfoder'), classificato proff.dk come 'engroshandel - annet'. Nessuna fonte pubblica conferma l'impiego di soia (unica commo | https://royalfireworks.dk/forhandler/vestjysk-specialfoder-aps/ - scheda rivenditore fuochi d'artificio a Vemb; https://www.proff.dk/firma/vestjysk-specialfoder-aps/vemb/ |  |

### Svezia (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Horreds Möbel Aktiebolag | dimensione | Dato 2022 NON aggiornabile con certezza e anzi CONTRADDETTO. allabolag.se riporta oggi per Horreds Möbel AB (556365-1974) 45 dipendenti (contro i 50 del 2022) e un intervallo di fatturato 50.000-99.999 tkr, cioè 50-99,9 MSEK ≈ 4,4 | https://www.allabolag.se/foretag/horreds-m%C3%B6bel-aktiebolag/horred/butiksinredningar-butiksutrustningar/2K0GDC6I5YDBD - '45 anställda ... omsättningsintervall 50 000-9 |  |

### Olanda (2)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Origin Bridge (Barchem) | denominazione | Forma giuridica NON risolta dopo 3 ricerche: nessuna fonte pubblica indicizzata riporta la rechtsvorm né una denominazione legale con suffisso. Restano solo KVK 70878315 e P.IVA NL001587917B24 pubblicati dall'azienda stessa. La st | https://originbridge.coffee/legal-information/ e https://originbridge.coffee/contact/ - 'Heidehoflaan 2B, 7244AG Barchem, The Netherlands ... CoC: 70878315 ... VAT: NL001 |  |
| Origin Bridge (Barchem) | email | L'email del foglio (info@bridgetoorigin.com) NON è quella principale del sito ufficiale: la pagina di contatto di originbridge.coffee indica come recapito dell'entità olandese europe@originbridge.coffee, tel. +31 85 301 6984. info | https://originbridge.coffee/contact/ - 'Origin Bridge Netherlands, Heidehoflaan 2B, 7244AG Barchem ... +31 85 301 6984 ... europe@originbridge.coffee'; recapito alternati | europe@originbridge.coffee |

### Belgio (18)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Bulo NV | referente | Referente probabilmente non aggiornato. Dirk Busschop risulta CEO in fonti risalenti (2009); l'azienda e' oggi guidata dalla terza generazione, Carlo e Louis Busschop, con Carlo Busschop indicato come Managing Director / CEO in fo | https://www.bulo.com/third_generation/ e https://rocketreach.co/carlo-busschop-email_93406361 - frammento: "Carlo Busschop, based in Mechelen, BE, is currently a Managing | Carlo Busschop — gedelegeerd bestuurder / Managing Director (DA CONFERMARE) |
| Buzzispace NV | email | Email 'n.d.': record privo di indirizzo di contatto nonostante il sito buzzi.space sia attivo. DA CONFERMARE. | https://www.buzzi.space/brand (sito attivo, nessun indirizzo e-mail nei frammenti) |  |
| Carlens NV | referente | Referente e ruolo assenti. Le fonti pubbliche citano 'Carl Carlens' in contesto gestionale, mentre il campo dimensione ipotizza 'Luc Carlens' da FinCheck: nomi discordanti, nessuno dei due confermato come gedelegeerd bestuurder. D | https://www.limoco-industries.be/referenties/240-houthandel-carlens-keuze-voor-leverancier-dicht-bij-huis - frammento: risultati che referenziano "Carl Carlens" in contes |  |
| Confortluxe NV | referente | Referente e ruolo assenti benche' gli amministratori siano pubblici e confermati (Jacqueline Pauwels, Jimmy Ollevier, Heidi Ollevier). Il fondatore Andre Ollevier, storico gedelegeerd bestuurder, e' deceduto: non usarlo come refer | https://fincheck.be/en/confortluxe/0412.863.078/Wervik/connections - frammento: "The current board members of Confortluxe are Jacqueline Pauwels, Jimmy Ollevier, and Heid | Jimmy Ollevier — bestuurder (ruolo di gedelegeerd bestuurder DA CONFERMARE) |
| Decolvenaere BV | dimensione | Fatturato fortemente sottostimato. Il campo riporta 'oltre 10 milioni di euro' (fonte giornalistica Sterck Magazine), ma i dati di bilancio piu' recenti indicano un fatturato totale di 38.585.036 EUR, con altre fonti che collocano | Frammenti di ricerca su Decolvenaere BV (BE 0400.079.171): "The most recent financial statements show a total turnover of EUR 38,585,036.00" e "turnover is between EUR 25 | Fatturato ~38,6 M EUR (ultimo bilancio depositato NBB) — DA RICONFERMARE sulla fonte NBB primaria |
| Extremis NV | dimensione | Fatturato potenzialmente obsoleto: il campo riporta 12.900.125 EUR e 24,8 FTE dall'ultimo bilancio, ma risulta gia' depositato un bilancio piu' recente (deposito 02-07-2026) i cui dati non sono riflessi nel record. DA AGGIORNARE. | https://www.companyweb.be/en/0434625128/extremis - frammento: "The most recent financial statements of Extremis were filed on 02-07-2026" |  |
| Houthandel Denis Luyten NV | referente | Referente e ruolo assenti; il campo dimensione dichiara esplicitamente che il nome del gestore non e' pubblicato. Nemmeno le ricerche mirate restituiscono il gedelegeerd bestuurder in carica (azienda alla 4a generazione della fami | https://www.companyweb.be/en/0403778831/houthandel-denis-luyten - frammento: "At the time of its most recent financial statements, Houthandel Denis Luyten recorded a tota |  |
| Hulpiau Hides BV | referente | Referente e ruolo assenti. Le fonti pubbliche citano Raimond Hulpiau come 'current senior manager' (fratello del fondatore Christiaan Hulpiau), ma il ruolo formale (zaakvoerder/gedelegeerd bestuurder) non e' pubblicato: DA CONFERM | https://www.hulpiauhides.com/en/about-us/ - frammento: "Christiaan Hulpiau, brother of current senior manager Raimond Hulpiau, founded Hulpiau Hides" |  |
| Jori NV | referente | Referente e ruolo assenti e non ricostruibili dalle fonti pubbliche consultate: nessun nome di gedelegeerd bestuurder/CEO emerge per Jori NV (BE 0888.984.313). DA CONFERMARE. Fatturato 16.143.273 EUR, 106,8 FTE e sede Hoogweg 52,  | https://www.companyweb.be/en/0888984313/jori - frammento: "with a revenue of EUR 16.143.273, Jori from Wervik ranks 19th in the furniture manufacturing sector... There ar |  |
| Keukenontwerpers NV | filiera | Perimetro EUDR debole. L'azienda opera con l'insegna SieMatic Keukenontwerpers come rivenditore/installatore a valle di cucine prodotte dalla tedesca SieMatic: non e' l'operatore che immette per primo il prodotto in legno sul merc | https://www.keukenontwerpers.com/ e https://trustlocal.be/antwerpen/geel/keukenbouwer/siematic-keukenontwerpers/ - frammento: "SieMatic Keukenontwerpers has been a partne |  |
| Keukenontwerpers NV | referente | Referente e ruolo assenti; nessuna fonte pubblica restituisce il gedelegeerd bestuurder di Keukenontwerpers NV (BE 0472.648.534). L'email geel@keukenontwerpers.com non e' inoltre riscontrabile letteralmente nei frammenti. DA CONFE | https://trendstop.knack.be/nl/detail/472648534/keukenontwerpers.aspx - frammento: "With a turnover of 16,033,016 euros, Keukenontwerpers is ranked 7th in the Kitchen Furn |  |
| Lavrijsen Houtbedrijf NV | dimensione | Fatturato obsoleto e indirizzo errato. Il campo riporta 12.763.339 EUR (dato trendstop), mentre l'ultimo bilancio depositato indica 14.093.447 EUR e 23,1 FTE (non '20-49 addetti'). Inoltre la sede legale registrata e' Koning-Alber | https://www.companyweb.be/en/0407106030/houtbedrijf-lavrijsen - frammento: "Houtbedrijf Lavrijsen recorded a total turnover of EUR 14,093,447.00... The registered office  | Fatturato 14.093.447 EUR e 23,1 FTE (ultimo bilancio NBB); sede Koning-Albertstraat 123, 2440 Geel |
| Radermecker SRL | referente | Referente e ruolo assenti. La conceria e' stata rilevata nell'aprile 2016 da due ingegneri francesi, Loic Honore e Nicolas Quintin, che ne sono gli attuali gestori: candidati referenti (gerant / administrateur delegue) da conferma | https://www.lavenir.net/regions/wallonie-picarde/comines-warneton/2022/01/14/cuirs-selliers-la-specialite-de-la-tannerie-radermecker-a-comines-YLAPU6LGVNA2RARMXD734SCPGU/ |  |
| Radermecker SRL | email | Email 'n.d.': nessun indirizzo di contatto nel record. Il sito radermecker.com espone una pagina contatti, ma l'indirizzo non e' recuperabile via frammenti di ricerca. DA CONFERMARE. | https://www.radermecker.com/pages/on-parle-de-nous-dans-la-presse (sito attivo, indirizzo e-mail non estraibile dai frammenti) |  |
| Sas NV (Sas Coffee) | referente | Herman Sas risulta ancora 'gedelegeerd bestuurder' negli estratti KBO pubblicati (pappers.be, insieme a Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HELFINCO), ma nessuna fonte post-cessione a Nimbus (05/2024) lo riconferm | https://www.pappers.be/nl/company/sas-0404190783 - 'Herman Sas is de gedelegeerd bestuurder; overige bestuurders: Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HEL |  |
| Sas NV (Sas Coffee) | email | L'email nel foglio (info@sas-koffie.be) NON e' quella pubblicata sul sito ufficiale sas-coffee.com: la pagina di contatto riporta CUSTOMERSERVICE@SAS-COFFEE.COM, tel. +32 14 61 12 00, indirizzo LILSEDIJK 36 - 2340 BEERSE. info@sas | https://sas-coffee.com/en/contact/ - 'CUSTOMERSERVICE@SAS-COFFEE.COM \| +32 14 61 12 00 \| LILSEDIJK 36 - 2340 BEERSE - BELGIUM' | customerservice@sas-coffee.com ; sede Lilsedijk 36, 2340 Beerse DA CONFERMARE |
| Silco NV | dimensione | Discordanza 4,8 vs 8,4 M€ NON risolta: le due banche dati continuano a riportare cifre diverse per lo stesso ultimo bilancio depositato (14-06-2024). Trendstop: EUR 8.358.215 (23a nel settore 'koffie en thee'); Companyweb/Fincheck | https://trendstop.knack.be/nl/detail/715792692/silco.aspx - 'omzet van 8.358.215 euro, 23e in de sector Koffie en thee'; https://www.companyweb.be/en/0715792692/silco - ' |  |
| Tannerie Masure SA | email | Email 'n.d.'. Il sito masure.be ha una pagina contatti attiva ma l'indirizzo non e' verificabile dai frammenti. DA CONFERMARE. | https://www.masure.be/contact (pagina contatti esistente; indirizzo e-mail non presente nei frammenti) |  |

---

## Casi di gravità BASSA (23)


### Danimarca (9)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| BØJSØ DØRE & VINDUER A/S | dimensione | Organico non allineato: le fonti reperite indicano 43 dipendenti, il record ne indica 41. Inoltre il campo non riporta alcun dato economico verificato (né fatturato né bruttofortjeneste): la collocazione in forbice 5-40 M€ resta u | https://www.proff.dk/firma/b%C3%B8js%C3%B8-d%C3%B8re-vinduer-as/vorbasse/producenter/GJL0QJI016D — frammento: "Bøjsø doors and windows was founded in 1972 and has 43 empl | 43 dipendenti (proff.dk, CVR 12224494); dato economico da recuperare a bilancio |
| COPENHAGEN CHOCOLATE FACTORY ApS | denominazione | IDENTITA' ANNOTATA CONFERMATA CORRETTA: CVR 32761844, Amager Landevej 123, 2770 Kastrup, costituita il 26-01-2010, ApS; opera con i binavne 'Simply Chocolate Copenhagen' e www.simplychocolate.dk; direttore Niels Ostenkaer; capogru | https://cvrapi.dk/virksomhed/dk/copenhagen-chocolate-factory-aps/32761844 ; https://www.simplychocolate.dk/pages/handelsbetingelser - 'www.simplychocolate.dk ejes og driv |  |
| FREDERICIA FURNITURE A/S | dimensione | Refuso nell'unità di misura: "risultato ante imposte 6,5 M€ DKK" mescola euro e corone danesi. Il valore va espresso in una sola valuta. | Testo del campo dimensione del record stesso: "risultato ante imposte 6,5 M€ DKK" | risultato ante imposte 6,5 mio DKK (~0,87 M€) |
| Farstrup Furniture A/S | ruolo | DA CONFERMARE: i registri elencano due direktør (Jan Andersen e Steen Cederholm-Johansen) senza qualificare esplicitamente Cederholm-Johansen come administrerende direktør. Il ruolo indicato non è riconfermato. | https://www.proff.dk/firma/farstrup-furniture-as/s%C3%B8nders%C3%B8/producenter/GKF1OMI016D — frammento: "The directors are Jan Andersen and Steen Cederholm-Johansen ...  |  |
| INNOVATION LIVING A/S (già Innovation Randers | linkedin | URL LinkedIn con prefisso di locale tedesco (de.linkedin.com) per una società danese. Non è un errore di pagina ma è incoerente con lo standard del dataset (dk. o www.). | Valore del record: https://de.linkedin.com/company/innovation-living-a-s | https://dk.linkedin.com/company/innovation-living-a-s |
| Just Coffee | sede | La sede registrata al CVR e' Frederiksborgvej 551, 4000 Roskilde, non Jyllinge: il riferimento a Jyllinge deriva dal testo promozionale del sito ('risteriet ligger paa en gaard i Jyllinge lige uden for Roskilde'). Il comune e' com | https://www.proff.dk/firma/just-coffee-is/roskilde/producenter/GUO2ZPI016D - 'Frederiksborgvej 551, 4000 Roskilde'; https://estatistik.dk/virksomhed/just-coffee-is/354923 | Frederiksborgvej 551, 4000 Roskilde, Regione Sjaelland |
| NIELAUS A/S | dimensione | Numero di dipendenti non allineato alla fonte citata: la scheda proff.dk (CVR 35480943) riporta 19 addetti, il record ne indica 11. | https://www.proff.dk/firma/nielaus-as/bramming/m%C3%B8bler/GUJZBOI015G — frammento: "NIELAUS A/S is a furniture production company located at Vejrup Storegade 63, 6740 Br | 19 dipendenti (proff.dk, CVR 35480943) — verificare l'anno di riferimento |
| NIELAUS A/S | email | DA CONFERMARE: l'indirizzo info@nielaus.dk non compare letteralmente in nessuna fonte pubblica reperita; la pagina Kontakt del sito ufficiale protegge l'indirizzo dagli spambot e non lo espone in chiaro nei frammenti. | https://www.nielaus.dk/da/om-os/kontakt — frammento: "Email: Available on their website (protected against spambots)" |  |
| ONECOLLECTION A/S (House of Finn Juhl) | fonte | DA CONFERMARE: l'ID proff nell'URL citato (GXS757I015G) non coincide con quello della scheda ONECOLLECTION A/S CVR 29787786 reperita (GQYY8HI016D). L'URL potrebbe puntare a una scheda diversa/obsoleta. | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D — titolo: "ONECOLLECTION A/S - CVR-nr 29787786 - Ringkøbing" | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D |

### Svezia (2)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Gärsnäs Aktiebolag | referente | RICONFERMATO, nessuna correzione necessaria. Magnus Eriksson risulta tuttora VD di Gärsnäs Aktiebolag (556044-4746) e Dag Klockby styrelseordförande, coerentemente con l'annuncio ufficiale del sito (VD dal 01-01-2023, in precedenz | https://garsnas.se/en/new-ceo-at-garsnas/ ('Ny vd på Gärsnäs'); https://www.bolagsfakta.se/5560444746-Garsnas_Aktiebolag - 'Magnus Eriksson är VD ... Dag Klockby är styre | Magnus Eriksson, VD (confermato) |
| Horreds Möbel Aktiebolag | denominazione | Società CONFERMATA ATTIVA (scheda allabolag corrente, nessuna procedura concorsuale rilevata). Va però esplicitato il legame di gruppo: la capogruppo è Horreds Holding AB (esiste anche Horreds Möbel Utvecklings AB, 559016-3324). N | https://www.allabolag.se/5563651974/koncern e frammento allabolag: 'moderbolag är Horreds Holding AB'; https://www.allabolag.se/5590163324/horreds-mobel-utvecklings-ab | Indicare la capogruppo: Horreds Holding AB |

### Olanda (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Bangma Verpakking B.V. | sito | Il sito indicato nel foglio (https://www.bangma.nl) non è il dominio istituzionale usato oggi dall'azienda, che pubblica i propri contenuti su bangmaverpakking.nl (pagina 'Historie Bangma Verpakking'). DA CONFERMARE quale dei due  | https://bangmaverpakking.nl/over-ons/historie-bangma-verpakking/ - pagina istituzionale corrente dell'azienda | https://bangmaverpakking.nl/ (DA CONFERMARE) |

### Belgio (10)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Belignum NV | dimensione | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato il 02-07-2024 (esercizio 2023). | https://trendstop.knack.be/nl/detail/405348449/belignum.aspx - 'omzet van 14.746.642 euro, 40e in de sector houthandel... laatst neergelegde jaarrekening 02-07-2024... 10 | Fatturato EUR 14.746.642, esercizio 2023 (bilancio depositato 02-07-2024), 10,8 FTE - eliminare il riferimento a 16.075. |
| Buzzispace NV | dimensione | Il campo indica la produzione 'in Kempen' (implicitamente Belgio): le fonti aziendali collocano lo stabilimento produttivo a Bladel, nei Paesi Bassi. La sede sociale ad Anversa resta corretta, ma l'attivita' manifatturiera non e'  | https://officeinsight.com/officenewswire/buzzispace-appoints-new-ceo-announces-new-role-for-former-ceo-and-founder/ - frammento: "showrooms in Antwerp, London, New York,  |  |
| Callens NV (Callens African Woods) | referente | Thierry Maelfait risulta confermato alla guida, ma dal 2021-2022 e' entrata in azienda la figlia Sam Maelfait, indicata dalle fonti come zaakvoerster/marketingverantwoordelijke: verificare chi sia oggi il rappresentante legale. No | https://www.voka.be/nieuws/west-vlaanderen-ondernemers-2024-19/callens-african-woods-heeft-productiefaciliteiten-kameroen - frammento: "Sam Maelfait, daughter of Thierry, |  |
| Decadt Houthandel NV | ruolo | Stefaan Decadt e' confermato al vertice, ma il ruolo pubblicato e' 'bedrijfsleider' (LinkedIn) e non 'Algemeen directeur'; per una NV il titolo statutario sarebbe 'gedelegeerd bestuurder'. Inoltre coesistono due siti web riferiti  | https://be.linkedin.com/in/stefaan-decadt-8b8144113 - frammento: "Stefaan Decadt - bedrijfsleider bij decadt houthandel nv"; siti concorrenti https://decadt-hout.be/ e ht | Ruolo: Bedrijfsleider / gedelegeerd bestuurder |
| Decadt Houthandel NV | dimensione | Data di fondazione discordante: il campo indica 01-01-1975 (data di costituzione della NV) mentre le fonti aziendali datano l'attivita' al 1927. Fatturato 13.460.408 EUR confermato. | https://trendstop.knack.be/nl/detail/415284714/decadt-houthandel.aspx - frammento: "With a turnover of 13,460,408 euros, Decadt Houthandel is ranked 43rd in the timber tr |  |
| Denderwood NV | dimensione | Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta indeterminata e potenzialmente sotto la soglia dei 5 M EUR. Il campo lo dichiara ('TAGLIA DA VERIFICARE'), ma il dato non e' riscontrabile su N | https://www.atibt.org/en/members/24/denderwood e https://www.denderwood.com/over-ons/ - frammento: "Denderwood is located at J. Cardijnstraat, 3 B-9420 Erpe Mere, Belgium |  |
| Hulpiau Hides BV | dimensione | Il campo usa come proxy dimensionale il margine lordo (2.284.726 EUR) di UN'ALTRA entita' giuridica (Hulpiau BV, BE 0429.082.864), non della societa' target BE 0777.875.662, che deposita a schema abbreviato e non pubblica il fattu | https://www.companyweb.be/en/0777875662/hulpiau-hides - frammento: "There are 6.1 FTEs working at Hulpiau Hides according to staff figures in the most recent financial st |  |
| Lavrijsen Houtbedrijf NV | ruolo | Jan e Bert Lavrijsen sono confermati alla guida dell'azienda, ma per una NV il titolo statutario corretto e' 'gedelegeerd bestuurder / bestuurder', non 'zaakvoerder' (termine proprio delle BV). | https://lavrijsen.be/over-ons/ - frammento: "Jan and Bert Lavrijsen are at the helm of the company with secured succession" | Bestuurders / gedelegeerd bestuurders |
| Radermecker SRL | dimensione | Discordanza sugli addetti: il record indica 9,1 FTE (bilancio BNB), mentre la scheda Europages dichiara 20-49 dipendenti. Il fatturato non e' pubblicato (schema abbreviato): la collocazione dimensionale resta non verificabile. | https://www.europages.fr/TANNERIE-RADERMECKER/BEL069426-000019048001.html - frammento: "The company employs between 20 and 49 people" |  |
| Silco NV | sito | Nessun sito web proprio reperito per Silco NV in 3 ricerche: l'azienda compare solo su banche dati societarie (trendstop, companyweb, fincheck, northdata, staatsbladmonitor). Coerente con la struttura a 1 FTE. Il campo vuoto e' qu | https://www.northdata.com/Silco%20N.V.,%20Antwerpen/KBO%200715.792.692 - solo scheda registro; nessun dominio aziendale nei risultati | n.d. (nessun sito web aziendale) |

### (tutti) (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| (controllo di rientro) | denominazione | nessuna delle 7 aziende rimosse e' rientrata nei fogli. Controllo eseguito su _records.json (742 record, tutti i fogli) cercando in ogni campo, con radici tolleranti alle varianti: 'getama', 'dragsb', 'pacorini', 'immobra', 'lavaz | Verifica programmatica su _myeudr_build/verifica/_records.json: per ciascuna delle 7 radici, 0 corrispondenze nel campo 'denominazione' su tutti i 742 record; unico match |  |
