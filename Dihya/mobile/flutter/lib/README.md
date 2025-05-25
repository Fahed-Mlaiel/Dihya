# Dihya Mobile Flutter

## Présentation

Ce dossier contient le socle mobile Flutter du projet Dihya Coding, prêt à l’emploi, multilingue, sécurisé, modulaire, et extensible pour la gestion de projets IA, VR, AR, etc.

## Fonctionnalités principales
- Authentification JWT, gestion des rôles (admin, user, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Sécurité avancée (CORS, validation, audit, RGPD)
- Intégration API REST/GraphQL Dihya
- Génération automatique de projets web/mobile/scripts IA
- Système de plugins mobile
- Accessibilité et performance
- Prêt pour déploiement CI/CD, Docker, K8s, GitHub Actions

## Structure recommandée

```
lib/
  main.dart
  l10n/
    intl_fr.arb
    intl_en.arb
    ...
  models/
  services/
  screens/
  widgets/
  plugins/
  utils/
```

## Exemple d’initialisation

```dart
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'l10n/l10n.dart';

void main() => runApp(DihyaApp());

class DihyaApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dihya Coding',
      localizationsDelegates: [
        ...AppLocalizations.localizationsDelegates,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: AppLocalizations.supportedLocales,
      home: HomeScreen(),
    );
  }
}
```

## Sécurité & RGPD
- Toutes les données sensibles sont chiffrées localement
- Audit log et anonymisation intégrés
- Export des données utilisateur sur demande

## Tests
- Couverture unitaire et intégration via `flutter test`
- Mock API, fixtures, e2e

## Déploiement
- Compatible GitHub Actions, Docker, K8s, Codespaces

## Contribution
- Voir [CONTRIBUTING.md](../../../CONTRIBUTING.md)

---

# Dihya Mobile Flutter

## Overview (English)

This folder contains the advanced, production-ready Flutter mobile stack for Dihya Coding, with full i18n, security, modularity, and plugin support.

See above for features, structure, and usage.
