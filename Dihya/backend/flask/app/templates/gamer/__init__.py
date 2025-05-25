"""
Module Gamer - Gestion avancée des projets IA, VR, AR dans le secteur du gaming.
Sécurité, i18n, multitenancy, plugins, auditabilité RGPD.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_babel import _
from .policy import GAMER_POLICIES
from ...utils.security import role_required, validate_payload, waf_protect
from ...utils.audit import audit_log
from ...utils.i18n import get_locale
from ...utils.plugins import plugin_hook
from ...utils.ia import ia_fallback

gamer_bp = Blueprint('gamer', __name__, url_prefix='/api/gamer')

@gamer_bp.before_request
def before():
    waf_protect(request)
    audit_log(request, module='gamer')

@gamer_bp.route('/', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invite'])
def list_projects():
    locale = get_locale()
    projects = plugin_hook('gamer_list_projects', default=[{"id": 1, "name": _(u"Projet Gamer Démo", locale=locale)}])
    return jsonify(projects)

@gamer_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin'])
@validate_payload(['name', 'description'])
def create_project():
    data = request.json
    result = plugin_hook('gamer_create_project', default=data)
    if not result:
        result = ia_fallback('gamer', data)
    return jsonify(result), 201
