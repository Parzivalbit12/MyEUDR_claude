# Fase A — Controlli deterministici automatici

_Generato da `_myeudr_build/verifica/controlli_automatici.py` · nessun accesso di rete._

**Perimetro:** 742 record nel workbook (8 fogli) + 466 record nei 30 file JSON di build.


## Copertura campi per foglio

| Foglio | Record | Email | Referente | Ruolo | LinkedIn | Sito | Sede | Fonte | Dimensione |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Italia | 95 | 68 | 11 | 11 | 10 | 85 | 95 | 95 | 91 |
| Germania | 97 | 88 | 96 | 96 | 17 | 93 | 97 | 97 | 96 |
| Finlandia | 84 | 69 | 77 | 77 | 17 | 84 | 84 | 84 | 83 |
| Danimarca | 89 | 81 | 77 | 78 | 57 | 86 | 89 | 89 | 89 |
| Svezia | 89 | 80 | 75 | 75 | 58 | 88 | 89 | 89 | 89 |
| Olanda | 100 | 77 | 61 | 61 | 67 | 96 | 100 | 100 | 100 |
| Belgio | 95 | 73 | 54 | 54 | 45 | 92 | 95 | 95 | 95 |
| Austria | 93 | 90 | 92 | 92 | 26 | 92 | 93 | 93 | 93 |

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
| 6 | 6 · Tassonomia Filiera fuori elenco | 23 |
| 6b | 6b · Separatore filiera non em-dash | 0 |
| 7 | 7 · Fonte vuota o non URL | 0 |
| 7b | 7b · Dimensione vuota o n.d. | 6 |
| 7c | 7c · Sito web mancante | 26 |
| 8 | 8 · Dimensione fuori forbice 5–40 M€ senza segnalazione esplicita | 8 |
| 9 | 9 · Denominazione: registri, spazi, numeri | 0 |
| 9b | 9b · Forma giuridica incoerente col paese del foglio | 0 |
| 9c | 9c · Nessuna forma giuridica nel nome | 20 |
| 10 | 10 · TLD del sito estraneo al paese del foglio | 7 |
| 11 | 11 · Divergenze fra JSON di build e foglio Excel | 0 |
| 11b | 11b · Record presente nei JSON ma assente dal foglio | 0 |

**Totale rilievi automatici: 179**


## Macro-filiere osservate

