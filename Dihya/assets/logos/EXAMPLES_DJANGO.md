# Dihya Logos – Exemples Django

```python
from django.http import FileResponse
from Dihya.assets.logos.meta_logos import get_logo_path

def logo_file_view(request, logo):
    """Endpoint sécurisé, RGPD, multilingue, audit, accessibilité."""
    path = get_logo_path(logo)
    return FileResponse(open(path, 'rb'), as_attachment=True)
```
