# from datetime import date
# from enum import Enum
# from pydantic import SecretStr
# import pytest
# import asyncio
# import uuid
# from sqlalchemy.engine import make_url
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

# from app.models.models import (
#     Base,
#     Division,
#     Role,
#     User,
#     Faculty,
#     Department,
#     Citizenship,
#     Gender,
#     ScienceDegree,
#     ScientificTitle,
#     FacultyType,
#     DivisionType,
# )


# engine = create_async_engine(
#     url=make_url(
#         name_or_url="postgresql+asyncpg://root:iam3489495@localhost:5432/test"
#     ),
#     echo=True,
#     future=True,
# )

# async_session = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


# @pytest.mark.asyncio
# async def test_create_user():

#     async with async_session() as session:
#         role = Role(name="test_role")
#         role = await role.save(session)
#         assert role.name == "test_role"
#         user = User(
#             role_id=role.role_id,
#             citizenship=Citizenship.foreign,
#             passport="AB123456",
#             pini="12345678901234",
#             birth_date=date(1999, 9, 17),
#             gender=Gender.male,
#             address="Namangan viloyati, Turaqo'rg'on tumani",
#             specialization="Test Specialization",
#             science_degree=ScienceDegree.doctorofphilosophy,
#             scientific_title=ScientificTitle.docent,
#             first_name="Mashxura",
#             last_name="Sodiqova",
#             middle_name="Shuxrat qizi",
#             phone_number="+998948713838",
#             password=SecretStr("supersecret"),
#         )
#         role = await user.save(session)
#         assert user.user_id is not None
#         assert user.role_id == role.role_id
#         assert user.citizenship == Citizenship.foreign

#         faculty = Faculty(
#             name="Sanoatni axborotlshtirish",
#             code="SA",
#             type=FacultyType.local,
#             active=True,
#         )
#         await faculty.save(session)
#         assert faculty.name == "Sanoatni axborotlshtirish"
#         assert faculty.code == "SA"
#         assert faculty.type == FacultyType.local
#         assert faculty.active == True

#         department = Department(
#             faculty_id=faculty.faculty_id,
#             name="Axborot tizmlari va texnologiyalari",
#             code="AT",
#             active=True,
#         )
#         await faculty.save(session)
#         assert department.name == "Axborot tizmlari va texnologiyalari"
#         assert department.code == "AT"
#         assert department.active == True

#         division = Division(
#             name="Kadrlar bo'limi", code="99", type=DivisionType.division, active=True
#         )
#         session.add(division)
#         await session.commit()
#         await session.refresh(division)
#         assert division.name == "Kadrlar bo'limi"
#         assert division.code == "99"
#         assert division.type == DivisionType.division
#         assert division.active == True
