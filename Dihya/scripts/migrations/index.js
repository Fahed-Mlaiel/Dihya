// index.js - Orchestrateur de migrations Dihya Coding
// Sécurité, audit, RGPD, multitenancy, plugins, rollback

'use strict';

const fs = require('fs');
const path = require('path');
const { auditLog } = require('../../frontend/src/utils/utils.js');

const MIGRATIONS_DIR = __dirname;

function getMigrations() {
  return fs.readdirSync(MIGRATIONS_DIR)
    .filter(f => f.endsWith('.js') && f !== 'index.js')
    .sort();
}

async function runMigrations(direction = 'up') {
  const migrations = getMigrations();
  for (const file of (direction === 'up' ? migrations : migrations.reverse())) {
    const migration = require(path.join(MIGRATIONS_DIR, file));
    auditLog(`migration_${direction}_start`, { file });
    await migration[direction]();
    auditLog(`migration_${direction}_end`, { file });
  }
}

if (require.main === module) {
  const dir = process.argv[2] || 'up';
  runMigrations(dir).then(() => {
    console.log(`Migrations ${dir} terminées.`);
  }).catch(e => {
    auditLog('migration_failed', { error: e.message });
    process.exit(1);
  });
}

module.exports = { runMigrations };
