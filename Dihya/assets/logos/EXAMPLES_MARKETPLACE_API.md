# Dihya Logos – Exemple API marketplace

## Publication d’un logo via API REST
```http
POST /api/marketplace/logos
Content-Type: application/json
{
  "name": "Logo Dihya Cloud",
  "description": {"fr": "Logo cloud pour Dihya."},
  "file": "cloud.svg",
  "author": "Dihya Community",
  "license": "MIT"
}
```

## Publication d’un plugin via API REST
```http
POST /api/marketplace/plugins
Content-Type: application/json
{
  "name": "logo-optimizer",
  "file": "plugin_svg_optimizer.js"
}
```
