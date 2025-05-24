# Dihya Logos – Exemple intégration marketplace frontend

## React – Affichage d’un logo publié sur la marketplace
```jsx
import { useEffect, useState } from 'react';

function MarketplaceLogo({ logoName }) {
  const [svg, setSvg] = useState('');
  useEffect(() => {
    fetch(`/api/marketplace/logos/${logoName}.svg`)
      .then(res => res.text())
      .then(setSvg);
  }, [logoName]);
  return <span dangerouslySetInnerHTML={{ __html: svg }} />;
}

// <MarketplaceLogo logoName="cloud" />
```
