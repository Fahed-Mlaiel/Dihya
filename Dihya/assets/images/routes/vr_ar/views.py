"""
Dihya – VR/AR Images Views
Gestion ultra avancée des endpoints images IA, VR, AR (REST, GraphQL, multilingue, sécurité, plugins, RGPD).
"""
from typing import Any, Dict
from django.http import JsonResponse, HttpRequest, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext as _
from .schemas import VRARImageSchema
from .security import require_jwt, require_role, audit_log
from .plugins import run_plugins
import os

@csrf_exempt
@require_jwt
@require_role(['admin', 'user'])
def upload_vrar_image(request: HttpRequest) -> HttpResponse:
    """Upload d’une image IA/VR/AR, validation, audit, RGPD, plugins."""
    if request.method != 'POST':
        return JsonResponse({'error': _('Méthode non autorisée')}, status=405)
    image = request.FILES.get('image')
    if not image:
        return JsonResponse({'error': _('Aucun fichier envoyé')}, status=400)
    # Validation avancée (taille, format, sécurité)
    if image.size > 10*1024*1024:
        return JsonResponse({'error': _('Fichier trop volumineux')}, status=413)
    if not image.name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg')):
        return JsonResponse({'error': _('Format non supporté')}, status=415)
    # Stockage sécurisé
    dest = os.path.join('uploads/vr_ar/', image.name)
    with open(dest, 'wb+') as f:
        for chunk in image.chunks():
            f.write(chunk)
    # Audit, plugins, RGPD
    audit_log(request, action='upload', resource=image.name)
    run_plugins('post_upload', image_path=dest)
    return JsonResponse({'success': True, 'filename': image.name, 'message': _('Image uploadée avec succès')})

@require_jwt
@require_role(['admin', 'user', 'invite'])
def list_vrar_images(request: HttpRequest) -> HttpResponse:
    """Liste des images IA/VR/AR disponibles (REST, multilingue, audit, RGPD)."""
    files = os.listdir('uploads/vr_ar/')
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg'))]
    audit_log(request, action='list', resource='vr_ar_images')
    return JsonResponse({'images': images})

@require_jwt
@require_role(['admin', 'user', 'invite'])
def get_vrar_image(request: HttpRequest, filename: str) -> HttpResponse:
    """Téléchargement sécurisé d’une image IA/VR/AR (REST, RGPD, audit, plugins)."""
    path = os.path.join('uploads/vr_ar/', filename)
    if not os.path.exists(path):
        return JsonResponse({'error': _('Fichier non trouvé')}, status=404)
    audit_log(request, action='download', resource=filename)
    run_plugins('pre_download', image_path=path)
    return FileResponse(open(path, 'rb'), as_attachment=True)
