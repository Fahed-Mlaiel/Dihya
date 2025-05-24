# Dihya Logos – Exemples I18N (Internationalisation)

## React
```jsx
<Logos.main aria-label={i18n.t('logo.dihya')} role="img" />
```

## Django
```python
from django.utils.translation import gettext as _
label = _("Logo Dihya")
```

## Node.js
```js
const labels = { fr: 'Logo Dihya', en: 'Dihya logo', ar: 'شعار ديهيا', tzm: 'Agan Dihya' };
const lang = req.query.lang || 'fr';
res.setHeader('Content-Language', lang);
res.send(`<svg aria-label="${labels[lang]}" ...`);
```
