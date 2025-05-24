# 📈 Dihya Marketing Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵎⴰⵔⴽⵉⵜⵉⵏⴰⴳ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "marketing" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret marketing ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, analytics souverain uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des données marketing.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (marketeur, analyste, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité marketing.

---

## 🇬🇧 Usage Policy

This folder contains the "marketing" module templates for Dihya.
**Rules:**
- **Security**: No personal data, sensitive info, or marketing secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign analytics allowed.
- **Privacy**: No third-party tracking, no third-party cookies, user and marketing data privacy respected.
- **Roles**: Templates must integrate user role management (marketer, analyst, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and marketing compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "التسويق" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار تسويقية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، تحليلات سيادية فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وبياناتهم التسويقية.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مسوق، محلل، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق تسويقي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "marketing" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n marketing deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, analytics n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d marketing yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (marketer, analyst, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n marketing.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information marketing confidentielle ou de donnée personnelle : -->
  <!-- {{ campagne.secret_marketing }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Voir la campagne' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme marketing souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme marketing souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité marketing).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité marketing, excellence.
