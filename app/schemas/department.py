from enum import Enum
from typing import Annotated, Optional
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

config = ConfigDict(from_attributes=True)
from .faculty import FacultyResponse


class DepartmentCreate(BaseModel):
    faculty_id: UUID
    name: str = Field(
        title="Department’s name",
        description="Department’s name",
        examples=[
            "Energiya tejamkorligi va muqobil energiya manbalari",
            "Qishloq xo‘jaligini mexanizatsiyalashtirish",
            "Foydali qazilmalar va qayta ishlash texnologiyalari",
            "Arxitektura",
            "Muhandislik va kompyuter grafikasi",
            "Metrologiya va standartlashtirish",
            "Yo‘l harakati xavfsizligi",
            "O‘zbek tili va adabiyoti",
        ],
    )
    code: Annotated[str, StringConstraints(max_length=2, pattern=r"^\d{2}$")] = Field(
        title="Faculty’s identify code",
        description="Faculty’s identify code",
        examples=["01", "02"],
    )
    active: bool


class DepartmentResponse(BaseModel):
    department_id: UUID
    name: str = Field(
        title="Department’s name",
        description="Department’s name",
        examples=[
            "Energiya tejamkorligi va muqobil energiya manbalari",
            "Qishloq xo‘jaligini mexanizatsiyalashtirish",
            "Foydali qazilmalar va qayta ishlash texnologiyalari",
            "Arxitektura",
            "Muhandislik va kompyuter grafikasi",
            "Metrologiya va standartlashtirish",
            "Yo‘l harakati xavfsizligi",
            "O‘zbek tili va adabiyoti",
        ],
    )
    code: Annotated[str, StringConstraints(max_length=2, pattern=r"^\d{2}$")] = Field(
        title="Faculty’s identify code",
        description="Faculty’s identify code",
        examples=["01", "02"],
    )
    active: bool


class DepartmentFullResponse(DepartmentResponse):
    faculty: FacultyResponse
