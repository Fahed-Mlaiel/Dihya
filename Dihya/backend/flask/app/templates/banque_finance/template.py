"""
Template Métier : Banque & Finance
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

banque_finance_bp = Blueprint('banque_finance', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

comptes = []
clients = []
operations = []
credits = []
notifications = []

# --- ROUTES COMPTES BANCAIRES ---

@banque_finance_bp.route('/comptes', methods=['GET'])
@jwt_required()
def list_comptes():
    """Liste des comptes (Conseiller/Admin)"""
    return jsonify(comptes), 200

@banque_finance_bp.route('/comptes', methods=['POST'])
@jwt_required()
def creer_compte():
    """Créer un compte bancaire (Conseiller)"""
    data = request.get_json()
    compte = {
        "id": len(comptes) + 1,
        "client": data.get("client"),
        "type": data.get("type"),
        "solde": data.get("solde", 0.0),
        "historique": [],
        "statut": "actif"
    }
    comptes.append(compte)
    return jsonify({"message": "Compte créé", "compte": compte}), 201

# --- ROUTES CLIENTS ---

@banque_finance_bp.route('/clients', methods=['GET'])
@jwt_required()
def list_clients():
    """Liste des clients (Conseiller/Admin)"""
    return jsonify(clients), 200

@banque_finance_bp.route('/clients', methods=['POST'])
@jwt_required()
def creer_client():
    """Créer un client (Conseiller)"""
    data = request.get_json()
    client = {
        "id": len(clients) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "documents": data.get("documents", []),
        "comptes": [],
        "scoring": data.get("scoring", None)
    }
    clients.append(client)
    return jsonify({"message": "Client créé", "client": client}), 201

# --- ROUTES OPÉRATIONS BANCAIRES ---

@banque_finance_bp.route('/operations', methods=['GET'])
@jwt_required()
def list_operations():
    """Liste des opérations (Client/Admin)"""
    return jsonify(operations), 200

@banque_finance_bp.route('/operations', methods=['POST'])
@jwt_required()
def effectuer_operation():
    """Effectuer une opération bancaire (Client)"""
    data = request.get_json()
    operation = {
        "id": len(operations) + 1,
        "compte": data.get("compte"),
        "type": data.get("type"),
        "montant": data.get("montant"),
        "date": data.get("date"),
        "statut": "effectuée"
    }
    operations.append(operation)
    # Logique de débit/crédit simulée
    for c in comptes:
        if c["id"] == data.get("compte"):
            if data.get("type") == "debit":
                c["solde"] -= data.get("montant")
            elif data.get("type") == "credit":
                c["solde"] += data.get("montant")
            c["historique"].append(operation)
    return jsonify({"message": "Opération effectuée", "operation": operation}), 201

# --- ROUTES CRÉDITS ---

@banque_finance_bp.route('/credits', methods=['GET'])
@jwt_required()
def list_credits():
    """Liste des crédits (Client/Admin)"""
    return jsonify(credits), 200

@banque_finance_bp.route('/credits', methods=['POST'])
@jwt_required()
def demander_credit():
    """Demander un crédit (Client)"""
    data = request.get_json()
    credit = {
        "id": len(credits) + 1,
        "client": get_jwt_identity(),
        "montant": data.get("montant"),
        "taux": data.get("taux"),
        "duree": data.get("duree"),
        "statut": "en attente",
        "echeances": []
    }
    credits.append(credit)
    return jsonify({"message": "Crédit demandé", "credit": credit}), 201

# --- EXPORT COMPTES (CSV simulé) ---

@banque_finance_bp.route('/export/comptes', methods=['GET'])
@jwt_required()
def export_comptes():
    """Exporter les comptes (CSV simulé)"""
    csv = "id,client,type,solde,statut\n"
    for c in comptes:
        csv += f'{c["id"]},{c["client"]},{c["type"]},{c["solde"]},{c["statut"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE BANQUE & FINANCE ---