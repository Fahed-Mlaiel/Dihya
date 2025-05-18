"""
Template Métier : Automobile
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

automobile_bp = Blueprint('automobile', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

vehicules = []
entretiens = []
locations = []
conducteurs = []
alertes = []

# --- ROUTES VÉHICULES ---

@automobile_bp.route('/vehicules', methods=['GET'])
@jwt_required()
def list_vehicules():
    """Liste des véhicules (Admin/User)"""
    return jsonify(vehicules), 200

@automobile_bp.route('/vehicules', methods=['POST'])
@jwt_required()
def ajouter_vehicule():
    """Ajouter un véhicule (Admin)"""
    data = request.get_json()
    vehicule = {
        "id": len(vehicules) + 1,
        "marque": data.get("marque"),
        "modele": data.get("modele"),
        "annee": data.get("annee"),
        "immatriculation": data.get("immatriculation"),
        "statut": data.get("statut", "disponible"),
        "kilometrage": data.get("kilometrage", 0),
        "entretiens": []
    }
    vehicules.append(vehicule)
    return jsonify({"message": "Véhicule ajouté", "vehicule": vehicule}), 201

# --- ROUTES ENTRETIENS ---

@automobile_bp.route('/entretiens', methods=['GET'])
@jwt_required()
def list_entretiens():
    """Liste des entretiens (Admin/User)"""
    return jsonify(entretiens), 200

@automobile_bp.route('/entretiens', methods=['POST'])
@jwt_required()
def planifier_entretien():
    """Planifier un entretien (Admin)"""
    data = request.get_json()
    entretien = {
        "id": len(entretiens) + 1,
        "vehicule": data.get("vehicule"),
        "date": data.get("date"),
        "type": data.get("type"),
        "cout": data.get("cout"),
        "statut": data.get("statut", "prévu")
    }
    entretiens.append(entretien)
    return jsonify({"message": "Entretien planifié", "entretien": entretien}), 201

# --- ROUTES LOCATIONS ---

@automobile_bp.route('/locations', methods=['GET'])
@jwt_required()
def list_locations():
    """Liste des locations (Admin/User)"""
    return jsonify(locations), 200

@automobile_bp.route('/locations', methods=['POST'])
@jwt_required()
def reserver_location():
    """Réserver une location (User)"""
    data = request.get_json()
    location = {
        "id": len(locations) + 1,
        "vehicule": data.get("vehicule"),
        "utilisateur": get_jwt_identity(),
        "date_debut": data.get("date_debut"),
        "date_fin": data.get("date_fin"),
        "statut": "réservée",
        "contrat": data.get("contrat", "")
    }
    locations.append(location)
    return jsonify({"message": "Location réservée", "location": location}), 201

# --- ROUTES CONDUCTEURS ---

@automobile_bp.route('/conducteurs', methods=['GET'])
@jwt_required()
def list_conducteurs():
    """Liste des conducteurs (Admin)"""
    return jsonify(conducteurs), 200

@automobile_bp.route('/conducteurs', methods=['POST'])
@jwt_required()
def ajouter_conducteur():
    """Ajouter un conducteur (Admin)"""
    data = request.get_json()
    conducteur = {
        "id": len(conducteurs) + 1,
        "nom": data.get("nom"),
        "permis": data.get("permis"),
        "historique": [],
        "vehicules": data.get("vehicules", [])
    }
    conducteurs.append(conducteur)
    return jsonify({"message": "Conducteur ajouté", "conducteur": conducteur}), 201

# --- ROUTES ALERTES TECHNIQUES ---

@automobile_bp.route('/alertes', methods=['GET'])
@jwt_required()
def list_alertes():
    """Alertes techniques (Authentifié)"""
    return jsonify(alertes), 200

# --- EXPORT VÉHICULES (CSV simulé) ---

@automobile_bp.route('/export/vehicules', methods=['GET'])
@jwt_required()
def export_vehicules():
    """Exporter les véhicules (CSV simulé)"""
    csv = "id,marque,modele,annee,immatriculation,statut,kilometrage\n"
    for v in vehicules:
        csv += f'{v["id"]},{v["marque"]},{v["modele"]},{v["annee"]},{v["immatriculation"]},{v["statut"]},{v["kilometrage"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE AUTOMOBILE ---