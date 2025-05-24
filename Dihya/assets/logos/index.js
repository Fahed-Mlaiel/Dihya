/**
 * Dihya – Logo Registry
 * Ultra avancé, accessible, multilingue, souverain.
 * Centralise et exporte tous les logos SVG/React du projet pour usage multi-stack (React, Node, mobile, plugins, docs).
 * Prêt pour la production, la démo, la contribution.
 *
 * @module DihyaLogos
 */

// Exemple d'import de logos SVG React (à compléter selon vos assets)
import DihyaBrandmark from './brandmark.svg?react';
import DihyaAmazighLogo from './dihya-amazigh.svg?react';
import DihyaDarkLogo from './dihya-dark.svg?react';
import DihyaLightLogo from './dihya-light.svg?react';
import DihyaMainLogo from './dihya-main.svg?react';
import DihyaMinimalLogo from './dihya-minimal.svg?react';
import DihyaFavicon from './favicon.svg?react';

// Logos multilingues ou thématiques (exemples)
import DihyaArLogo from './dihya-ar.svg?react';
import DihyaEnLogo from './dihya-en.svg?react';
import DihyaFrLogo from './dihya-fr.svg?react';
import DihyaTzrLogo from './dihya-tzr.svg?react';

// Logos métiers ou plugins (exemples)
import EducationLogo from './education.svg?react';
import HealthLogo from './health.svg?react';
import LegalLogo from './legal.svg?react';

// --- LOGOS AVANCÉS, MULTILINGUES, SÉCURISÉS, ACCESSIBLES ---
// Ajout d'exemples de logos métiers, souverains, testés, accessibles, documentés
import BlockchainLogo from './blockchain.svg?react';
import CloudLogo from './cloud.svg?react';
import FinanceLogo from './finance.svg?react';
import IndustryLogo from './industry.svg?react';
import RHLogo from './rh.svg?react';
import SouveraineteLogo from './souverainete.svg?react';
import TestLogo from './test.svg?react';
import ThemeLogo from './theme.svg?react';

// Registre des logos
export const Logos = {
  main: DihyaMainLogo,
  amazigh: DihyaAmazighLogo,
  dark: DihyaDarkLogo,
  light: DihyaLightLogo,
  minimal: DihyaMinimalLogo,
  favicon: DihyaFavicon,
  brandmark: DihyaBrandmark,
  fr: DihyaFrLogo,
  en: DihyaEnLogo,
  ar: DihyaArLogo,
  tzr: DihyaTzrLogo,
  legal: LegalLogo,
  health: HealthLogo,
  education: EducationLogo,
  blockchain: BlockchainLogo,
  cloud: CloudLogo,
  finance: FinanceLogo,
  industry: IndustryLogo,
  rh: RHLogo,
  souverainete: SouveraineteLogo,
  theme: ThemeLogo,
  test: TestLogo
};

/**
 * Utilisation (React) :
 * import { Logos } from 'assets/logos';
 * <Logos.main aria-label="Logo Dihya" role="img" />
 *
 * Accessibilité : chaque logo doit avoir un aria-label pertinent et être utilisable au clavier.
 * Multilingue : utilisez aria-label dynamique selon la langue de l'utilisateur.
 *
 * Tous les logos sont documentés dans /docs/assets/logos.md et testés dans /tests/assets/logos.test.js
 * Accessibilité : aria-label, role="img", focusable, contrastes, multilingue.
 * Pour ajouter un logo, suivre la convention : SVG optimisé, nom explicite, doc, test, fallback.
 * Exemples d'intégration dans React, Node, mobile, plugins, docs fournis dans /docs/assets/USAGE.md
 */

// --- TESTS UNITAIRES (Jest) ---
// Voir tests/assets/logos.test.js pour la couverture complète (import, accessibilité, fallback, i18n, conformité)

export default Logos;
