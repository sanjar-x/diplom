from enum import Enum
from uuid import UUID
from datetime import date
from typing import Annotated, Optional
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


class Citizenship(str, Enum):
    uzbekistan = "uzbekistan"
    foreign = "foreign"
    without_citizenship = "without_citizenship"


class Gender(str, Enum):
    male = "male"
    female = "female"


class ScienceDegree(str, Enum):
    none = None
    doctorofphilosophy = "doctorofphilosophy"
    doctorofscience = "doctorofscience"


class ScientificTitle(str, Enum):
    none = None
    docent = "docent"
    professor = "professor"
    senior_researcher = "senior_researcher"
    academician = "academician"


class User(BaseModel):
    id: UUID = Field(title="User’s id", description="User’s id")
    model_config = config
    phone_number: str = Field(
        title="User’s phone number",
        description="User’s phone number",
        examples=["+998901234567"],
    )
    first_name: str = Field(
        title="User’s first name", description="User’s first name", examples=["Anvar"]
    )
    last_name: str = Field(
        title="User’s last name", description="User’s last name", examples=["Anvarov"]
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
        min_length=6,
        max_length=32,
    )
    admin: bool = Field(
        title="Checkbox",
        description="Admin status",
        examples=[True, False],
    )


class UserCreate(BaseModel):
    model_config = config
    phone_number: str = Field(
        title="User’s phone number",
        description="User’s phone number",
        examples=["+998901234567"],
    )
    citizenship: Citizenship = Field(
        title="User’s citizenship",
        description="User’s citizenship",
        examples=["uzbekistan", "foreign", "without_citizenship"],
    )
    passport: Annotated[str, StringConstraints(pattern=r"^[A-Z]{2}\d{7}$")]
    pini: Annotated[str, StringConstraints(pattern=r"^\d{14}$")] = Field(
        title="User’s personal identify number",
        description="User’s personal identify number",
        examples=["40608200485164"],
    )
    birth_date: date
    gender: Gender = Field(
        title="User’s gender",
        description="User’s gender",
        examples=["male", "female"],
    )
    address: str = Field(
        title="User’s address",
        description="User’s address",
        examples=[
            "Namangan viloyati, Turaqo'rg'on tumani, Sharq MFY, Bog' ko'cha 18-uy"
        ],
    )
    specialization: str
    science_degree: ScienceDegree
    scientific_title: ScientificTitle
    first_name: str = Field(
        title="User’s first name", description="User’s first name", examples=["Anvar"]
    )
    last_name: str = Field(
        title="User’s last name", description="User’s last name", examples=["Anvarov"]
    )
    middle_name: str
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
        min_length=6,
        max_length=32,
    )
    role_id: UUID = Field(title="Role’s id", description="Role’s id")


class UserResponse(BaseModel):
    user_id: UUID = Field(title="User’s id", description="User’s id")
    image: Optional[str] = Field(title="User’s image", description="User’s image")
    first_name: str = Field(title="User’s first name", description="User’s first name")
    last_name: str = Field(title="User’s last name", description="User’s last name")
    phone_number: str = Field(
        title="User’s phone number", description="User’s phone number"
    )


class TokenResponse(BaseModel):
    access_token: str = Field(
        title="User’s access token", description="User’s access token"
    )
    token_type: str = Field(title="User’s token type", description="User’s token type")


class UserLogin(BaseModel):
    model_config = config
    phone_number: str = Field(
        title="User’s phone number",
        description="User’s phone number",
        examples=["+998901234567"],
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
        min_length=6,
        max_length=32,
    )


class FacultyType(str, Enum):
    local = "local"
    joint = "joint"
    division = "division"
    other = "other"


class DivisionType(str, Enum):
    division = "division"
    administration = "administration"
    center = "center"  # type: ignore
    other = "other"


class EmployeeType(str, Enum):
    professor_teacher = "professor_teacher"
    administrative_management = "administrative_management"
    training_assistent = "training_assistent"
    technik = "technik"
    servise = "servise"


class LaborForm(str, Enum):
    main = "main"
    replacement_interior = "replacement_interior"
    replacement_extrior = "replacement_extrior"
    hourly = "hourly"


class Rate(float, Enum):
    quarter = 0.25
    half = 0.5
    three_quarters = 0.75
    one = 1.0


class EmployeeStatus(str, Enum):
    working = "working"
    on_vocation = "on_vocation"
    on_trip = "on_trip"
    dismissed = "dismissed"
