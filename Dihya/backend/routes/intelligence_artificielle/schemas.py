"""
Schemas Pydantic/GraphQL pour le module Intelligence Artificielle (Django routes)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AIProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet IA")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet IA")
    description: str = Field(..., description="Description du projet IA")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet IA")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AIAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset IA")
    project: int = Field(..., description="ID du projet IA associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset IA")
    type: str = Field(..., description="Type d’asset (dataset, modèle, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset IA")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class AIProjectListSchema(BaseModel):
    projects: List[AIProjectSchema]

class AIAssetListSchema(BaseModel):
    assets: List[AIAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AIProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class AIAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str
