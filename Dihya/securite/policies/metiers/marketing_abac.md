# Marketing – ABAC Policy

**Langues supportées :** fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

---

## Description
Politique d’accès basée sur les attributs (ABAC) pour la gestion marketing dans Dihya. Contrôle fin selon le rôle, le contexte, la conformité RGPD, et la localisation.

---

## Attributs principaux
- `role` : admin, user, invité
- `tenant` : organisation, projet
- `action` : create, read, update, delete, export
- `resource` : campagne, lead, analytics
- `locale` : fr, en, ar, ...
- `gdpr_consent` : booléen

---

## Exemple de règle (YAML)
```yaml
policy:
  - effect: allow
    action: [read, export]
    resource: campagne
    condition:
      role: [admin, user]
      gdpr_consent: true
  - effect: deny
    action: [delete]
    resource: analytics
    condition:
      role: invité
```

---

## Sécurité
- JWT obligatoire
- CORS strict
- Validation des entrées
- Audit log
- RGPD : anonymisation, export, consentement

---

## Extensibilité
- Plugins marketing
- Multi-tenant

---

## Documentation intégrée
Toutes les règles sont documentées en multilingue.

---

## Exemple d’utilisation (Python)
```python
"""
Vérification d’accès marketing (ABAC)
:param user: dict (doit contenir role, tenant, gdpr_consent)
:param action: str
:param resource: str
:return: bool
"""
def check_marketing_access(user: dict, action: str, resource: str) -> bool:
    # ...existing code...
    if not user.get('gdpr_consent', False):
        return False
    if user['role'] == 'admin':
        return True
    if user['role'] == 'user' and action in ['read', 'export']:
        return True
    return False
```

---

## RGPD & Auditabilité
- Logs complets
- Export sur demande
- Consentement requis

---

## Multilingue
- Messages d’erreur et logs traduits dynamiquement

---

## Conformité
- RGPD, ISO 27001, OWASP Top 10
