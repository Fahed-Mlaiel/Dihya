"""
Template Métier : Assurance
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

assurance_bp = Blueprint('assurance', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

contrats = []
clients = []
sinistres = []
devis = []
paiements = []

# --- ROUTES CONTRATS ---

@assurance_bp.route('/contrats', methods=['GET'])
@jwt_required()
def list_contrats():
    """Liste des contrats (Agent/Admin)"""
    return jsonify(contrats), 200

@assurance_bp.route('/contrats', methods=['POST'])
@jwt_required()
def creer_contrat():
    """Créer un contrat (Agent)"""
    data = request.get_json()
    contrat = {
        "id": len(contrats) + 1,
        "client": data.get("client"),
        "type": data.get("type"),
        "date_debut": data.get("date_debut"),
        "date_fin": data.get("date_fin"),
        "statut": "actif",
        "montant": data.get("montant"),
        "historique": []
    }
    contrats.append(contrat)
    return jsonify({"message": "Contrat créé", "contrat": contrat}), 201

# --- ROUTES CLIENTS ---

@assurance_bp.route('/clients', methods=['GET'])
@jwt_required()
def list_clients():
    """Liste des clients (Agent/Admin)"""
    return jsonify(clients), 200

@assurance_bp.route('/clients', methods=['POST'])
@jwt_required()
def creer_client():
    """Créer un client (Agent)"""
    data = request.get_json()
    client = {
        "id": len(clients) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "documents": data.get("documents", []),
        "contrats": [],
        "sinistres": []
    }
    clients.append(client)
    return jsonify({"message": "Client créé", "client": client}), 201

# --- ROUTES SINISTRES ---

@assurance_bp.route('/sinistres', methods=['GET'])
@jwt_required()
def list_sinistres():
    """Liste des sinistres (Agent/Admin)"""
    return jsonify(sinistres), 200

@assurance_bp.route('/sinistres', methods=['POST'])
@jwt_required()
def declarer_sinistre():
    """Déclarer un sinistre (Client)"""
    data = request.get_json()
    sinistre = {
        "id": len(sinistres) + 1,
        "contrat": data.get("contrat"),
        "date": data.get("date"),
        "description": data.get("description"),
        "statut": "en attente",
        "pieces_jointes": data.get("pieces_jointes", [])
    }
    sinistres.append(sinistre)
    return jsonify({"message": "Sinistre déclaré", "sinistre": sinistre}), 201

# --- ROUTES DEVIS ---

@assurance_bp.route('/devis', methods=['GET'])
@jwt_required()
def list_devis():
    """Liste des devis (Agent/Admin)"""
    return jsonify(devis), 200

@assurance_bp.route('/devis', methods=['POST'])
@jwt_required()
def creer_devis():
    """Créer un devis (Agent)"""
    data = request.get_json()
    devis_obj = {
        "id": len(devis) + 1,
        "client": data.get("client"),
        "type": data.get("type"),
        "montant": data.get("montant"),
        "date": data.get("date"),
        "statut": "en attente"
    }
    devis.append(devis_obj)
    return jsonify({"message": "Devis créé", "devis": devis_obj}), 201

# --- EXPORT CONTRATS (CSV simulé) ---

@assurance_bp.route('/export/contrats', methods=['GET'])
@jwt_required()
def export_contrats():
    """Exporter les contrats (CSV simulé)"""
    csv = "id,client,type,date_debut,date_fin,statut,montant\n"
    for c in contrats:
        csv += f'{c["id"]},{c["client"]},{c["type"]},{c["date_debut"]},{c["date_fin"]},{c["statut"]},{c["montant"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE ASSURANCE ---