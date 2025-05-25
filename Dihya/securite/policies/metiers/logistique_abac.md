# Logistique – ABAC Policy

**Langues supportées :** fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

---

## Description
Politique d’accès basée sur les attributs (ABAC) pour la gestion logistique dans Dihya. Permet un contrôle fin des accès selon le rôle, le contexte, la localisation, le niveau de sécurité, et la conformité RGPD.

---

## Attributs principaux
- `role` : admin, user, invité
- `tenant` : organisation, projet
- `action` : create, read, update, delete, export
- `resource` : inventaire, transport, entrepôt, commande
- `locale` : fr, en, ar, ...
- `security_level` : élevé, normal, restreint
- `gdpr_consent` : booléen

---

## Exemple de règle (YAML)
```yaml
policy:
  - effect: allow
    action: [read, export]
    resource: inventaire
    condition:
      role: [admin, user]
      gdpr_consent: true
  - effect: deny
    action: [delete]
    resource: entrepôt
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
- Ajout d’attributs custom via plugins
- Support multi-tenant

---

## Documentation intégrée
Chaque règle doit être documentée en multilingue (voir i18n).

---

## Exemple d’utilisation (Python)
```python
"""
Vérification d’accès logistique (ABAC)
:param user: dict (doit contenir role, tenant, gdpr_consent)
:param action: str
:param resource: str
:return: bool
"""
def check_logistique_access(user: dict, action: str, resource: str) -> bool:
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
- Toutes les actions sont loguées
- Export des accès sur demande
- Consentement utilisateur requis

---

## Multilingue
- Les messages d’erreur et de logs sont traduits dynamiquement selon la locale

---

## Conformité
- Conforme RGPD, ISO 27001, OWASP Top 10
