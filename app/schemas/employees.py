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

from .user import UserResponse
from .division import DivisionResponse
from .department import DepartmentResponse


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


class EmployeeCreate(BaseModel):
    user_id: UUID = Field(title="Users’s ID", description="Users’s ID")
    division_id: Optional[UUID] = Field(
        None, title="Division’s ID", description="Division’s ID"
    )
    department_id: Optional[UUID] = Field(
        None, title="Department’s ID", description="Department’s ID"
    )
    type: EmployeeType = Field(
        title="Employee’s type",
        description="Employee’s type",
        examples=[
            "professor_teacher",
            "administrative_management",
            "training_assistent",
            "technik",
        ],
    )
    labor_form: LaborForm = Field(
        title="Labor Form",
        description="Labor Form",
        examples=["main", "replacement_interior", "replacement_extrior", "hourly"],
    )
    rate: Rate = Field(title="Rate", description="Rate", examples=[0.25, 0.5, 0.75, 1])
    status: EmployeeStatus = Field(
        title="Employee status",
        description="Employee status",
        examples=["working", "on_vocation", "on_trip", "dismissed"],
    )
    contract_number: int
    contract_date: date


class EmployeeResponse(BaseModel):
    employee_id: UUID = Field(title="Employee’s ID", description="Employee’s ID")
    division_id: Optional[UUID] = Field(
        None, title="Division’s ID", description="Division’s ID"
    )
    department_id: Optional[UUID] = Field(
        None, title="Department’s ID", description="Department’s ID"
    )
    type: EmployeeType = Field(
        title="Employee’s type",
        description="Employee’s type",
        examples=[
            "professor_teacher",
            "administrative_management",
            "training_assistent",
            "technik",
        ],
    )
    labor_form: LaborForm = Field(
        title="Labor Form",
        description="Labor Form",
        examples=["main", "replacement_interior", "replacement_extrior", "hourly"],
    )
    rate: Rate = Field(title="Rate", description="Rate", examples=[0.25, 0.5, 0.75, 1])
    status: EmployeeStatus = Field(
        title="Employee status",
        description="Employee status",
        examples=["working", "on_vocation", "on_trip", "dismissed"],
    )
    contract_number: int
    contract_date: date


class EmployeeFullResponse(BaseModel):
    employee_id: UUID = Field(title="Employee’s ID", description="Employee’s ID")
    type: EmployeeType = Field(
        title="Employee’s type",
        description="Employee’s type",
        examples=[
            "professor_teacher",
            "administrative_management",
            "training_assistent",
            "technik",
        ],
    )
    labor_form: LaborForm = Field(
        title="Labor Form",
        description="Labor Form",
        examples=["main", "replacement_interior", "replacement_extrior", "hourly"],
    )
    rate: Rate = Field(title="Rate", description="Rate", examples=[0.25, 0.5, 0.75, 1])
    status: EmployeeStatus = Field(
        title="Employee status",
        description="Employee status",
        examples=["working", "on_vocation", "on_trip", "dismissed"],
    )
    contract_number: int
    contract_date: date
    user: UserResponse
    division: Optional[DivisionResponse]
    department: Optional[DepartmentResponse]
