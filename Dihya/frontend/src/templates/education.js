/**
 * @file education.js
 * @description Template éducation pour Dihya Coding : génération de pages cours, modules, quiz, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère une page de cours éducatif.
 * @param {object} course - Données du cours { id, title, description, modules, image }
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateCoursePage(course, options = {}) {
  if (!validateCourse(course)) return '<!-- Cours invalide -->';
  if (options.log !== false && hasConsent()) {
    logEducationEvent('generate_course_page', {
      courseId: anonymizeId(course.id),
      timestamp: new Date().toISOString()
    });
  }
  return `
    <article class="course" itemscope itemtype="http://schema.org/Course">
      <h1 itemprop="name">${sanitize(course.title)}</h1>
      <img src="${sanitize(course.image)}" alt="${sanitize(course.title)}" itemprop="image" />
      <p itemprop="description">${sanitize(course.description)}</p>
      <section class="modules" aria-label="Modules">
        <h2>Modules</h2>
        <ul>
          ${(course.modules || []).map(m => `
            <li>
              <strong>${sanitize(m.title)}</strong>
              <p>${sanitize(m.summary)}</p>
              <button class="btn" onclick="openModule('${sanitize(m.id)}')">Ouvrir</button>
            </li>
          `).join('')}
        </ul>
      </section>
    </article>
  `;
}

/**
 * Génère une page de module éducatif.
 * @param {object} module - Données du module { id, title, content, resources }
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateModulePage(module, options = {}) {
  if (!validateModule(module)) return '<!-- Module invalide -->';
  if (options.log !== false && hasConsent()) {
    logEducationEvent('generate_module_page', {
      moduleId: anonymizeId(module.id),
      timestamp: new Date().toISOString()
    });
  }
  return `
    <section class="module" itemscope itemtype="http://schema.org/CreativeWork">
      <h2 itemprop="name">${sanitize(module.title)}</h2>
      <div itemprop="text">${sanitize(module.content)}</div>
      <section class="resources" aria-label="Ressources">
        <h3>Ressources complémentaires</h3>
        <ul>
          ${(module.resources || []).map(r => `
            <li>
              <a href="${sanitize(r.url)}" target="_blank" rel="noopener noreferrer">${sanitize(r.label)}</a>
            </li>
          `).join('')}
        </ul>
      </section>
    </section>
  `;
}

/**
 * Génère une page de quiz éducatif.
 * @param {object} quiz - Données du quiz { id, title, questions: [{ q, choices, answer }] }
 * @param {object} [options] - Options avancées (SEO, logs, RGPD)
 * @returns {string} HTML généré
 */
export function generateQuizPage(quiz, options = {}) {
  if (!validateQuiz(quiz)) return '<!-- Quiz invalide -->';
  if (options.log !== false && hasConsent()) {
    logEducationEvent('generate_quiz_page', {
      quizId: anonymizeId(quiz.id),
      timestamp: new Date().toISOString()
    });
  }
  return `
    <section class="quiz" aria-label="Quiz">
      <h2>${sanitize(quiz.title)}</h2>
      <form onsubmit="return submitQuiz(event)">
        <ol>
          ${(quiz.questions || []).map((q, i) => `
            <li>
              <p>${sanitize(q.q)}</p>
              ${(q.choices || []).map((c, j) => `
                <label>
                  <input type="radio" name="q${i}" value="${sanitize(c)}" required />
                  ${sanitize(c)}
                </label>
              `).join('')}
            </li>
          `).join('')}
        </ol>
        <button class="btn" type="submit">Valider</button>
      </form>
    </section>
  `;
}

/**
 * Valide un objet cours.
 * @param {object} course
 * @returns {boolean}
 */
function validateCourse(course) {
  return course &&
    typeof course.id === 'string' &&
    typeof course.title === 'string' &&
    typeof course.description === 'string' &&
    Array.isArray(course.modules) &&
    typeof course.image === 'string';
}

/**
 * Valide un objet module.
 * @param {object} module
 * @returns {boolean}
 */
function validateModule(module) {
  return module &&
    typeof module.id === 'string' &&
    typeof module.title === 'string' &&
    typeof module.content === 'string' &&
    Array.isArray(module.resources);
}

/**
 * Valide un objet quiz.
 * @param {object} quiz
 * @returns {boolean}
 */
function validateQuiz(quiz) {
  return quiz &&
    typeof quiz.id === 'string' &&
    typeof quiz.title === 'string' &&
    Array.isArray(quiz.questions) &&
    quiz.questions.every(q =>
      typeof q.q === 'string' &&
      Array.isArray(q.choices) &&
      typeof q.answer !== 'undefined'
    );
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
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('education_template_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logEducationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('education_template_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('education_template_logs', JSON.stringify(logs));
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
 * Efface les logs éducation (droit à l’oubli RGPD).
 */
export function clearLocalEducationTemplateLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('education_template_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */

// Ajout de l'export par défaut pour compatibilité avec import Education from './templates/education';
export default {
  generateCoursePage,
  generateModulePage,
  generateQuizPage,
  clearLocalEducationTemplateLogs,
};