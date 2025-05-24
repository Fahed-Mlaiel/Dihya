/**
 * Dihya – Icon Registry
 * Ultra avancé, accessible, multilingue, souverain.
 * Centralise et exporte tous les icônes SVG/React du projet pour usage multi-stack (React, Node, mobile, plugins).
 * Prêt pour la production, la démo, la contribution.
 *
 * @module DihyaIcons
 */

// index.js – Dihya Icons Entrypoint

// Point d’entrée pour l’import/export des icônes
// Exemples d’utilisation, conventions, scripts d’automatisation

// Exemple d'import d'icônes SVG React (à compléter selon vos assets)
import AccessibilityIcon from './accessibility.svg?react';
import AdminIcon from './admin.svg?react';
import DihyaLogo from './dihya-logo.svg?react';
import LanguageArIcon from './lang-ar.svg?react';
import LanguageEnIcon from './lang-en.svg?react';
import LanguageFrIcon from './lang-fr.svg?react';
import LanguageTzrIcon from './lang-tzr.svg?react';
import PluginIcon from './plugin.svg?react';
import SecurityIcon from './security.svg?react';
import TemplateIcon from './template.svg?react';
import UserIcon from './user.svg?react';

// --- ICÔNES AVANCÉES, MULTILINGUES, ACCESSIBLES, SÉCURISÉES ---
// Ajout d'exemples d'icônes métiers, souverains, testés, accessibles, documentés
import AuditIcon from './audit.svg?react';
import BlockchainIcon from './blockchain.svg?react';
import CloudIcon from './cloud.svg?react';
import FinanceIcon from './finance.svg?react';
import HealthIcon from './health.svg?react';
import IndustryIcon from './industry.svg?react';
import RHIcon from './rh.svg?react';
import SouveraineteIcon from './souverainete.svg?react';
import TestIcon from './test.svg?react';
import ThemeIcon from './theme.svg?react';

// Icônes accessibles, multilingues, prêtes à l'emploi
export const Icons = {
  dihya: DihyaLogo,
  user: UserIcon,
  admin: AdminIcon,
  langFr: LanguageFrIcon,
  langEn: LanguageEnIcon,
  langAr: LanguageArIcon,
  langTzr: LanguageTzrIcon,
  accessibility: AccessibilityIcon,
  security: SecurityIcon,
  plugin: PluginIcon,
  template: TemplateIcon,
  // Ajoutez ici vos nouveaux icônes métiers ou personnalisés
  audit: AuditIcon,
  blockchain: BlockchainIcon,
  cloud: CloudIcon,
  finance: FinanceIcon,
  health: HealthIcon,
  industry: IndustryIcon,
  rh: RHIcon,
  souverainete: SouveraineteIcon,
  theme: ThemeIcon,
  test: TestIcon
};

/**
 * Utilisation (React) :
 * import { Icons } from 'assets/icons';
 * <Icons.dihya aria-label="Logo Dihya" role="img" />
 *
 * Accessibilité : chaque icône doit avoir un aria-label pertinent et être utilisable au clavier.
 * Multilingue : utilisez aria-label dynamique selon la langue de l'utilisateur.
 */

/**
 * Tous les icônes sont documentés dans /docs/assets/icons.md et testés dans /tests/assets/icons.test.js
 * Accessibilité : aria-label, role="img", focusable, contrastes, multilingue.
 * Pour ajouter un icône, suivre la convention : SVG optimisé, nom explicite, doc, test, fallback.
 * Exemples d'intégration dans React, Node, mobile, plugins, docs fournis dans /docs/assets/USAGE.md
 */

// --- TESTS UNITAIRES (Jest) ---
// Voir tests/assets/icons.test.js pour la couverture complète (import, accessibilité, fallback, i18n, conformité)

export default Icons;
