from enum import Enum
from typing import Annotated
from uuid import UUID
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ConfigDict,
    SecretStr,
    StringConstraints,
    constr,
)


class DivisionType(str, Enum):
    division = "division"
    administration = "administration"
    center = "center"  # type: ignore
    other = "other"


class DivisionCreate(BaseModel):
    name: str = Field(
        title="Division’s name",
        description="Division’s name",
        examples=[
            "Institut xotin - qizlar maslahat kengashi",
            "Ta'lim sifatini nazorat qilish bo’limi",
            "Xalqaro hamkorlik bo’limi",
            "Sirtqi bo'lim",
            "O'quv uslubiy boshqarma",
            "Marketing va talabalar amaliyoti bo’limi",
            "Magistratura bo'limi",
            "Iqtidorli talabalarning ilmiy-tadqiqot faoliyatini tashkil etish bo‘limi",
            "Yoshlar bilan ishlash, ma'naviyat va ma'rifat bo'limi",
            "Ilmiy va ilmiy pedagogik kadrlar tayyorlash",
            "Xodimlar bo'limi",
            "Devonxona bo'limi",
            "Axbоrоt-resurs markazi",
            "Raqamli ta'lim texnologiya markazi",
        ],
    )
    code: Annotated[str, StringConstraints(max_length=3)]
    type: DivisionType = Field(
        title="Division’s type",
        description="Division’s type",
        examples=["division", "administration", "center", "other"],
    )
    active: bool


class DivisionResponse(BaseModel):
    division_id: UUID
    name: str = Field(
        title="Division’s name",
        description="Division’s name",
        examples=[
            "Institut xotin - qizlar maslahat kengashi",
            "Ta'lim sifatini nazorat qilish bo’limi",
            "Xalqaro hamkorlik bo’limi",
            "Sirtqi bo'lim",
            "O'quv uslubiy boshqarma",
            "Marketing va talabalar amaliyoti bo’limi",
            "Magistratura bo'limi",
            "Iqtidorli talabalarning ilmiy-tadqiqot faoliyatini tashkil etish bo‘limi",
            "Yoshlar bilan ishlash, ma'naviyat va ma'rifat bo'limi",
            "Ilmiy va ilmiy pedagogik kadrlar tayyorlash",
            "Xodimlar bo'limi",
            "Devonxona bo'limi",
            "Axbоrоt-resurs markazi",
            "Raqamli ta'lim texnologiya markazi",
        ],
    )
    code: Annotated[str, StringConstraints(max_length=3)]
    type: DivisionType = Field(
        title="Division’s type",
        description="Division’s type",
        examples=["division", "administration", "center", "other"],
    )
    active: bool
