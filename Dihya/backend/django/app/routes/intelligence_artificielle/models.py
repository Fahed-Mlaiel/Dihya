"""
Modèles Intelligence Artificielle (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class ModeleIA(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du modèle / Model name / اسم النموذج / ⵉⵙⴰⵏ ⵏ ⵎⵓⴷⴰⵍ'))
    type = models.CharField(max_length=100, help_text=_('Type (classification, régression, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    version = models.CharField(max_length=50, help_text=_('Version / الإصدار / ⵜⴰⵙⵉⵏⵜ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵎⵓⴷⴰⵍ'))
    proprietaire = models.CharField(max_length=255, help_text=_('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Modèle IA')
        verbose_name_plural = _('Modèles IA')
