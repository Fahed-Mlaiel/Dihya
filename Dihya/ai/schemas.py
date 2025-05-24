"""
Schemas Pydantic/GraphQL pour le module IA Dihya (Python)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional
from pydantic import BaseModel, Field, constr

class AIRequestSchema(BaseModel):
    prompt: constr(min_length=1, max_length=4096) = Field(..., description="Prompt utilisateur (multilingue)")
    lang: Optional[str] = Field('fr', description="Langue cible (fr, en, ar, tzr, etc.)")
    engine: Optional[str] = Field('mixtral', description="Moteur IA (mixtral, llama, mistral, openai)")

class AIResponseSchema(BaseModel):
    text: str = Field(..., description="Réponse générée par l'IA")
    lang: str = Field(..., description="Langue de la réponse")
    engine: str = Field(..., description="Moteur IA utilisé")
    error: Optional[str] = Field(None, description="Erreur éventuelle")

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AIResponseType:
    text: str
    lang: str
    engine: str
    error: Optional[str]
