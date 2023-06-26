from fastapi.testclient import TestClient
from pytest import mark
import pytest
import main
from models.models import User


client = TestClient(main.app)




def test_register_user():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Lobato",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "090.163.990-70"
}
    
    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user
    assert expected_user in main.users
    main.users.remove(expected_user)
    

def test_register_cpf_invalido():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Lobato",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "090.163.990-72"
}
    
    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 409, "Status code != 409"
    assert response.json() == {"detail":"Cpf inválido."}



def test_user_ja_cadastrado():
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Lobato",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "090.163.990-70"
}
    
    test_user = User(first_name='Marcos', last_name='Vinicius', day=19,month=8, year=2005, job_role="Intern Assosiate", cpf="090.163.990-70")        

    main.users.append(test_user)

    response = client.post("/user/register", json=expected_user)

    assert response.status_code == 409, "Status code != 409"
    assert response.json() == {"detail":"Usuário já cadastrado."}, "Retorno diferente do esperado"
    assert test_user in main.users, "Usuário não estava cadastrado como era esperado"
    main.users.remove(test_user)
    
