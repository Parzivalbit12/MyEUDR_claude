# Fase A — Controlli deterministici automatici

_Generato da `_myeudr_build/verifica/controlli_automatici.py` · nessun accesso di rete._

**Perimetro:** 734 record nel workbook (8 fogli) + 458 record nei 30 file JSON di build.


## Copertura campi per foglio

| Foglio | Record | Email | Referente | Ruolo | LinkedIn | Sito | Sede | Fonte | Dimensione |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Italia | 95 | 68 | 11 | 11 | 10 | 85 | 95 | 95 | 91 |
| Germania | 97 | 88 | 96 | 96 | 17 | 93 | 97 | 97 | 96 |
| Finlandia | 84 | 69 | 77 | 77 | 17 | 84 | 84 | 84 | 83 |
| Danimarca | 88 | 80 | 77 | 78 | 57 | 85 | 88 | 88 | 88 |
| Svezia | 89 | 80 | 75 | 75 | 58 | 88 | 89 | 89 | 89 |
| Olanda | 99 | 76 | 61 | 61 | 66 | 95 | 99 | 99 | 99 |
| Belgio | 92 | 71 | 53 | 53 | 44 | 89 | 92 | 92 | 92 |
| Austria | 90 | 87 | 89 | 89 | 25 | 89 | 90 | 90 | 90 |

## Riepilogo rilievi

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
| 9c | 9c · Nessuna forma giuridica nel nome | 16 |
| 9d | 9d · Maiuscolo/minuscolo incoerente dentro il foglio | 51 |
| 9e | 9e · Forma giuridica scritta in stile incoerente (foglio Italia) | 0 |
| 10 | 10 · TLD del sito estraneo al paese del foglio | 7 |
| 11 | 11 · Divergenze fra JSON di build e foglio Excel | 0 |
| 11b | 11b · Record presente nei JSON ma assente dal foglio | 0 |

**Totale rilievi automatici: 203**


## Macro-filiere osservate

| Macro | Occorrenze | In tassonomia |
|---|--:|:--:|
| Legno/Arredo | 201 | ✅ |
| Carta/Packaging | 127 | ✅ |
| Caffè | 95 | ✅ |
| Cacao/Cioccolato | 80 | ✅ |
| Mangimi/Soia | 61 | ✅ |
| Gomma | 48 | ✅ |
| Legno/Segheria | 39 | ✅ |
| Bovini/Carne | 35 | ✅ |
| Pelle/Concia | 32 | ✅ |
| Olio di palma | 16 | ✅ |

---

## 1 · Duplicati fra fogli del workbook  (0)

_Nessun rilievo._

---

## 1b · Duplicati fra i JSON di build  (0)

_Nessun rilievo._

---

## 1c · Denominazioni diverse con lo stesso sito web  (1)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Belgio | hamlet.be | stesso sito per: Belgio: A & A Chocolaterie NV \| Belgio: Pralinart NV |  |

---

