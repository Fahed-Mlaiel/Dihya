# Marketing – Policy Métier

**Langues supportées :** fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

---

## Objectif
Définir les règles d’accès, d’audit, de conformité et d’extension pour la gestion marketing dans Dihya.

---

## Rôles supportés
- Administrateur (admin)
- Utilisateur (user)
- Invité (guest)

---

## Cas d’usage
- Consultation de campagnes
- Gestion des leads
- Analyse marketing
- Export de données (RGPD)

---

## Sécurité
- Authentification JWT
- CORS dynamique
- Validation stricte
- Audit log structuré
- WAF/anti-DDOS

---

## Internationalisation
- Toutes les routes et messages sont traduits dynamiquement
- Support multilingue complet

---

## Exemples de routes RESTful
- `GET /api/marketing/campagnes`
- `POST /api/marketing/lead`
- `DELETE /api/marketing/analytics/{id}`

---

## Exemples de queries GraphQL
```graphql
query {
  marketingCampagnes(locale: "fr") {
    id
    nom
    statut
  }
}
```

---

## RGPD & Auditabilité
- Export des logs et données sur demande
- Anonymisation automatique
- Consentement utilisateur requis

---

## Extensibilité
- Plugins marketing via API/CLI
- Multi-tenant

---

## Documentation intégrée
Toutes les routes et règles sont documentées en multilingue.

---

## Conformité
- RGPD, ISO 27001, OWASP Top 10
