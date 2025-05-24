// Dihya Blockchain – Backup décentralisé sur IPFS
const { create } = require('ipfs-http-client');
const fs = require('fs');

async function backupToIPFS(filePath) {
  const ipfs = create();
  const file = fs.readFileSync(filePath);
  const { cid } = await ipfs.add(file);
  console.log('Backup IPFS CID:', cid.toString());
  return cid.toString();
}

if (require.main === module) {
  const file = process.argv[2];
  if (!file) throw new Error('Usage: node backup_ipfs.js <file>');
  backupToIPFS(file).catch(console.error);
}
