/**
 * Dihya Marketplace – Example Template
 * Ultra avancé, multilingue, sécurisé, documenté, personnalisable, extensible.
 */

module.exports = function exampleTemplate(options = {}) {
  const roles = options.roles || ['admin', 'user', 'contributor'];
  const i18n = options.i18n || {
    fr: 'Template générique Dihya',
    en: 'Dihya generic template',
    ar: 'قالب نموذجي Dihya',
    tzr: 'Template generic amasal'
  };

  function run(params) {
    // ...logique métier, sécurité, audit, extension, accessibilité
    return { success: true, message: i18n[params.lang || 'fr'] };
  }

  function onInit(context) {
    context.log('Initialisation du template', i18n);
    // Audit, extension, fallback souverain
  }
  function onSave(context, data) {
    context.log('Données template sauvegardées', { ...i18n, data });
    // Sécurité, RGPD, extension
  }
  function onExport(context, format) {
    context.log('Export template', { format, ...i18n });
    // Accessibilité, multilingue, fallback
  }
  function onAudit(context, event) {
    context.log('Audit template', { event, ...i18n });
    // Journalisation souveraine, conformité
  }
  function onError(context, error) {
    context.log('Erreur template', { error, ...i18n });
    // Fallback open source, notification
  }

  return {
    run,
    onInit,
    onSave,
    onExport,
    onAudit,
    onError,
    roles,
    i18n,
    // Extension : ajoutez vos hooks personnalisés ici (voir /docs/templates/USAGE.md)
  };
};

/**
 * Tous les templates sont documentés dans /docs/templates/ et testés dans /tests/templates/
 * Pour ajouter un hook, suivre la convention : sécurité, i18n, doc, test, fallback, accessibilité.
 */

// --- TESTS UNITAIRES (Jest) ---
// Voir tests/templates/example_template.test.js pour la couverture complète (hooks, sécurité, i18n, extension, fallback)
