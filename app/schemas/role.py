from uuid import UUID
from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, model_validator


class RoleCreate(BaseModel):
    name: str


class RoleResponse(BaseModel):
    role_id: UUID
    name: str
