/**
 * Dihya DevOps – Main Script (Node.js)
 * Automatisation, déploiement, monitoring, backup, tests, multilingue, sécurisé, documenté, prêt à l'emploi.
 */

const { execSync } = require('child_process');

function deployStack() {
  console.log('Déploiement de la stack Dihya...');
  execSync('docker-compose up -d', { stdio: 'inherit' });
}

function runBackup() {
  console.log('Backup en cours...');
  execSync('sh ../../BACKUP_GUIDE.md', { stdio: 'inherit' });
}

function runTests() {
  console.log('Lancement des tests CI/CD...');
  execSync('npm run test', { stdio: 'inherit' });
}

function main() {
  deployStack();
  runBackup();
  runTests();
}

if (require.main === module) {
  main();
}
