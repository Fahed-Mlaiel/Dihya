"""
Gestion des modèles IA open source de fallback pour Dihya Coding.

Ce module permet d’intégrer et d’orchestrer des modèles open source (Mixtral, LLaMA, Mistral, etc.)
en cas de quota dépassé ou d’indisponibilité des API propriétaires (OpenAI, etc.).

Bonnes pratiques :
- Ne jamais exposer de prompts ou de données sensibles dans les logs ou erreurs.
- Logger chaque appel à un modèle fallback avec horodatage, utilisateur, type de génération et statut.
- Prévoir une validation stricte des entrées et sorties.
- Modulariser chaque wrapper de modèle pour faciliter l’ajout ou la mise à jour.
- Documenter chaque modèle supporté et ses limitations.

Exemple d’utilisation :
    from app.ai_fallback.models import generate_with_fallback
    code, preview_url = generate_with_fallback("Créer une todo app", "webapp", "react+flask")
"""

from datetime import datetime

def log_fallback_call(user, model, status, details=""):
    """
    Logge chaque appel à un modèle IA fallback.
    """
    log_file = "logs/ai_fallback.log"
    entry = f"{datetime.utcnow().isoformat()} | user={user} | model={model} | status={status} | {details}"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass

def generate_with_mixtral(prompt, project_type, stack):
    """
    Génère du code avec Mixtral (exemple fictif).
    """
    # TODO: Intégrer l’appel réel au modèle Mixtral local ou API
    code = f"# Code généré par Mixtral pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/mixtral_demo"
    return code, preview_url

def generate_with_llama(prompt, project_type, stack):
    """
    Génère du code avec LLaMA (exemple fictif).
    """
    # TODO: Intégrer l’appel réel au modèle LLaMA local ou API
    code = f"# Code généré par LLaMA pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/llama_demo"
    return code, preview_url

def generate_with_mistral(prompt, project_type, stack):
    """
    Génère du code avec Mistral (exemple fictif).
    """
    # TODO: Intégrer l’appel réel au modèle Mistral local ou API
    code = f"# Code généré par Mistral pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/mistral_demo"
    return code, preview_url

def generate_with_fallback(prompt, project_type, stack, user="anonymous"):
    """
    Orchestration : tente chaque modèle open source jusqu’à succès.
    :return: (code, preview_url)
    """
    for model_func, model_name in [
        (generate_with_mixtral, "Mixtral"),
        (generate_with_llama, "LLaMA"),
        (generate_with_mistral, "Mistral"),
    ]:
        try:
            code, preview_url = model_func(prompt, project_type, stack)
            log_fallback_call(user, model_name, "SUCCESS")
            return code, preview_url
        except Exception as e:
            log_fallback_call(user, model_name, "FAIL", str(e))
    # Si aucun modèle ne fonctionne
    return "# Erreur : aucun modèle fallback disponible.", ""