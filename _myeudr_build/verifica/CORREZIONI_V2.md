# CORREZIONI v2 — changelog di `MyEUDR_Lead_Mapping_v2.xlsx`

> Generato da `_myeudr_build/v2/genera_changelog.py` il 2026-09-01. Rieseguibile: rilegge le tabelle di correzione e il diff cella per cella.

Questo documento elenca **tutto** ciò che cambia rispetto alla v1 (`MyEUDR_Lead_Mapping.xlsx`, che non è stata toccata) e — altrettanto importante — ciò che è stato **deliberatamente non applicato**, con il motivo.

---

## 1. Il quadro in numeri

- **215 celle cambiate** su 727 aziende.
- **1 riga rimossa** (§4).
- **0 campi svuotati** e **0 record orfani**, verificati cella per cella contro il backup pre-modifica (`verifica_integrita.py`).
- Ordine degli 8 fogli invariato: Italia, Germania, Finlandia, Danimarca, Svezia, Olanda, Belgio, Austria.

| Campo | Celle | | Foglio | Celle |
|---|--:|---|---|--:|
| `dimensione` | 72 | | Svezia | 42 |
| `email` | 34 | | Italia | 38 |
| `referente` | 31 | | Belgio | 35 |
| `ruolo` | 29 | | Olanda | 32 |
| `sito` | 17 | | Germania | 25 |
| `linkedin` | 14 | | Danimarca | 21 |
| `filiera` | 8 | | Finlandia | 11 |
| `denominazione` | 6 | | Austria | 11 |
| `fonte` | 4 | |  |  |

---

## 2. Il criterio, che è lo stesso della v1

La v2 **non riparte da zero**: continua il criterio già fissato in §0-bis del `REPORT_VERIFICA.md`. Una correzione entra nel foglio solo se ricade in una categoria già decisa **e** ha evidenza a fonte. In particolare:

| Regola | Come è stata rispettata |
|---|---|
| Mai un dato non verificato | Le proposte con riserva («DA CONFERMARE», «probabilmente», «da verificare») non sono state applicate: sono andate alla riverifica del PASSO 3, e quelle rimaste incerte restano rilievi aperti. |
| Mai svuotare un campo valorizzato | L'applicatore salta ogni proposta che porterebbe un valore vuoto. Verificato a posteriori: **0 campi svuotati**. |
| Rimozioni solo per commodity fuori Allegato I o azienda cessata | Una sola rimozione, categoria «cessata». Il fuori taglia da solo continua a non bastare. |
| Le denominazioni si verificano al registro, non all'ortografia | Ogni cambio di denominazione porta un numero di registro o una P.IVA nell'evidenza. È la lezione di Arko. |
| Integrità dopo ogni applicazione | Righe per foglio, ordine dei fogli, campi svuotati e record orfani, confrontati col backup pre-modifica dopo ogni lotto. |

---

## 3. Correzioni applicate

### 3.1 Denominazioni accertate a registro

Regola 5: normalizzare *come è scritta* una forma giuridica non dice *quale* sia quella giusta — su Arko l'assunzione era falsa. Qui ogni riga porta il numero di registro.

