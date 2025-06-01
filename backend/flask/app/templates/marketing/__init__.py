"""
Module d'API pour la gestion avancée des projets marketing.
Sécurité, i18n, audit, plugins, conformité RGPD, multitenancy, SEO.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_babel import _
from .utils import validate_project_payload, role_required, log_audit_event
from .plugins import run_plugin_hooks
from .i18n import get_locale

bp = Blueprint('marketing', __name__, url_prefix='/api/marketing')
bp_marketing = bp

@bp.route('/projects', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user'])
def list_projects():
    tenant = get_jwt_identity().get('tenant')
    projects = current_app.db.get_marketing_projects(tenant=tenant)
    log_audit_event('list_marketing_projects', tenant=tenant)
    return jsonify({'projects': projects, 'msg': _('Liste des projets marketing')})

@bp.route('/projects', methods=['POST'])
@jwt_required()
@role_required(['admin'])
def create_project():
    data = request.json
    validate_project_payload(data)
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.create_marketing_project(data, tenant=tenant)
    run_plugin_hooks('after_create_marketing_project', project)
    log_audit_event('create_marketing_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet marketing créé')}), 201

@bp.route('/projects/<project_id>', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invité'])
def get_project(project_id):
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.get_marketing_project(project_id, tenant=tenant)
    log_audit_event('get_marketing_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet marketing récupéré')})

# SEO, robots, sitemap
@bp.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /api/", 200, {'Content-Type': 'text/plain'}

@bp.route('/sitemap.xml')
def sitemap():
    return current_app.generate_sitemap('marketing'), 200, {'Content-Type': 'application/xml'}

__all__ = ["bp", "bp_marketing"]
