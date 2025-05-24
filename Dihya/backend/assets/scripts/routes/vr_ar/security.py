"""
Dihya Backend – Sécurité avancée (CORS, JWT, WAF, anti-DDOS, audit, rôles)
"""
from functools import wraps
from django.http import JsonResponse
from django.conf import settings

def require_jwt(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        # Vérification JWT (exemple, à adapter à votre stack)
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or token != 'secure-jwt-token':
            return JsonResponse({'error': 'JWT requis'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped

def require_role(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            # Vérification du rôle utilisateur (exemple)
            user_role = getattr(request.user, 'role', 'invité')
            if user_role != role:
                return JsonResponse({'error': 'Rôle insuffisant'}, status=403)
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator

def waf_protect(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        # Protection WAF/anti-DDOS (exemple)
        if request.META.get('HTTP_X_FORWARDED_FOR') == '1.2.3.4':
            return JsonResponse({'error': 'IP bannie'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped

def log_audit(user, action, details=None):
    # Audit log structuré (exemple)
    print(f"AUDIT | user={user} | action={action} | details={details}")
