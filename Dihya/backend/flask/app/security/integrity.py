"""
Module de vérification d’intégrité des données pour Dihya Coding.

Ce module fournit des fonctions pour garantir l’intégrité des données critiques (hash, signature, contrôle de cohérence)
et détecter toute altération ou corruption, conformément aux exigences de sécurité et de conformité RGPD.

Bonnes pratiques :
- Utiliser des algorithmes de hachage robustes (SHA-256, SHA-512).
- Signer les données sensibles si besoin (HMAC, signature asymétrique).
- Ne jamais stocker ou transmettre de hash de données sensibles sans sel.
- Logger les anomalies d’intégrité pour audit.
- Prévoir des tests unitaires pour chaque helper d’intégrité.

Exemple d’utilisation :
    from app.security.integrity import hash_data, verify_hash

    digest = hash_data("valeur")
    assert verify_hash("valeur", digest)
"""

import hashlib
import hmac
from typing import Union

def hash_data(data: Union[str, bytes], salt: Union[str, bytes] = "") -> str:
    """
    Calcule le hash SHA-256 d'une donnée, avec un sel optionnel.

    Args:
        data (str|bytes): Donnée à hasher.
        salt (str|bytes): Sel optionnel pour renforcer la sécurité.

    Returns:
        str: Hash hexadécimal.
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    if isinstance(salt, str):
        salt = salt.encode("utf-8")
    return hashlib.sha256(salt + data).hexdigest()

def verify_hash(data: Union[str, bytes], expected_hash: str, salt: Union[str, bytes] = "") -> bool:
    """
    Vérifie qu'une donnée correspond à un hash SHA-256 donné.

    Args:
        data (str|bytes): Donnée à vérifier.
        expected_hash (str): Hash attendu.
        salt (str|bytes): Sel utilisé lors du hash.

    Returns:
        bool: True si la donnée correspond au hash, False sinon.
    """
    return hash_data(data, salt) == expected_hash

def hmac_sign(data: Union[str, bytes], secret: Union[str, bytes]) -> str:
    """
    Génère une signature HMAC-SHA256 pour une donnée.

    Args:
        data (str|bytes): Donnée à signer.
        secret (str|bytes): Clé secrète HMAC.

    Returns:
        str: Signature hexadécimale.
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    if isinstance(secret, str):
        secret = secret.encode("utf-8")
    return hmac.new(secret, data, hashlib.sha256).hexdigest()

def verify_hmac(data: Union[str, bytes], signature: str, secret: Union[str, bytes]) -> bool:
    """
    Vérifie une signature HMAC-SHA256.

    Args:
        data (str|bytes): Donnée à vérifier.
        signature (str): Signature attendue.
        secret (str|bytes): Clé secrète HMAC.

    Returns:
        bool: True si la signature est valide, False sinon.
    """
    return hmac.compare_digest(hmac_sign(data, secret), signature)