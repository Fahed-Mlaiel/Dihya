"""
Dihya – Tâches asynchrones pour Services à la Personne
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_beneficiaire(b_id, message):
    # TODO: Envoyer notification (mail, SMS, push) au bénéficiaire
    pass

@shared_task
def tache_rapport_prestations():
    # TODO: Générer rapport PDF/CSV des prestations
    pass
