# __init__.py pour le module voyage
# Permet l'importation des sous-modules (models, serializers, views, permissions, audit, i18n, plugins, templates, tasks, etc.)
# Conforme aux bonnes pratiques Django, facilite l'extension et la modularité.

from .models import *
from .serializers import *
from .views import *
from .permissions import *
from .audit import *
from .i18n import *
