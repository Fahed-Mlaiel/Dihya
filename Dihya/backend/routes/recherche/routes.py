"""
Routes pour la gestion avancée de la recherche (IA, VR, AR, etc.)
RESTful + GraphQL, sécurité maximale, multilingue, multitenant, plugins, audit, RGPD.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.seo import seo_log
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/recherche", tags=["Recherche"])

@router.get("/projects", summary="Lister les projets de recherche", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
@seo_log
async def list_projects(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les projets de recherche (IA, VR, AR, etc.) pour le tenant courant.
    """
    # Appel plugin (ex: enrichissement IA)
    projects = plugin_hook("recherche_list_projects", tenant=tenant, user=user, locale=locale) or []
    return projects

@router.post("/projects", summary="Créer un projet de recherche", response_model=Dict[str, Any])
@require_role(["admin", "user"])
@waf_protect
@validate_jwt
@audit_log
async def create_project(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Crée un nouveau projet de recherche avec fallback IA si besoin.
    """
    # Validation RGPD, audit, etc.
    project = plugin_hook("recherche_create_project", data=data, tenant=tenant, user=user, locale=locale)
    if not project:
        project = ai_fallback("create_project", data)
    return project

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")
