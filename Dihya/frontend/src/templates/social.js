/**
 * @file social.js
 * @description Template social pour Dihya Coding : génération de profils, posts, fil d’actualité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère une page de profil utilisateur social.
 * @param {object} user - Données utilisateur { id, username, bio, avatar, followers }
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateProfilePage(user, options = {}) {
  if (!validateUser(user)) return '<!-- Profil invalide -->';
  if (options.log !== false && hasConsent()) {
    logSocialEvent('generate_profile_page', {
      userId: anonymizeId(user.id),
      timestamp: new Date().toISOString()
    });
  }
  return `
    <section class="profile" itemscope itemtype="http://schema.org/Person">
      <img src="${sanitize(user.avatar)}" alt="Avatar de ${sanitize(user.username)}" itemprop="image" />
      <h1 itemprop="name">${sanitize(user.username)}</h1>
      <p itemprop="description">${sanitize(user.bio)}</p>
      <span class="followers">${sanitize(user.followers)} abonnés</span>
    </section>
  `;
}

/**
 * Génère un fil d’actualité social.
 * @param {Array} posts - Liste des posts [{ id, author, content, date }]
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateFeed(posts, options = {}) {
  if (!Array.isArray(posts)) return '<!-- Fil invalide -->';
  if (options.log !== false && hasConsent()) {
    logSocialEvent('generate_feed', {
      postCount: posts.length,
      timestamp: new Date().toISOString()
    });
  }
  return `
    <section class="feed" aria-label="Fil d’actualité">
      <h2>Fil d’actualité</h2>
      <ul>
        ${posts.map(post => `
          <li class="post" itemscope itemtype="http://schema.org/SocialMediaPosting">
            <strong itemprop="author">${sanitize(post.author)}</strong>
            <p itemprop="articleBody">${sanitize(post.content)}</p>
            <time itemprop="datePublished" datetime="${sanitize(post.date)}">${formatDate(post.date)}</time>
          </li>
        `).join('')}
      </ul>
    </section>
  `;
}

/**
 * Génère un formulaire de création de post social.
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generatePostForm(options = {}) {
  if (options.log !== false && hasConsent()) {
    logSocialEvent('generate_post_form', {
      timestamp: new Date().toISOString()
    });
  }
  return `
    <form class="post-form" aria-label="Créer un post" onsubmit="return submitPost(event)">
      <textarea name="content" maxlength="280" required placeholder="Exprimez-vous…"></textarea>
      <button class="btn" type="submit">Publier</button>
    </form>
  `;
}

/**
 * Valide un objet utilisateur.
 * @param {object} user
 * @returns {boolean}
 */
function validateUser(user) {
  return user &&
    typeof user.id === 'string' &&
    typeof user.username === 'string' &&
    typeof user.bio === 'string' &&
    typeof user.avatar === 'string' &&
    typeof user.followers === 'number';
}

/**
 * Sanitize une chaîne pour éviter l’injection.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  return String(str).replace(/[\r\n<>]/g, '');
}

/**
 * Formate une date pour affichage.
 * @param {string} dateStr
 * @returns {string}
 */
function formatDate(dateStr) {
  const d = new Date(dateStr);
  return isNaN(d) ? '' : d.toLocaleDateString('fr-FR', { year: 'numeric', month: 'short', day: 'numeric' });
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('social_template_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSocialEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('social_template_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('social_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un identifiant pour les logs.
 * @param {string} id
 * @returns {string}
 */
function anonymizeId(id) {
  if (!id) return '';
  return id.length > 8 ? id.slice(0, 2) + '***' + id.slice(-2) : '***';
}

/**
 * Efface les logs social (droit à l’oubli RGPD).
 */
export function clearLocalSocialTemplateLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('social_template_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */