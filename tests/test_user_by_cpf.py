from fastapi.testclient import TestClient
import main
import pytest
from pytest import mark
from models import User


client = TestClient(main.app)



def test_user_by_cpf():
    cpf = "897.789.610-00"

    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    user_2 = User(first_name='Pedro', last_name='Santos', age=32, cpf='856.139.390-47')
        
    main.users.append(user_1)
    main.users.append(user_2)

    response = client.get("/user/897.789.610-00")

    for user in main.users:
        if user.cpf == cpf:
            expected_user = user

    assert response.status_code == 200
    assert response.json() == expected_user

    assert user_1 in main.users
    main.users.remove(user_1)
    
    assert user_2 in main.users
    main.users.remove(user_2)



def test_user_invalid_cpf():
    cpf = "897.789.610-10"
    response = client.get("/user/897.789.610-10")
    
    assert response.status_code == 409
    assert response.json() == {"detail": "Cpf inválido."}


def test_user_not_found():
    cpf = "666.116.780-77"

    response = client.get("user/666.116.780-77")

    assert response.status_code == 404
    assert response.json() == {"detail":"Usuário não encontrado."}

