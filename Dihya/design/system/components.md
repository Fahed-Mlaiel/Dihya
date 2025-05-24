# 🧩 Dihya – Composants UI (Design System)

Documentation avancée sur les composants UI réutilisables : boutons, inputs, cards, modals, notifications, etc.

---

## Structure
- **Button** : accessible, multilingue, variantes (primaire, secondaire, danger)
- **Input** : champs texte, select, radio, accessibles, multilingues
- **Card** : conteneur, responsive, personnalisable
- **Modal** : dialogues, alertes, focus management, ARIA
- **Notification** : alertes, toasts, multilingue, accessibles

---

## Bonnes pratiques
- Respecter l’accessibilité (focus, ARIA, contrastes)
- Proposer des variantes multilingues (fr, en, ar, tzr)
- Documenter chaque composant (props, slots, exemples)
- Tester la souveraineté (aucune dépendance propriétaire)

---

## Exemples d’intégration
- **React** :
```jsx
import { Button } from '../system/components';
<Button variant="primary" lang="fr">Valider</Button>
```
- **Docs** : intégrer des extraits de code et captures UI

---

## Contribution
- Ajouter/modifier un composant : documenter, tester, vérifier l’accessibilité

---

## Contact
[design@dihya.io](mailto:design@dihya.io)
