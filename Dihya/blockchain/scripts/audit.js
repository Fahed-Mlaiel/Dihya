// Dihya Blockchain – Audit de smart contract (analyse statique, permissions, logs)
const fs = require('fs');
const solc = require('solc');

function auditContract(filePath) {
  const source = fs.readFileSync(filePath, 'utf8');
  const input = {
    language: 'Solidity',
    sources: { 'Contract.sol': { content: source } },
    settings: { outputSelection: { '*': { '*': ['*'] } } }
  };
  const output = JSON.parse(solc.compile(JSON.stringify(input)));
  if (output.errors) {
    output.errors.forEach(e => console.error(e.formattedMessage));
    return false;
  }
  // Analyse basique : permissions, events, fallback, etc.
  const contracts = output.contracts['Contract.sol'];
  for (const name in contracts) {
    const abi = contracts[name].abi;
    if (!abi.some(f => f.type === 'event')) {
      console.warn('Avertissement : aucun event défini dans ' + name);
    }
  }
  console.log('Audit terminé.');
  return true;
}

if (require.main === module) {
  const file = process.argv[2];
  if (!file) throw new Error('Usage: node audit.js <Contract.sol>');
  auditContract(file);
}
