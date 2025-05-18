"""
Template Métier : Agriculture
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

agriculture_bp = Blueprint('agriculture', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

exploitations = []
cultures = []
stocks = []
alertes = []
producteurs = []

# --- ROUTES EXPLOITATIONS AGRICOLES ---

@agriculture_bp.route('/exploitations', methods=['GET'])
@jwt_required()
def list_exploitations():
    """Liste des exploitations agricoles (Producteur/Admin)"""
    return jsonify(exploitations), 200

@agriculture_bp.route('/exploitations', methods=['POST'])
@jwt_required()
def creer_exploitation():
    """Créer une exploitation agricole (Producteur)"""
    data = request.get_json()
    exploitation = {
        "id": len(exploitations) + 1,
        "nom": data.get("nom"),
        "localisation": data.get("localisation"),
        "superficie": data.get("superficie"),
        "cultures": [],
        "historique": []
    }
    exploitations.append(exploitation)
    return jsonify({"message": "Exploitation créée", "exploitation": exploitation}), 201

# --- ROUTES CULTURES ---

@agriculture_bp.route('/cultures', methods=['GET'])
@jwt_required()
def list_cultures():
    """Liste des cultures (Producteur/Admin)"""
    return jsonify(cultures), 200

@agriculture_bp.route('/cultures', methods=['POST'])
@jwt_required()
def ajouter_culture():
    """Ajouter une culture (Producteur)"""
    data = request.get_json()
    culture = {
        "id": len(cultures) + 1,
        "type": data.get("type"),
        "parcelle": data.get("parcelle"),
        "date_semis": data.get("date_semis"),
        "date_recolte": data.get("date_recolte"),
        "interventions": [],
        "rendement": data.get("rendement")
    }
    cultures.append(culture)
    return jsonify({"message": "Culture ajoutée", "culture": culture}), 201

# --- ROUTES STOCKS ---

@agriculture_bp.route('/stocks', methods=['GET'])
@jwt_required()
def list_stocks():
    """Voir les stocks (Producteur/Admin)"""
    return jsonify(stocks), 200

@agriculture_bp.route('/stocks', methods=['POST'])
@jwt_required()
def ajouter_stock():
    """Ajouter au stock (Producteur)"""
    data = request.get_json()
    stock = {
        "id": len(stocks) + 1,
        "type": data.get("type"),
        "quantite": data.get("quantite"),
        "date": data.get("date"),
        "categorie": data.get("categorie")
    }
    stocks.append(stock)
    return jsonify({"message": "Stock ajouté", "stock": stock}), 201

# --- ROUTES ALERTES MÉTÉO ---

@agriculture_bp.route('/alertes', methods=['GET'])
@jwt_required()
def get_alertes():
    """Alertes météo (tous utilisateurs)"""
    return jsonify(alertes), 200

# --- EXPORT EXPLOITATIONS (CSV simulé) ---

@agriculture_bp.route('/export/exploitations', methods=['GET'])
@jwt_required()
def export_exploitations():
    """Exporter les exploitations (CSV simulé)"""
    csv = "id,nom,localisation,superficie\n"
    for e in exploitations:
        csv += f'{e["id"]},{e["nom"]},{e["localisation"]},{e["superficie"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE AGRICULTURE ---