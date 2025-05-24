"""
Dihya – VR/AR Images Schemas
Schemas Pydantic/DRF pour validation, documentation, OpenAPI, GraphQL-ready, multilingue.
"""
from typing import Optional
from pydantic import BaseModel, Field

class VRARImageSchema(BaseModel):
    filename: str = Field(..., description="Nom du fichier image")
    size: int = Field(..., description="Taille en octets")
    content_type: str = Field(..., description="Type MIME")
    uploaded_by: str = Field(..., description="Utilisateur ayant uploadé")
    created_at: Optional[str] = Field(None, description="Horodatage ISO8601")
    lang: Optional[str] = Field('fr', description="Langue de l’interface")
