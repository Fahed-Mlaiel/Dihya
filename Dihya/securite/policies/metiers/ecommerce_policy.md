# Politique de sécurité e-commerce (ABAC)

## Description
Politique d'accès basée sur les attributs (ABAC) pour la gestion des droits dans les applications e-commerce.

## Rôles supportés
- admin
- vendeur
- client
- invité

## Attributs contrôlés
- Statut du compte
- Historique d'achat
- Localisation
- Langue
- Score de confiance

## Exemples de règles
- Un admin peut accéder à tous les modules.
- Un vendeur peut gérer ses propres produits et commandes.
- Un client peut accéder à ses commandes et données personnelles.
- Un invité a un accès limité au catalogue.

## Sécurité
- JWT obligatoire
- CORS strict
- Validation des entrées
- Audit logging
- RGPD: export/anonymisation sur demande

## Internationalisation
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple d'intégration (Python)
```python
"""
@policy('ecommerce')
def can_access_order(user, order):
    '''Vérifie si l'utilisateur peut accéder à la commande.'''
    if user.role == 'admin':
        return True
    if user.role == 'vendeur' and order.seller_id == user.id:
        return True
    if user.role == 'client' and order.client_id == user.id:
        return True
    return False
"""
```

## Extensibilité
- Ajout de plugins via API/CLI
- Support multitenant

## Auditabilité
- Logs structurés, exportables, anonymisables

## Conformité
- RGPD, PCI DSS, ISO 27001

---

# E-commerce Security Policy (EN)
(See French section for details. All rules are mirrored in English, Arabic, German, etc.)
