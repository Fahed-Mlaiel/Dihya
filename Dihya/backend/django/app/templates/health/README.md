# 🩺 Dihya – Health Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **health** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, internationalisation, SEO, modularité, et souveraineté numérique.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs.
- **Sécurité** : Pas de données de santé ou personnelles, pas de scripts inline, conformité RGPD/secret médical.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (médecin, patient, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines.

---

## 🇬🇧 Overview

This folder contains the **health** module HTML templates for Dihya.
Designed for : security, accessibility, privacy, i18n, SEO, modularity, and digital sovereignty.

- **Stack compatible**: Django, Jinja2, alternative engines.
- **Security**: No health or personal data, no inline scripts, GDPR/medical secrecy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (doctor, patient, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering).
- **Sovereignty**: No calls to non-sovereign external resources.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "health" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، التعدد اللغوي، تحسين محركات البحث، السيادة الرقمية.

- **التوافق**: Django، Jinja2، محركات أخرى.
- **الأمان**: لا بيانات صحية أو شخصية، لا سكريبتات داخلية، متوافق مع GDPR/سرية طبية.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (طبيب، مريض، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض).
- **السيادة**: لا موارد خارجية غير سيادية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "health" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka n wawal n tneɣruft neɣ n wudem, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (asqelmed, amuddu, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de données sensibles ou médicales.
- Pour chaque nouveau template, ajoutez un test d’accessibilité et de rendu.

---

## 🧩 Exemple de template conforme

```django
{# filepath: health/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Santé" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme santé souveraine' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue patient" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Médecin" %}</span>
      {% else %}
        <span class="role">{% trans "Patient" %}</span>
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
  </footer>
</body>
</html>
```

---

## 🧪 Tests & CI

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_health
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
- [Dihya Docs](../../../../docs/)

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, excellence.
