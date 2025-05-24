"""
Dihya – Tâches asynchrones pour Tourisme
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_client(reservation_id, message):
    # TODO: Envoyer notification (mail, push) au client
    pass

@shared_task
def tache_rapport_reservations():
    # TODO: Générer rapport PDF/CSV des réservations
    pass
