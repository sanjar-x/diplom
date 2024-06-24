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
    code: Annotated[str, StringConstraints(max_length=3, pattern=r"^\d{3}$")] = Field(
        title="Faculty’s identify code",
        description="Faculty’s identify code",
        examples=["001", "002"],
    )
    type: FacultyType = Field(
        title="Faculty’s type",
        description="Faculty’s type",
        examples=["local", "joint", "division", "other"],
    )


class FacultyResponse(BaseModel):
    faculty_id: UUID = Field(title="Faculty’s id", description="Faculty’s id")
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
