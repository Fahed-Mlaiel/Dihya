"""
Template Métier : Administration Publique
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

administration_publique_bp = Blueprint('administration_publique', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par SQLAlchemy ou autre ORM) ---

demarches = []
citoyens = []
agents = []
messages = []
notifications = []

# --- ROUTES DÉMARCHES ---

@administration_publique_bp.route('/demarches', methods=['GET'])
@jwt_required()
def list_demarches():
    """Liste toutes les démarches (Admin/Agent)"""
    # Filtrage par rôle possible ici
    return jsonify(demarches), 200

@administration_publique_bp.route('/demarches', methods=['POST'])
@jwt_required()
def creer_demarche():
    """Créer une nouvelle démarche (Citoyen/Agent)"""
    data = request.get_json()
    demarche = {
        "id": len(demarches) + 1,
        "type": data.get("type"),
        "statut": "en attente",
        "citoyen_id": get_jwt_identity(),
        "date": data.get("date"),
        "pieces_jointes": data.get("pieces_jointes", []),
        "historique": []
    }
    demarches.append(demarche)
    # Notifier l'agent/responsable ici
    return jsonify({"message": "Démarche créée", "demarche": demarche}), 201

@administration_publique_bp.route('/demarches/<int:id>', methods=['GET'])
@jwt_required()
def get_demarche(id):
    """Détail d’une démarche"""
    for d in demarches:
        if d["id"] == id:
            return jsonify(d), 200
    return jsonify({"error": "Démarche non trouvée"}), 404

@administration_publique_bp.route('/demarches/<int:id>', methods=['PUT'])
@jwt_required()
def update_demarche(id):
    """Modifier une démarche (Agent/Admin)"""
    data = request.get_json()
    for d in demarches:
        if d["id"] == id:
            d.update(data)
            d["historique"].append({"action": "modification", "by": get_jwt_identity()})
            return jsonify({"message": "Démarche mise à jour", "demarche": d}), 200
    return jsonify({"error": "Démarche non trouvée"}), 404

@administration_publique_bp.route('/demarches/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_demarche(id):
    """Supprimer une démarche (Admin)"""
    global demarches
    demarches = [d for d in demarches if d["id"] != id]
    return jsonify({"message": "Démarche supprimée"}), 200

# --- ROUTES CITOYEN ---

@administration_publique_bp.route('/citoyens/me', methods=['GET'])
@jwt_required()
def get_citoyen_profile():
    """Profil du citoyen connecté"""
    user_id = get_jwt_identity()
    for c in citoyens:
        if c["id"] == user_id:
            return jsonify(c), 200
    return jsonify({"error": "Citoyen non trouvé"}), 404

@administration_publique_bp.route('/citoyens/register', methods=['POST'])
def register_citoyen():
    """Inscription citoyen"""
    data = request.get_json()
    citoyen = {
        "id": len(citoyens) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "documents": [],
        "statut": "actif",
        "historique": []
    }
    citoyens.append(citoyen)
    return jsonify({"message": "Inscription réussie", "citoyen": citoyen}), 201

# --- AUTH SIMPLIFIÉE (à remplacer par vrai système JWT/OAuth2) ---

@administration_publique_bp.route('/auth/login', methods=['POST'])
def login():
    """Connexion (mock)"""
    data = request.get_json()
    # Ici, on retourne un token simulé (à remplacer)
    return jsonify({"access_token": "demo-token", "user_id": 1}), 200

# --- MESSAGERIE ---

@administration_publique_bp.route('/messages', methods=['POST'])
@jwt_required()
def send_message():
    """Envoyer un message (citoyen/agent)"""
    data = request.get_json()
    msg = {
        "id": len(messages) + 1,
        "expediteur": get_jwt_identity(),
        "destinataire": data.get("destinataire"),
        "contenu": data.get("contenu"),
        "date": data.get("date")
    }
    messages.append(msg)
    return jsonify({"message": "Message envoyé", "msg": msg}), 201

# --- NOTIFICATIONS ---

@administration_publique_bp.route('/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    """Notifications de l'utilisateur"""
    user_id = get_jwt_identity()
    user_notifications = [n for n in notifications if n["user_id"] == user_id]
    return jsonify(user_notifications), 200

# --- EXPORT DEMARCHES (CSV/PDF simulé) ---

@administration_publique_bp.route('/export/demarches', methods=['GET'])
@jwt_required()
def export_demarches():
    """Exporter les démarches (CSV simulé)"""
    # Ici, on retourne du CSV brut pour la démo
    csv = "id,type,statut,date\n"
    for d in demarches:
        csv += f'{d["id"]},{d["type"]},{d["statut"]},{d["date"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE ADMINISTRATION PUBLIQUE ---