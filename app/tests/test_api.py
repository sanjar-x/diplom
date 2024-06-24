from datetime import date
from typing import Any, Dict
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_role():
    response = client.post("/roles/", json={"name": "admin"})
    print(response)
    assert response.status_code == 201
    response_data: Dict[str, Any] = response.json()
    assert response_data.get("name") == "admin"


def test_create_user():
    response = client.post(
        url="/roles/",
        json={
            "role_name": "admin",
            "citizenship": "uzbekistan",
            "passport": "AB123456",
            "pini": "12345678901234",
            "birth_date": "2024-06-24",
            "gender": "female",
            "address": "Namangan viloyati, Turaqo'rg'on tumani",
            "specialization": "Engineer programmer",
            "science_degree": "doctorofphilosophy",
            "scientific_title": "docent",
            "first_name": "Mashxura",
            "last_name": "Sodiqova",
            "middle_name": "Shuxrat qizi",
            "phone_number": "+998948713838",
            "password": "supersecret",
        },
    )
    assert response.status_code == 200
    response_data: Dict[str, Any] = response.json()
    assert response_data["first_name"] == "Mashxura"
    assert response_data["role"]["name"] == "admin"
