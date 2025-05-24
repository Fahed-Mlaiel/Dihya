# Dihya Logos – Exemples Fallback/Legacy

## Utilisation PNG/ICO pour legacy
```html
<img src="dihya-main.png" alt="Logo Dihya" />
<link rel="icon" type="image/x-icon" href="dihya-main.ico" />
```

## Fallback Node.js
```js
app.get('/logos/:logo', (req, res) => {
  const logo = req.params.logo;
  if (fs.existsSync(`${logo}.svg`)) {
    res.sendFile(`${logo}.svg`);
  } else if (fs.existsSync(`${logo}.png`)) {
    res.sendFile(`${logo}.png`);
  } else {
    res.status(404).json({ error: 'Logo not found' });
  }
});
```
