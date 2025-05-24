"""
Dihya – Tâches asynchrones pour Social
- Notifications, IA, génération de rapports, modération
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_profil(profil_id, message):
    # TODO: Envoyer notification (mail, push) au profil
    pass

@shared_task
def tache_rapport_posts():
    # TODO: Générer rapport PDF/CSV des posts
    pass
