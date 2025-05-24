"""
Dihya Backend – Schémas Pydantic pour IA/VR/AR
Validation, sécurité, RGPD, i18n, multitenancy, plugins.
"""
from pydantic import BaseModel, Field, EmailStr, constr
from typing import List, Optional, Dict

class ProjectBase(BaseModel):
    name: constr(min_length=3, max_length=128)
    description: Optional[str] = Field(None, description="Description multilingue")
    owner_email: EmailStr
    language: constr(min_length=2, max_length=8)
    is_active: bool = True
    tags: List[str] = []
    class Config:
        schema_extra = {
            "example": {
                "name": "Projet VR Immersif",
                "description": "Expérience VR collaborative multilingue.",
                "owner_email": "admin@dihya.ai",
                "language": "fr",
                "is_active": True,
                "tags": ["VR", "IA", "collaboratif"]
            }
        }

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    name: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    tags: Optional[List[str]]

class ProjectOut(ProjectBase):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

class UserRole(BaseModel):
    user_email: EmailStr
    role: str  # admin, user, invité
    project_id: int

class PluginConfig(BaseModel):
    name: str
    enabled: bool
    config: Dict[str, str]

class AuditLog(BaseModel):
    action: str
    user: EmailStr
    project_id: int
    timestamp: str
    details: Optional[Dict]
