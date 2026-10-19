# Plugin Pair per Codex

**Assistenza per applicazioni PHP Pair e sviluppo del framework, basata sulla versione realmente installata.**

Autore: **Viames Marino** · Licenza **MIT** · Versione **0.3.0**

[Sito](https://viames.github.io/pair-plugin/) · [Release](https://github.com/viames/pair-plugin/releases) · [English](README.md)

## Installazione

```sh
codex plugin marketplace add viames/pair-plugin
codex plugin add pair@viames-pair
```

Apri una nuova chat nel progetto Pair e richiama `@Pair`. Per fissare una versione, aggiungi il marketplace con `--ref v0.3.0`.

Se usi già `pair@local`, dopo aver installato questa distribuzione disabilita la vecchia copia nelle impostazioni dei plugin, per evitare istruzioni duplicate.

## Funzionalità

Sei skill per orientamento, moduli, API, form, migrazioni e CRUD. I riferimenti caricati quando servono comprendono ORM, autenticazione e contratti mobile, cache, servizi, PWA/push, diagnostica, pacchetti e aggiornamenti del framework.

La [mappa delle funzionalità](plugins/pair/skills/pair/references/capabilities.md) indica dove trovare le API effettive. Il plugin preserva i flussi legacy e le autorizzazioni già fornite dall'utente.

## Distribuzione e verifiche

Le release comprendono lo ZIP del marketplace, lo ZIP del solo plugin e le impronte SHA-256. Lo ZIP del marketplace può essere estratto e aggiunto con `codex plugin marketplace add /percorso/estratto`.

Il plugin è gratuito, senza server MCP o dipendenze runtime proprie. Usa strumenti, permessi e modello dell'host. I servizi del modello mantengono le proprie condizioni; non viene richiesta una chiave API aggiuntiva dal plugin.

La distribuzione è pubblica su GitHub e installabile tramite marketplace Codex. Non implica l'approvazione nel catalogo OpenAI. I controlli strutturali sono distinti dai [23 scenari comportamentali](plugins/pair/validation/scenarios.md), predisposti per prove sui modelli scelti e non dichiarati tutti superati.

Per aggiornare: `codex plugin marketplace upgrade viames-pair`, quindi `codex plugin add pair@viames-pair`. Apri una nuova chat dopo l'aggiornamento.

[Privacy](plugins/pair/PRIVACY.md) · [Licenza MIT](LICENSE) · [Assistenza](https://github.com/viames/pair-plugin/issues)
