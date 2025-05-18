# 📱 Dihya Coding – Mobile (Flutter)

Application mobile Dihya Coding : génération moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🎯 Objectifs

- **Design moderne** : UI/UX Flutter responsive, accessible, compatible mobile et SEO (store)
- **Sécurité** : validation stricte, anonymisation, logs sécurisés, stockage local protégé
- **Conformité RGPD** : consentement utilisateur, droit à l’oubli, logs anonymisés, portabilité
- **Auditabilité** : chaque action/log est traçable, effaçable, documentée
- **Extensibilité** : architecture modulaire, ajout facile de modules, routes, templates
- **Robustesse** : gestion des erreurs, fallback, tests automatisés, monitoring
- **Documentation claire** : docstring, commentaires, guides, exemples

---

## 🏗️ Structure du projet

- `lib/`
  - `main.dart` : Point d’entrée, navigation, RGPD, auditabilité
  - `screens/` : Pages métiers (e-commerce, éducation, social…)
  - `utils/` : Utilitaires sécurité, RGPD, logs, API, export, fallback
  - `widgets/` : Composants réutilisables
- `assets/` : Images, icônes, polices
- `pubspec.yaml` : Dépendances, polices, assets, auditabilité

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Jamais de données sensibles dans le code ou les logs, validation stricte, anonymisation, tokens sécurisés
- **RGPD** : Consentement explicite, logs anonymisés, droit à l’oubli, portabilité des données
- **Auditabilité** : Chaque module/fonction/log est commenté, traçable, effaçable
- **Extensibilité** : Ajout de modules, routes, templates ou utilitaires sans dette technique
- **Robustesse** : Tests automatisés, gestion des erreurs, fallback, monitoring
- **Documentation** : Docstring Dart, guides, exemples, fichiers README par dossier

---

## 📝 Exemple d’utilisation

```dart
import 'utils/rgpd.dart';
import 'utils/logger.dart';

void main() {
  if (Rgpd.hasConsent('app')) {
    Logger.logEvent('init', {'timestamp': DateTime.now().toIso8601String()});
  }
}
```

---

## 📚 Documentation associée

- [main.dart](./lib/main.dart)
- [pubspec.yaml](./pubspec.yaml)
- [utils/](./lib/utils/)
- [screens/](./lib/screens/)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

## 🧪 Tests & auditabilité

- **Unitaires** : `test/`
- **Logs** : anonymisés, effaçables, traçables

---

## 🏷️ Variables d’environnement

Voir `pubspec.yaml` et la documentation Flutter pour la configuration RGPD, sécurité, auditabilité, robustesse.

---

> **Dihya Coding : mobile moderne, robuste, extensible et conforme RGPD pour chaque génération.**