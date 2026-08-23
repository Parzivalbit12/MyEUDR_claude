# REPORT DI VERIFICA — MyEUDR Lead Mapping

Verifica record per record del censimento (742 aziende, 8 fogli). Fase A: controlli deterministici offline. Fase B: riscontro sul web, record per record.

**Totale rilievi Fase B: 12** (alta 3 · media 4 · bassa 5).


## Sintesi per foglio

| Foglio | Rilievi | alta | media | bassa | Aziende toccate |
|---|--:|--:|--:|--:|--:|
| Italia | 0 | 0 | 0 | 0 | 0 |
| Germania | 0 | 0 | 0 | 0 | 0 |
| Finlandia | 0 | 0 | 0 | 0 | 0 |
| Danimarca | 5 | 1 | 1 | 3 | 4 |
| Svezia | 0 | 0 | 0 | 0 | 0 |
| Olanda | 0 | 0 | 0 | 0 | 0 |
| Belgio | 7 | 2 | 3 | 2 | 3 |
| Austria | 0 | 0 | 0 | 0 | 0 |
| **TOTALE** | **12** | **3** | **4** | **5** | **7** |

## Rilievi per campo

| Campo | Rilievi | alta |
|---|--:|--:|
| dimensione | 5 | 1 |
| referente | 2 | 1 |
| email | 2 | 0 |
| sito | 1 | 0 |
| denominazione | 1 | 1 |
| fonte | 1 | 0 |

---

## Casi di gravità ALTA (3)

_Dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, oppure fuori dal perimetro dell'Allegato I EUDR._


### Danimarca (1)

**AUBO PRODUCTION A/S** — campo `referente`  
Referente non attuale: Torben Andersen è il PREDECESSORE. La carica di administrerende direktør è passata a Torben Paulin (ingresso registrato 22.01.2026 secondo lasso.dk). Contattare Torben Andersen come vertice attuale è un dato falso.  
*Evidenza:* https://lasso.dk/firmaer/28854846/ny-administrerende-direktr-i-aubo-production-as/ — titolo "Ny administrerende direktør i AUBO PRODUCTION A/S"; frammento: "Torben Paulin overtook the position of administrerende direktør (CEO) at AUBO PRODUCTION A/S from Torben Andersen"  
*Correzione proposta:* Torben Paulin — Adm. direktør


### Belgio (2)

**Sas NV (Sas Coffee)** — campo `dimensione`  
CONFERMATO: l'azienda NON e' piu' indipendente ne' familiare. Acquisita da Miko NV (11/2021) e rivenduta il 24-05-2024 al fondo di private equity olandese Nimbus Investments; il sito di Nimbus la elenca come societa' di portafoglio con 'complete repositioning and rebranding'. Le decisioni di compliance EUDR si prendono a livello di gruppo/fondo: lead NON valido come impresa familiare indipendente.  
*Evidenza:* https://nimbus.com/ - 'Sas Coffee, a specialist in private label coffee, recently became part of the Nimbus portfolio'; https://www.made-in.be/kempen/kempens-koffiebedrijf-miko-blijft-achter-met-financiele-kater-van-20-miljoen-euro-na-verkoop-sas-koffie/ ; https://fd.nl/bedrijfsleven/1517530/investeerder-nimbus-koopt-belgische-koffiebrander-sas  
*Correzione proposta:* Segnalare nel campo dimensione: 'controllata di Nimbus Investments (NL) dal 24-05-2024 - non indipendente' oppure rimuovere il lead

**Silco NV** — campo `denominazione`  
RILIEVO NUOVO emerso in verifica: la sede di Silco (Italielei 181, 2000 Antwerpen) e' lo stesso indirizzo di EFICO NV, il grande trader di caffe' verde di Anversa (fatturato ~289 M€), il cui presidente e' Philippe Van Gestel e che e' controllata dalla famiglia Van Gestel (Noord Natie). L'amministratore di Silco indicato nel foglio e' 'Philip Van Gestel'. Forte indizio che Silco sia un veicolo del gruppo Efico/Van Gestel e non una trading house indipendente: in tal caso la compliance EUDR si deciderebbe a livello di capogruppo e il lead non sarebbe valido. DA CONFERMARE il legame societario.  
*Evidenza:* https://www.tendata.com/en/buyer/efico-nv-italielei-181-2000-antwerp-belgium-BELN376bec4ab92398acd7b73f7696701f41.html - 'EFICO NV. ITALIELEI 181. 2000 ANTWERP BELGIUM'; https://www.companyweb.be/en/0431096011/efico ; frammento: 'Philippe Van Gestel is the chairman of Efico... Noord Natie (the Van Gestel family) has control over Efico'  
*Correzione proposta:* — (nessun valore certo: rilievo aperto)


---

## Casi di gravità MEDIA (4)


