# 🏨 Dihya Hotellerie Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⴰⵏⴻⴳⴳⴰⵔ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "hotellerie" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible ou client ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des clients.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (gestionnaire, client, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité et de rendu.

---

## 🇬🇧 Usage Policy

This folder contains the "hotellerie" module templates for Dihya.
**Rules:**
- **Security**: No sensitive or customer data must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.).
- **Privacy**: No tracking, no third-party cookies, customer privacy respected.
- **Roles**: Templates must integrate user role management (manager, guest, admin, customer…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility and rendering tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الفندقة" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو بيانات العملاء في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية**: لا تستخدم موارد خارجية غير سيادية.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية العملاء.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مدير، ضيف، مشرف، عميل...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "hotellerie" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi neɣ n uclay n templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (amekkan, azay, admin, acilay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri d uskan.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de variable sensible ou client : -->
  <!-- {{ client.credit_card }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Réserver une chambre' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue à l'hôtel" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme hôtelière souveraine' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, excellence.
