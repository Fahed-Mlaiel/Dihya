# Dihya Logos – Exemples RBAC (Rôles & Permissions)

## Exemple de contrôle d’accès Node.js
```js
app.use((req, res, next) => {
  const role = req.headers['x-role'] || 'invite';
  if (role !== 'admin' && req.path.startsWith('/logos/')) {
    return res.status(403).json({ error: 'Accès refusé' });
  }
  next();
});
```

## Exemple Django
```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def logo_file_view(request, logo):
    ...
```
