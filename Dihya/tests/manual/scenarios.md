# 📋 Dihya – Scénarios de Tests Manuels

## Structure d’un scénario
- **ID**
- **Titre**
- **Langue**
- **Métier**
- **Pré-requis**
- **Étapes**
- **Résultat attendu**
- **Sécurité/Accessibilité**
- **Conformité**

---

## Exemples

### ID: MAN-001
**Titre** : Connexion multilingue (fr, en, ar, tzr)
**Langue** : fr, en, ar, tzr
**Métier** : Tous
**Pré-requis** : Compte utilisateur valide
**Étapes** :
1. Aller sur la page de connexion
2. Sélectionner chaque langue
3. Saisir identifiants valides
4. Valider
**Résultat attendu** : Connexion réussie, interface dans la langue choisie
**Sécurité/Accessibilité** : Pas de fuite de données, navigation clavier OK
**Conformité** : RGPD, souveraineté OK

---

### ID: MAN-002
**Titre** : Parcours utilisateur – Création de compte (tous métiers)
**Langue** : fr, en, ar, tzr
**Métier** : Tous
**Pré-requis** : Aucun
**Étapes** :
1. Aller sur la page d’inscription
2. Remplir le formulaire dans chaque langue
3. Valider
**Résultat attendu** : Compte créé, email de bienvenue reçu dans la bonne langue
**Sécurité/Accessibilité** : Pas de XSS, alt/aria-label présents
**Conformité** : RGPD, accessibilité OK

---

### ID: MAN-003
**Titre** : Test accessibilité – Navigation clavier sur dashboard
**Langue** : fr, en, ar, tzr
**Métier** : Tous
**Pré-requis** : Compte utilisateur
**Étapes** :
1. Se connecter
2. Naviguer sur le dashboard uniquement au clavier
**Résultat attendu** : Toutes les fonctionnalités accessibles au clavier
**Sécurité/Accessibilité** : Focus visible, ARIA, pas de piège clavier
**Conformité** : WCAG 2.1 AA
