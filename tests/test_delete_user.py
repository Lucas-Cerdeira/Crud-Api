from fastapi.testclient import TestClient
import main
from models import User
import pytest



client = TestClient(main.app)


def test_delete_user():
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    main.users.append(user_1)

    response = client.delete("/user/delete/897.789.610-00")
    
    assert response.status_code == 200
    assert response.json() == {"Success":"Usuário deletado com sucesso."}
    assert not user_1 in main.users



def test_delete_user_when_cpf_invalido():

    response = client.delete("/user/delete/897.789.610-10")

    assert response.status_code == 409
    assert response.json() == {"detail":"Cpf inválido."}


def test_delete_user_when_usuario_nao_encontrado():

    response = client.delete("/user/delete/499.576.410-00")

    assert response.status_code == 404
    assert response.json() == {"detail":"Usuário não encontrado."}







