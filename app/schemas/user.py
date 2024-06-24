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
from .role import RoleResponse


config = ConfigDict(from_attributes=True)


class Citizenship(str, Enum):
    uzbekistan = "uzbekistan"
    foreign = "foreign"
    without_citizenship = "without_citizenship"


class Gender(str, Enum):
    male = "male"
    female = "female"


class ScienceDegree(str, Enum):
    without = "without"
    doctorofphilosophy = "doctorofphilosophy"
    doctorofscience = "doctorofscience"


class ScientificTitle(str, Enum):
    without = "without"
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
    role_name: str = Field(
        title="Role’s name", description="Role’s name", examples=["user"]
    )
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
    science_degree: ScienceDegree = Field(
        title="User’s science degree",
        description="User’s science degree",
        examples=["without", "doctorofphilosophy", "doctorofscience"],
    )
    scientific_title: ScientificTitle = Field(
        title="User’s science title",
        description="User’s science title",
        examples=["without", "docent", "professor", "senior_researcher", "academician"],
    )
    first_name: str = Field(
        title="User’s first name", description="User’s first name", examples=["Anvar"]
    )
    last_name: str = Field(
        title="User’s last name", description="User’s last name", examples=["Anvarov"]
    )
    middle_name: str = Field(
        title="User’s last name",
        description="User’s last name",
        examples=["Anvarovich"],
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
        min_length=6,
        max_length=32,
    )


class UserResponse(BaseModel):
    model_config = config
    user_id: UUID = Field(title="User’s id", description="User’s id")
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
    science_degree: ScienceDegree = Field(
        title="User’s science degree",
        description="User’s science degree",
        examples=["without", "doctorofphilosophy", "doctorofscience"],
    )
    scientific_title: ScientificTitle = Field(
        title="User’s science title",
        description="User’s science title",
        examples=["without", "docent", "professor", "senior_researcher", "academician"],
    )
    first_name: str = Field(
        title="User’s first name", description="User’s first name", examples=["Anvar"]
    )
    last_name: str = Field(
        title="User’s last name", description="User’s last name", examples=["Anvarov"]
    )
    middle_name: str = Field(
        title="User’s last name",
        description="User’s last name",
        examples=["Anvarovich"],
    )
    role: Optional[RoleResponse] = None


class UserUpdate(BaseModel):
    user_id: Optional[UUID] = Field(
        default=None, title="User’s id", description="User’s id"
    )
    role_name: Optional[str] = Field(
        default=None, title="Role’s name", description="Role’s name"
    )
    phone_number: Optional[str] = Field(
        default=None,
        title="User’s phone number",
        description="User’s phone number",
        examples=["+998901234567"],
    )
    citizenship: Optional[Citizenship] = Field(
        default=None,
        title="User’s citizenship",
        description="User’s citizenship",
        examples=["uzbekistan", "foreign", "without_citizenship"],
    )
    passport: Optional[
        Annotated[str, StringConstraints(pattern=r"^[A-Z]{2}\d{7}$")]
    ] = None
    pini: Optional[Annotated[str, StringConstraints(pattern=r"^\d{14}$")]] = Field(
        default=None,
        title="User’s personal identify number",
        description="User’s personal identify number",
        examples=["40608200485164"],
    )
    birth_date: Optional[date] = None
    gender: Optional[Gender] = Field(
        default=None,
        title="User’s gender",
        description="User’s gender",
        examples=["male", "female"],
    )
    address: Optional[str] = Field(
        default=None,
        title="User’s address",
        description="User’s address",
        examples=[
            "Namangan viloyati, Turaqo'rg'on tumani, Sharq MFY, Bog' ko'cha 18-uy"
        ],
    )
    specialization: Optional[str] = None
    science_degree: Optional[ScienceDegree] = Field(
        default=None,
        title="User’s science degree",
        description="User’s science degree",
        examples=["without", "doctorofphilosophy", "doctorofscience"],
    )
    scientific_title: Optional[ScientificTitle] = Field(
        default=None,
        title="User’s science title",
        description="User’s science title",
        examples=["without", "docent", "professor", "senior_researcher", "academician"],
    )
    first_name: Optional[str] = Field(
        default=None,
        title="User’s first name",
        description="User’s first name",
        examples=["Anvar"],
    )
    last_name: Optional[str] = Field(
        default=None,
        title="User’s last name",
        description="User’s last name",
        examples=["Anvarov"],
    )
    middle_name: Optional[str] = Field(
        default=None,
        title="User’s middle name",
        description="User’s middle name",
        examples=["Anvarovich"],
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