| Macro | Occorrenze | In tassonomia |
|---|--:|:--:|
| Legno/Arredo | 187 | ✅ |
| Carta/Packaging | 130 | ✅ |
| Caffè | 94 | ✅ |
| Cacao/Cioccolato | 80 | ✅ |
| Mangimi/Soia | 60 | ✅ |
| Gomma | 49 | ✅ |
| Bovini/Carne | 35 | ✅ |
| Legno/Segheria | 33 | ✅ |
| Pelle/Concia | 32 | ✅ |
| Olio di palma | 19 | ✅ |
| Legno/Compensato-Prodotti | 14 | ❌ |
| Caffè (import caffè verde) | 2 | ❌ |
| Legno/Segheria-Piallatura | 2 | ❌ |
| Legno/Segheria e trasformazione | 1 | ❌ |
| Legno/Commercio-export sahatavara | 1 | ❌ |
| Legno/CLT (trasformazione) | 1 | ❌ |
| Legno/Segheria (betulla) | 1 | ❌ |
| Legno/Piallatura (pannelli/paneelit) | 1 | ❌ |

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
| Danimarca | Copenhagen Coffee Lab ApS | [STEM DIVERSO — DA CONFERMARE] email @cphcoffeelab.com vs sito copenhagencoffeelab.com  (email: webshop@cphcoffeelab.com \| sito: https://copenhagencoffeelab.com/en) | xlsx:Danimarca!r54 |
| Danimarca | Estate Coffee Copenhagen A/S | [STEM DIVERSO — DA CONFERMARE] email @estatecph.com vs sito estatecoffee.dk  (email: kontakt@estatecph.com \| sito: https://estatecoffee.dk/) | xlsx:Danimarca!r56 |
| Danimarca | H.C. JACOBSEN A/S | [STEM DIVERSO — DA CONFERMARE] email @hc-jacobsen.dk vs sito hcemballage.dk  (email: info@hc-jacobsen.dk \| sito: https://hcemballage.dk/) | xlsx:Danimarca!r72 |
| Olanda | Houtimport Reuver B.V. | [STEM DIVERSO — DA CONFERMARE] email @hireuver.nl vs sito houtimportreuver.nl  (email: verkoop@hireuver.nl \| sito: https://www.houtimportreuver.nl) | xlsx:Olanda!r17 |
| Olanda | Origin Bridge (Barchem) | [STEM DIVERSO — DA CONFERMARE] email @bridgetoorigin.com vs sito originbridge.coffee  (email: info@bridgetoorigin.com \| sito: https://originbridge.coffee/) | xlsx:Olanda!r67 |
| Olanda | Van Benthem Diervoeders Vollenhove B.V. | [STEM DIVERSO — DA CONFERMARE] email @vanbenthemvollenhove.nl vs sito vbvoer.nl  (email: info@vanbenthemvollenhove.nl \| sito: https://www.vbvoer.nl/) | xlsx:Olanda!r93 |
| Belgio | Sas NV (Sas Coffee) | [STEM DIVERSO — DA CONFERMARE] email @sas-koffie.be vs sito sas-coffee.com  (email: info@sas-koffie.be \| sito: https://sas-coffee.com/) | xlsx:Belgio!r56 |
| Belgio | Gudrun Commercial NV | [STEM DIVERSO — DA CONFERMARE] email @chocolates.be vs sito gudrungroup.be  (email: info@chocolates.be \| sito: https://gudrungroup.be/) | xlsx:Belgio!r69 |
| Belgio | Oxfam Fair Trade CV | [STEM DIVERSO — DA CONFERMARE] email @oft.be vs sito oxfamfairtrade.be  (email: info@oft.be \| sito: https://www.oxfamfairtrade.be/) | xlsx:Belgio!r73 |
| Austria | Gruber Karton Kreativ GmbH | [STEM DIVERSO — DA CONFERMARE] email @gruber-karton-kreativ.at vs sito gruber-kartonagen.at  (email: office@gruber-karton-kreativ.at \| sito: https://gruber-kartonagen.at) | xlsx:Austria!r51 |
| Austria | Fürst GmbH | [STEM DIVERSO — DA CONFERMARE] email @fuerst.cc vs sito original-mozartkugel.com  (email: versand@fuerst.cc \| sito: https://www.original-mozartkugel.com) | xlsx:Austria!r72 |
| Austria | Heidi Chocolat AG | [STEM DIVERSO — DA CONFERMARE] email @schwedenbomben.at vs sito niemetz.at  (email: office@schwedenbomben.at \| sito: https://niemetz.at) | xlsx:Austria!r73 |
| Austria | Schwaninger Vieh Export GmbH | [STEM DIVERSO — DA CONFERMARE] email @schwaninger.co.at vs sito viehexport.com  (email: office@schwaninger.co.at \| sito: https://www.viehexport.com/) | xlsx:Austria!r94 |

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
| Danimarca | MEJLING LANDHANDEL / SÆBY FRØSALG | [FREEMAIL/PEC] email @mail.dk vs sito mejlinglandhandel.dk  (email: mejlingudlejning@mail.dk \| sito: https://mejlinglandhandel.dk/) | xlsx:Danimarca!r81 |
| Olanda | Houtimport Lekkerkerker B.V. | [FREEMAIL/PEC] email @planet.nl vs sito houtimportlekkerkerker.nl  (email: houtimportlekkerkerker@planet.nl \| sito: https://www.houtimportlekkerkerker.nl) | xlsx:Olanda!r16 |
| Belgio | Decadt Houthandel NV | [FREEMAIL/PEC] email @telenet.be vs sito decadt-hout.be  (email: decadt.hout@telenet.be \| sito: https://decadt-hout.be/) | xlsx:Belgio!r12 |
| Belgio | Emballages Gruselle SRL | [FREEMAIL/PEC] email @skynet.be vs sito emballagesgruselle.eu  (email: gruselle@skynet.be \| sito: https://www.emballagesgruselle.eu) | xlsx:Belgio!r43 |
| Austria | WIESTRADING Gesellschaft m.b.H. | [FREEMAIL/PEC] email @aon.at vs sito wiestrading.at  (email: wiesingerviehhandel@aon.at \| sito: https://www.wiestrading.at/) | xlsx:Austria!r95 |

---

## 2d · Email su dominio affine al sito (TLD/variante) — rischio basso  (52)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | 3C Lavorazione Pelli S.r.l. | [STESSO NOME, TLD DIVERSO] email @conceria3c.it vs sito conceria3c.com  (email: info@conceria3c.it \| sito: https://www.conceria3c.com) | xlsx:Italia!r3 |
| Italia | Compensati Toro SpA | [STESSO NOME, TLD DIVERSO] email @compensatitoro.com vs sito compensatitoro.it  (email: info@compensatitoro.com \| sito: https://compensatitoro.it) | xlsx:Italia!r29 |
| Italia | Itlas Srl Società Benefit | [STESSO NOME, TLD DIVERSO] email @itlas.it vs sito itlas.com  (email: info@itlas.it \| sito: https://www.itlas.com) | xlsx:Italia!r32 |
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
| Danimarca | SCANLUX PACKAGING A/S | [STEM AFFINE] email @scanlux.com vs sito scanlux-packaging.com  (email: scanlux@scanlux.com \| sito: https://scanlux-packaging.com/) | xlsx:Danimarca!r49 |
| Danimarca | DANSK GUMMI INDUSTRI A/S | [STESSO NOME, TLD DIVERSO] email @danskgummi.dk vs sito danskgummi.com  (email: sales@danskgummi.dk \| sito: https://danskgummi.com/) | xlsx:Danimarca!r71 |
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
| Olanda | Papierfabriek Schut B.V. | [STESSO NOME, TLD DIVERSO] email @schutpapier.com vs sito schutpapier.nl  (email: info@schutpapier.com \| sito: https://schutpapier.nl) | xlsx:Olanda!r48 |
| Olanda | Veldhuis Media B.V. | [STEM AFFINE] email @veldhuis.nl vs sito veldhuismedia.nl  (email: info@veldhuis.nl \| sito: https://www.veldhuismedia.nl) | xlsx:Olanda!r51 |
| Olanda | Hesselink Koffiesystemen B.V. | [STESSO NOME, TLD DIVERSO] email @hesselinkkoffie.eu vs sito hesselinkkoffie.nl  (email: info@hesselinkkoffie.eu \| sito: https://hesselinkkoffie.nl/) | xlsx:Olanda!r62 |
| Olanda | Chocolatemakers B.V. | [STESSO NOME, TLD DIVERSO] email @chocolatemakers.nl vs sito chocolatemakers.com  (email: info@chocolatemakers.nl \| sito: https://www.chocolatemakers.com/) | xlsx:Olanda!r74 |
| Olanda | DO IT Organic Food Ingredients B.V. | [STEM AFFINE] email @organic.nl vs sito doitorganic.nl  (email: sales@organic.nl \| sito: https://www.doitorganic.nl/) | xlsx:Olanda!r95 |
| Olanda | Spack B.V. | [STEM AFFINE] email @spackbv.com vs sito spack.nl  (email: info@spackbv.com \| sito: https://www.spack.nl/) | xlsx:Olanda!r97 |
| Belgio | Bulo NV | [STESSO NOME, TLD DIVERSO] email @bulo.be vs sito bulo.com  (email: info@bulo.be \| sito: https://bulo.com) | xlsx:Belgio!r7 |
| Belgio | Lavrijsen Houtbedrijf NV | [STEM AFFINE] email @lavrijsen-geel.be vs sito lavrijsen.be  (email: info@lavrijsen-geel.be \| sito: https://lavrijsen.be/) | xlsx:Belgio!r21 |
| Belgio | Allbox NV | [STEM AFFINE] email @allbox.be vs sito allboxnetwork.be  (email: info@allbox.be \| sito: https://allboxnetwork.be) | xlsx:Belgio!r36 |
| Belgio | Etilux SA | [STESSO NOME, TLD DIVERSO] email @etilux.be vs sito etilux.com  (email: info@etilux.be \| sito: https://www.etilux.com) | xlsx:Belgio!r44 |
| Belgio | Belvas SA | [STEM AFFINE] email @belvas.be vs sito chocolaterie-belvas.be  (email: info@belvas.be \| sito: https://www.chocolaterie-belvas.be/) | xlsx:Belgio!r61 |
| Belgio | Chocolaterie Ickx NV | [STEM AFFINE] email @choc-ickx.be vs sito ickx.be  (email: avangastel@choc-ickx.be \| sito: https://www.ickx.be/) | xlsx:Belgio!r63 |
| Belgio | Hercorub NV | [STESSO NOME, TLD DIVERSO] email @hercorub.com vs sito hercorub.be  (email: info@hercorub.com \| sito: https://www.hercorub.be/) | xlsx:Belgio!r78 |
| Belgio | Royale Lacroix SA | [STESSO NOME, TLD DIVERSO] email @royalelacroix.be vs sito royalelacroix.com  (email: info@royalelacroix.be \| sito: https://www.royalelacroix.com/) | xlsx:Belgio!r88 |
| Belgio | Ameloot BV | [STEM AFFINE] email @ameloot.org vs sito omerameloot.com  (email: petra@ameloot.org \| sito: https://omerameloot.com/nl) | xlsx:Belgio!r89 |
| Austria | Waldviertler Werkstätten GmbH | [STEM AFFINE] email @gea.at vs sito gea-waldviertler.at  (email: gea@gea.at \| sito: https://gea-waldviertler.at/) | xlsx:Austria!r5 |
| Austria | Alvorada Kaffeerösterei GmbH | [STESSO NOME, TLD DIVERSO] email @alvorada.com vs sito alvorada.wien  (email: sales@alvorada.com \| sito: http://alvorada.wien) | xlsx:Austria!r41 |
| Austria | EZA Fairer Handel GmbH | [STESSO NOME, TLD DIVERSO] email @eza.at vs sito eza.cc  (email: office@eza.at \| sito: https://www.eza.cc) | xlsx:Austria!r65 |
| Austria | J. Hornig GmbH | [STESSO NOME, TLD DIVERSO] email @jhornig.at vs sito jhornig.com  (email: online@jhornig.at \| sito: https://www.jhornig.com) | xlsx:Austria!r67 |
| Austria | Königshofer GmbH | [STEM AFFINE] email @koenigshofer.at vs sito koenigshofer-futtermittel.at  (email: ebergassing@koenigshofer.at \| sito: https://www.koenigshofer-futtermittel.at) | xlsx:Austria!r82 |

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

## 6 · Tassonomia Filiera fuori elenco  (23)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Imperator S.r.l. | macro fuori tassonomia: «Caffè (import caffè verde)»  (valore intero: «Caffè (import caffè verde)») | xlsx:Italia!r65 |
| Italia | Sandalj Trading Company S.p.A. | macro fuori tassonomia: «Caffè (import caffè verde)»  (valore intero: «Caffè (import caffè verde)») | xlsx:Italia!r71 |
| Finlandia | Alavus Ikkunat Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — finestre/porte in legno») | xlsx:Finlandia!r4 |
| Finlandia | Aureskosken Jalostetehdas Oy | macro fuori tassonomia: «Legno/Segheria e trasformazione»  (valore intero: «Legno/Segheria e trasformazione») | xlsx:Finlandia!r5 |
| Finlandia | CWP Coloured Wood Products Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — impiallacciatura betulla colorata») | xlsx:Finlandia!r6 |
| Finlandia | Hoisko CLT (CLT Finland Oy) | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — CLT») | xlsx:Finlandia!r12 |
| Finlandia | Hollolan Viilu ja Laminaatti Oy (HVL) | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — impiallacciatura/laminati») | xlsx:Finlandia!r13 |
| Finlandia | Jet-Puu Oy | macro fuori tassonomia: «Legno/Segheria-Piallatura»  (valore intero: «Legno/Segheria-Piallatura») | xlsx:Finlandia!r15 |
| Finlandia | Kiilax Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — compensato betulla/lamellare») | xlsx:Finlandia!r18 |
| Finlandia | Kinnaskoski Oy | macro fuori tassonomia: «Legno/Segheria-Piallatura»  (valore intero: «Legno/Segheria-Piallatura») | xlsx:Finlandia!r19 |
| Finlandia | Lammin Ikkuna Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — finestre/porte in legno-alluminio») | xlsx:Finlandia!r22 |
| Finlandia | Lappiporras Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — scale in legno») | xlsx:Finlandia!r23 |
| Finlandia | Late-Rakenteet Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — legno lamellare/glulam») | xlsx:Finlandia!r25 |
| Finlandia | Mahogany Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — impiallacciatura ed erikoisvaneri») | xlsx:Finlandia!r27 |
| Finlandia | Ollikaisen Hirsirakenne Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — hirsi/lamellare (glulam)») | xlsx:Finlandia!r30 |
| Finlandia | Orasko Oy | macro fuori tassonomia: «Legno/Commercio-export sahatavara»  (valore intero: «Legno/Commercio-export sahatavara») | xlsx:Finlandia!r31 |
| Finlandia | Oy CrossLam Kuhmo Ltd | macro fuori tassonomia: «Legno/CLT (trasformazione)»  (valore intero: «Legno/CLT (trasformazione)») | xlsx:Finlandia!r32 |
| Finlandia | Oy Haka-Wood Ab | macro fuori tassonomia: «Legno/Segheria (betulla)»  (valore intero: «Legno/Segheria (betulla)») | xlsx:Finlandia!r33 |
| Finlandia | Piklas Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — finestre/porte in legno-alluminio») | xlsx:Finlandia!r36 |
| Finlandia | Sepa Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — capriate/prodotti strutturali») | xlsx:Finlandia!r40 |
| Finlandia | Siparila Oy | macro fuori tassonomia: «Legno/Piallatura (pannelli/paneelit)»  (valore intero: «Legno/Piallatura (pannelli/paneelit)») | xlsx:Finlandia!r41 |
| Finlandia | Sysmän Ikkuna ja Ovi Oy (Päijänne-Ovet) | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — finestre/porte in legno») | xlsx:Finlandia!r43 |
| Finlandia | Timberwise Oy | macro fuori tassonomia: «Legno/Compensato-Prodotti»  (valore intero: «Legno/Compensato-Prodotti — parquet/pavimenti in legno») | xlsx:Finlandia!r44 |

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
| Italia | Conceria Emmedue | Dimensione = 'n.d.' | xlsx:Italia!r10 |
| Italia | Segheria Saccavini Srl | Dimensione = 'n.d.' | xlsx:Italia!r37 |
| Germania | Münchner Kaffeerösterei GmbH | Dimensione = 'n.d.' | xlsx:Germania!r52 |
| Finlandia | Helsingin Kumi Oy | Dimensione = 'n.d.' | xlsx:Finlandia!r77 |

---

## 7c · Sito web mancante  (26)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Arko SpA | Sito = '' | xlsx:Italia!r22 |
| Italia | C.I.M.A. Srl (Compensati Impiallacciature Materiali Affini) | Sito = '' | xlsx:Italia!r26 |
| Italia | Holzland Fuchs Srl | Sito = '' | xlsx:Italia!r31 |
| Italia | Zalf SpA (Zalf Industria Mobili Componibili) | Sito = '' | xlsx:Italia!r38 |
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
| Danimarca | DANSK KAFFE ApS | Sito = '' | xlsx:Danimarca!r55 |
| Danimarca | TJØRNEHØJ MØLLE A/S | Sito = 'n.d.' | xlsx:Danimarca!r84 |
| Danimarca | VESTJYSK SPECIALFODER ApS | Sito = 'n.d.' | xlsx:Danimarca!r85 |
| Svezia | Aktiebolaget Cool & Candy | Sito = 'n.d.' | xlsx:Svezia!r77 |
| Olanda | Snel Industrie voor Karton en Papierveredeling B.V. | Sito = '' | xlsx:Olanda!r49 |
| Olanda | Chocolade- en Suikerwerkfabriek Marandi B.V. | Sito = 'n.d.' | xlsx:Olanda!r72 |
| Olanda | Continental Chocolate B.V. | Sito = 'n.d.' | xlsx:Olanda!r75 |
| Olanda | Rousseau Chocolade B.V. | Sito = 'n.d.' | xlsx:Olanda!r81 |
| Belgio | Label-Pak-Int'l Co SA | Sito = 'n.d.' | xlsx:Belgio!r47 |
| Belgio | Silco NV | Sito = '' | xlsx:Belgio!r57 |
| Belgio | Slachthuis Velzeke BV | Sito = 'n.d.' | xlsx:Belgio!r94 |
| Austria | Tschurtschenthaler Gerberei GmbH | Sito = 'n.d.' | xlsx:Austria!r4 |

---

## 8 · Dimensione fuori forbice 5–40 M€ senza segnalazione esplicita  (8)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Svezia | Nordiska Kaffebolaget H. Hansson & Co Aktiebolag | valori stimati M€: 4.84 («54,7 MSEK») \| campo: Fatturato 54,7 MSEK (~4,8 M€) 2024 (+8,4%); 17 dipendenti (14 nel 2023) (fonte: allabolag.se, bilancio 2024). Org.nr 556083-2379. SNI 46370 kaffe/te a | xlsx:Svezia!r75 |
| Svezia | Malmö Chokladfabrik AB | valori stimati M€: 3.77 («42,6 MSEK») \| campo: Fatturato 42,6 MSEK (~3,8 M€) esercizio 2025 (+31,6%); 16 dipendenti (fonte: allabolag.se / bolagsfakta.se). Org.nr 556664-6286. Sotto la fascia tolle | xlsx:Svezia!r81 |
| Svezia | Forsbecks Eftr. Aktiebolag | valori stimati M€: 52.21 («589.951 KSEK») \| campo: ATTENZIONE TAGLIA: fatturato 589.951 KSEK (~52,2 M€) con soli 31-35 dipendenti — bilancio 2022 (fonte allabolag/bolagsfakta); org.nr 556002-3417. Sopr | xlsx:Svezia!r86 |
| Belgio | Baeten & Co NV | valori stimati M€: 42.81 («42.810.588 EUR») \| campo: Fatturato 42.810.588 EUR (bilancio NBB depositato 15-07-2025) — taglia gonfiata dal costo materia prima: solo 13,7 FTE; n. impresa BE 0447.081.908 | xlsx:Belgio!r86 |
| Belgio | Royale Lacroix SA | valori stimati M€: 49.35 («49.349.520 EUR») \| campo: Fatturato 49.349.520 EUR (bilancio NBB, ultimo esercizio pubblicato) — taglia gonfiata dal costo materia prima: solo 18,6 FTE; n. impresa BE 0404.423. | xlsx:Belgio!r88 |
| Belgio | Ameloot BV | valori stimati M€: 49.30 («49.298.205 EUR») \| campo: Fatturato 49.298.205 EUR (Trends Top/NBB, ultimo esercizio); n. impresa BE 0413.029.562. AZIENDA DI CONFINE: sopra i 40 M€ ma PMI familiare indipenden | xlsx:Belgio!r89 |
| Belgio | Dierickx NV | valori stimati M€: 40.84 («40.843.828 EUR») \| campo: Fatturato 40.843.828 EUR (ultimo bilancio depositato NBB, via Trends Top/Companyweb); azienda familiare indipendente alla 5a generazione; n. impresa B | xlsx:Belgio!r90 |
| Belgio | Jos Leemput BV | valori stimati M€: 44.95 («44.954.796 EUR») \| campo: Fatturato 44.954.796 EUR e 16,2 FTE (ultimo bilancio depositato NBB, via Companyweb/FinCheck); n. impresa BE 0424.110.724. AZIENDA DI CONFINE: sopra 4 | xlsx:Belgio!r92 |

---

## 9 · Denominazione: registri, spazi, numeri  (0)

_Nessun rilievo._

---

## 9b · Forma giuridica incoerente col paese del foglio  (0)

_Nessun rilievo._

---

## 9c · Nessuna forma giuridica nel nome  (20)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Italia | Conceria Beschin | nessuna forma giuridica riconoscibile | xlsx:Italia!r7 |
| Italia | Conceria Cilp | nessuna forma giuridica riconoscibile | xlsx:Italia!r8 |
| Italia | Conceria Daniela | nessuna forma giuridica riconoscibile | xlsx:Italia!r9 |
| Italia | Conceria Emmedue | nessuna forma giuridica riconoscibile | xlsx:Italia!r10 |
| Germania | Paletten Meyer | nessuna forma giuridica riconoscibile | xlsx:Germania!r17 |
| Germania | impuls Kaffeemanufaktur | nessuna forma giuridica riconoscibile | xlsx:Germania!r58 |
| Germania | Confiserie Dengel (Inh. Uwe Dengel) | nessuna forma giuridica riconoscibile | xlsx:Germania!r63 |
| Germania | Schell Schokoladenmanufaktur (Inh. Eberhard Schell) | nessuna forma giuridica riconoscibile | xlsx:Germania!r72 |
| Danimarca | NPI (Nordic Panel Import) | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r27 |
| Danimarca | EMBALLAGEFABRIKKEN THY PAP | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r41 |
| Danimarca | Just Coffee | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r58 |
| Danimarca | MEJLING LANDHANDEL / SÆBY FRØSALG | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r81 |
| Danimarca | Naturli' Foods | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r86 |
| Danimarca | Grambogård | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r89 |
| Danimarca | JN Meat International | nessuna forma giuridica riconoscibile | xlsx:Danimarca!r90 |
| Olanda | Origin Bridge (Barchem) | nessuna forma giuridica riconoscibile | xlsx:Olanda!r67 |
| Austria | steininger.designers gmbh | nessuna forma giuridica riconoscibile | xlsx:Austria!r39 |
| Austria | weinberger-holz gmbh | nessuna forma giuridica riconoscibile | xlsx:Austria!r40 |
| Austria | BAG Ölmühle BetriebsgmbH | nessuna forma giuridica riconoscibile | xlsx:Austria!r42 |
| Austria | Margarethner Verpackungsgesellschaft m.b.H. | nessuna forma giuridica riconoscibile | xlsx:Austria!r53 |

---

## 10 · TLD del sito estraneo al paese del foglio  (7)

| Foglio | Denominazione | Rilievo | Origine |
|---|---|---|---|
| Germania | Sawade GmbH | sito https://sawade.berlin — TLD .berlin estraneo a Germania | xlsx:Germania!r71 |
| Finlandia | Ålands Skogsindustrier Ab | sito https://www.skogsindustrier.ax — TLD .ax estraneo a Finlandia | xlsx:Finlandia!r48 |
| Danimarca | DANSK HÅRDTTRÆ SAVVÆRK A/S (DHS) | sito https://dhs.as/ — TLD .as estraneo a Danimarca | xlsx:Danimarca!r8 |
| Belgio | Buzzispace NV | sito https://www.buzzi.space — TLD .space estraneo a Belgio | xlsx:Belgio!r8 |
| Austria | RELAX Natürlich Wohnen GmbH | sito https://relax.eco — TLD .eco estraneo a Austria | xlsx:Austria!r26 |
| Austria | Alvorada Kaffeerösterei GmbH | sito http://alvorada.wien — TLD .wien estraneo a Austria | xlsx:Austria!r41 |
| Austria | EZA Fairer Handel GmbH | sito https://www.eza.cc — TLD .cc estraneo a Austria | xlsx:Austria!r65 |

---

## 11 · Divergenze fra JSON di build e foglio Excel  (0)

_Nessun rilievo._

---

## 11b · Record presente nei JSON ma assente dal foglio  (0)

_Nessun rilievo._
