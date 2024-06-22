from enum import Enum
from typing import Annotated
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ConfigDict,
    SecretStr,
    StringConstraints,
    constr,
)


class FacultyType(str, Enum):
    local = "local"
    joint = "joint"
    division = "division"
    other = "other"


class FacultyCreate(BaseModel):
    name: str = Field(
        title="Faculty’s name",
        description="Faculty’s address",
        examples=[
            "Iqtisodiyot va boshqaruv fakulteti",
            "Energetika va mehnat muhofazasi fakulteti",
            "Mashinasozlik fakulteti",
            "Transport fakulteti",
            "Muhandislik kommunikatsiyalari fakulteti",
            "Sanoatni axborotlashtirish fakulteti",
            "Qurilish fakulteti",
        ],
    )
    code: str
    type: FacultyType = Field(
        title="Faculty’s type",
        description="Faculty’s type",
        examples=["local", "joint", "division", "other"],
    )


class FacultyResponse(BaseModel):
    name: str = Field(
        title="Faculty’s name",
        description="Faculty’s address",
        examples=[
            "Iqtisodiyot va boshqaruv fakulteti",
            "Energetika va mehnat muhofazasi fakulteti",
            "Mashinasozlik fakulteti",
            "Transport fakulteti",
            "Muhandislik kommunikatsiyalari fakulteti",
            "Sanoatni axborotlashtirish fakulteti",
            "Qurilish fakulteti",
        ],
    )
    code: Annotated[str, StringConstraints(max_length=3, pattern=r"^\d+$")]
    type: FacultyType = Field(
        title="Faculty’s type",
        description="Faculty’s type",
        examples=["local", "joint", "division", "other"],
    )
    active: bool
