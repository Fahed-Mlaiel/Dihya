# 🧪 Dihya – Tests d’Intégration 3D

---

## 🇫🇷 Présentation

Ce dossier contient les **tests d’intégration avancés** pour la gestion 3D (assets, scènes, interactions immersives) sur la plateforme Dihya.
Il garantit la robustesse, la sécurité, la compatibilité multi-stack (Django, React, Node, Unity, Flutter…), l’accessibilité et la souveraineté numérique des fonctionnalités 3D.

---

## 🚀 Ce qui est testé

- **Import/export d’assets 3D** (GLB, OBJ, FBX…)
- **Chargement et rendu de scènes immersives**
- **Interactions utilisateur** (vocales, gestuelles, multi-utilisateur)
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/3D
- **Accessibilité** : navigation clavier, ARIA, fallback audio/texte
- **Compatibilité** : web, mobile, Unity, PWA
- **Fallback IA open source** pour la validation ou la correction d’assets/scènes

---

## 🛠️ Exemple de test d’intégration (Pytest + Selenium)

```python
import pytest
from selenium import webdriver

def test_3d_scene_loads():
    driver = webdriver.Firefox()
    driver.get("http://localhost:8000/vr_ar/scene/test/")
    assert "VR/AR" in driver.title
    canvas = driver.find_element("id", "vr-ar-canvas")
    assert canvas.is_displayed()
    driver.quit()
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests d’intégration 3D, sécurité, accessibilité
- **English**: 3D integration tests, security, accessibility
- **العربية**: اختبارات تكامل ثلاثية الأبعاد، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ 3D ⴷ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🧩 Structure recommandée

- `test_assets.py` : tests d’import/export et validation d’assets 3D
- `test_scene.py` : tests de chargement/rendu de scènes immersives
- `test_interactions.py` : tests d’interactions vocales, gestuelles, multi-utilisateur
- `test_accessibility.py` : tests d’accessibilité 3D (clavier, ARIA, fallback)
- `test_security.py` : tests de sécurité et conformité RGPD/3D

---

## 🧪 Lancer les tests

```bash
pytest .
```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des fonctionnalités 3D de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
