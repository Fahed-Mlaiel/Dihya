"""
Serializers Intelligence Artificielle (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ModeleIASerializer(serializers.ModelSerializer):
    class Meta:
        model = 'ModeleIA'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du modèle / Model name / اسم النموذج / ⵉⵙⴰⵏ ⵏ ⵎⵓⴷⴰⵍ')},
            'type': {'help_text': _('Type (classification, régression, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'version': {'help_text': _('Version / الإصدار / ⵜⴰⵙⵉⵏⵜ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵎⵓⴷⴰⵍ')},
            'proprietaire': {'help_text': _('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ')},
        }
