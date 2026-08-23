# Prompt di VERIFICA QUALITÀ — MyEUDR Lead Mapping

> Da incollare come primo messaggio in una nuova sessione di Claude Code sul repository
> `Parzivalbit12/MyEUDR_claude`, branch `claude/myeudr-lead-census-k3i1rk`.

---

Devi eseguire una **verifica record per record** del censimento lead MyEUDR, per trovare refusi,
attribuzioni errate e ogni altro errore introdotto durante la raccolta. **Non è un task di ricerca
di nuove aziende**: è un controllo qualità del lavoro esistente.

## 1. Contesto

`MyEUDR_Lead_Mapping.xlsx` contiene **8 fogli e 742 aziende** (Italia 95, Germania 97, Finlandia 84,
Danimarca 89, Svezia 89, Olanda 100, Belgio 95, Austria 93). Sono potenziali clienti di MyEUDR,
software di compliance all'EU Deforestation Regulation. I dati grezzi stanno in
`_myeudr_build/<prefix>_NN_*.json` (prefissi: dk, se, nl, be, at; Italia/Germania/Finlandia
esistono solo come fogli Excel). Colonne del foglio, in ordine:
`Denominazione, Filiera EUDR, Dimensione, Referente, Ruolo, LinkedIn, Email/PEC, Sito web, Sede, Fonte`.

Leggi `MyEUDR_CONTINUA.md` per il metodo, i criteri del cliente e le esclusioni già motivate.

## 2. Vincoli d'ambiente (leggi PRIMA di iniziare)

- Il proxy di egress **nega per policy** (403 al CONNECT) tutti i domini esterni: **WebFetch e curl
  non funzionano** su registri e siti aziendali. Non provarli, non ritentarli.
- Funziona **solo WebSearch**, i cui frammenti contengono spesso i dati necessari.
- Il **limite di sessione degli agenti si riattiva spesso** (è successo 8 volte). Quindi:
  lancia **massimo 2-3 agenti per volta** e imponi a ciascuno il **salvataggio incrementale**
  (scrivere il file dei rilievi ogni 3-4 record, mai solo alla fine).
- Committa e pusha dopo ogni lotto chiuso, sul branch indicato. Non aprire nuove PR: usa la #1.

## 3. Fase A — controlli deterministici (senza rete, falli tu subito)

Scrivi ed esegui uno script Python su tutti i JSON e sul workbook. Cerca:

1. **Duplicati**: stessa azienda in più file o più fogli (normalizza il nome: minuscole, via
   punteggiatura, forme giuridiche e contenuto tra parentesi).
2. **Email sospette di essere dedotte**: dominio dell'email diverso dal dominio del `sito`.
   È il segnale tipico di un indirizzo costruito per analogia, vietato dalle regole del cliente.
3. **Email o LinkedIn ripetuti** su aziende diverse (errore di copia-incolla).
4. **URL LinkedIn** che non contengono `linkedin.com`; siti che non iniziano per `http`.
5. **Entità HTML residue** (`&amp;`, `&gt;`, `&#39;`) in qualunque campo.
6. **Tassonomia `Filiera`**: deve essere `<Macro>` o `<Macro> — <dettaglio>`, con macro tra
   `Legno/Arredo, Legno/Segheria, Carta/Packaging, Caffè, Cacao/Cioccolato, Gomma, Mangimi/Soia,
   Bovini/Carne, Pelle/Concia, Olio di palma`. Segnala i valori fuori elenco (nel foglio Finlandia
   esistono varianti storiche: annotale ma non riscrivere i fogli già consegnati senza dirlo).
7. **Campo `Fonte` vuoto o non URL**, e `Dimensione` vuoto.
8. **Numeri incoerenti in `Dimensione`**: cifre che, convertite, cadono fuori dalla forbice 5-40 M€
   senza che il campo contenga una segnalazione esplicita di taglia.
9. **Denominazione**: numeri di registro rimasti nel nome (CVR, KVK, org.nr, Firmenbuch),
   doppi spazi, forme giuridiche incoerenti col paese del foglio
   (IT: S.r.l./S.p.A. · DE/AT: GmbH/AG · DK: A/S/ApS · SE: AB · NL: B.V./N.V. · BE: NV/BV/SA/SRL).

Produci `_myeudr_build/verifica/00_controlli_automatici.md` con i risultati.

## 4. Fase B — verifica sul web, record per record

Dividi il lavoro per foglio e lancia agenti (2-3 per volta) con questo mandato. Ogni agente prende
**un blocco di 15-20 record** e per ciascuno verifica, con al massimo 2-3 query WebSearch:

1. **L'azienda esiste, è attiva e indipendente.** Segnala fallimenti, liquidazioni, cessazioni e
   acquisizioni recenti. (Sono già stati trovati 7 casi di insolvenza e 3 di cessazione: è un
   rischio reale, non teorico.)