## 2 · Email con dominio diverso dal sito (sospette di deduzione)  (24)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Conceria Ferrari S.r.l. | [STEM DIVERSO — DA CONFERMARE] email @ferrarilasi.it vs sito conceriaferrari.com  (email: ferrari@ferrarilasi.it \| sito: https://www.conceriaferrari.com) | xlsx:Italia!r11 |
| Italia | Cartotecnica Montebello S.p.A. | [STEM DIVERSO — DA CONFERMARE] email @cartomontebello.com vs sito cartotecnicamontebello.it  (email: info@cartomontebello.com \| sito: https://www.cartotecnicamontebello.it) | xlsx:Italia!r47 |
| Germania | PFT Holz in Form GmbH | [STEM DIVERSO — DA CONFERMARE] email @pft-holzinform.de vs sito formsperrholz.de  (email: info@pft-holzinform.de \| sito: https://formsperrholz.de) | xlsx:Germania!r16 |
| Germania | Winter & Freis GmbH & Co. KG | [STEM DIVERSO — DA CONFERMARE] email @winter-und-freis.de vs sito holzkiste-palette.de  (email: info@winter-und-freis.de \| sito: https://holzkiste-palette.de) | xlsx:Germania!r23 |
| Germania | EGGER Druck + Medien GmbH | [STEM DIVERSO — DA CONFERMARE] email @madika.de vs sito eggerdruck.de  (email: service@madika.de \| sito: https://www.eggerdruck.de) | xlsx:Germania!r27 |
| Germania | Willy Hagen GmbH (Hagen Kaffee) | [STEM DIVERSO — DA CONFERMARE] email @hagenkaffee.de vs sito hagen-onlineshop.de  (email: info@hagenkaffee.de \| sito: https://www.hagen-onlineshop.de) | xlsx:Germania!r57 |
| Germania | Knorr & Macho GmbH | [STEM DIVERSO — DA CONFERMARE] email @knorr-macho.de vs sito gummi-formteile.eu  (email: info@knorr-macho.de \| sito: https://gummi-formteile.eu) | xlsx:Germania!r78 |
| Germania | Wilhelm Ströh jun. GmbH & Co. KG | [STEM DIVERSO — DA CONFERMARE] email @stroeh-hobbersdorf.de vs sito hobbersdorfer-muehle.com  (email: info@stroeh-hobbersdorf.de \| sito: https://www.hobbersdorfer-muehle.com) | xlsx:Germania!r94 |
| Finlandia | Pantsarin Saha Oy | [STEM DIVERSO — DA CONFERMARE] email @kivilompolo.fi vs sito pantsarinsaha.fi  (email: rauno@kivilompolo.fi \| sito: https://pantsarinsaha.fi) | xlsx:Finlandia!r34 |
| Finlandia | Metsäpaahtimo (Sampokone Oy) | [STEM DIVERSO — DA CONFERMARE] email @sampokone.fi vs sito metsapaahtimo.fi  (email: info@sampokone.fi \| sito: https://metsapaahtimo.fi) | xlsx:Finlandia!r71 |
| Danimarca | VERMUND LARSEN A/S (VELA / VERMUND) | [STEM DIVERSO — DA CONFERMARE] email @vela.dk vs sito vermund.eu  (email: mail@vela.dk \| sito: https://vermund.eu/) | xlsx:Danimarca!r35 |
| Danimarca | Copenhagen Coffee Lab ApS | [STEM DIVERSO — DA CONFERMARE] email @cphcoffeelab.com vs sito copenhagencoffeelab.com  (email: webshop@cphcoffeelab.com \| sito: https://copenhagencoffeelab.com/en) | xlsx:Danimarca!r53 |
| Danimarca | Estate Coffee Copenhagen A/S | [STEM DIVERSO — DA CONFERMARE] email @estatecph.com vs sito estatecoffee.dk  (email: kontakt@estatecph.com \| sito: https://estatecoffee.dk/) | xlsx:Danimarca!r55 |
| Danimarca | H.C. JACOBSEN A/S | [STEM DIVERSO — DA CONFERMARE] email @hc-jacobsen.dk vs sito hcemballage.dk  (email: info@hc-jacobsen.dk \| sito: https://hcemballage.dk/) | xlsx:Danimarca!r71 |
| Olanda | Houtimport Reuver B.V. | [STEM DIVERSO — DA CONFERMARE] email @hireuver.nl vs sito houtimportreuver.nl  (email: verkoop@hireuver.nl \| sito: https://www.houtimportreuver.nl) | xlsx:Olanda!r17 |
| Olanda | Origin Bridge (Barchem) | [STEM DIVERSO — DA CONFERMARE] email @bridgetoorigin.com vs sito originbridge.coffee  (email: info@bridgetoorigin.com \| sito: https://originbridge.coffee/) | xlsx:Olanda!r66 |
| Olanda | Van Benthem Diervoeders Vollenhove B.V. | [STEM DIVERSO — DA CONFERMARE] email @vanbenthemvollenhove.nl vs sito vbvoer.nl  (email: info@vanbenthemvollenhove.nl \| sito: https://www.vbvoer.nl/) | xlsx:Olanda!r92 |
| Belgio | Sas NV (Sas Coffee) | [STEM DIVERSO — DA CONFERMARE] email @sas-koffie.be vs sito sas-coffee.com  (email: info@sas-koffie.be \| sito: https://sas-coffee.com/) | xlsx:Belgio!r55 |
| Belgio | Gudrun Commercial NV | [STEM DIVERSO — DA CONFERMARE] email @chocolates.be vs sito gudrungroup.be  (email: info@chocolates.be \| sito: https://gudrungroup.be/) | xlsx:Belgio!r67 |
| Belgio | Oxfam Fair Trade CV | [STEM DIVERSO — DA CONFERMARE] email @oft.be vs sito oxfamfairtrade.be  (email: info@oft.be \| sito: https://www.oxfamfairtrade.be/) | xlsx:Belgio!r71 |
| Austria | Gruber Karton Kreativ GmbH | [STEM DIVERSO — DA CONFERMARE] email @gruber-karton-kreativ.at vs sito gruber-kartonagen.at  (email: office@gruber-karton-kreativ.at \| sito: https://gruber-kartonagen.at) | xlsx:Austria!r49 |
| Austria | Fürst GmbH | [STEM DIVERSO — DA CONFERMARE] email @fuerst.cc vs sito original-mozartkugel.com  (email: versand@fuerst.cc \| sito: https://www.original-mozartkugel.com) | xlsx:Austria!r69 |
| Austria | Heidi Chocolat AG | [STEM DIVERSO — DA CONFERMARE] email @schwedenbomben.at vs sito niemetz.at  (email: office@schwedenbomben.at \| sito: https://niemetz.at) | xlsx:Austria!r70 |
| Austria | Schwaninger Vieh Export GmbH | [STEM DIVERSO — DA CONFERMARE] email @schwaninger.co.at vs sito viehexport.com  (email: office@schwaninger.co.at \| sito: https://www.viehexport.com/) | xlsx:Austria!r91 |

---

## 2b · Email presente ma sito assente (non verificabile per dominio)  (1)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Germania | Demharter Mischfutterwerk GmbH & Co. KG | email Demharter-Mischfutter@t-online.de ma campo sito vuoto | xlsx:Germania!r87 |

---

## 2c · Email su dominio freemail/PEC (accettabile ma non aziendale)  (10)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Cuoificio Bisonte S.p.A. | [FREEMAIL/PEC] email @tiscali.it vs sito cuoificiobisonte.it  (email: bisonte.cuoificio@tiscali.it \| sito: https://www.cuoificiobisonte.it) | xlsx:Italia!r19 |
| Italia | Bartoli S.p.A. | [FREEMAIL/PEC] email @pec.it vs sito bartolispa.it  (email: bartolispa@pec.it \| sito: https://www.bartolispa.it) | xlsx:Italia!r39 |
| Italia | Antica Dolceria Bonajuto S.r.l. | [FREEMAIL/PEC] email @pec.it vs sito bonajuto.it  (email: bonajuto@pec.it \| sito: https://www.bonajuto.it) | xlsx:Italia!r74 |
| Italia | Mangimi Cavallo S.r.l. | [FREEMAIL/PEC] email @virgilio.it vs sito mangimicavallo.it  (email: mangimi.cavallo@virgilio.it \| sito: https://mangimicavallo.it) | xlsx:Italia!r89 |
| Danimarca | EMBALLAGEFABRIKKEN THY PAP | [FREEMAIL/PEC] email @mail.dk vs sito thy-pap.dk  (email: thy-pap@mail.dk \| sito: https://thy-pap.dk/) | xlsx:Danimarca!r41 |
| Danimarca | MEJLING LANDHANDEL / SÆBY FRØSALG | [FREEMAIL/PEC] email @mail.dk vs sito mejlinglandhandel.dk  (email: mejlingudlejning@mail.dk \| sito: https://mejlinglandhandel.dk/) | xlsx:Danimarca!r80 |
| Olanda | Houtimport Lekkerkerker B.V. | [FREEMAIL/PEC] email @planet.nl vs sito houtimportlekkerkerker.nl  (email: houtimportlekkerkerker@planet.nl \| sito: https://www.houtimportlekkerkerker.nl) | xlsx:Olanda!r16 |
| Belgio | Decadt Houthandel NV | [FREEMAIL/PEC] email @telenet.be vs sito decadt-hout.be  (email: decadt.hout@telenet.be \| sito: https://decadt-hout.be/) | xlsx:Belgio!r12 |
| Belgio | Emballages Gruselle SRL | [FREEMAIL/PEC] email @skynet.be vs sito emballagesgruselle.eu  (email: gruselle@skynet.be \| sito: https://www.emballagesgruselle.eu) | xlsx:Belgio!r42 |
| Austria | WIESTRADING Gesellschaft m.b.H. | [FREEMAIL/PEC] email @aon.at vs sito wiestrading.at  (email: wiesingerviehhandel@aon.at \| sito: https://www.wiestrading.at/) | xlsx:Austria!r92 |

---

## 2d · Email su dominio affine al sito (TLD/variante) — rischio basso  (52)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | 3 C - Lavorazione Pelli S.r.l. | [STESSO NOME, TLD DIVERSO] email @conceria3c.it vs sito conceria3c.com  (email: info@conceria3c.it \| sito: https://www.conceria3c.com) | xlsx:Italia!r3 |
| Italia | Compensati Toro S.p.A. | [STESSO NOME, TLD DIVERSO] email @compensatitoro.com vs sito compensatitoro.it  (email: info@compensatitoro.com \| sito: https://compensatitoro.it) | xlsx:Italia!r29 |
| Italia | Itlas S.r.l. Società Benefit | [STESSO NOME, TLD DIVERSO] email @itlas.it vs sito itlas.com  (email: info@itlas.it \| sito: https://www.itlas.com) | xlsx:Italia!r32 |
| Italia | Grafica Nappa S.r.l. | [STESSO NOME, TLD DIVERSO] email @graficanappa.com vs sito graficanappa.it  (email: commerciale@graficanappa.com \| sito: https://www.graficanappa.it) | xlsx:Italia!r49 |
| Italia | Scatolificio Cartotecnica Schiassi S.r.l. | [STEM AFFINE] email @schiassi.it vs sito scatolificioschiassi.it  (email: info@schiassi.it \| sito: https://www.scatolificioschiassi.it) | xlsx:Italia!r52 |
| Germania | Weinheimer Leder GmbH | [STESSO NOME, TLD DIVERSO] email @weinheimer-leder.de vs sito weinheimer-leder.com  (email: info@weinheimer-leder.de \| sito: https://www.weinheimer-leder.com) | xlsx:Germania!r5 |
| Germania | List + Beisler GmbH | [STESSO NOME, TLD DIVERSO] email @list-beisler.de vs sito list-beisler.coffee  (email: info@list-beisler.de \| sito: https://www.list-beisler.coffee) | xlsx:Germania!r49 |
| Germania | Effbe GmbH | [STESSO NOME, TLD DIVERSO] email @effbe-diaphragm.com vs sito effbe-diaphragm.de  (email: contact@effbe-diaphragm.com \| sito: https://effbe-diaphragm.de) | xlsx:Germania!r75 |
| Finlandia | Hollolan Viilu ja Laminaatti Oy (HVL) | [STESSO NOME, TLD DIVERSO] email @hvloy.fi vs sito hvloy.com  (email: jukka.vuoriheimo@hvloy.fi \| sito: https://hvloy.com) | xlsx:Finlandia!r13 |
| Finlandia | Siparila Oy | [STESSO NOME, TLD DIVERSO] email @siparila.fi vs sito siparila.com  (email: orders@siparila.fi \| sito: https://www.siparila.com) | xlsx:Finlandia!r41 |
| Finlandia | Goodio (Helsinki Heaven Oy) | [STEM AFFINE] email @goodio.fi vs sito goodiochocolate.com  (email: info@goodio.fi \| sito: https://goodiochocolate.com) | xlsx:Finlandia!r75 |
| Danimarca | HØRNING PARKET A/S | [STESSO NOME, TLD DIVERSO] email @horningfloor.dk vs sito horningfloor.com  (email: sales@horningfloor.dk \| sito: https://www.horningfloor.com/) | xlsx:Danimarca!r16 |
| Danimarca | INNOVATION LIVING A/S (già Innovation Randers A/S) | [STESSO NOME, TLD DIVERSO] email @innovationliving.dk vs sito innovationliving.com  (email: info@innovationliving.dk \| sito: https://www.innovationliving.com/) | xlsx:Danimarca!r18 |
| Danimarca | JKE DESIGN A/S | [STESSO NOME, TLD DIVERSO] email @jke-design.dk vs sito jke-design.com  (email: info@jke-design.dk \| sito: https://jke-design.com/da) | xlsx:Danimarca!r19 |
| Danimarca | SIKA DESIGN A/S | [STESSO NOME, TLD DIVERSO] email @sika-design.com vs sito sika-design.dk  (email: info@sika-design.com \| sito: https://sika-design.dk/) | xlsx:Danimarca!r28 |
| Danimarca | SOFTLINE A/S | [STEM AFFINE] email @softline.dk vs sito softlinefurniture.com  (email: info@softline.dk \| sito: https://softlinefurniture.com/) | xlsx:Danimarca!r30 |
| Danimarca | KLS PUREPRINT A/S | [STEM AFFINE] email @kls.dk vs sito klspureprint.dk  (email: kls@kls.dk \| sito: https://klspureprint.dk/) | xlsx:Danimarca!r46 |
| Danimarca | SCANLUX PACKAGING A/S | [STEM AFFINE] email @scanlux.com vs sito scanlux-packaging.com  (email: scanlux@scanlux.com \| sito: https://scanlux-packaging.com/) | xlsx:Danimarca!r48 |
| Danimarca | DANSK GUMMI INDUSTRI A/S | [STESSO NOME, TLD DIVERSO] email @danskgummi.dk vs sito danskgummi.com  (email: sales@danskgummi.dk \| sito: https://danskgummi.com/) | xlsx:Danimarca!r70 |
| Svezia | Tärnsjö Garveri Aktiebolag | [STESSO NOME, TLD DIVERSO] email @tarnsjogarveri.se vs sito tarnsjogarveri.com  (email: info@tarnsjogarveri.se \| sito: https://tarnsjogarveri.com/) | xlsx:Svezia!r3 |
| Svezia | Fogia Collection Aktiebolag | [STESSO NOME, TLD DIVERSO] email @fogia.se vs sito fogia.com  (email: info@fogia.se \| sito: https://www.fogia.com/) | xlsx:Svezia!r16 |
| Svezia | Johanson Design Aktiebolag | [STESSO NOME, TLD DIVERSO] email @johansondesign.se vs sito johansondesign.com  (email: info@johansondesign.se \| sito: https://johansondesign.com/) | xlsx:Svezia!r22 |
| Svezia | Nydala Trävaru Aktiebolag | [STEM AFFINE] email @nydalatra.se vs sito nydalatravaru.se  (email: mail@nydalatra.se \| sito: https://nydalatravaru.se/) | xlsx:Svezia!r34 |
| Svezia | Woodsafe Timber Protection AB | [STESSO NOME, TLD DIVERSO] email @woodsafe.com vs sito woodsafe.se  (email: kundtjanst@woodsafe.com \| sito: https://www.woodsafe.se) | xlsx:Svezia!r47 |
| Svezia | ZilenZio AB | [STESSO NOME, TLD DIVERSO] email @zilenzio.se vs sito zilenzio.com  (email: info@zilenzio.se \| sito: https://zilenzio.com/) | xlsx:Svezia!r48 |
| Svezia | Candy People AB | [STESSO NOME, TLD DIVERSO] email @candypeople.com vs sito candypeople.se  (email: info@candypeople.com \| sito: https://candypeople.se/) | xlsx:Svezia!r78 |
| Svezia | Forsbecks Eftr. Aktiebolag | [STESSO NOME, TLD DIVERSO] email @forsbecks.com vs sito forsbecks.se  (email: per-magnus.johansson@forsbecks.com \| sito: https://www.forsbecks.se/) | xlsx:Svezia!r86 |
| Olanda | De Leeuw Huidenhandel N.V. | [STESSO NOME, TLD DIVERSO] email @deleeuwhides.nl vs sito deleeuwhides.com  (email: sales@deleeuwhides.nl \| sito: https://www.deleeuwhides.com) | xlsx:Olanda!r3 |
| Olanda | Beijleveld Houtimport B.V. | [STEM AFFINE] email @beyleveld.com vs sito beyleveldhoutimport.com  (email: info@beyleveld.com \| sito: https://www.beyleveldhoutimport.com) | xlsx:Olanda!r8 |
| Olanda | Van Ierssel Houtimport B.V. | [STEM AFFINE] email @vanierssel.nl vs sito vaniersselhoutimport.nl  (email: info@vanierssel.nl \| sito: https://www.vaniersselhoutimport.nl) | xlsx:Olanda!r23 |
| Olanda | Van den Berg Hardhout B.V. | [STESSO NOME, TLD DIVERSO] email @vandenberghardhout.nl vs sito vandenberghardhout.com  (email: info@vandenberghardhout.nl \| sito: https://www.vandenberghardhout.com) | xlsx:Olanda!r25 |
| Olanda | Kargro Banden B.V. | [STEM AFFINE] email @kargro.nl vs sito kargrobanden.nl  (email: info@kargro.nl \| sito: https://kargrobanden.nl) | xlsx:Olanda!r32 |
| Olanda | Papierfabriek Schut B.V. | [STESSO NOME, TLD DIVERSO] email @schutpapier.com vs sito schutpapier.nl  (email: info@schutpapier.com \| sito: https://schutpapier.nl) | xlsx:Olanda!r47 |
| Olanda | Veldhuis Media B.V. | [STEM AFFINE] email @veldhuis.nl vs sito veldhuismedia.nl  (email: info@veldhuis.nl \| sito: https://www.veldhuismedia.nl) | xlsx:Olanda!r50 |
| Olanda | Hesselink Koffiesystemen B.V. | [STESSO NOME, TLD DIVERSO] email @hesselinkkoffie.eu vs sito hesselinkkoffie.nl  (email: info@hesselinkkoffie.eu \| sito: https://hesselinkkoffie.nl/) | xlsx:Olanda!r61 |
| Olanda | Chocolatemakers B.V. | [STESSO NOME, TLD DIVERSO] email @chocolatemakers.nl vs sito chocolatemakers.com  (email: info@chocolatemakers.nl \| sito: https://www.chocolatemakers.com/) | xlsx:Olanda!r73 |
| Olanda | DO IT Organic Food Ingredients B.V. | [STEM AFFINE] email @organic.nl vs sito doitorganic.nl  (email: sales@organic.nl \| sito: https://www.doitorganic.nl/) | xlsx:Olanda!r94 |
| Olanda | Spack B.V. | [STEM AFFINE] email @spackbv.com vs sito spack.nl  (email: info@spackbv.com \| sito: https://www.spack.nl/) | xlsx:Olanda!r96 |
| Belgio | Bulo NV | [STESSO NOME, TLD DIVERSO] email @bulo.be vs sito bulo.com  (email: info@bulo.be \| sito: https://bulo.com) | xlsx:Belgio!r7 |
| Belgio | Lavrijsen Houtbedrijf NV | [STEM AFFINE] email @lavrijsen-geel.be vs sito lavrijsen.be  (email: info@lavrijsen-geel.be \| sito: https://lavrijsen.be/) | xlsx:Belgio!r21 |
| Belgio | Allbox NV | [STEM AFFINE] email @allbox.be vs sito allboxnetwork.be  (email: info@allbox.be \| sito: https://allboxnetwork.be) | xlsx:Belgio!r36 |
| Belgio | Etilux SA | [STESSO NOME, TLD DIVERSO] email @etilux.be vs sito etilux.com  (email: info@etilux.be \| sito: https://www.etilux.com) | xlsx:Belgio!r43 |
| Belgio | Belvas SA | [STEM AFFINE] email @belvas.be vs sito chocolaterie-belvas.be  (email: info@belvas.be \| sito: https://www.chocolaterie-belvas.be/) | xlsx:Belgio!r60 |
| Belgio | Chocolaterie Ickx NV | [STEM AFFINE] email @choc-ickx.be vs sito ickx.be  (email: avangastel@choc-ickx.be \| sito: https://www.ickx.be/) | xlsx:Belgio!r62 |
| Belgio | Hercorub NV | [STESSO NOME, TLD DIVERSO] email @hercorub.com vs sito hercorub.be  (email: info@hercorub.com \| sito: https://www.hercorub.be/) | xlsx:Belgio!r76 |
| Belgio | Royale Lacroix SA | [STESSO NOME, TLD DIVERSO] email @royalelacroix.be vs sito royalelacroix.com  (email: info@royalelacroix.be \| sito: https://www.royalelacroix.com/) | xlsx:Belgio!r85 |
| Belgio | Ameloot BV | [STEM AFFINE] email @ameloot.org vs sito omerameloot.com  (email: petra@ameloot.org \| sito: https://omerameloot.com/nl) | xlsx:Belgio!r86 |
| Austria | Waldviertler Werkstätten GmbH | [STEM AFFINE] email @gea.at vs sito gea-waldviertler.at  (email: gea@gea.at \| sito: https://gea-waldviertler.at/) | xlsx:Austria!r5 |
| Austria | Alvorada Kaffeerösterei GmbH | [STESSO NOME, TLD DIVERSO] email @alvorada.com vs sito alvorada.wien  (email: sales@alvorada.com \| sito: http://alvorada.wien) | xlsx:Austria!r40 |
| Austria | EZA Fairer Handel GmbH | [STESSO NOME, TLD DIVERSO] email @eza.at vs sito eza.cc  (email: office@eza.at \| sito: https://www.eza.cc) | xlsx:Austria!r63 |
| Austria | J. Hornig GmbH | [STESSO NOME, TLD DIVERSO] email @jhornig.at vs sito jhornig.com  (email: online@jhornig.at \| sito: https://www.jhornig.com) | xlsx:Austria!r64 |
| Austria | Königshofer GmbH | [STEM AFFINE] email @koenigshofer.at vs sito koenigshofer-futtermittel.at  (email: ebergassing@koenigshofer.at \| sito: https://www.koenigshofer-futtermittel.at) | xlsx:Austria!r79 |

---

## 3 · Stessa email su aziende diverse  (0)

_Nessun rilievo._

---

## 3b · Stesso LinkedIn su aziende diverse  (1)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Belgio | https://be.linkedin.com/company/a&a-chocolaterie-pralin'art | condiviso da: Belgio: A & A Chocolaterie NV \| Belgio: Pralinart NV |  |

---

## 4 · URL malformati (LinkedIn / sito)  (0)

_Nessun rilievo._

---

## 4b · Email sintatticamente non conformi  (0)

_Nessun rilievo._

---

## 5 · Entità HTML residue  (0)

_Nessun rilievo._

---

## 6 · Tassonomia Filiera fuori elenco  (0)

_Nessun rilievo._

---

## 6b · Separatore filiera non em-dash  (0)

_Nessun rilievo._

---

## 7 · Fonte vuota o non URL  (0)

_Nessun rilievo._

---

## 7b · Dimensione vuota o n.d.  (6)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Conceria Beschin | Dimensione = 'n.d.' | xlsx:Italia!r7 |
| Italia | Conceria Daniela | Dimensione = 'n.d.' | xlsx:Italia!r9 |
| Italia | Conceria Emmedue S.r.l. | Dimensione = 'n.d.' | xlsx:Italia!r10 |
| Italia | Segheria Saccavini S.r.l. | Dimensione = 'n.d.' | xlsx:Italia!r37 |
| Germania | Münchner Kaffeerösterei GmbH | Dimensione = 'n.d.' | xlsx:Germania!r52 |
| Finlandia | Helsingin Kumi Oy | Dimensione = 'n.d.' | xlsx:Finlandia!r77 |

---

## 7c · Sito web mancante  (26)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Arko S.r.l. | Sito = '' | xlsx:Italia!r22 |
| Italia | C.I.M.A. S.r.l. (Compensati Impiallacciature Materiali Affin | Sito = '' | xlsx:Italia!r26 |
| Italia | Holzland Fuchs S.r.l. | Sito = '' | xlsx:Italia!r31 |
| Italia | Zalf S.p.A. (Zalf Industria Mobili Componibili) | Sito = '' | xlsx:Italia!r38 |
| Italia | Gambarotta S.r.l. | Sito = '' | xlsx:Italia!r76 |
| Italia | Diesse Rubber Hoses S.p.A. | Sito = '' | xlsx:Italia!r81 |
| Italia | Ellegi S.p.A. | Sito = '' | xlsx:Italia!r82 |
| Italia | F.lli Paris S.r.l. | Sito = '' | xlsx:Italia!r83 |
| Italia | Insit Industria S.p.A. | Sito = '' | xlsx:Italia!r84 |
| Italia | Mangimificio S.Antonio S.r.l. | Sito = '' | xlsx:Italia!r90 |
| Germania | HCS Hamburg Cocoa Services GmbH | Sito = '' | xlsx:Germania!r68 |
| Germania | Küper GmbH & Co. KG | Sito = '' | xlsx:Germania!r79 |
| Germania | Bärmühle Langenhessen GmbH Mischfutterwerk | Sito = '' | xlsx:Germania!r86 |
| Germania | Demharter Mischfutterwerk GmbH & Co. KG | Sito = '' | xlsx:Germania!r87 |
| Danimarca | DANSK KAFFE ApS | Sito = '' | xlsx:Danimarca!r54 |
| Danimarca | TJØRNEHØJ MØLLE A/S | Sito = 'n.d.' | xlsx:Danimarca!r83 |
| Danimarca | VESTJYSK SPECIALFODER ApS | Sito = 'n.d.' | xlsx:Danimarca!r84 |
| Svezia | Aktiebolaget Cool & Candy | Sito = 'n.d.' | xlsx:Svezia!r77 |
| Olanda | Snel Industrie voor Karton en Papierveredeling B.V. | Sito = '' | xlsx:Olanda!r48 |
| Olanda | Chocolade- en Suikerwerkfabriek Marandi B.V. | Sito = 'n.d.' | xlsx:Olanda!r71 |
| Olanda | Continental Chocolate B.V. | Sito = 'n.d.' | xlsx:Olanda!r74 |
| Olanda | Rousseau Chocolade B.V. | Sito = 'n.d.' | xlsx:Olanda!r80 |
| Belgio | Label-Pak-Int'l Co SA | Sito = 'n.d.' | xlsx:Belgio!r46 |
| Belgio | Silco NV | Sito = '' | xlsx:Belgio!r56 |
| Belgio | Slachthuis Velzeke BV | Sito = 'n.d.' | xlsx:Belgio!r91 |
| Austria | Tschurtschenthaler Gerberei GmbH | Sito = 'n.d.' | xlsx:Austria!r4 |

---

## 8 · Dimensione fuori forbice 5–40 M€ senza segnalazione esplicita  (8)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Svezia | Nordiska Kaffebolaget H. Hansson & Co Aktiebolag | valori stimati M€: 4.84 («54,7 MSEK») \| campo: Fatturato 54,7 MSEK (~4,8 M€) 2024 (+8,4%); 17 dipendenti (14 nel 2023) (fonte: allabolag.se, bilancio 2024). Org.nr 556083-2379. SNI 46370 kaffe/te a | xlsx:Svezia!r75 |
| Svezia | Malmö Chokladfabrik AB | valori stimati M€: 3.77 («42,6 MSEK») \| campo: Fatturato 42,6 MSEK (~3,8 M€) esercizio 2025 (+31,6%); 16 dipendenti (fonte: allabolag.se / bolagsfakta.se). Org.nr 556664-6286. Sotto la fascia tolle | xlsx:Svezia!r81 |
| Svezia | Forsbecks Eftr. Aktiebolag | valori stimati M€: 52.21 («589.951 KSEK») \| campo: ATTENZIONE TAGLIA: fatturato 589.951 KSEK (~52,2 M€) con soli 31-35 dipendenti — bilancio 2022 (fonte allabolag/bolagsfakta); org.nr 556002-3417. Sopr | xlsx:Svezia!r86 |
| Belgio | Baeten & Co NV | valori stimati M€: 42.81 («42.810.588 EUR») \| campo: Fatturato 42.810.588 EUR (bilancio NBB depositato 15-07-2025) — taglia gonfiata dal costo materia prima: solo 13,7 FTE; n. impresa BE 0447.081.908 | xlsx:Belgio!r84 |
| Belgio | Royale Lacroix SA | valori stimati M€: 49.35 («49.349.520 EUR») \| campo: Fatturato 49.349.520 EUR (bilancio NBB, ultimo esercizio pubblicato) — taglia gonfiata dal costo materia prima: solo 18,6 FTE; n. impresa BE 0404.423. | xlsx:Belgio!r85 |
| Belgio | Ameloot BV | valori stimati M€: 49.30 («49.298.205 EUR») \| campo: Fatturato 49.298.205 EUR (Trends Top/NBB, ultimo esercizio); n. impresa BE 0413.029.562. AZIENDA DI CONFINE: sopra i 40 M€ ma PMI familiare indipenden | xlsx:Belgio!r86 |
| Belgio | Dierickx NV | valori stimati M€: 40.84 («40.843.828 EUR») \| campo: Fatturato 40.843.828 EUR (ultimo bilancio depositato NBB, via Trends Top/Companyweb); azienda familiare indipendente alla 5a generazione; n. impresa B | xlsx:Belgio!r87 |
| Belgio | Jos Leemput BV | valori stimati M€: 44.95 («44.954.796 EUR») \| campo: Fatturato 44.954.796 EUR e 16,2 FTE (ultimo bilancio depositato NBB, via Companyweb/FinCheck); n. impresa BE 0424.110.724. AZIENDA DI CONFINE: sopra 4 | xlsx:Belgio!r89 |

---

## 9 · Denominazione: registri, spazi, numeri  (0)

_Nessun rilievo._

---

## 9b · Forma giuridica incoerente col paese del foglio  (0)

_Nessun rilievo._

---

## 9c · Nessuna forma giuridica nel nome  (16)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Conceria Beschin | nessuna forma giuridica riconoscibile | xlsx:Italia!r7 |
| Italia | Conceria Daniela | nessuna forma giuridica riconoscibile | xlsx:Italia!r9 |
| Germania | Josef Meyer Palettenbau Inh. Julian Meyer (Paletten Meyer) | nessuna forma giuridica riconoscibile | xlsx:Germania!r17 |
| Germania | impuls Kaffeemanufaktur | nessuna forma giuridica riconoscibile | xlsx:Germania!r58 |
| Germania | Confiserie Dengel (Inh. Uwe Dengel) | nessuna forma giuridica riconoscibile | xlsx:Germania!r63 |
| Germania | Schell Schokoladenmanufaktur (Inh. Eberhard Schell) | nessuna forma giuridica riconoscibile | xlsx:Germania!r72 |
| Danimarca | EMBALLAGEFABRIKKEN THY PAP | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r41 |
| Danimarca | MEJLING LANDHANDEL / SÆBY FRØSALG | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r80 |
| Danimarca | Naturli' Foods | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r85 |
| Danimarca | Grambogård | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r88 |
| Danimarca | JN Meat International | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r89 |
| Olanda | Origin Bridge (Barchem) | nessuna forma giuridica riconoscibile | xlsx:Olanda!r66 |
| Austria | steininger.designers gmbh | nessuna forma giuridica riconoscibile | xlsx:Austria!r38 |
| Austria | weinberger-holz gmbh | nessuna forma giuridica riconoscibile | xlsx:Austria!r39 |
| Austria | BAG Ölmühle BetriebsgmbH | nessuna forma giuridica riconoscibile | xlsx:Austria!r41 |
| Austria | Margarethner Verpackungsgesellschaft m.b.H. | nessuna forma giuridica riconoscibile | xlsx:Austria!r51 |

---

## 9d · Maiuscolo/minuscolo incoerente dentro il foglio  (51)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Germania | FMS AG | maiuscolo integrale da registro: 1/97 record del foglio Germania sono in MAIUSCOLO, gli altri 96 in forma normale | xlsx:Germania!r29 |
| Danimarca | NIELAUS A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r3 |
| Danimarca | AUBO PRODUCTION A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r6 |
| Danimarca | BØJSØ DØRE & VINDUER A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r7 |
| Danimarca | DANSK HÅRDTTRÆ SAVVÆRK A/S (DHS) | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r8 |
| Danimarca | DINESEN FLOORS A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r9 |
| Danimarca | FREDERICIA FURNITURE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r10 |
| Danimarca | GLOBAL TIMBER A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r12 |
| Danimarca | GRAMRODE MØBELFABRIK A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r13 |
| Danimarca | HAMMEL FURNITURE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r14 |
| Danimarca | HVIDBJERG VINDUET A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r15 |
| Danimarca | HØRNING PARKET A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r16 |
| Danimarca | JKE DESIGN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r19 |
| Danimarca | KEFLICO A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r20 |
| Danimarca | KRYDSFINER-HANDELEN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r21 |
| Danimarca | KVIST INDUSTRIES A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r22 |
| Danimarca | LILLEHEDEN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r24 |
| Danimarca | MULTIFORM A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r25 |
| Danimarca | N. EILERSEN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r26 |
| Danimarca | SIKA DESIGN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r28 |
| Danimarca | SKOVBY MØBELFABRIK A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r29 |
| Danimarca | SOFTLINE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r30 |
| Danimarca | SOMMER-SAVEX A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r31 |
| Danimarca | SUPERWOOD A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r32 |
| Danimarca | TIMBERMAN DENMARK A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r34 |
| Danimarca | VERMUND LARSEN A/S (VELA / VERMUND) | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r35 |
| Danimarca | SKOVS KORN A/S. KORN- OG FODERSTOFAGENTUR | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r36 |
| Danimarca | ALL CREATIVE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r37 |
| Danimarca | BOXEN EMBALLAGE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r38 |
| Danimarca | BUCHS A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r39 |
| Danimarca | COLOR LABEL A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r40 |
| Danimarca | EMBALLAGEFABRIKKEN THY PAP | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r41 |
| Danimarca | IKAST ETIKET A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r43 |
| Danimarca | KAILOW A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r45 |
| Danimarca | KLS PUREPRINT A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r46 |
| Danimarca | MC EMBALLAGE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r47 |
| Danimarca | SCANLUX PACKAGING A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r48 |
| Danimarca | STOK EMBALLAGE K/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r51 |
| Danimarca | PETER BEIER CHOKOLADE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r64 |
| Danimarca | PR CHOKOLADE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r65 |
| Danimarca | AVK GUMMI A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r69 |
| Danimarca | DANSK GUMMI INDUSTRI A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r70 |
| Danimarca | H.C. JACOBSEN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r71 |
| Danimarca | RG ROM GUMMI A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r72 |
| Danimarca | SKANDINAVISK DÆK IMPORT A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r74 |
| Danimarca | CEBECO FOURAGE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r77 |
| Danimarca | CR FODERSERVICE K/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r79 |
| Danimarca | MEJLING LANDHANDEL / SÆBY FRØSALG | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r80 |
| Danimarca | NORDVEST FODER A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r81 |
| Danimarca | NUTRIMIN A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r82 |
| Danimarca | TJØRNEHØJ MØLLE A/S | maiuscolo integrale da registro: 50/88 record del foglio Danimarca sono in MAIUSCOLO, gli altri 38 in forma normale | xlsx:Danimarca!r83 |

---

## 9e · Forma giuridica scritta in stile incoerente (foglio Italia)  (0)

_Nessun rilievo._

---

## 10 · TLD del sito estraneo al paese del foglio  (7)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Germania | Sawade GmbH | sito https://sawade.berlin — TLD .berlin estraneo a Germania | xlsx:Germania!r71 |
| Finlandia | Ålands Skogsindustrier Ab | sito https://www.skogsindustrier.ax — TLD .ax estraneo a Finlandia | xlsx:Finlandia!r48 |
| Danimarca | DANSK HÅRDTTRÆ SAVVÆRK A/S (DHS) | sito https://dhs.as/ — TLD .as estraneo a Danimarca | xlsx:Danimarca!r8 |
| Belgio | Buzzispace NV | sito https://www.buzzi.space — TLD .space estraneo a Belgio | xlsx:Belgio!r8 |
| Austria | RELAX Natürlich Wohnen GmbH | sito https://relax.eco — TLD .eco estraneo a Austria | xlsx:Austria!r27 |
| Austria | Alvorada Kaffeerösterei GmbH | sito http://alvorada.wien — TLD .wien estraneo a Austria | xlsx:Austria!r40 |
| Austria | EZA Fairer Handel GmbH | sito https://www.eza.cc — TLD .cc estraneo a Austria | xlsx:Austria!r63 |

---

## 11 · Divergenze fra JSON di build e foglio Excel  (0)

_Nessun rilievo._

---

## 11b · Record presente nei JSON ma assente dal foglio  (0)

_Nessun rilievo._
