from fastapi.testclient import TestClient
from main import app
import main
from models.models import User
import pytest


client = TestClient(app)


def test_show_users_with_many_users():
    user_1 = User(first_name='Marcos', last_name='Vinicius', day=19,month=8, year=2005, job_role="Intern Assosiate", cpf="090.163.990-70")
    user_2 = User(first_name='Lucas', last_name='Felipe', day=29 ,month=10, year=2002, job_role="Intern Assosiate", cpf="373.443.960-41")
    main.users.append(user_1)
    main.users.append(user_2)
    response = client.get("/user")

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == main.users, "Retorno diferente do esperado"
    assert user_1 in main.users
    main.users.remove(user_1)
    assert user_2 in main.users
    main.users.remove(user_2)



def test_show_users_without_users():
    main.users = []
    response = client.get("/user")

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == {"Mensagem":"Nenhum usuário cadastrado."}, "Retorno diferente do esperado"



    

