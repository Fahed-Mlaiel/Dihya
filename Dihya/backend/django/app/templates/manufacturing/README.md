# 🏭 Dihya – Manufacturing Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **manufacturing** (production industrielle) de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité industrielle (RGPD, obligations qualité/traçabilité), internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, MES, audit qualité, traçabilité.
- **Sécurité** : Pas de données sensibles, information confidentielle, ou secret industriel, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (opérateur, superviseur, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité manufacturing).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **manufacturing** module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, industrial compliance (GDPR, quality/tracing), i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, MES, quality audit, traceability.
- **Security**: No sensitive data, confidential info, or industrial secrets, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (operator, supervisor, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, manufacturing compliance).
- **Sovereignty**: No calls to non-sovereign external resources, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "التصنيع" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق الصناعي (RGPD)، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، MES، تدقيق الجودة، تتبع الإنتاج.
- **الأمان**: لا بيانات حساسة أو معلومات سرية أو أسرار صناعية، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مشغل، مشرف، مشرف عام، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق صناعي).
- **السيادة**: لا موارد خارجية غير سيادية، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "manufacturing" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n manufacturing, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n manufacturing, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (operator, supervisor, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n manufacturing.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher d’information industrielle confidentielle ou de donnée sensible.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité manufacturing.

---

## 🧩 Exemple de template conforme

```django
{# filepath: manufacturing/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Manufacturing" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme manufacturing souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme manufacturing souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Superviseur" %}</span>
      {% else %}
        <span class="role">{% trans "Opérateur" %}</span>
      {% endif %}
    {% else %}
      <a href="{% url 'login' %}">{% trans "Connexion" %}</a>
    {% endif %}
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
  <footer>
    <small>&copy; 2025 Dihya</small>
    <a href="{% url 'legal_mentions' %}">{% trans "Mentions légales" %}</a>
  </footer>
</body>
</html>
```

---

## 🧪 Tests & CI

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité manufacturing) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_manufacturing
  ```

---

## 🤝 Contribution

- Toute contribution doit respecter la [policy.md](./policy.md).
- Les PRs non conformes sont refusées.
- Multilingue : tout nouveau texte doit être balisé pour la traduction.

---

## 📚 Ressources

- [Django i18n](https://docs.djangoproject.com/fr/stable/topics/i18n/translation/)
- [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres/)
- [CNIL RGPD](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on)
- [Dihya Docs](../../../../docs/)

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité manufacturing, excellence.
