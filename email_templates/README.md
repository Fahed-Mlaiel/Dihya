# Dihya Email Templates

## Présentation (français)
Ce dossier contient tous les modèles d’emails transactionnels, notifications, et templates multilingues utilisés par la plateforme Dihya. Chaque template est conçu pour être personnalisable, sécurisé, accessible, et compatible avec les principaux clients email.

## Overview (English)
This folder contains all transactional email templates, notifications, and multilingual templates used by the Dihya platform. Each template is customizable, secure, accessible, and compatible with major email clients.

## دليل القوالب البريدية (العربية)
يحتوي هذا المجلد على جميع قوالب البريد الإلكتروني والمعاملات والإشعارات متعددة اللغات لمنصة ديهيا. كل قالب قابل للتخصيص وآمن ومتوافق مع جميع العملاء.

## ⵉⵎⴰⵣⵉⵖⵏ (amazigh)
Aganfu agi yegber akk inagan n email n Dihya, s uselkim, tazwart, tazwart n tutlayin.

### Structure
- index.js : Point d’entrée pour la gestion des templates.
- Exemples de templates : welcome, reset_password, notification, etc.

### Sécurité & Accessibilité
- Aucune donnée sensible en dur.
- Utilisation de balises accessibles (ARIA, alt, etc.).
- Prise en charge du dark mode et fallback texte.

### Personnalisation
- Variables dynamiques (nom, lien, etc.)
- Support multilingue (fr, en, ar, amazigh)

### Exemples d’utilisation
Voir `index.js` pour l’intégration Node.js/Express.

---

# Email Templates Inventory
- welcome_email.html
- password_reset.html
- notification_alert.html

# Contribution
Merci de suivre les guidelines de sécurité, d’accessibilité et de multilinguisme pour chaque nouveau template.

---

## 🔒 Sécurité avancée
- Validation stricte des variables injectées (XSS, injection).
- Aucun secret ou donnée sensible dans les templates.
- Audit automatique via scripts CI/CD.

## ♿ Accessibilité avancée
- Tous les emails sont testés avec des lecteurs d’écran (NVDA, VoiceOver).
- Contraste élevé, police lisible, dark mode natif.
- Structure ARIA et balises alt systématiques.

## 🌍 Multilinguisme & Souveraineté
- Tous les templates sont disponibles en français, anglais, arabe, amazigh.
- Les contenus sont hébergés sur des serveurs souverains (voir POLITIQUE_SOUVERAINETE.md).

## 🧩 Extensibilité & Plugins
- Ajoutez vos propres hooks dans `index.js` pour transformer dynamiquement les emails.
- Support de plugins pour la personnalisation métier.

## 🧪 Tests & CI/CD
- Chaque template est testé (unit, intégration, e2e) via `test.sh` et `jest`.
- Linting automatique (`lint.sh`).
- Vérification de la conformité RGAA/ARIA.

## 🚀 Exemples d’intégration multi-stack
- Node.js/Express : voir `index.js`
- Python (Flask/Django) : voir `/scripts/main.py`
- PHP : voir `/docs/EMAIL_PHP.md`

## 📄 Documentation & Contribution
- Toute contribution doit inclure :
  - Un template par langue
  - Un test unitaire et un test d’accessibilité
  - Un exemple d’intégration
- Voir `/CONTRIBUTING.md` et `/ACCESSIBILITY_GUIDE_ADVANCED.md`

---

# 🧪 Tests unitaires (exemple)
```js
const { loadEmailTemplate } = require('./index');
test('Charge le template de bienvenue en français', () => {
  const html = loadEmailTemplate('welcome_email', { username: 'Dihya', link: 'https://dihya.app' }, 'fr');
  expect(html).toContain('Dihya');
});
