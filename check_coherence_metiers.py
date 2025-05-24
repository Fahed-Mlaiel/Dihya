"""
check_coherence_metiers.py – Dihya Coding
Script ultra avancé pour l’audit de cohérence multi-stack des métiers/templates/modules.
- Vérifie la présence de chaque métier dans toutes les stacks (backend Django/Node, frontend, docs, policies, tests…)
- Détecte les doublons, incohérences de nommage, oublis de tests, manques de documentation, etc.
- Compatible CI/CD, Codespaces, audit RGPD, multilingue, souveraineté numérique.
- Sortie claire, multilingue, accessible, prête à l’emploi pour contribution ou audit.
"""

import os
import re

def list_metiers_templates(base_path, ext):
    """Liste les métiers ayant un template backend (Django/Node)"""
    metiers = set()
    if not os.path.isdir(base_path):
        return metiers
    for name in os.listdir(base_path):
        path = os.path.join(base_path, name)
        if os.path.isdir(path) and name not in ("README.md", "__pycache__"):
            if os.path.isfile(os.path.join(path, f"template.{ext}")):
                metiers.add(name)
    return metiers

def list_metiers_docs(docs_path):
    """Liste les métiers documentés (backend/docs/metiers)"""
    metiers = set()
    if not os.path.isdir(docs_path):
        return metiers
    for name in os.listdir(docs_path):
        if name.endswith(".md") and name != "README.md":
            metiers.add(name.replace(".md", ""))
    return metiers

def list_metiers_policies(policies_path):
    """Liste les métiers ayant une policy sécurité"""
    metiers = set()
    if not os.path.isdir(policies_path):
        return metiers
    for name in os.listdir(policies_path):
        if name.endswith("_policy.md"):
            metiers.add(name.replace("_policy.md", ""))
    return metiers

def list_metiers_tests(tests_path, ext):
    """Liste les métiers ayant des tests (unit/integration/e2e)"""
    metiers = set()
    if not os.path.isdir(tests_path):
        return metiers
    for name in os.listdir(tests_path):
        path = os.path.join(tests_path, name)
        if os.path.isdir(path):
            for f in os.listdir(path):
                if f.startswith("test_") and f.endswith(f".{ext}"):
                    metier = f.replace("test_", "").replace(f".{ext}", "")
                    metiers.add(metier)
    return metiers

def list_metiers_frontend_templates(base_path):
    """Liste les métiers ayant un template frontend (React/Vue)"""
    metiers = set()
    if not os.path.isdir(base_path):
        return metiers
    for name in os.listdir(base_path):
        path = os.path.join(base_path, name)
        if os.path.isdir(path) and name != "README.md":
            if os.path.isfile(os.path.join(path, "template.js")):
                metiers.add(name)
    return metiers

def list_metiers_frontend_docs(docs_path):
    """Liste les métiers ayant une doc frontend (Card.md)"""
    metiers = set()
    if not os.path.isdir(docs_path):
        return metiers
    for name in os.listdir(docs_path):
        if name.endswith("Card.md"):
            base = name.replace("Card.md", "")
            metiers.add(base)
    return metiers

def normalize(metier):
    """Normalise le nom d’un métier pour comparaison (case, accents, tirets, underscores)"""
    return re.sub(r'[^a-z0-9]', '', metier.lower())

# Chemins à adapter selon la structure réelle du projet
django_tpl = "Dihya/backend/django/app/templates"
node_tpl = "Dihya/backend/node/app/templates"
frontend_tpl = "Dihya/frontend/src/generation/templates"
docs_backend = "docs/metiers"
docs_frontend = "Dihya/frontend/src/metiers_docs"
policies = "Dihya/securite/policies/metiers"
tests_django = "Dihya/backend/django/app/tests/integration"
tests_node = "Dihya/backend/node/app/tests/integration"
tests_frontend = "Dihya/frontend/src/tests/integration"

django_metiers = list_metiers_templates(django_tpl, "py")
node_metiers = list_metiers_templates(node_tpl, "js")
frontend_metiers = list_metiers_frontend_templates(frontend_tpl)
docs_metiers = list_metiers_docs(docs_backend)
docs_cards = list_metiers_frontend_docs(docs_frontend)
policies_metiers = list_metiers_policies(policies)
tests_django_metiers = list_metiers_tests(tests_django, "py")
tests_node_metiers = list_metiers_tests(tests_node, "js")
tests_frontend_metiers = list_metiers_tests(tests_frontend, "js")

all_metiers = django_metiers | node_metiers | frontend_metiers | docs_metiers | docs_cards

def find_missing(ref, *others):
    """Détecte les métiers présents dans ref mais absents dans les autres stacks"""
    missing = {}
    for m in ref:
        nm = normalize(m)
        for o in others:
            if nm not in {normalize(x) for x in o}:
                missing.setdefault(m, []).append(o)
    return missing

def print_missing(title, missing):
    """Affiche les métiers manquants dans chaque stack"""
    if missing:
        print(f"--- {title} ---")
        for m, stacks in missing.items():
            print(f"  {m}")
        print()
    else:
        print(f"--- {title} : OK ---\n")

print("=== Vérification de cohérence métiers multi-stack (Dihya Coding) ===\n")

missing_in_node = find_missing(django_metiers, node_metiers)
missing_in_frontend = find_missing(django_metiers, frontend_metiers)
missing_in_docs = find_missing(django_metiers, docs_metiers)
missing_in_cards = find_missing(django_metiers, docs_cards)
missing_in_policies = find_missing(django_metiers, policies_metiers)
missing_test_django = find_missing(django_metiers, tests_django_metiers)
missing_test_node = find_missing(node_metiers, tests_node_metiers)
missing_test_frontend = find_missing(frontend_metiers, tests_frontend_metiers)

print_missing("Métiers Django absents dans Node", missing_in_node)
print_missing("Métiers Django absents dans Frontend", missing_in_frontend)
print_missing("Métiers Django absents dans Docs backend", missing_in_docs)
print_missing("Métiers Django absents dans Docs frontend (Card)", missing_in_cards)
print_missing("Métiers Django absents dans Policies", missing_in_policies)
print_missing("Métiers Django sans test Django", missing_test_django)
print_missing("Métiers Node sans test Node", missing_test_node)
print_missing("Métiers Frontend sans test Frontend", missing_test_frontend)

print("--- Doublons de nommage potentiels (CamelCase vs underscore) ---")
all_metiers_list = list(all_metiers)
for i, m in enumerate(all_metiers_list):
    for n in all_metiers_list[i+1:]:
        if normalize(m) == normalize(n) and m != n:
            print(f"  {m} <-> {n}")
print()

print("=== Vérification terminée ===")
