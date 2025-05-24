"""
Dihya Backend – Module routes.vr_ar
Initialisation du module, chargement dynamique des plugins, configuration i18n, sécurité, audit, RGPD.
"""
from .views import *
from .schemas import *
from .urls import urlpatterns
from .plugins import *

__all__ = ["urlpatterns"]
