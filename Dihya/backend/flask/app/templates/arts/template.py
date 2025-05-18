"""
Template Métier : Arts
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

arts_bp = Blueprint('arts', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

evenements = []
portfolios = []
galeries = []
reservations = []
artistes = []

# --- ROUTES ÉVÉNEMENTS ARTISTIQUES ---

@arts_bp.route('/evenements', methods=['GET'])
def list_evenements():
    """Liste des événements artistiques (Public)"""
    return jsonify(evenements), 200

@arts_bp.route('/evenements', methods=['POST'])
@jwt_required()
def creer_evenement():
    """Créer un événement artistique (Organisateur)"""
    data = request.get_json()
    evenement = {
        "id": len(evenements) + 1,
        "titre": data.get("titre"),
        "date": data.get("date"),
        "lieu": data.get("lieu"),
        "description": data.get("description"),
        "artistes": data.get("artistes", []),
        "galerie": data.get("galerie"),
        "reservations": []
    }
    evenements.append(evenement)
    return jsonify({"message": "Événement créé", "evenement": evenement}), 201

# --- ROUTES PORTFOLIOS D'ARTISTES ---

@arts_bp.route('/portfolios', methods=['GET'])
def list_portfolios():
    """Liste des portfolios (Public)"""
    return jsonify(portfolios), 200

@arts_bp.route('/portfolios', methods=['POST'])
@jwt_required()
def creer_portfolio():
    """Créer un portfolio (Artiste)"""
    data = request.get_json()
    portfolio = {
        "id": len(portfolios) + 1,
        "artiste": get_jwt_identity(),
        "oeuvres": data.get("oeuvres", []),
        "description": data.get("description"),
        "visibilite": data.get("visibilite", "public")
    }
    portfolios.append(portfolio)
    return jsonify({"message": "Portfolio créé", "portfolio": portfolio}), 201

# --- ROUTES GALERIES ---

@arts_bp.route('/galeries', methods=['GET'])
def list_galeries():
    """Liste des galeries (Public)"""
    return jsonify(galeries), 200

@arts_bp.route('/galeries', methods=['POST'])
@jwt_required()
def creer_galerie():
    """Créer une galerie (Organisateur)"""
    data = request.get_json()
    galerie = {
        "id": len(galeries) + 1,
        "nom": data.get("nom"),
        "localisation": data.get("localisation"),
        "oeuvres": data.get("oeuvres", []),
        "expositions": data.get("expositions", [])
    }
    galeries.append(galerie)
    return jsonify({"message": "Galerie créée", "galerie": galerie}), 201

# --- ROUTES RÉSERVATIONS ---

@arts_bp.route('/reservations', methods=['GET'])
@jwt_required()
def list_reservations():
    """Liste des réservations (Authentifié)"""
    user_id = get_jwt_identity()
    user_reservations = [r for r in reservations if r["utilisateur"] == user_id]
    return jsonify(user_reservations), 200

@arts_bp.route('/reservations', methods=['POST'])
@jwt_required()
def reserver_evenement():
    """Réserver une place à un événement (Utilisateur)"""
    data = request.get_json()
    reservation = {
        "id": len(reservations) + 1,
        "utilisateur": get_jwt_identity(),
        "evenement": data.get("evenement"),
        "date": data.get("date"),
        "statut": "confirmée"
    }
    reservations.append(reservation)
    return jsonify({"message": "Réservation effectuée", "reservation": reservation}), 201

# --- EXPORT ÉVÉNEMENTS (CSV simulé) ---

@arts_bp.route('/export/evenements', methods=['GET'])
@jwt_required()
def export_evenements():
    """Exporter les événements (CSV simulé)"""
    csv = "id,titre,date,lieu\n"
    for e in evenements:
        csv += f'{e["id"]},{e["titre"]},{e["date"]},{e["lieu"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE ARTS ---