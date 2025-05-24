// Test Node.js/Jest pour valider l’import et l’accessibilité des logos Dihya
const fs = require('fs');
const path = require('path');

describe('Dihya Logos SVG', () => {
  const logos = [
    'dihya-main','dihya-amazigh','dihya-dark','dihya-light','dihya-minimal','brandmark','favicon','dihya-ar','dihya-en','dihya-fr','dihya-tzr','education','health','legal','blockchain','cloud','finance','industry','rh','souverainete','theme','test'
  ];
  logos.forEach(logo => {
    it(`${logo}.svg doit exister et être accessible`, () => {
      const file = path.join(__dirname, `${logo}.svg`);
      expect(fs.existsSync(file)).toBe(true);
      const svg = fs.readFileSync(file, 'utf8');
      expect(svg).toMatch(/<svg/);
      expect(svg).toMatch(/aria-label/);
      expect(svg).toMatch(/role="img"/);
      expect(svg).toMatch(/focusable="false"/);
    });
  });
});
