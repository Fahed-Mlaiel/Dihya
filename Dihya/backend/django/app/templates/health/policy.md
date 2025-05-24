# 🩺 Dihya Health Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵉⵙⵉⵏⴰⵡⵉⵏ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "health" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée de santé ou personnelle ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect du secret médical.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (médecin, patient, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité et de rendu.

---

## 🇬🇧 Usage Policy

This folder contains the "health" module templates for Dihya.
**Rules:**
- **Security**: No health or personal data must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.).
- **Privacy**: No tracking, no third-party cookies, medical confidentiality respected.
- **Roles**: Templates must integrate user role management (doctor, patient, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility and rendering tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "health" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات صحية أو شخصية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية**: لا تستخدم موارد خارجية غير سيادية.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام سرية المعلومات الطبية.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (طبيب، مريض، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "health" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka n wawal n tneɣruft neɣ n wudem deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n tneɣruft yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (asqelmed, amuddu, admin, azay…).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri d uskan.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de variable sensible ou médicale : -->
  <!-- {{ patient.medical_record }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Prendre rendez-vous' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue patient" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme santé souveraine' %}">
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
