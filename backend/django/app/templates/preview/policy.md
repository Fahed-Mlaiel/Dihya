# 👁️ Dihya Preview Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⴰⵎⴰⵣⵉⵖ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "preview" (prévisualisation de contenus, assets, médias, documents, etc.) de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret de preview ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier/tactile, ARIA, responsive).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, preview souverain uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des droits preview.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (lecteur, éditeur, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, données structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité preview.
- **Droits d’auteur** : Respect absolu des droits d’auteur et licences preview/médias.

---

## 🇬🇧 Usage Policy

This folder contains the "preview" module templates for Dihya (content, asset, media, document preview, etc.).
**Rules:**
- **Security**: No personal data, sensitive info, or preview secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard/touch nav, ARIA, responsive).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign preview.
- **Privacy**: No third-party tracking, no third-party cookies, user and preview/media rights privacy respected.
- **Roles**: Templates must integrate user role management (reader, editor, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, structured data are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and preview compliance tests.
- **Copyright**: Absolute respect for copyright and preview/media licenses.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "المعاينة" في ديهيا (معاينة محتوى، وسائط، مستندات...).
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار معاينة في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG)، دعم لوحة المفاتيح/اللمس، ARIA، استجابة التصميم.
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، معاينة سيادية فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وحقوق المعاينة/الوسائط.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (قارئ، محرر، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف وبيانات منظمة.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق معاينة.
- **حقوق النشر**: احترام مطلق لحقوق النشر ورخص المعاينة/الوسائط.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "preview" n Dihya (tawuri n preview n ugbur, amedya, isefka...).
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n preview deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG, tawuri n tneflit, ARIA, responsive.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, preview n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d preview/media yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (reader, editor, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n preview.
- **Azref n tazwart**: Asirem n tazwart d izerfan n preview/media ilaq ad yili.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information preview confidentielle ou de donnée personnelle : -->
  <!-- {{ preview.secret_asset }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <img src="{% static 'preview/doc.jpg' %}" alt="{% trans 'Document à prévisualiser' %}" />
  ```
- **i18n** :
  ```django
  <h1>{% trans "Prévisualisation de document" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Prévisualisation souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité preview).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité preview, excellence.
