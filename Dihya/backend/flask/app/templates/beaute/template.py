"""
Template Métier : Beauté
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

beaute_bp = Blueprint('beaute', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

salons = []
prestations = []
rendezvous = []
clients = []
notifications = []

# --- ROUTES SALONS ---

@beaute_bp.route('/salons', methods=['GET'])
@jwt_required()
def list_salons():
    """Liste des salons (Admin/User)"""
    return jsonify(salons), 200

@beaute_bp.route('/salons', methods=['POST'])
@jwt_required()
def creer_salon():
    """Créer un salon (Admin)"""
    data = request.get_json()
    salon = {
        "id": len(salons) + 1,
        "nom": data.get("nom"),
        "adresse": data.get("adresse"),
        "equipe": data.get("equipe", []),
        "prestations": [],
        "planning": []
    }
    salons.append(salon)
    return jsonify({"message": "Salon créé", "salon": salon}), 201

# --- ROUTES PRESTATIONS ---

@beaute_bp.route('/prestations', methods=['GET'])
def list_prestations():
    """Liste des prestations (Public)"""
    return jsonify(prestations), 200

@beaute_bp.route('/prestations', methods=['POST'])
@jwt_required()
def ajouter_prestation():
    """Ajouter une prestation (Admin)"""
    data = request.get_json()
    prestation = {
        "id": len(prestations) + 1,
        "nom": data.get("nom"),
        "tarif": data.get("tarif"),
        "duree": data.get("duree"),
        "description": data.get("description"),
        "disponibilite": data.get("disponibilite", True)
    }
    prestations.append(prestation)
    return jsonify({"message": "Prestation ajoutée", "prestation": prestation}), 201

# --- ROUTES RENDEZ-VOUS ---

@beaute_bp.route('/rendezvous', methods=['GET'])
@jwt_required()
def list_rendezvous():
    """Liste des rendez-vous (Salon/Client)"""
    return jsonify(rendezvous), 200

@beaute_bp.route('/rendezvous', methods=['POST'])
@jwt_required()
def prendre_rendezvous():
    """Prendre rendez-vous (Client)"""
    data = request.get_json()
    rdv = {
        "id": len(rendezvous) + 1,
        "client": get_jwt_identity(),
        "salon": data.get("salon"),
        "prestation": data.get("prestation"),
        "date": data.get("date"),
        "statut": "confirmé"
    }
    rendezvous.append(rdv)
    return jsonify({"message": "Rendez-vous pris", "rendezvous": rdv}), 201

# --- ROUTES CLIENTS ---

@beaute_bp.route('/clients', methods=['GET'])
@jwt_required()
def list_clients():
    """Liste des clients (Admin/Salon)"""
    return jsonify(clients), 200

@beaute_bp.route('/clients', methods=['POST'])
@jwt_required()
def creer_client():
    """Créer un client (Salon)"""
    data = request.get_json()
    client = {
        "id": len(clients) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "historique": [],
        "fidelite": data.get("fidelite", 0)
    }
    clients.append(client)
    return jsonify({"message": "Client créé", "client": client}), 201

# --- EXPORT RENDEZ-VOUS (CSV simulé) ---

@beaute_bp.route('/export/rendezvous', methods=['GET'])
@jwt_required()
def export_rendezvous():
    """Exporter les rendez-vous (CSV simulé)"""
    csv = "id,client,salon,prestation,date,statut\n"
    for r in rendezvous:
        csv += f'{r["id"]},{r["client"]},{r["salon"]},{r["prestation"]},{r["date"]},{r["statut"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE BEAUTÉ ---