2. **La `Filiera` è corretta e rientra davvero nell'Allegato I EUDR** (legno, carta/cartone, caffè,
   cacao, gomma, soia, olio di palma, bovini/pelle). Segnala come ERRORE DI PERIMETRO chi lavora
   solo lino, colza, girasole, zucca, silicone, plastica o biodiesel, e gli operatori di **sola
   logistica/magazzinaggio** (non immettono la commodity sul mercato UE).
3. **L'email appartiene davvero a quell'azienda**: deve comparire letteralmente in una fonte
   pubblica. Se non la ritrovi, segnalala come DA CONFERMARE — non cancellarla d'ufficio.
4. **Il referente è l'attuale vertice di quella società** (non un omonimo, non un predecessore,
   non l'amministratore della capogruppo). Verifica anche che il `Ruolo` sia coerente col paese
   (Geschäftsführer, VD, adm. direktør, directeur, gedelegeerd bestuurder/administrateur délégué).
5. **Il LinkedIn è la pagina di quell'azienda** (i prefissi regionali dk./nl./se. sono legittimi).
6. **Il sito è il dominio giusto** e non di un'omonima estera. *Caso reale già intercettato:*
   `nutrimin.com` è canadese, l'azienda danese è `nutrimin.dk`.
7. **La sede** (città e regione) è coerente con il paese del foglio.
8. **La `Dimensione`** dichiara che tipo di dato è (fatturato, bruttofortjeneste, totale di
   bilancio, dipendenti, volumi) con fonte e anno, e la conversione valutaria è giusta:
   **DKK 7,46/€ · SEK 11,3/€**; NL, BE e AT sono già in euro.
   ⚠️ Insidia svedese: allabolag riporta spesso in **KSEK** (migliaia). "10 820 KSEK" fa ~1 M€,
   non 10 M€: controlla che nessuna micro-impresa sia entrata per questo equivoco.
9. **La `Fonte`** è pertinente e sostiene davvero il dato riportato.

**Non modificare i dati.** Ogni agente scrive solo un file di rilievi
`_myeudr_build/verifica/<foglio>_<blocco>.json`, array di oggetti con chiavi:
`foglio, denominazione, campo, problema, gravita, evidenza, correzione_proposta`
dove `gravita` ∈ `alta` (dato falso o azienda non contattabile/non EUDR), `media` (dato dubbio o
obsoleto), `bassa` (refuso formale). `evidenza` deve contenere un URL o la citazione del frammento.

## 5. Punti già noti da riverificare per primi

- **Sas NV** (Belgio): non è più familiare — Miko 2021, poi Nimbus Investments 05/2024. Referente
  Herman Sas da riconfermare.
- **Silco** (4,8 vs 8,4 M€) e **Belignum** (16,1 vs 14,7 M€): fatturati discordanti tra fonti.
- **Just Coffee** (Danimarca): ragione sociale CVR mai verificata.
- **Vestjysk Specialfoder** (Danimarca): allo stesso indirizzo risulta un'omonima **sotto fallimento**.
- **Tjørnehøj Mølle** (Danimarca): il fatturato trovato è del **2003**.
- **Horreds Möbel** (Svezia): ultimo dato del 2022. **Gärsnäs**: VD discordante tra fonti, risolto
  con l'annuncio ufficiale — riconfermare.
- **Origin Bridge** (Olanda): forma giuridica probabilmente non B.V.
- **Estate Coffee Copenhagen** = Smage-Compagniet A/S e **Copenhagen Chocolate Factory** = marchio
  Simply Chocolate: verificare che l'identità annotata sia corretta.
- **Bangma Verpakking** (Olanda): maggioranza di De Jong Verpakking dal luglio 2020.
- **Aziende rimosse durante la raccolta** (controlla che non siano rientrate da qualche parte):
  Getama Danmark, Dragsbæk, Pacorini Antwerp, Immobra, Lavazza Kaffee, Segafredo Zanetti Austria,
  Kaffee Partner Austria.
- **Italia**: ha referente solo 11/95 ed è il foglio più vecchio — merita un controllo formale
  su denominazioni ed email.

## 6. Consegna finale

1. `_myeudr_build/verifica/REPORT_VERIFICA.md`: sintesi per foglio, conteggio rilievi per gravità,
   elenco dei casi `alta` con evidenza, e le correzioni che proponi.
2. **Applica solo le correzioni certe** (refusi formali, entità HTML, forme giuridiche, filiere fuori
   Allegato I, aziende cessate), rigenera i fogli con
   `python add_country.py <prefix> <Paese> /home/user/MyEUDR_claude/MyEUDR_Lead_Mapping.xlsx`
   e **ripristina l'ordine dei fogli** (Italia, Germania, Finlandia, Danimarca, Svezia, Olanda,
   Belgio, Austria) con `wb._sheets=[wb[n] for n in ordine]`, perché lo script riaccoda in fondo.
3. Lascia i casi dubbi **nel report, non nel foglio**: meglio un rilievo aperto che una correzione
   inventata. Vale la stessa regola ferrea della raccolta: **mai un dato non verificato**.
4. Committa e pusha; aggiorna `MyEUDR_CONTINUA.md` con l'esito della verifica.
