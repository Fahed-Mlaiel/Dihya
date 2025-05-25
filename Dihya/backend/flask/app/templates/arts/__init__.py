"""
Module Arts pour Dihya Coding
Gestion avancée des événements, galeries, portfolios, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_arts_routes, bp_arts

register_arts_routes(bp_arts)

__all__ = ["bp_arts"]