### Danimarca (1)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| SØRENSEN LÆDER A/S (Sorensen Leather) | dimensione | Dato obsoleto e non allineato alla fonte: il record indica bruttofortjeneste 23,85 mio DKK (2022) e ca. 20 dipendenti, mentre la scheda proff.dk attuale (CVR 50828514) riporta bruttofortjeneste 13.056 tkr (13,06 mio DKK ≈ 1,75 M€) | https://www.proff.dk/regnskab/s%C3%B8rensen-l%C3%A6der-as/lystrup/skind-l%C3%A6der-og-pels/GKJEN4I07RD — frammento: "Bruttofortjeneste: 13.056 tkr ... Number of employees | Bruttofortjeneste 13,06 mio DKK (~1,75 M€) e 16 dipendenti — proff.dk, CVR 50828514 (ultimo bilancio disponibile); fattu |

### Belgio (3)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Sas NV (Sas Coffee) | referente | Herman Sas risulta ancora 'gedelegeerd bestuurder' negli estratti KBO pubblicati (pappers.be, insieme a Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HELFINCO), ma nessuna fonte post-cessione a Nimbus (05/2024) lo riconferm | https://www.pappers.be/nl/company/sas-0404190783 - 'Herman Sas is de gedelegeerd bestuurder; overige bestuurders: Dominic Sas, Danielle Vanden Eede, Micheline Sas, NV HEL |  |
| Sas NV (Sas Coffee) | email | L'email nel foglio (info@sas-koffie.be) NON e' quella pubblicata sul sito ufficiale sas-coffee.com: la pagina di contatto riporta CUSTOMERSERVICE@SAS-COFFEE.COM, tel. +32 14 61 12 00, indirizzo LILSEDIJK 36 - 2340 BEERSE. info@sas | https://sas-coffee.com/en/contact/ - 'CUSTOMERSERVICE@SAS-COFFEE.COM \| +32 14 61 12 00 \| LILSEDIJK 36 - 2340 BEERSE - BELGIUM' | customerservice@sas-coffee.com ; sede Lilsedijk 36, 2340 Beerse DA CONFERMARE |
| Silco NV | dimensione | Discordanza 4,8 vs 8,4 M€ NON risolta: le due banche dati continuano a riportare cifre diverse per lo stesso ultimo bilancio depositato (14-06-2024). Trendstop: EUR 8.358.215 (23a nel settore 'koffie en thee'); Companyweb/Fincheck | https://trendstop.knack.be/nl/detail/715792692/silco.aspx - 'omzet van 8.358.215 euro, 23e in de sector Koffie en thee'; https://www.companyweb.be/en/0715792692/silco - ' |  |

---

## Casi di gravità BASSA (5)


### Danimarca (3)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| NIELAUS A/S | dimensione | Numero di dipendenti non allineato alla fonte citata: la scheda proff.dk (CVR 35480943) riporta 19 addetti, il record ne indica 11. | https://www.proff.dk/firma/nielaus-as/bramming/m%C3%B8bler/GUJZBOI015G — frammento: "NIELAUS A/S is a furniture production company located at Vejrup Storegade 63, 6740 Br | 19 dipendenti (proff.dk, CVR 35480943) — verificare l'anno di riferimento |
| NIELAUS A/S | email | DA CONFERMARE: l'indirizzo info@nielaus.dk non compare letteralmente in nessuna fonte pubblica reperita; la pagina Kontakt del sito ufficiale protegge l'indirizzo dagli spambot e non lo espone in chiaro nei frammenti. | https://www.nielaus.dk/da/om-os/kontakt — frammento: "Email: Available on their website (protected against spambots)" |  |
| ONECOLLECTION A/S (House of Finn Juhl) | fonte | DA CONFERMARE: l'ID proff nell'URL citato (GXS757I015G) non coincide con quello della scheda ONECOLLECTION A/S CVR 29787786 reperita (GQYY8HI016D). L'URL potrebbe puntare a una scheda diversa/obsoleta. | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D — titolo: "ONECOLLECTION A/S - CVR-nr 29787786 - Ringkøbing" | https://www.proff.dk/firma/onecollection-as/ringk%C3%B8bing/producenter/GQYY8HI016D |

### Belgio (2)

| Azienda | Campo | Problema | Evidenza | Correzione proposta |
|---|---|---|---|---|
| Belignum NV | dimensione | Discordanza 16,1 vs 14,7 M€ RISOLTA a favore di 14,7 M€: due fonti indipendenti (trendstop NL e trendstop FR/Levif) riportano concordemente EUR 14.746.642 e 10,8 FTE per l'ultimo bilancio depositato il 02-07-2024 (esercizio 2023). | https://trendstop.knack.be/nl/detail/405348449/belignum.aspx - 'omzet van 14.746.642 euro, 40e in de sector houthandel... laatst neergelegde jaarrekening 02-07-2024... 10 | Fatturato EUR 14.746.642, esercizio 2023 (bilancio depositato 02-07-2024), 10,8 FTE - eliminare il riferimento a 16.075. |
| Silco NV | sito | Nessun sito web proprio reperito per Silco NV in 3 ricerche: l'azienda compare solo su banche dati societarie (trendstop, companyweb, fincheck, northdata, staatsbladmonitor). Coerente con la struttura a 1 FTE. Il campo vuoto e' qu | https://www.northdata.com/Silco%20N.V.,%20Antwerpen/KBO%200715.792.692 - solo scheda registro; nessun dominio aziendale nei risultati | n.d. (nessun sito web aziendale) |
