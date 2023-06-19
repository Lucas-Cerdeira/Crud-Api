from fastapi.testclient import TestClient
from main import app
import main
from models import User
import pytest


client = TestClient(app)


def test_show_users_with_users():
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    user_2 = User(first_name='Pedro', last_name='Santos', age=32, cpf='856.139.390-47')
    main.users.append(user_1)
    main.users.append(user_2)
    response = client.get("/user")

    assert response.status_code == 200
    assert response.json() == main.users
    assert user_1 in main.users
    main.users.remove(user_1)
    assert user_2 in main.users
    main.users.remove(user_2)



def test_show_users_without_users():
    main.users = []
    response = client.get("/user")

    assert response.status_code == 200
    assert response.json() == {"Mensagem":"Nenhum usuário cadastrado."}



    

