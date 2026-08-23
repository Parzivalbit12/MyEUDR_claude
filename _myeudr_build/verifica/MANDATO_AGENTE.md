# Mandato per l'agente di verifica (Fase B) — MyEUDR Lead Mapping

## Cosa devi fare
Verifichi **record per record** un blocco di lead già raccolti. **NON cerchi aziende nuove.**
**NON modifichi i dati.** Produci solo un file di rilievi.

## Vincoli d'ambiente — leggili prima di iniziare
- **WebFetch e curl NON funzionano**: il proxy di egress nega (403 al CONNECT) tutti i domini
  esterni. Non provarli, non ritentarli: sprecheresti il budget.
- Funziona **solo WebSearch**. I frammenti dei risultati contengono quasi sempre il dato utile.
- Budget: **massimo 2-3 query WebSearch per record**. Se dopo 3 query il dato non emerge,
  scrivi il rilievo come `DA CONFERMARE` e passa oltre. Non insistere.
- **SALVATAGGIO INCREMENTALE OBBLIGATORIO**: scrivi il file di output dopo i primi 3 record e
  poi **riscrivilo ogni 3-4 record**. Il limite di sessione si riattiva spesso; se salvi solo
  alla fine perdi tutto il lavoro.

## Cosa verificare, per ogni record
1. **Esistenza e stato.** L'azienda esiste, è attiva e indipendente. Segnala **fallimenti,
   liquidazioni, cessazioni, acquisizioni recenti** (sono già emersi 7 casi di insolvenza e 3 di
   cessazione: è un rischio reale). Una controllata di un gruppo estero non è un lead valido:
   la compliance si decide a livello di capogruppo.
2. **Filiera / perimetro EUDR.** Deve rientrare nell'**Allegato I EUDR**: legno, carta/cartone,
   caffè, cacao, gomma, soia, olio di palma, bovini/pelle. Segnala come **ERRORE DI PERIMETRO**
   (gravità alta) chi lavora **solo** lino, colza, girasole, zucca, silicone, plastica o biodiesel,
   e gli operatori di **sola logistica/magazzinaggio** (non immettono la commodity sul mercato UE).
3. **Email.** Deve comparire **letteralmente** in una fonte pubblica. Se non la ritrovi,
   segnalala `DA CONFERMARE` — **non proporne la cancellazione d'ufficio** e non inventarne altre.
4. **Referente e Ruolo.** Deve essere l'**attuale vertice di quella società**: non un omonimo,
   non un predecessore, non l'amministratore della capogruppo. Il ruolo dev'essere coerente col
   paese: *Geschäftsführer* (DE/AT), *VD* (SE), *adm. direktør* (DK), *directeur* (NL),
   *gedelegeerd bestuurder / administrateur délégué* (BE), *toimitusjohtaja* (FI),
   *Amministratore Delegato / Presidente* (IT).
5. **LinkedIn.** Deve essere la pagina **di quell'azienda**. I prefissi regionali
   `dk.` `nl.` `se.` `be.` `at.` `fi.` `it.` sono **legittimi**, non sono errori.
6. **Sito.** Dominio giusto, non di un'omonima estera.
   *Caso reale già intercettato:* `nutrimin.com` è canadese, l'azienda danese è `nutrimin.dk`.
7. **Sede.** Città e regione coerenti col paese del foglio.
8. **Dimensione.** Deve dichiarare **che tipo di dato è** (fatturato, bruttofortjeneste, totale di
   bilancio, dipendenti, volumi) **con fonte e anno**. Verifica la conversione valutaria:
   **DKK 7,46/€ · SEK 11,3/€**; NL, BE, AT, DE, IT, FI sono già in euro.
   ⚠️ **Insidia svedese:** allabolag riporta spesso in **KSEK (migliaia)**. "10 820 KSEK" fa
   **~1 M€, non 10 M€**: controlla che nessuna micro-impresa sia entrata per questo equivoco.
   Forbice target del cliente: **5–40 M€** (sweet spot 10–20). Fuori forbice senza segnalazione
   esplicita nel campo = rilievo.
9. **Fonte.** L'URL dev'essere pertinente e sostenere davvero il dato riportato.

## Query che funzionano
- `"<azienda>" kontakt e-mail telefon` · `"<azienda>" Impressum Geschäftsführer E-Mail`
- `"<azienda>" VD omsättning allabolag` · `"<azienda>" directeur KVK` · `"<azienda>" NBB omzet`
- `"<azienda>" konkurs|fallimento|Insolvenz|faillissement|likvidation` (stato dell'azienda)

## Output — UNICO file da scrivere
Percorso esatto: `_myeudr_build/verifica/<nome_blocco>.json`
Un **array JSON** di oggetti, ciascuno con **esattamente** queste chiavi:

```json
{
 "foglio": "Danimarca",
 "denominazione": "ESEMPIO A/S",
 "campo": "email",
 "problema": "descrizione sintetica del rilievo",
 "gravita": "alta|media|bassa",
 "evidenza": "URL della fonte oppure citazione letterale del frammento di ricerca",
 "correzione_proposta": "valore corretto, oppure '' se non hai un valore certo"
}
```

**Gravità:**
- `alta` — dato falso, azienda non contattabile, azienda cessata/fallita/acquisita, fuori perimetro EUDR.
- `media` — dato dubbio o obsoleto (es. fatturato di 3+ anni fa, referente non riconfermato).
- `bassa` — refuso formale (maiuscole, forma giuridica, TLD, spaziatura).

**`evidenza` deve sempre contenere un URL o la citazione del frammento.** Un rilievo senza
evidenza non vale nulla.

## Regola ferrea
**Mai un dato non verificato.** Nel dubbio scrivi un rilievo `DA CONFERMARE` con
`correzione_proposta: ""`. Meglio un rilievo aperto che una correzione inventata.
Se un record risulta **corretto in tutto**, non scrivere nulla per quel record.
