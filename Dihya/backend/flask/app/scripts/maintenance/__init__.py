"""
Initialisation du module de scripts de maintenance pour Dihya Coding.

Ce package regroupe les scripts d’automatisation pour la maintenance régulière du backend :
purge de logs, rotation des backups, nettoyage des données temporaires, vérification de l’intégrité, etc.

Bonnes pratiques :
- Documenter chaque script de maintenance (usage, fréquence, sécurité)
- Ne jamais supprimer de données critiques sans sauvegarde préalable
- Prévoir l’extensibilité pour de nouveaux scripts ou tâches planifiées
- Valider les entrées/sorties pour éviter les erreurs destructrices
- Journaliser chaque opération de maintenance pour auditabilité
"""