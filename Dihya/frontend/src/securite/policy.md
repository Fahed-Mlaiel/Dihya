# Policy de sécurité Dihya Frontend

## Objectif
Garantir la sécurité maximale des modules frontend (CORS, JWT, validation, audit, WAF, anti-DDOS, RGPD, logs, anonymisation).

## Politiques principales
- CORS strict (origines autorisées dynamiques)
- Authentification JWT (expiration, refresh, blacklist)
- Validation de toutes les entrées (anti-XSS, anti-injection)
- Auditabilité (logs structurés, export, anonymisation)
- WAF intégré (règles personnalisables)
- Protection anti-DDOS (rate limiting, captcha)
- RGPD (droit à l’oubli, export, consentement)

## Exemple d’intégration
```js
import { secureRoute } from './policy';
app.use('/api', secureRoute);
```

## Internationalisation
Supporte : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Extensibilité
Ajoutez vos propres règles via plugins.
