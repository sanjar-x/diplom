from __future__ import annotations
import uuid
from enum import Enum
from datetime import date
from typing import List, Any
from starlette import status
from pydantic import SecretStr
from bcrypt import gensalt, hashpw
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from sqlalchemy import ForeignKey
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    joinedload,
)
from sqlalchemy.dialects.postgresql import (
    INTEGER,
    VARCHAR,
    TEXT,
    UUID,
    DATE,
    BYTEA,
    BOOLEAN,
    ENUM,
)


class Citizenship(Enum):
    uzbekistan = "uzbekistan"
    foreign = "foreign"
    without_citizenship = "without_citizenship"


class Gender(Enum):
    male = "male"
    female = "female"


class ScienceDegree(Enum):
    none = None
    doctorofphilosophy = "doctorofphilosophy"
    doctorofscience = "doctorofscience"


class ScientificTitle(str, Enum):
    none = None
    docent = "docent"
    professor = "professor"
    senior_researcher = "senior_researcher"
    academician = "academician"


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


class Base(AsyncAttrs, DeclarativeBase):
    async def save(self, session: AsyncSession):
        try:
            session.add(self)
            await session.commit()
            await session.refresh(self)
            return self

        except SQLAlchemyError as exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(exception)
            ) from exception

    async def delete(self, session: AsyncSession):
        try:
            await session.delete(self)
            await session.commit()
            return True
        except SQLAlchemyError as exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(exception)
            ) from exception

    async def update(self, session: AsyncSession, **kwargs):
        try:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return await session.commit()
        except SQLAlchemyError as exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(exception)
            ) from exception

    @classmethod
    async def find_all(cls, database_session: AsyncSession):
        _result = await database_session.execute(select(cls))
        return list(_result.scalars().all())

    @classmethod
    async def find_all_with(cls, database_session: AsyncSession, options: List[Any]):
        _stmt = select(cls).options(*options)
        _result = await database_session.execute(_stmt)
        return list(_result.scalars().all())

    @classmethod
    async def find(cls, database_session: AsyncSession, where: list[Any]):
        _stmt = select(cls).where(*where)
        _result = await database_session.execute(_stmt)
        return _result.scalars().first()

    @classmethod
    async def find_with(
        cls, database_session: AsyncSession, options: List[Any], where: List[Any]
    ):
        _stmt = select(cls).options(*options).where(*where)
        _result = await database_session.execute(_stmt)
        return _result.scalars().first()


crypt_context = CryptContext(schemes=["bcrypt"])


class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(TEXT, nullable=False)
    users: Mapped[List[User]] = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("roles.role_id")
    )
    citizenship: Mapped[Enum] = mapped_column(ENUM(Citizenship))
    passport: Mapped[str] = mapped_column(VARCHAR(9), nullable=False)
    pini: Mapped[str] = mapped_column(VARCHAR(14), nullable=False)
    birth_date: Mapped[date] = mapped_column(DATE)
    gender: Mapped[Enum] = mapped_column(ENUM(Gender))
    address: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    specialization: Mapped[str] = mapped_column(VARCHAR(255))
    science_degree: Mapped[Enum] = mapped_column(ENUM(ScienceDegree))
    scientific_title: Mapped[Enum] = mapped_column(ENUM(ScientificTitle))
    first_name: Mapped[str] = mapped_column(VARCHAR(31), nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR(31), nullable=False)
    middle_name: Mapped[str] = mapped_column(VARCHAR(31), nullable=False)
    phone_number: Mapped[str] = mapped_column(VARCHAR(15), unique=True, nullable=False)
    _password: Mapped[bytes] = mapped_column(BYTEA(60), nullable=False)
    image: Mapped[str] = mapped_column(TEXT, nullable=True)

    @property
    def password(self):
        return self._password.decode("utf-8")

    @password.setter
    def password(self, password: SecretStr):
        _secret_value = password.get_secret_value()
        self._password = hashpw(_secret_value.encode("utf-8"), gensalt())

    role: Mapped[Role] = relationship("Role", back_populates="users")
    employee: Mapped[Employee] = relationship("Employee", back_populates="user")

    def check_password(self, password: SecretStr):
        return crypt_context.verify(password.get_secret_value(), self.password)


class Faculty(Base):
    __tablename__ = "faculties"

    faculty_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    code: Mapped[str] = mapped_column(VARCHAR(3), nullable=False)
    type: Mapped[Enum] = mapped_column(ENUM(FacultyType), nullable=False)
    active: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    departments: Mapped[List[Department]] = relationship(
        "Department", back_populates="faculty"
    )


class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    faculty_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("faculties.faculty_id")
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    code: Mapped[str] = mapped_column(VARCHAR(2), nullable=False)
    active: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    faculty: Mapped[Faculty] = relationship("Faculty", back_populates="departments")


class Division(Base):
    __tablename__ = "divisions"
    division_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    code: Mapped[str] = mapped_column(VARCHAR(3), nullable=False)
    type: Mapped[Enum] = mapped_column(ENUM(DivisionType))
    active: Mapped[bool] = mapped_column(BOOLEAN, default=True)


class Positions(Base):
    __tablename__ = "positions"

    position_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Employee(Base):
    __tablename__ = "employies"
    employee_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id")
    )
    department_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    division_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    type: Mapped[Enum] = mapped_column(
        ENUM(EmployeeType), default=EmployeeType.professor_teacher
    )
    labor_form: Mapped[Enum] = mapped_column(ENUM(LaborForm))
    rate: Mapped[Enum] = mapped_column(ENUM(Rate))
    status: Mapped[Enum] = mapped_column(ENUM(EmployeeStatus))
    contract_number: Mapped[int] = mapped_column(INTEGER, nullable=False)
    contract_date: Mapped[date] = mapped_column(DATE)

    user: Mapped[User] = relationship("User", back_populates="employee")


class QualificationPlace(Base):
    __tablename__ = "qualification_places"
    place_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Qualification(Base):
    __tablename__ = "qualifications"
    qualification_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    employee_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    position_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    place_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)
    theme: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    year: Mapped[str] = mapped_column(VARCHAR(4))
    start_date: Mapped[date] = mapped_column(DATE)
    end_date: Mapped[date] = mapped_column(DATE)
    document: Mapped[str] = mapped_column(VARCHAR(255))


class Contest(Base):
    __tablename__ = "contests"
    contest_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    employee_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    position_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    theme: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    year: Mapped[str] = mapped_column(VARCHAR(4))
    start_date: Mapped[date] = mapped_column(DATE)
    end_date: Mapped[date] = mapped_column(DATE)
    document: Mapped[str] = mapped_column(VARCHAR(255))