| Foglio | Da | A | Fonte |
|---|---|---|---|
| Austria | Fürst GmbH | **Cafe-Konditorei Fürst GmbH** | https://firmen.wko.at/cafe-konditorei-f%C3%BCrst-gmbh-cafe-konditorei/salzburg/ — Firmenbuchnummer … |
| Belgio | Hexpol Compounding BV | **Hexpol Compounding SRL** | https://www.companyweb.be/en/0430105126/hexpol-compounding — «Hexpol Compounding (SRL) - Eupen (470… |
| Danimarca | JOHNSEN GRAPHIC SOLUTIONS A/S (oggi anche Joh… | **JOHNSEN PRINT & DIGITAL MEDIA A/S (già Johnse…** | https://virmo.dk/firma/18624141-johnsen-print-digital-media-as — CVR 18624141 |
| Finlandia | Piiroinen Oy | **Arvo Piiroinen Oy** | https://www.proff.fi/yrityksen/arvo-piiroinen-oy/salo/... — Y-tunnus 0139391-8 |
| Germania | Weibler Confiserie Chocolaterie GmbH | **Weibler Confiserie Chocolaterie GmbH & Co. KG** | https://www.northdata.com/Weibler%20Confiserie%20Chocolaterie%20GmbH%20&%20Co%C2%B7KG,%20Cremlingen… |
| Olanda | Origin Bridge (Barchem) | **BENZU (eenmanszaak) — handelsnaam «Origin Bri…** | https://originbridge.coffee/legal-information/ — KvK 70878315; registro: «BENZU (Eenmanszaak)» |

### 3.2 Legami di gruppo non dichiarati o errati

Per la §3 del report questi **sono errori di dato**, non decisioni di selezione: il campo taceva il legame o indicava la capogruppo sbagliata. Il sottoinsieme più grave è quello dei record che *affermano un'indipendenza che non c'è* — qui rientra Ginsten Slakteri.

| Foglio | Azienda | Clausola aggiunta | Fonte |
|---|---|---|---|
| Germania | Röstfein Kaffee GmbH | n.d. (torrefazione media, gegr. 1908). Legame di gruppo: controllata al 100% da Zentralko… | northdata / wer-zu-wem, Röstfein Kaffee GmbH, Magdeburg, HRB 107856; https://ww… |
| Olanda | Chocolatemakers B.V. | Legame di gruppo: dal 2025 confluita in The Chocolate Impact Group (fusione con Hands Off… | https://www.doen.nl/en/nieuws/dutch-chocolate-companies-hands-off-and-chocolate… |
| Svezia | Aktiebolaget Ginsten Slakteri | Bovini/Carne — macello (bovini, suini, ovini) e commercio carni, in gruppo familiare | https://www.allabolag.se/organisation/aktiebolaget-ginsten-slakteri/harplinge/l… |
| Svezia | Aktiebolaget Ginsten Slakteri | Capogruppo: Aktiebolaget Joh. M. Johansson, Kött- & Charkuteriaffär (gruppo familiare di … | https://www.allabolag.se/organisation/aktiebolaget-ginsten-slakteri/harplinge/l… |
| Belgio | Slachthuis Swaegers NV | Il gruppo familiare ha rilevato anche il macello di Bastogne. | https://derijkstebelgen.be/nieuws/vader-en-dochter-swaegers-nemen-slachthuis-va… |
| Danimarca | KVIST INDUSTRIES A/S | Controllata da KVIST HOLDING A/S, partecipata dal fondo Dansk Ejerkapital; fatturato non … | https://www.danskejerkapital.dk/portefoelje/kvist-industries/ ; https://www.pro… |
| Danimarca | TIMBERMAN DENMARK A/S | Controllata del gruppo svedese quotato Volati AB dal dicembre 2024 (in precedenza Cortice… | https://ligeher.nu/mariagerfjord/nyheder/mennesker/svensk-koncern-koeber-hadsun… |
| Danimarca | KLS PUREPRINT A/S | Controllata (oggi integralmente) di F.; E.; BORDING A/S dopo il riacquisto della quota di… | https://signprintpack.dk/2025/01/06/bording-oger-ejerandelen-af-kls-pureprint-o… |
| Danimarca | Copenhagen Coffee Lab ApS | Capogruppo Copenhagen Coffee Lab Holding ApS (gruppo di 6 societa'); 70% Steen Skallebæk … | https://nordic9.com/news/steen-skallebk-and-ole-kristoffersen-acquire-70-of-cop… |
| Danimarca | DANSK KAFFE ApS | Capogruppo KAFFEA ApS (gruppo di 2 societa'), societa' costituita il 27.11.2013.; Micro-i… | https://proff.dk/firma/dansk-kaffe-aps/odense-c/kaffe-og-te-agentur-og-engros/0… |
| Danimarca | La Cabra Risteri ApS (gruppo La… | Risultato es. 2025 -2,7 mio.; DKK (virmo.dk, CVR 43681176). | https://virmo.dk/firma/43681176-la-cabra-risteri-aps - frammento: 'For the fisc… |
| Danimarca | RG ROM GUMMI A/S | Controllata tramite RGDE ApS, societa in portafoglio del fondo Dansk Ejerkapital. | https://www.danskejerkapital.dk/portefoelje/rom-gummi-a-s/ (scheda di portafogl… |
| Danimarca | H.C. JACOBSEN A/S | Capogruppo BEA HOLDING ApS; presidente CdA Pernille Andersen; distributore di imballaggi … | https://estatistik.dk/virksomhed/hc-jacobsen-as/75144911 - frammento: 'H.C. Jac… |
| Danimarca | NUTRIMIN A/S | Controllata di Nutreco N.V. (gruppo SHV, Paesi Bassi) - Trouw Nutrition, dal 01/12/2021. | https://www.nutreco.com/en/news/nutreco-finalises-acquisition-of-danish-nutrimi… |
| Danimarca | TJØRNEHØJ MØLLE A/S | Controllata del gruppo DLG (grande operatore, fuori target lead). | https://travservice.dk/velkommen-til-tjornehoj-molle/ e https://www.dlg.dk/Fode… |
| Danimarca | Grambogård | Controllata di FoodService Danmark A/S (gruppo Dagrofa). | https://www.tv2fyn.dk/assens/okoslagteri-solgt-dagrofa-kober-grambogard ; https… |
| Finlandia | CWP Coloured Wood Products Oy | Controllata di Auroora Yhtiöt Oyj (Tampere) — riqualificare il lead sulla capogruppo o sc… | https://auroora.com/en/auroora-yhtiot-acquires-cwp-coloured-wood-products-a-man… |
| Finlandia | Nordic Label Oy Ab | /note: controllata dal gruppo belga Asteria Group (ex Tilgmann Group); compliance decisa … | https://pmlehti.fi/uutiset/toimiala/nordic-label-myytiin-asteria-groupille/ - '… |
| Germania | H. Heitz Furnierkantenwerk GmbH… | Controllata di INDUS Holding AG (gruppo quotato) dal 2016; dato dimensionale da integrare… | https://www.h-heitz.de/aktuelles/presse/ - 'Seit 2016 gehoert Heitz zur INDUS, … |
| Germania | Weibler Confiserie Chocolaterie… | Controllata di United Chocolate GmbH (Beherrschungs-/Gewinnabführungsvertrag) — non di Ha… | https://www.theobroma-cacao.de/blog/aktuelles-aus-der-welt-der-schokolade-3/uni… |
| Germania | Effbe GmbH | Controllata della Woco Gruppe (Woco Franz Josef Wolf Holding GmbH) — valutare la complian… | https://www.wocogroup.com/en/company e https://de.linkedin.com/company/effbe-gm… |
| Germania | RIGDON GmbH | Controllata della Hörger Gruppe (WRZ Hörger GmbH u.; Co.; KG, Sontheim) dal 2017. | https://reifenpresse.de/2017/09/08/rigdon-gmbh-verkauft-neuer-eigentuemer-setzt… |
| Italia | Zalf SpA (Zalf Industria Mobili… | /note: 'societa' del Gruppo Euromobil (marchi Euromobil, Zalf, Desiree) - decisione EUDR … | https://www.gruppoeuromobil.com/en/group/history e https://www.zalf.com/en/comp… |
| Svezia | Aktiebolaget Karlaträ | Koncern di 2 società, moderbolag Karlaträ Försäljning AB (holding di vendita del medesimo… | allabolag.se: «Aktiebolaget Karlaträ ingår i en koncern med totalt 2 bolag, där… |
| Svezia | Balungstrands Sågverk AB | Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dal 2025, dopo… | allabolag.se: «Balungstrands Sågverk AB är ett dotterbolag med Profuragruppen A… |
| Svezia | Brattby Sågverks AB | Koncern con moderbolag Brattby Trading Aktiebolag. | allabolag.se (556415-5066): «företaget ingår i en koncern med moderbolag Brattb… |
| Svezia | Bäckebrons Sågverk Aktiebolag | Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dopo il fallim… | https://www.lesprom.com/en/news/Profura_reacquires_B%C3%A4ckebrons_and_Balungst… |
| Svezia | Drömtrappor AB | Moderbolag Förvaltnings AB Klätterbjörken; fatturato in calo da 126,4 MSEK (2024) a 83,2 … | allabolag.se (556309-7038): «Omsättning 2024: 126 413 tkr; 2025: 83 213 KSEK»; … |
| Svezia | Glimakra of Sweden AB | Controllata di Garpco Aktiebolag (dal 2007), koncern di 25 società / 311 addetti / 667 MS… | allabolag.se koncern (556120-7837): «moderbolaget är Garpco Aktiebolag ... konc… |
| Svezia | Hjältevadshus AB | Perdita d'esercizio 2025 (marginalità -32,6%); koncern Pulsen AB, 56 società. | allabolag.se (556232-9135): «omsättning 2025: 140 766 tkr ... vinstmarginal -32… |
| Svezia | Horreds Möbel Aktiebolag | Capogruppo Horreds Holding AB / Horreds Möbel Utvecklings AB (org.nr 559016-3324), gruppo… | https://www.allabolag.se/5563651974/koncern — «Horreds Möbel AB is part of a gr… |
| Svezia | Johanson Design Aktiebolag | Capogruppo Johanson Design Invest Aktiebolag (org.nr 556691-6457), gruppo di 5 società; 3… | https://www.allabolag.se/5563585206/koncern — «Johanson Design Aktiebolag is pa… |
| Svezia | NC Nordic Care AB | Capogruppo Materia Group AB (gruppo di arredo); lead da valutare a livello di capogruppo. | https://www.allabolag.se/foretag/nc-nordic-care-ab/valdemarsvik/m%C3%B6bler/2JZ… |
| Svezia | Nola Industrier AB | Capogruppo Sentensen Aktiebolag (gruppo di 3 società, 88,0 MSEK). | https://www.allabolag.se/foretag/nola-industrier-ab/stockholm/kontorsinredninga… |
| Svezia | Nydala Trävaru Aktiebolag | Capogruppo Nydala Trä Holding AB (gruppo di 2 società). | https://www.allabolag.se/organisation/nydala-trc3a4varu-aktiebolag/vrigstad/sc3… |
| Svezia | Sjöbergs Workbenches AB | Gruppo Idun Woodcraft AB, 74 società (gruppo Idun). | https://www.allabolag.se/organisation/sj%C3%B6bergs-workbenches-ab/stockaryd/tr… |
| Svezia | Småland Timber AB | Controllata da Green Wood Sverige AB (org.nr 559248-6616), holding del legno con sede a S… | allabolag/bolagsfakta: «Småland Timber AB ... moderbolag Green Wood Sverige AB»… |
| Svezia | Stockhult Glommers Timber AB | Controllata dal gruppo Stockhult (Stockhult Timber AB / Stockhult Holding AB). | allabolag organisation: «moderbolag Stockhult Timber AB ... koncern med totalt … |
| Svezia | Stolab Möbel AB | Capogruppo Martinvest i Smålandsstenar AB / Moid AB (holding familiare, 4 società). | allabolag/bolagsfakta: «Moderbolag är Martinvest i Smålandsstenar AB och koncer… |
| Svezia | Sunnerbo Fönster AB | Controllata da Sunnerbo Windows & Doors AB (org.nr 556986-4902); esercizio 2024 in perdit… | allabolag: «Moderbolaget är Sunnerbo Windows & Doors AB ... 40 anställda och gj… |
| Svezia | Swedese Möbler Aktiebolag | Capogruppo Patino Group AB (holding della proprietà). | allabolag/merinfo: «Moderbolaget är Patino Group AB ... Nuvarande ägare Anna Jo… |
| Svezia | VårgårdaHus AB | Controllata del gruppo danese HusCompagniet A/S tramite Svenska HusCompagniet AB — lead d… | mynewsdesk/TB-Gruppen: «TB-Gruppen säljer VårgårdaHus till EQT-ägda HusCompagni… |
| Svezia | ZilenZio AB | Capogruppo ZilenZio Selling Silence AB / Easier AB. | allabolag: «Moderbolag är ZilenZio Selling Silence AB och koncernmoderbolag är … |
| Svezia | Åsljunga Pallen Aktiebolag | Capogruppo Åsljunga-Pallen Service Aktiebolag (org.nr 556398-3211). | allabolag/bolagsfakta: «Moderbolaget är Åsljunga-Pallen Service Aktiebolag ... … |
| Svezia | Aktiebolaget Halmstads Gummifab… | Capogruppo Janmon AB. | allabolag: «Moderbolaget är Janmon AB ... Aktiebolaget Halmstads Gummifabrik ha… |
| Svezia | Rubber Company, R. Holmquist Ak… | Capogruppo Rubber Förvaltning Aktiebolag (gruppo di 5 società). | allabolag organisation: «...ingår i en koncern med totalt 5 bolag ... Moderbola… |
| Svezia | Bording AB | Controllata di F E Bording A/S (DK) — lead da valutare a livello di capogruppo danese. | allabolag/bolagsfakta: «Moderbolaget är F E Bording A/S ... Bordings hovedkonto… |
| Svezia | Econopack Aktiebolag | Capogruppo operativa S-Pack AB (aPak AB, Crispo Paper AB, Econopack AB); capogruppo ultim… | https://www.allabolag.se/foretag/s-pack-ab/m%C3%B6lndal/kontorstj%C3%A4nster/2K… |
| Svezia | Klippans Bruk AB | Capogruppo Sundh Center AB (holding di proprieta' della famiglia Sundh). | https://www.merinfo.se/foretag/Klippans-Bruk-AB-5565303228/2k1frgc-f5r8/styrels… |
| Svezia | Lenanders Grafiska AB | Controllata (100%) di Scandinavian Print Group (DK) dal 1/9/2021; capogruppo di riferimen… | https://grafkom.io/2021/08/30/scandinavian-print-group-acquires-its-fourth-swed… |
| Svezia | Nordiska Kaffebolaget H. Hansso… | Capogruppo WB Stockholm AB (org.nr 556705-8754, stessa sede) - holding/operativa di propr… | https://www.bolagsfakta.se/5567058754-WB_Stockholm_AB - 'WB Stockholm AB is the… |
| Svezia | Delicato Bakverk Aktiebolag | Moderbolag diretto Belveens Bageri AB; capogruppo di vertice Eldkvarn AB (gruppo di 8 soc… | https://www.allabolag.se/5561194720/delicato-bakverk-aktiebolag - 'Delicato Bak… |
| Svezia | Grahns Konfektyr AB | Controllata dal gruppo quotato Humble Group AB - compliance decisa a livello di capogrupp… | https://www.bolagsfakta.se/5567248884-Grahns_Konfektyr_AB - 'Moderbolaget ar Hu… |
| Svezia | Liljeholmens Stearinfabriks AB | Controllata via Liljeholmens Group AB / ALG Holding AB, capogruppo di vertice Tibia Intre… | https://www.allabolag.se/5560416348/liljeholmens-stearinfabriks-ab e https://ww… |
| Svezia | Narkes Slakteri i Gallersta Akt… | Controllata da Kott & Charkgruppen i Narke AB (gruppo di 5 societa)'. | https://allabolag.se/5565144861/koncern - 'The company is part of a group with … |
| Svezia | Nya Siljans Chark AB | Capogruppo Siljans Chark Holding AB (holding dei soci Par Nilsson e Mats Arjes); societa … | https://www.allabolag.se/organisation/nya-siljans-chark-ab/mora/livsmedel/2KHO5… |

*56 record.*

### 3.3 Filiere: commodity mancanti o imprecise

| Foglio | Azienda | Da | A | Fonte |
|---|---|---|---|---|
| Svezia | Aktiebolaget Ginsten Slakte… | Bovini/Carne — macello indipendente (bo… | **Bovini/Carne — macello (bovini, suini, ovini) e commercio car…** | https://www.allabolag.se/organisation/aktiebolaget-ginsten-slakteri/h… |
| Belgio | Vanrobaeys Granen & Zaden NV | Mangimi/Soia — granaglie e semi per man… | **Mangimi/Soia — mangimi per colombi (duivenvoer) a base di gra…** | https://www.vanrobaeysbelgium.com/nl-BE — composizione Power Rui «get… |
| Belgio | Baeten & Co NV | Olio di palma — raffinazione oli e gras… | **Olio di palma + Bovini — raffinazione di grassi animali (sego…** | https://baetennv.be/eng/our-products — «Baeten & Co is specialised in… |
| Belgio | Vleeshandel Vens NV | Bovini/Carne — ingrosso e sezionamento | **Bovini/Carne — sezionamento e commercio di carne (ingrosso pi…** | https://vleeshandelvens.be/afhaalpunten/ e https://vleeshandelvens.be… |
| Finlandia | Kiilax Oy | Legno/Arredo — compensato betulla/lamel… | **Legno/Arredo — botole d'ispezione e prodotti in compensato (p…** | https://vainu.io/company/kiilax-oy-... — «manufactures inspection hat… |
| Finlandia | Vainion Teurastamo Oy | Bovini/Carne | **Bovini/Carne — prevalentemente ovino (~15.000 capi/anno); bov…** | https://www.seutuneloset.fi/paikalliset/8458336 — «Suomen suurin lamm… |
| Germania | Schellinger KG | Mangimi/Soia | **Mangimi/Soia + Legno — pellet di legno Sonnen-Pellets (dal 19…** | https://www.depv.de/unternehmen/8c7524a3-... e https://schellinger-kg… |
| Italia | Spaggiari Industria Gomma S… | Gomma | **Gomma — articoli tecnici in gomma naturale (NR), sintetica, s…** | https://spaggiarigomma.com/ — «componenti in gomma naturale, sintetic… |

### 3.4 Contatti: email, sito, LinkedIn, fonte

Applicate solo le proposte che sono un **valore ben formato** per quel campo (una email che rispetta la sintassi, un URL nudo, una pagina LinkedIn aziendale). Le proposte in prosa sono state escluse dall'automatismo.

| Foglio | Azienda | Campo | Da | A |
|---|---|---|---|---|
| Austria | "Sojarei" Vollwertkost-Gesell… | `email` | info@sojarei.at | **office@sojarei.at** |
| Austria | Alvorada Kaffeerösterei GmbH | `sito` | http://alvorada.wien | **https://www.alvorada.com** |
| Austria | Ludwig Reiter Schuhmanufaktur… | `email` | office@ludwig-reiter.com | **reiter@ludwig-reiter.com** |
| Austria | Mischfutterwerk Großschedl Gm… | `sito` | http://www.grosschedl-futter.at | **https://www.grosschedl-futter.at** |
| Austria | Natural Products & Drugs GmbH | `email` | n.d. | **office@np-d.com** |
| Austria | Natural Products & Drugs GmbH | `sito` | http://www.np-d.com | **https://www.benenaturalproducts.com** |
| Austria | Ulrich Etiketten Gesellschaft… | `sito` | https://ulrich.at | **https://www.ulrich-etiketten.at** |
| Belgio | Bruyerre Chocolates SA | `linkedin` | — | **https://be.linkedin.com/company/bruyerre-ch…** |
| Belgio | Chocolaterie Ickx NV | `sito` | https://www.ickx.be/ | **https://www.choc-ickx.be/** |
| Belgio | Desmedt Labels BV | `email` | n.d. | **info@desmedt.be** |
| Belgio | Etilux SA | `linkedin` | — | **https://be.linkedin.com/company/etilux** |
| Belgio | Manufacture Belge de Chocolat… | `linkedin` | — | **https://be.linkedin.com/company/manufacture…** |
| Belgio | Oxfam Fair Trade CV | `linkedin` | — | **https://be.linkedin.com/company/oxfam-fair-…** |
| Belgio | Van De Walle SRL | `email` | info@vdw-grossisteenviande.be | **vdwgrossiste@skynet.be** |
| Belgio | Varia-Pack NV | `linkedin` | — | **https://be.linkedin.com/company/varia-pack-…** |
| Belgio | Vleeshandel Vens NV | `email` | n.d. | **info@vleeshandelvens.be** |
| Belgio | coffeeRoots NV | `linkedin` | https://fr.linkedin.com/company/coffe… | **https://be.linkedin.com/company/coffeeroots** |
| Danimarca | ONECOLLECTION A/S (House of F… | `fonte` | https://www.proff.dk/firma/onecollect… | **https://www.proff.dk/firma/onecollection-as…** |
| Finlandia | Akonkosken Saha Oy | `email` | akonkoskensaha@akonkoskensaha.fi | **akonkoskensaha@netikka.fi** |
| Finlandia | Brunberg Oy | `email` | n.d. | **tilaukset@brunberg.fi** |
| Finlandia | E J Hiipakka Oy | `sito` | https://www.ejh.fi | **https://www.hiipakka.net** |
| Finlandia | Goodio (Helsinki Heaven Oy) | `email` | info@goodio.fi | **feedback@goodio.fi** |
| Finlandia | ROST-kahvipaahtimo (Oy Kaffec… | `email` | hei@rost.fi | **rost@rost.fi** |
| Finlandia | St Michel Print Oy | `email` | paul.dima@stmichelprint.fi | **rami.paajanen@stmichelprint.fi** |
| Germania | Benecke Coffee GmbH & Co. KG | `email` | info@benecke-coffee.de | **info@rehmcoffee.de** |
| Germania | Büttenpapierfabrik Gmund GmbH… | `email` | n.d. | **info@gmund.com** |
| Germania | Christian Göbel Holzgroßhandl… | `email` | info@goebel-holz.de | **info@goebel-holz.com** |
| Germania | EGGER Druck + Medien GmbH | `email` | service@madika.de | **egger@eggerdruck.de** |
| Germania | Effbe GmbH | `sito` | https://effbe-diaphragm.de | **https://www.effbe.de** |
| Germania | HCS Hamburg Cocoa Services Gm… | `sito` | — | **https://www.cocoaservices.de** |
| Germania | Heinrich Meier Mühle und Futt… | `linkedin` | — | **https://de.linkedin.com/company/meier-muehle** |
| Germania | Hoppenworth & Ploch (Food Pro… | `email` | orders@hoppenworth-ploch.de | **info@hoppenworth-ploch.de** |
| Germania | Küper GmbH & Co. KG | `email` | n.d. | **info@kuepergermany.com** |
| Germania | Küper GmbH & Co. KG | `sito` | — | **https://kuepergermany.com** |
| Germania | Max Cropp GmbH & Co. KG (Timb… | `email` | n.d. | **info@cropp-timber.com** |
| Germania | Röstfein Kaffee GmbH | `fonte` | https://www.roestfein.de/impressum | **https://www.roestfein.de/impressum.html** |
| Germania | Südbadische Gummiwerke GmbH | `fonte` | https://www.s-b-g.de/impressum-agb/ | **http://www.s-b-g.de/Kontakt/Impressum_15.ht…** |
| Italia | A.T. Gomma Guarnizioni Indust… | `linkedin` | — | **https://it.linkedin.com/company/a-t-gomma-g…** |
| Italia | Bartoli S.p.A. | `email` | bartolispa@pec.it | **info@bartolispa.it** |
| Italia | C.I.M.A. S.r.l. (Compensati I… | `sito` | — | **https://www.cima-srl.com** |
| Italia | Compensati Toro S.p.A. | `email` | info@compensatitoro.com | **info@compensatitoro.it** |
| Italia | Conceria Ambassador S.p.A. | `linkedin` | — | **https://it.linkedin.com/company/conceria-am…** |
| Italia | Conceria Italia S.p.A. | `fonte` | https://www.conceriaitalia.com/contat… | **https://www.conceriaitalia.com/nuova-pagina** |
| Italia | Cortal Extrasoy S.p.A. | `email` | n.d. | **info@cortal.it** |
| Italia | Diesse Rubber Hoses S.p.A. | `linkedin` | — | **https://it.linkedin.com/company/diesse-rubb…** |
| Italia | Diesse Rubber Hoses S.p.A. | `sito` | — | **https://www.diesserubber.com** |
| Italia | Ellegi S.p.A. | `sito` | — | **https://ellegi.com** |
| Italia | Gambarotta S.r.l. | `sito` | — | **https://www.gambarotta.eu** |
| Italia | Holzland Fuchs S.r.l. | `sito` | — | **https://www.avantishop.it** |
| Italia | Imperator S.r.l. | `sito` | https://www.imperator.it | **https://www.imperator.cc** |
| Italia | Industria Cartaria Fenili S.p… | `email` | n.d. | **info@icfenili.it** |
| Italia | Slitti S.r.l. | `email` | n.d. | **info@slitti.it** |
| Italia | Zalf S.p.A. (Zalf Industria M… | `email` | n.d. | **zalfcen@zalf.com** |
| Olanda | Bannink Packaging B.V. | `email` | n.d. | **info@bannink.nl** |
| Olanda | Blanche Dael B.V. (Maison Bla… | `email` | n.d. | **office@blanchedael.nl** |
| Olanda | Brandsma Koffie B.V. | `email` | n.d. | **info@brandsmakoffie.nl** |
| Olanda | Bruns B.V. | `email` | n.d. | **jan.burgmans@bruns.nl** |
| Olanda | Daarnhouwer & Co B.V. | `email` | n.d. | **cocoa@daarnhouwer.nl** |
| Olanda | Drukkerij Van der Eems B.V. | `email` | sjoukje@vandereems.nl | **dj@vandereems.nl** |
| Olanda | Facta International B.V. | `email` | n.d. | **a.molenaar@facta-international.com** |
| Olanda | Giraffe Coffee B.V. | `email` | n.d. | **info@giraffecoffee.com** |
| Olanda | Gras Wood Wide B.V. | `linkedin` | — | **https://nl.linkedin.com/company/graswoodwide** |
| Olanda | Martinez Chocolade B.V. | `email` | n.d. | **info@martinezchocolade.nl** |
| Olanda | Rousseau Chocolade B.V. | `sito` | n.d. | **https://www.rousseau.nl/** |
| Olanda | S.R.C. (Special Refining Comp… | `email` | n.d. | **info@refinery.nl** |
| Olanda | Snel Industrie voor Karton en… | `sito` | — | **https://www.snelbv.nl** |
| Svezia | Aktiebolaget Johan Hansson | `linkedin` | — | **https://se.linkedin.com/company/ab-johan-ha…** |
| Svezia | Aktiebolaget Karlaträ | `linkedin` | — | **https://se.linkedin.com/company/ab-johan-ha…** |
| Svezia | Ekstrands Dörrar & Fönster AB | `linkedin` | — | **https://se.linkedin.com/company/ekstrand-&-…** |

*69 celle.*

### 3.5 Referenti e ruoli

Molte proposte erano nella forma «Nome Cognome — Ruolo»: applicate alla lettera avrebbero scritto il ruolo dentro il campo *Referente*. Uno splitter le separa nei due campi. Due guardie in senso opposto:

- un valore di **Ruolo** che non contiene nessuna parola-ruolo è in realtà un nome di persona finito nel campo sbagliato → scartato;
- un valore di **Referente** che è solo un titolo («Geschäftsführer») → scartato.

| Foglio | Azienda | Campo | Da | A |
|---|---|---|---|---|
| Belgio | Bruyerre Chocolates SA | `referente` | — | **Marc Delsemme** |
| Belgio | Bruyerre Chocolates SA | `ruolo` | — | **Amministratore / co-proprietario (titolo statut…** |
| Belgio | Bulo NV | `referente` | Dirk Busschop | **Carlo Busschop** |
| Belgio | Bulo NV | `ruolo` | CEO | **CEO / Managing Director** |
| Belgio | Confiserie De Bie - L'Abeille… | `referente` | — | **Bert Verriet** |
| Belgio | Confiserie De Bie - L'Abeille… | `ruolo` | — | **CEO** |
| Belgio | Confortluxe NV | `referente` | — | **Jimmy Ollevier** |
| Belgio | Confortluxe NV | `ruolo` | — | **Bestuurder** |
| Belgio | Dolfin SA | `referente` | — | **Jean-Jacques de Gruben** |
| Belgio | Dolfin SA | `ruolo` | — | **Directeur général (CEO)** |
| Belgio | Kartonnage Lefevere-Beel NV | `ruolo` | CEO / Bestuurder | **Vaste vertegenwoordiger / Bestuurder** |
| Belgio | La Chocolaterie Galler SA | `referente` | — | **Sebastien Desclee** |
| Belgio | La Chocolaterie Galler SA | `ruolo` | — | **CEO** |
| Belgio | Libeert NV | `referente` | Lily Libeert | **Ignace Libeert** |
| Belgio | Libeert NV | `ruolo` | Co-directrice (4a generazione del… | **gedelegeerd bestuurder (mantenere eventualmente…** |
| Belgio | Voeders Mellaerts NV | `referente` | — | **Dirk Mellaerts** |
| Belgio | Voeders Mellaerts NV | `ruolo` | — | **Bestuurder** |
| Germania | Effbe GmbH | `referente` | Franz Josef Wolf | **Joachim Geimer** |
| Germania | Gebr. Westhoff GmbH & Co. KG | `referente` | Max J.W. Ültzen | **Max J.W. Ueltzen, Christian Bruns, Pauline von …** |
| Germania | HCS Hamburg Cocoa Services Gm… | `referente` | Edmund Agyapong-Poku | **Nathaniel Durant** |
| Germania | Lindner Kartonagen GmbH | `referente` | Jutta Summann, Emanuel Dick | **Jutta Summann, Johannes Kunze** |
| Italia | Bartoli S.p.A. | `referente` | — | **Giorgio Giovanni Bartoli** |
| Italia | Bartoli S.p.A. | `ruolo` | — | **Presidente / Amministratore unico** |
| Italia | C.I.M.A. S.r.l. (Compensati I… | `referente` | — | **Alessandro Dal Soglio** |
| Italia | C.I.M.A. S.r.l. (Compensati I… | `ruolo` | — | **Presidente** |
| Italia | Cartonificio Sandreschi S.r.l. | `referente` | — | **Ernesto Sandreschi** |
| Italia | Cartonificio Sandreschi S.r.l. | `ruolo` | — | **Presidente / Legale rappresentante** |
| Italia | Cesare Trucillo S.p.A. (Caffè… | `referente` | — | **Matteo Trucillo** |
| Italia | Cesare Trucillo S.p.A. (Caffè… | `ruolo` | — | **Presidente e Amministratore Delegato** |
| Italia | Cortal Extrasoy S.p.A. | `referente` | — | **Gianpietro Didoné** |
| Italia | Cortal Extrasoy S.p.A. | `ruolo` | — | **Presidente** |
| Italia | Domori S.p.A. | `referente` | — | **Riccardo Illy** |
| Italia | Domori S.p.A. | `ruolo` | — | **Amministratore Delegato** |
| Italia | Insit Industria S.p.A. | `referente` | — | **Guglielmo Debenedetti** |
| Italia | Insit Industria S.p.A. | `ruolo` | — | **Presidente** |
| Italia | Majani 1796 S.p.A. | `referente` | — | **Francesco Mezzadri Majani** |
| Italia | Majani 1796 S.p.A. | `ruolo` | — | **Presidente e Amministratore Delegato** |
| Italia | Original Parquet S.p.A. | `referente` | — | **Giovanni Ballardini** |
| Italia | Original Parquet S.p.A. | `ruolo` | — | **Direttore Generale** |
| Italia | Segheria Saccavini S.r.l. | `referente` | — | **Nella De Sabbata** |
| Italia | Segheria Saccavini S.r.l. | `ruolo` | — | **Presidente** |
| Olanda | Ascot Amsterdam B.V. | `referente` | — | **Merijn Bruinse** |
| Olanda | Ascot Amsterdam B.V. | `ruolo` | — | **Managing Director** |
| Olanda | BeBo Parket B.V. | `referente` | Frans Bolier | **Kees van de Beek / Marielle Zwolsman** |
| Olanda | BeBo Parket B.V. | `ruolo` | Directeur / mede-eigenaar | **Directeur** |
| Olanda | De Groot Drukkerij B.V. | `referente` | Anton de Groot | **Wim Everts** |
| Olanda | De Groot Drukkerij B.V. | `ruolo` | Directeur | **Algemeen directeur** |
| Olanda | Gunnewick Mengvoeders B.V. | `referente` | — | **Marc van Uum** |
| Olanda | Gunnewick Mengvoeders B.V. | `ruolo` | — | **Algemeen directeur** |
| Olanda | Randstad Vleesgroothandel B.V. | `referente` | J.H.M. van der Arend | **John van der Arend** |
| Olanda | Randstad Vleesgroothandel B.V. | `ruolo` | Algemeen directrice | **Directeur** |
| Olanda | Rousseau Chocolade B.V. | `referente` | — | **Paul Diepstraten** |
| Olanda | Rousseau Chocolade B.V. | `ruolo` | — | **Directeur** |
| Olanda | Van Kooten Vleesgroothandel B… | `referente` | — | **Wilco van Kooten, Gerwin van Kooten** |
| Olanda | Van Kooten Vleesgroothandel B… | `ruolo` | — | **Directeuren / eigenaren** |
| Olanda | Zaadhof's Cartonnage Fabrieke… | `ruolo` | Directeur | **Directeur (co-gestione con Karina Wessels); fon…** |
| Svezia | Lars Carlsson Trävaru Aktiebo… | `referente` | — | **Lars Anders Hilding Carlsson** |
| Svezia | Lars Carlsson Trävaru Aktiebo… | `ruolo` | — | **Styrelseordförande / ansvarig (nessun VD regist…** |
| Svezia | Lykke Coffee Farms AB | `referente` | — | **Johan Wellander** |
| Svezia | Lykke Coffee Farms AB | `ruolo` | — | **Ordförande / grundare (nessun VD registrato)** |

*60 celle.*

### 3.6 Dimensione

È un campo di testo libero che contiene dati già verificati: sostituirlo in blocco li perderebbe. Le proposte sono state quindi divise fra **clausole da aggiungere in coda** (un legame di gruppo, un numero di registro, un dato di bilancio) e sostituzioni integrali, queste ultime solo quando un agente ha ricostruito il campo per intero con la fonte.

| Foglio | Azienda | Cosa cambia |
|---|---|---|
| Austria | CARINI GmbH | sostituito: Fatturato oltre 18 Mio. € nel 2010 (con 123 dipendenti; fonte Wirtschaftszeit.at); dato di fatturato piu' r… |
| Austria | Rudolf Frierss & Söhne Fleisc… | aggiunto: Bilanzsumme 13,3 Mio. € al 31.03.2025 (firmenabc.at). |
| Austria | Salzer Papier GmbH | aggiunto: FN 211554i, LG St.; Pölten. |
| Belgio | Corpack NV | aggiunto: N. impresa BE 0452.991.978. 44,3 FTE (bilancio NBB depositato 17-07-2026); fatturato non pubblicato, stimat… |
| Belgio | Decolvenaere BV | sostituito: Fatturato totale 38.585.036 € nell'ultimo bilancio depositato (deposito NBB del 27-01-2025, quindi esercizi… |
| Belgio | Euro Meat Group NV | aggiunto: N. impresa BE 0832.292.464. |
| Belgio | Slachthuis Swaegers NV | aggiunto: Il gruppo familiare ha rilevato anche il macello di Bastogne. |
| Danimarca | BUCHS A/S | sostituito: Bruttofortjeneste 14.746.681 DKK nel 2024 (~1,98 M€, cambio 7,46), contro 16.092.571 DKK nel 2023; risultat… |
| Danimarca | CAFÉU DENMARK ApS | aggiunto: ndenti non pubblicati. Fatturato non pubblicato (ApS, bilancio in forma ridotta). CVR 33243537, capitale 80… |
| Danimarca | COLOR LABEL A/S | aggiunto: ' registrato nel 1991). Etichette autoadesive per food, chimica e retail; parco macchine flexo Nilpeter (10… |
| Danimarca | Copenhagen Coffee Lab ApS | aggiunto: Capogruppo Copenhagen Coffee Lab Holding ApS (gruppo di 6 societa'); 70% Steen Skallebæk e Ole Kristofferse… |
| Danimarca | DANSK KAFFE ApS | aggiunto: Capogruppo KAFFEA ApS (gruppo di 2 societa'), societa' costituita il 27.11.2013.; Micro-impresa MOLTO SOTTO… |
| Danimarca | EMBALLAGEFABRIKKEN THY PAP | aggiunto: CVR 25352769 (THY PAP, enkeltmandsvirksomhed).; Fatturato e addetti non pubblicati per forma giuridica; mic… |
| Danimarca | Estate Coffee Copenhagen A/S | sostituito: Bruttofortjeneste 15 mio DKK nel 2024 (~2,01 M€, cambio 7,46; 11 mio DKK nel 2023); fatturato non pubblicat… |
| Danimarca | Grambogård | aggiunto: Controllata di FoodService Danmark A/S (gruppo Dagrofa). |
| Danimarca | H. EMBALLAGE ApS | sostituito: Bruttofortjeneste 8.149.124 DKK nel 2024 (~1,09 M€, cambio 7,46), contro 7.847.995 DKK nel 2023; risultato … |
| Danimarca | H.C. JACOBSEN A/S | aggiunto: Capogruppo BEA HOLDING ApS; presidente CdA Pernille Andersen; distributore di imballaggi ed elastici, FUORI… |
| Danimarca | KLS PUREPRINT A/S | aggiunto: Controllata (oggi integralmente) di F.; E.; BORDING A/S dopo il riacquisto della quota di Knud Erik Larsen … |
| Danimarca | KVIST INDUSTRIES A/S | aggiunto: Controllata da KVIST HOLDING A/S, partecipata dal fondo Dansk Ejerkapital; fatturato non pubblicato (bilanc… |
| Danimarca | La Cabra Risteri ApS (gruppo … | aggiunto: Risultato es. 2025 -2,7 mio.; DKK (virmo.dk, CVR 43681176). |
| Danimarca | NIELAUS A/S | sostituito: 19 dipendenti (krak.dk/proff.dk, CVR 35480943; il valore '11' riportato altrove si riferisce alla produktio… |
| Danimarca | NUTRIMIN A/S | aggiunto: Controllata di Nutreco N.V. (gruppo SHV, Paesi Bassi) - Trouw Nutrition, dal 01/12/2021. |
| Danimarca | RG ROM GUMMI A/S | aggiunto: Controllata tramite RGDE ApS, societa in portafoglio del fondo Dansk Ejerkapital. |
| Danimarca | STIBO COMPLETE A/S (già Rosen… | sostituito: Nettoomsaetning 748 mio DKK nell'esercizio 2025 (~100,3 M€, cambio 7,46), con perdita di 33,5 mio DKK dovut… |
| Danimarca | TIMBERMAN DENMARK A/S | aggiunto: Controllata del gruppo svedese quotato Volati AB dal dicembre 2024 (in precedenza Corticeira Amorim); Mogen… |
| Danimarca | TJØRNEHØJ MØLLE A/S | aggiunto: Controllata del gruppo DLG (grande operatore, fuori target lead). |
| Finlandia | CWP Coloured Wood Products Oy | aggiunto: Controllata di Auroora Yhtiöt Oyj (Tampere) — riqualificare il lead sulla capogruppo o scartare. |
| Finlandia | Nordic Label Oy Ab | aggiunto: /note: controllata dal gruppo belga Asteria Group (ex Tilgmann Group); compliance decisa a livello di capog… |
| Germania | Effbe GmbH | aggiunto: Controllata della Woco Gruppe (Woco Franz Josef Wolf Holding GmbH) — valutare la compliance a livello di ca… |
| Germania | H. Heitz Furnierkantenwerk Gm… | aggiunto: Controllata di INDUS Holding AG (gruppo quotato) dal 2016; dato dimensionale da integrare con fonte e anno. |
| Germania | RIGDON GmbH | aggiunto: Controllata della Hörger Gruppe (WRZ Hörger GmbH u.; Co.; KG, Sontheim) dal 2017. |
| Germania | Röstfein Kaffee GmbH | aggiunto: . Legame di gruppo: controllata al 100% da Zentralkonsum eG (Berlino) — HRB 107856. |
| Germania | Sawade GmbH | aggiunto: Nota: socio di maggioranza Fintura Corporate Finance (Berlino) dal 2021, post-insolvenza in Eigenverwaltung. |
| Germania | Weibler Confiserie Chocolater… | aggiunto: Controllata di United Chocolate GmbH (Beherrschungs-/Gewinnabführungsvertrag) — non di Halloren. |
| Italia | Zalf S.p.A. (Zalf Industria M… | aggiunto: /note: 'societa' del Gruppo Euromobil (marchi Euromobil, Zalf, Desiree) - decisione EUDR a livello di capog… |
| Olanda | Bocca Coffee B.V. | aggiunto: Acquisizione di Single Estate Coffee Roasters da Cavesco; fatturato e organico da riaggiornare post-operazi… |
| Olanda | Chocolatemakers B.V. | aggiunto: Legame di gruppo: dal 2025 confluita in The Chocolate Impact Group (fusione con Hands Off; marchi Chocolate… |
| Olanda | Veldhuis Media B.V. | aggiunto: Partecipazione di minoranza Wadinko NV dal dicembre 2023. |
| Svezia | Aktiebolaget Ginsten Slakteri | aggiunto: Capogruppo: Aktiebolaget Joh. M. Johansson, Kött- & Charkuteriaffär (gruppo familiare di 4 societa'). |
| Svezia | Aktiebolaget Halmstads Gummif… | aggiunto: Capogruppo Janmon AB. |
| Svezia | Aktiebolaget Karlaträ | aggiunto: Koncern di 2 società, moderbolag Karlaträ Försäljning AB (holding di vendita del medesimo gruppo familiare). |
| Svezia | Balungstrands Sågverk AB | aggiunto: Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dal 2025, dopo il fallimento di … |
| Svezia | Bording AB | aggiunto: Controllata di F E Bording A/S (DK) — lead da valutare a livello di capogruppo danese. |
| Svezia | Brattby Sågverks AB | aggiunto: Koncern con moderbolag Brattby Trading Aktiebolag. |
| Svezia | Bäckebrons Sågverk Aktiebolag | aggiunto: Controllata di Green Wood Sverige AB; koncernmoderbolag Profuragruppen AB (dopo il fallimento di Ziegler Gr… |
| Svezia | Delicato Bakverk Aktiebolag | aggiunto: Moderbolag diretto Belveens Bageri AB; capogruppo di vertice Eldkvarn AB (gruppo di 8 societa)'. |
| Svezia | Drömtrappor AB | aggiunto: Moderbolag Förvaltnings AB Klätterbjörken; fatturato in calo da 126,4 MSEK (2024) a 83,2 MSEK (2025). |
| Svezia | Econopack Aktiebolag | aggiunto: Capogruppo operativa S-Pack AB (aPak AB, Crispo Paper AB, Econopack AB); capogruppo ultima Lameja Invest AB… |
| Svezia | Glimakra of Sweden AB | aggiunto: Controllata di Garpco Aktiebolag (dal 2007), koncern di 25 società / 311 addetti / 667 MSEK. |
| Svezia | Grahns Konfektyr AB | aggiunto: Controllata dal gruppo quotato Humble Group AB - compliance decisa a livello di capogruppo. Esercizio 2024 … |
| Svezia | Hjältevadshus AB | aggiunto: Perdita d'esercizio 2025 (marginalità -32,6%); koncern Pulsen AB, 56 società. |
| Svezia | Horreds Möbel Aktiebolag | aggiunto: Capogruppo Horreds Holding AB / Horreds Möbel Utvecklings AB (org.nr 559016-3324), gruppo di 3 società. |
| Svezia | Johanson Design Aktiebolag | aggiunto: Capogruppo Johanson Design Invest Aktiebolag (org.nr 556691-6457), gruppo di 5 società; 3 controllate diret… |
| Svezia | Klippans Bruk AB | aggiunto: Capogruppo Sundh Center AB (holding di proprieta' della famiglia Sundh). |
| Svezia | Lenanders Grafiska AB | aggiunto: Controllata (100%) di Scandinavian Print Group (DK) dal 1/9/2021; capogruppo di riferimento per la complian… |
| Svezia | Liljeholmens Stearinfabriks AB | aggiunto: Controllata via Liljeholmens Group AB / ALG Holding AB, capogruppo di vertice Tibia Intressenter AB; contro… |
| Svezia | NC Nordic Care AB | aggiunto: Capogruppo Materia Group AB (gruppo di arredo); lead da valutare a livello di capogruppo. |
| Svezia | Nola Industrier AB | aggiunto: Capogruppo Sentensen Aktiebolag (gruppo di 3 società, 88,0 MSEK). |
| Svezia | Nordiska Kaffebolaget H. Hans… | aggiunto: Capogruppo WB Stockholm AB (org.nr 556705-8754, stessa sede) - holding/operativa di proprieta familiare; gr… |
| Svezia | Nya Siljans Chark AB | aggiunto: Capogruppo Siljans Chark Holding AB (holding dei soci Par Nilsson e Mats Arjes); societa subentrata alla pr… |
| Svezia | Nydala Trävaru Aktiebolag | aggiunto: Capogruppo Nydala Trä Holding AB (gruppo di 2 società). |
| Svezia | Närkes Slakteri i Gällersta A… | aggiunto: Controllata da Kott & Charkgruppen i Narke AB (gruppo di 5 societa)'. |
| Svezia | Rubber Company, R. Holmquist … | aggiunto: Capogruppo Rubber Förvaltning Aktiebolag (gruppo di 5 società). |
| Svezia | Sjöbergs Workbenches AB | aggiunto: Gruppo Idun Woodcraft AB, 74 società (gruppo Idun). |
| Svezia | Småland Timber AB | aggiunto: Controllata da Green Wood Sverige AB (org.nr 559248-6616), holding del legno con sede a Sunne. |
| Svezia | Stockhult Glommers Timber AB | aggiunto: Controllata dal gruppo Stockhult (Stockhult Timber AB / Stockhult Holding AB). |
| Svezia | Stolab Möbel AB | aggiunto: Capogruppo Martinvest i Smålandsstenar AB / Moid AB (holding familiare, 4 società). |
| Svezia | Sunnerbo Fönster AB | aggiunto: Controllata da Sunnerbo Windows & Doors AB (org.nr 556986-4902); esercizio 2024 in perdita -1,3 MSEK. |
| Svezia | Swedese Möbler Aktiebolag | aggiunto: Capogruppo Patino Group AB (holding della proprietà). |
| Svezia | VårgårdaHus AB | aggiunto: Controllata del gruppo danese HusCompagniet A/S tramite Svenska HusCompagniet AB — lead da valutare a livel… |
| Svezia | ZilenZio AB | aggiunto: Capogruppo ZilenZio Selling Silence AB / Easier AB. |
| Svezia | Åsljunga Pallen Aktiebolag | aggiunto: Capogruppo Åsljunga-Pallen Service Aktiebolag (org.nr 556398-3211). |

*72 celle.*

### 3.7 Sede

Nessuna correzione di sede applicata: le 21 proposte sono precisazioni redazionali (sede legale accanto a quella operativa, nuovo nome del comune dopo una fusione) oppure — in un caso, Libeert — un valore che appartiene a un altro campo. Restano rilievi aperti.

---

## 4. La riga rimossa

**Skagerak Denmark A/S** (Danimarca) — categoria «b».

Societa' estinta: il CVR 28855990 risulta «opløst efter fusion» e non ha piu' alcun direktør registrato. La persona giuridica censita non esiste piu'. Stesso criterio gia' applicato in v1 a Odense Seglmærkefabrik («opløst efter fusion») e a Kaffekompaniet. Si aggiunge il legame gia' noto con Fritz Hansen, fra i big esclusi.

> Fonte: https://estatistik.dk/virksomhed/skagerak-denmark-as/28855990/roller — «0 direktører; status: OPLØST EFTER FUSION»

Nessun'altra riga è stata tolta. In particolare **non** è stato rimosso nessun fuori taglia: STOK Emballage (92 M€), Flatz (72 M€), DO IT (~125 M€) e Henry Lamotte (138 M€) restano nei fogli come rilievi aperti, perché la taglia non è fra le categorie che il mandato autorizza a correggere d'ufficio. È una decisione che spetta al cliente.

---

## 5. La riverifica dei casi con riserva (PASSO 3)

96 rilievi portavano una proposta con riserva esplicita. Sono stati affidati ad agenti con due vincoli: **massimo 2-3 query WebSearch per caso** — chi resta incerto dopo tre resta incerto — e **salvataggio incrementale ogni 3-4 record**. Il secondo vincolo si è rivelato decisivo: un agente è stato interrotto dal limite di quota e i record già lavorati erano salvati.

- **46 riserve sciolte e applicate.**
- **17 confermate come già corrette**: erano falsi allarmi. Fra queste Blå Station e Candy People (il dominio `.se` è quello giusto), Conceria Lomar, Spaggiari e il LinkedIn di Van den Berg Hardhout. Sono la conferma che valeva la pena non applicarle d'ufficio.
- **3 restano incerte** e restano tali: Sopraco NV, Nord Legnami Group, Lecont S.r.l.

Le correzioni più significative emerse dalla riverifica:

| Foglio | Azienda | Cosa è emerso |
|---|---|---|
| Germania | Lindner Kartonagen | «Emanuel Dick», il referente nel foglio, **non trova riscontro in nessuna fonte pubblica**. I Geschäftsführer reali sono Jutta Summann e Johannes Kunze (HRB 100588). |
| Italia | Domori S.p.A. | Dal 29.05.2026 l'AD è **Riccardo Illy**, non Giacomo Biviano (che resta consigliere). |
| Germania | Gebr. Westhoff | L'Impressum attuale non riporta più Werner Schulte: i GF sono Ültzen, Bruns e von Mettenheim (HRB 4460). |
| Danimarca | Skagerak Denmark | La riserva si è sciolta in modo inatteso: la società è estinta. Da qui la rimozione al §4. |
| Italia | Original Parquet | Giovanni Ballardini è Direttore Generale, non Presidente: il Presidente è il padre Roberto. |

---

## 6. Ciò che NON è stato applicato, e perché

Questa sezione è la più importante per il cliente: sono le cose che restano da decidere.

### 6.1 Le tre categorie del PASSO 4

Dei 100 rilievi di gravità `alta` che avevano una correzione proposta ancora aperta, **49 sono stati sciolti in v2** e **51 restano aperti**, così ripartiti:

| Categoria | Casi | Trattamento |
|---|--:|---|
| Legame di gruppo | 31 | Dove il legame era **non dichiarato o errato** è stato corretto (§3.2): è un errore di dato. Dove era **già dichiarato** nel campo non è un errore, ed è una **decisione di selezione che spetta al cliente**. |
| Fuori taglia | 12 | **Non rimossi.** Il mandato non autorizza a togliere una riga per la sola dimensione. Il dato corretto è nel foglio, la decisione al cliente. |
| Operatore vs commerciante | 5 | **Lasciati e segnalati.** Stabilire se un commerciante sia «operatore» ai sensi dell'EUDR è una valutazione **giuridica**, non un dato verificabile a fonte. |
| Dato datato o incompleto | 3 | Restano rilievi aperti nel report. |

I **dieci record operatore/commerciante** già individuati in v1 restano tutti nei fogli, invariati: Varia-Pack, Hausberger, Pappersgrossisten, Däckteam, Svenska Gummihuset, Cebeco Fourage, Skovs Korn, Rickl-Mühle, SRC, Kargro Banden.

### 6.2 Proposte che sono decisioni, non dati

Le proposte che cominciano con «Rimuovere», «Escludere», «Valutare», «Declassare», «Indicare» non sono un valore da scrivere in una cella: sono una raccomandazione. Non sono state applicate.

| Foglio | Azienda | Campo | Proposta |
|---|---|---|---|
| Austria | Heidi Chocolat AG | `denominazione` | Rimuovere o declassare: succursale austriaca di Heidi Chocolat SA (Zug, CH), gruppo Kex Con… |
| Austria | Testa Rossa Caffe GmbH | `filiera` | Valutare come lead il Handelshaus Wedl (torrefazione) al posto di Testa Rossa Caffe GmbH |
| Belgio | A & A Chocolaterie NV | `linkedin` | Mantenere entrambi i record. Segnalare esplicitamente nel campo linkedin che la pagina http… |
| Belgio | Emballages Gruselle SRL | `dimensione` | Rimuovere il record (micro-impresa fuori forbice) |
| Belgio | Euro Meat Group NV | `dimensione` | Segnalare esplicitamente: «unita' della holding Cadus (4 macelli BE, ~25% delle macellazion… |
| Belgio | Hexpol Compounding BV | `dimensione` | Indicare nel campo dimensione: «controllata del gruppo HEXPOL AB (Svezia, Nasdaq Stockholm)… |
| Belgio | Koffie St.-Michel NV | `dimensione` | Rimuovere il record (micro-impresa fuori forbice) |
| Belgio | Slachthuis Velzeke BV | `dimensione` | Indicare: «dal 01-01-2025 controllata dalla holding Cadus (rilevata da Vion Food Group) — s… |
| Belgio | Tannerie Masure SA | `denominazione` | Valutare il lead a livello di capogruppo Groupe Saturne / Financiere Saturne (FR): la socie… |
| Belgio | Varia-Pack NV | `filiera` | Rimuovere il record (distributore a valle, non immettitore) |
| Danimarca | BØJSØ DØRE & VINDUER A/S | `denominazione` | Escludere o riclassificare il lead: indirizzare il contatto alla capogruppo Inwido Denmark … |
| Danimarca | COPENHAGEN CHOCOLATE FACTOR… | `dimensione` | Indicare l'anno di riferimento del fatturato 48,3 mio. DKK e precisare 22 dipendenti |
| Danimarca | HVIDBJERG VINDUET A/S | `dimensione` | Controllata del gruppo tedesco ACO (via ACO Nordic) — escludere o riclassificare il lead, c… |
| Danimarca | JKE DESIGN A/S | `denominazione` | Escludere o riclassificare il lead: contatto a livello di capogruppo Ballingslöv Internatio… |
| Danimarca | LILLEHEDEN A/S | `dimensione` | Aggiornare il bruttofortjeneste all'ultimo esercizio disponibile e valutare il lead a livel… |
| Danimarca | N. EILERSEN A/S | `fonte` | Indicare esplicitamente CVR 35118519 per N. EILERSEN A/S |
| Danimarca | SKJERN PAPER A/S (già Skjer… | `dimensione` | Controllata di Sonoco Products Company (USA) dal Q4 2022 (acquisizione ~675 mio DKK). Produ… |
| Danimarca | SKOVS KORN A/S. KORN- OG FO… | `filiera` | Escludere o declassare il lead salvo verifica che la societa' operi anche in conto proprio … |
| Danimarca | STOK EMBALLAGE K/S | `dimensione` | Fatturato 686,7 mio DKK nel 2025 (~92 M€) — FUORI FORBICE (>40 M€). Controllata di maggiora… |
| Germania | ETS Mischfutterwerk GmbH & … | `denominazione` | Segnalare nel record: JV Eilers Futtermittel / agritura Raiffeisen eG (+ Raiffeisen Teuto-S… |
| Italia | Diesse Rubber Hoses S.p.A. | `dimensione` | indicare fatturato con anno e usare come fonte https://topaziende.quotidiano.net/lombardia/… |
| Italia | GranCarni S.p.A. | `denominazione` | Segnalare nel record: societa soggetta a direzione e coordinamento di Gruppo Balletta S.p.A. |
| Olanda | Bangma Verpakking B.V. | `dimensione` | Rimuovere il record (controllata Stora Enso) oppure riportare esplicitamente la catena Bang… |
| Olanda | Continental Chocolate B.V. | `dimensione` | Segnalare appartenenza al gruppo Baronie (BE) / Baronie-de Heer B.V.; valutare esclusione c… |
| Olanda | Zaadhof's Cartonnage Fabrie… | `fonte` | Rimuovere il fatturato di 6 M€ o indicarne la fonte reale; dichiarare che il fatturato non … |
| Svezia | Aktiebolaget Cool & Candy | `dimensione` | Segnalare esplicitamente nel campo che la compliance e decisa dalla capogruppo quotata Humb… |
| Svezia | Däckteam i Sverige Aktiebol… | `filiera` | Rimuovere il lead (commerciante a valle, non immette per primo sul mercato UE) |
| Svezia | Norbag AB | `dimensione` | Segnalare esplicitamente che il decisore compliance e' Tingstad Group AB (Goteborg). Fattur… |
| Svezia | Puratos Sweden AB | `filiera` | Rimuovere il lead (filiale distributiva di gruppo estero, non immette per prima sul mercato… |
| Svezia | Svenska Gummihuset Aktiebol… | `filiera` | Rimuovere il record dal foglio Svezia (fuori perimetro EUDR: rivenditore/officina pneumatic… |

*30 rilievi, più 30 sul solo campo Dimensione.*

### 6.3 Correzioni scartate perché avrebbero introdotto un errore nuovo

| Foglio | Azienda | Campo | Proposta | Perché no |
|---|---|---|---|---|
| Austria | BIOSERVICE Zach Ges.m.b.H. | `ruolo` | Mag. DI (FH) Dr. Robert Zach | la proposta non contiene una parola-ruolo: non e' un ruolo |
| Italia | Conceria Beschin, Conceria Daniela | `denominazione` | aggiungere la forma giuridica | Ciascuna corrisponde a **due entità omonime distinte** al Registro (una S.n.c. e una S.r.l. nello stesso comune): scegliere la forma significherebbe *decidere* quale sia l'operatore EUDR. Già escluse in v1, confermata l'esclusione. |
| Germania | Göbel, Fuhlrott, Josef Schulte, SAF Kartonagen | `denominazione` | espandere la ragione sociale abbreviata | Le forme brevi sono **corrette**, solo abbreviate. Esclusione già decisa in v1, mantenuta per coerenza. |
| Svezia | Abstracta, Gyllsjö Träindustri | `denominazione` | `AB` → `Aktiebolag` | Il foglio svedese **non ha uno stile maggioritario** (47 `AB` contro 42 `Aktiebolag`): normalizzare sarebbe arbitrario. Esclusione già decisa in v1. |
| Italia | Cartiera S. Rocco | `denominazione` | `CARTIERA S.ROCCO S.P.A.` | È solo il maiuscolo del registro, come per il foglio Danimarca: non si impone la grafia registrale. |
| Belgio | Repro NV | `filiera` | `Mangimi/Soia` → `Soia` | Romperebbe la tassonomia adottata dagli altri fogli. La riclassificazione di Repro era già stata decisa in v1. |
| Danimarca | 51 denominazioni in MAIUSCOLO | `denominazione` | *title case* | Rovinerebbe gli acronimi: `JKE DESIGN` → `Jke Design`, e lo stesso per NPI, MC, KLS, H.C., DHS. |

### 6.4 Rilievi che restano semplicemente aperti

- **202** sul campo Dimensione: la proposta non è riconducibile a una clausola accertata (spesso è una stima da riconfermare, o un commento).
- **10** proposte che sembravano applicabili ma il cui *problema* era esso stesso dubitativo («probabilmente errato», «da verificare»): meglio un rilievo aperto che un dato incerto scritto nel foglio. La riverifica del PASSO 3 ne ha confermate diverse come già corrette.
- Le **email dubbie** restano `DA CONFERMARE`: il mandato vieta sia di inventarle sia di cancellarle d'ufficio.
- **Cafe Solo Oy** (Finlandia) resta l'unico record dell'intero censimento mai coperto dalla verifica web.

---

## 7. Due difetti dell'infrastruttura, trovati applicando

Vale la pena registrarli perché riguardano gli script che il progetto continuerà a usare.

**Il confronto fra denominazioni era troppo largo.** `applica_correzioni.py` e `applica_referenti.py` consideravano uguali due nomi che condividono i **primi 12 caratteri**. In svedese questo fa collidere fra loro *tutte* le società che cominciano per `Aktiebolaget` — nel foglio Svezia sono sei — e infatti una correzione destinata a **Ginsten Slakteri** è finita su **Karlaträ**, una segheria. L'ha intercettata la guardia sul valore attuale, che ha visto `Legno/Segheria` dove si aspettava `Bovini/Carne`: è esattamente il lavoro per cui la guardia esiste. In v2 il match esatto ha la precedenza e il ripiego fuzzy si applica solo se è **unico**. **Verificato che in v1 il difetto non ha prodotto scritture sbagliate**: delle 131 correzioni di referente applicate allora, quattro toccavano nomi collidenti e tutte e quattro hanno raggiunto il record giusto.

**La verifica d'integrità confrontava le righe per posizione.** Ma `add_country.py` riordina il foglio per filiera e nome: correggere una denominazione **sposta legittimamente la riga**, e il confronto posizionale leggeva lo spostamento come una valanga di campi svuotati. Ora `verifica_integrita.py` confronta i record **per identità**, seguendo le rinomine e le rimozioni dichiarate.

Una terza cosa, minore ma utile: le clausole aggiunte al campo Dimensione usano una forma `__APPEND__` con **ancora** sul valore attuale invece della guardia `da`. Con la sola guardia, due clausole sulla stessa azienda si annullavano a vicenda — la seconda trovava il campo già cambiato dalla prima e veniva saltata. Succedeva a Grahns Konfektyr e a Liljeholmens, che ne avevano due ciascuna.

---

## 8. Come rieseguire

Tutti gli script stanno in `_myeudr_build/v2/` e sono **rieseguibili**: una seconda esecuzione applica 0 correzioni e riporta tutto come «già uguale».

```bash
python _myeudr_build/v2/inventario.py        # confronta le proposte col foglio attuale
python _myeudr_build/v2/classifica.py        # valore applicabile / decisione / da guardare
python _myeudr_build/v2/costruisci_tabelle.py
python _myeudr_build/v2/dimensione.py        # clausole da aggiungere al campo Dimensione
python _myeudr_build/v2/da_agenti.py A B C   # esiti della riverifica -> tabelle
python _myeudr_build/v2/applica_v2.py        # applica (--dry-run per provare)
python _myeudr_build/v2/rimuovi.py           # le rimozioni, con la loro motivazione
python _myeudr_build/v2/verifica_integrita.py
python _myeudr_build/v2/genera_changelog.py  # rigenera questo documento
```

I due percorsi della v1 restano validi e sono rispettati: **DK/SE/NL/BE/AT** si correggono nei JSON di build e si rigenerano con `add_country.py` (rigenerazione riverificata **identica cella per cella** prima di iniziare); **IT/DE/FI** si correggono nella cella in posto, perché rigenerarli da un JSON esportato riordinerebbe le righe già consegnate. Dopo ogni rigenerazione l'ordine dei fogli viene ripristinato.

`MyEUDR_Lead_Mapping.xlsx` (v1) **non è stata toccata**; `_myeudr_build/v2/backup_v1.xlsx` ne conserva la copia usata come termine di confronto.

