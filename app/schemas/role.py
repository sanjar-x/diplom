from uuid import UUID
from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator


class RoleCreate(BaseModel):
    name: str = Field(title="Role’s name", description="Role’s name", examples=["user"])


class RoleResponse(BaseModel):
    role_id: UUID
    name: str = Field(title="Role’s name", description="Role’s name", examples=["user"])
