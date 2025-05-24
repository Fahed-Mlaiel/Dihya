# 📢 Dihya Publicité Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵓⴳⴰⵡⴰⵙ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "publicité" (gestion d’annonces, bannières, campagnes, tracking souverain, etc.) de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret publicitaire ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier/tactile, ARIA, responsive).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, tracking souverain uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des droits publicitaires.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (annonceur, régie, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, données structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité publicité.
- **Droits d’auteur** : Respect absolu des droits d’auteur et licences publicitaires/images.

---

## 🇬🇧 Usage Policy

This folder contains the "publicité" (advertising) module templates for Dihya (ads management, banners, campaigns, sovereign tracking, etc.).
**Rules:**
- **Security**: No personal data, sensitive info, or advertising secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard/touch nav, ARIA, responsive).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign tracking.
- **Privacy**: No third-party tracking, no third-party cookies, user and advertising/image rights privacy respected.
- **Roles**: Templates must integrate user role management (advertiser, agency, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, structured data are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and advertising compliance tests.
- **Copyright**: Absolute respect for copyright and advertising/image licenses.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الإعلانات" في ديهيا (إدارة الإعلانات، لافتات، حملات، تتبع سيادي...).
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار إعلانية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG)، دعم لوحة المفاتيح/اللمس، ARIA، استجابة التصميم.
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، تتبع سيادي فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وحقوق الإعلانات/الصور.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (معلن، وكالة، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف وبيانات منظمة.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق إعلانات.
- **حقوق النشر**: احترام مطلق لحقوق النشر ورخص الإعلانات/الصور.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "publicité" n Dihya (tawuri n annonces, banners, campaigns, tracking n tmurt...).
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n publicité deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG, tawuri n tneflit, ARIA, responsive.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, tracking n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d publicité/image yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (annonceur, régie, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n publicité.
- **Azref n tazwart**: Asirem n tazwart d izerfan n publicité/image ilaq ad yili.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information publicitaire confidentielle ou de donnée personnelle : -->
  <!-- {{ pub.secret_campaign }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <img src="{% static 'publicite/banner.jpg' %}" alt="{% trans 'Bannière publicitaire' %}" />
  ```
- **i18n** :
  ```django
  <h1>{% trans "Nouvelle campagne publicitaire" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Publicité souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité publicité).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité publicité, excellence.
