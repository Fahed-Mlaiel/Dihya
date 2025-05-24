# Dihya Logos – Exemples Plugins

## Ajout d’un plugin Node.js pour audit accessibilité
```js
// plugin_a11y_audit.js déjà fourni
node plugin_a11y_audit.js
```

## Ajout d’un plugin Python pour export RGPD
```python
# plugin_rgpd_export.py (exemple)
from meta_logos import meta_logos
import json
with open('meta_logos_export.json', 'w', encoding='utf-8') as f:
    json.dump(meta_logos, f, ensure_ascii=False, indent=2)
```
