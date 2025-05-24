# 📱 Dihya Mobile Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵎⵓⴱⵉⵍ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "mobile" (PWA, web mobile, intégration Flutter/React Native, etc.) de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret mobile ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation tactile/voix, ARIA, responsive).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, notifications push souveraines uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des données mobiles.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (utilisateur mobile, admin, invité…).
- **SEO & PWA** : Balises meta, titres, descriptions, manifest, balises structurées, viewport responsive obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu, de conformité mobile et PWA.

---

## 🇬🇧 Usage Policy

This folder contains the "mobile" module templates for Dihya (PWA, mobile web, Flutter/React Native integration, etc.).
**Rules:**
- **Security**: No personal data, sensitive info, or mobile secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, touch/voice nav, ARIA, responsive).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign push notifications.
- **Privacy**: No third-party tracking, no third-party cookies, user and mobile data privacy respected.
- **Roles**: Templates must integrate user role management (mobile user, admin, guest…).
- **SEO & PWA**: Meta tags, titles, descriptions, manifest, structured tags, responsive viewport are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, mobile and PWA compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الموبايل" في ديهيا (PWA، ويب موبايل، تكامل Flutter/React Native...).
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار موبايل في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG)، دعم اللمس/الصوت، ARIA، استجابة التصميم.
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، إشعارات دفع سيادية فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وبياناتهم.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مستخدم موبايل، مشرف، زائر...).
- **تحسين محركات البحث & PWA**: يجب تضمين وسوم meta والعناوين والوصف وmanifest وviewport.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق موبايل وPWA.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "mobile" n Dihya (PWA, web mobile, Flutter, React Native...).
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n mobile deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG, tawuri n tneflit, ARIA, responsive.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, push n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d mobile yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (mobile user, admin, azay...).
- **SEO & PWA**: Meta, title, description, manifest, viewport, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n mobile/PWA.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information mobile confidentielle ou de donnée personnelle : -->
  <!-- {{ mobile.secret_device }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Menu mobile' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur l’application mobile souveraine" %}</h1>
  ```
- **SEO & PWA** :
  ```html
  <meta name="description" content="{% trans 'Application mobile souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="manifest" href="{% static 'mobile/manifest.json' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité mobile/PWA).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité mobile, excellence.
