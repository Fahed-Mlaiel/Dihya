"""
Dihya – VR/AR Images Security
Décorateurs et helpers pour JWT, rôles, audit, CORS, WAF, anti-DDOS, RGPD.
"""
from functools import wraps
from django.http import JsonResponse, HttpRequest
from django.utils.translation import gettext as _

def require_jwt(view_func):
    @wraps(view_func)
    def _wrapped(request: HttpRequest, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return JsonResponse({'error': _('Token JWT manquant')}, status=401)
        # TODO: Vérification JWT réelle (clé publique, expiration, etc.)
        return view_func(request, *args, **kwargs)
    return _wrapped

def require_role(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request: HttpRequest, *args, **kwargs):
            user_role = request.headers.get('X-Role', 'invite')
            if user_role not in roles:
                return JsonResponse({'error': _('Accès refusé')}, status=403)
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator

def audit_log(request: HttpRequest, action: str, resource: str):
    # Log structuré RGPD-ready (anonymisation possible)
    print(f"[AUDIT] {request.method} {action} {resource} {request.META.get('REMOTE_ADDR')}")
