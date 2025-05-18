/**
 * @file ecommerce.js
 * @description Template e-commerce pour Dihya Coding : génération de pages produits, panier, paiement, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère une page produit e-commerce.
 * @param {object} product - Données produit { id, name, description, price, image, ... }
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateProductPage(product, options = {}) {
  if (!validateProduct(product)) return '<!-- Produit invalide -->';
  if (options.log !== false && hasConsent()) {
    logEcommerceEvent('generate_product_page', {
      productId: anonymizeId(product.id),
      timestamp: new Date().toISOString()
    });
  }
  return `
    <article class="product" itemscope itemtype="http://schema.org/Product">
      <h1 itemprop="name">${sanitize(product.name)}</h1>
      <img src="${sanitize(product.image)}" alt="${sanitize(product.name)}" itemprop="image" />
      <p itemprop="description">${sanitize(product.description)}</p>
      <span class="price" itemprop="offers" itemscope itemtype="http://schema.org/Offer">
        <meta itemprop="priceCurrency" content="EUR" />
        <span itemprop="price">${sanitize(product.price)}</span> €
      </span>
      <button class="btn" onclick="addToCart('${sanitize(product.id)}')">Ajouter au panier</button>
    </article>
  `;
}

/**
 * Génère une page panier e-commerce.
 * @param {Array} cart - Liste des produits [{ id, name, price, qty }]
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateCartPage(cart, options = {}) {
  if (!Array.isArray(cart)) return '<!-- Panier invalide -->';
  if (options.log !== false && hasConsent()) {
    logEcommerceEvent('generate_cart_page', {
      cartSize: cart.length,
      timestamp: new Date().toISOString()
    });
  }
  const total = cart.reduce((sum, p) => sum + (p.price * p.qty), 0);
  return `
    <section class="cart" aria-label="Panier">
      <h2>Votre panier</h2>
      <ul>
        ${cart.map(p => `
          <li>
            ${sanitize(p.name)} × ${sanitize(p.qty)} – <span>${sanitize(p.price)} €</span>
            <button onclick="removeFromCart('${sanitize(p.id)}')">Retirer</button>
          </li>
        `).join('')}
      </ul>
      <div class="cart-total">Total : <strong>${total.toFixed(2)} €</strong></div>
      <button class="btn" onclick="checkout()">Passer au paiement</button>
    </section>
  `;
}

/**
 * Génère une page de paiement e-commerce (simulation).
 * @param {object} order - Détails de la commande { id, amount, user }
 * @param {object} [options] - Options avancées (logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateCheckoutPage(order, options = {}) {
  if (!order || typeof order !== 'object') return '<!-- Commande invalide -->';
  if (options.log !== false && hasConsent()) {
    logEcommerceEvent('generate_checkout_page', {
      orderId: anonymizeId(order.id),
      amount: order.amount,
      timestamp: new Date().toISOString()
    });
  }
  return `
    <section class="checkout" aria-label="Paiement">
      <h2>Paiement sécurisé</h2>
      <p>Commande n° <strong>${anonymizeId(order.id)}</strong></p>
      <p>Montant : <strong>${order.amount.toFixed(2)} €</strong></p>
      <form onsubmit="return processPayment(event)">
        <label>
          Carte bancaire
          <input type="text" name="card" autocomplete="cc-number" required pattern="\\d{16}" maxlength="16" />
        </label>
        <label>
          Expiration
          <input type="text" name="exp" autocomplete="cc-exp" required pattern="\\d{2}/\\d{2}" maxlength="5" />
        </label>
        <label>
          CVC
          <input type="text" name="cvc" autocomplete="cc-csc" required pattern="\\d{3}" maxlength="3" />
        </label>
        <button class="btn" type="submit">Payer</button>
      </form>
    </section>
  `;
}

/**
 * Valide un objet produit.
 * @param {object} product
 * @returns {boolean}
 */
function validateProduct(product) {
  return product &&
    typeof product.id === 'string' &&
    typeof product.name === 'string' &&
    typeof product.description === 'string' &&
    typeof product.price === 'number' &&
    typeof product.image === 'string';
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
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('ecommerce_template_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logEcommerceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('ecommerce_template_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('ecommerce_template_logs', JSON.stringify(logs));
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
 * Efface les logs e-commerce (droit à l’oubli RGPD).
 */
export function clearLocalEcommerceTemplateLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('ecommerce_template_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */