"""
Helpers de chiffrement et déchiffrement pour Dihya Coding.

Ce module fournit des fonctions pour chiffrer et déchiffrer des données sensibles (AES-256-GCM),
gérer les clés de chiffrement et garantir la confidentialité conformément aux exigences RGPD et OWASP.

Bonnes pratiques :
- Ne jamais stocker de clés en dur dans le code source.
- Utiliser des clés fortes, stockées dans des variables d’environnement ou un coffre-fort.
- Toujours utiliser un IV/nonce unique pour chaque opération de chiffrement.
- Ne jamais logguer ou exposer de données chiffrées ou de clés.
- Prévoir des tests unitaires pour chaque helper de chiffrement.

Exemple d’utilisation :
    from app.security.crypto import encrypt_data, decrypt_data

    ciphertext, nonce, tag = encrypt_data("secret", key)
    plaintext = decrypt_data(ciphertext, key, nonce, tag)
"""

import os
from typing import Tuple, Union
from base64 import b64encode, b64decode

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def get_crypto_key(env_var: str = "CRYPTO_KEY") -> bytes:
    """
    Récupère la clé de chiffrement depuis une variable d'environnement.

    Args:
        env_var (str): Nom de la variable d'environnement.

    Returns:
        bytes: Clé de chiffrement.

    Raises:
        ValueError: Si la clé est absente ou invalide.
    """
    key = os.environ.get(env_var)
    if not key:
        raise ValueError(f"La clé de chiffrement '{env_var}' est requise.")
    key_bytes = b64decode(key) if not isinstance(key, bytes) else key
    if len(key_bytes) not in (16, 24, 32):
        raise ValueError("La clé doit faire 128, 192 ou 256 bits (16, 24 ou 32 octets).")
    return key_bytes

def encrypt_data(plaintext: Union[str, bytes], key: bytes) -> Tuple[str, str, str]:
    """
    Chiffre une donnée avec AES-256-GCM.

    Args:
        plaintext (str|bytes): Donnée à chiffrer.
        key (bytes): Clé de chiffrement (32 octets recommandé).

    Returns:
        Tuple[str, str, str]: (ciphertext base64, nonce base64, tag base64)
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return (
        b64encode(ciphertext).decode(),
        b64encode(nonce).decode(),
        b64encode(encryptor.tag).decode()
    )

def decrypt_data(ciphertext_b64: str, key: bytes, nonce_b64: str, tag_b64: str) -> str:
    """
    Déchiffre une donnée AES-256-GCM.

    Args:
        ciphertext_b64 (str): Donnée chiffrée (base64).
        key (bytes): Clé de chiffrement.
        nonce_b64 (str): Nonce utilisé (base64).
        tag_b64 (str): Tag d'authentification (base64).

    Returns:
        str: Donnée déchiffrée (texte clair).

    Raises:
        Exception: Si la décryption échoue.
    """
    ciphertext = b64decode(ciphertext_b64)
    nonce = b64decode(nonce_b64)
    tag = b64decode(tag_b64)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode("utf-8")