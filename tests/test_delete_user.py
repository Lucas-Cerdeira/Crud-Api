from fastapi.testclient import TestClient
import main
from models.models import User
import pytest



client = TestClient(main.app)


def test_delete_user():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)

    response = client.delete(f"/user/delete/{cpf}")
    
    assert response.status_code == 200, "Status code != 200"
    assert response.json() == {"Success":"Usuário deletado com sucesso."}, "Retorno diferente do esperado"
    assert not user_1 in main.users, "user_1 não foi deletado"



def test_delete_user_when_cpf_invalido():
    cpf = "897.789.610-10"

    response = client.delete(f"/user/delete/{cpf}")

    assert response.status_code == 409
    assert response.json() == {"detail":"Cpf inválido."}


def test_delete_user_when_usuario_nao_encontrado():
    cpf = "897.789.610-00"

    response = client.delete(f"/user/delete/{cpf}")

    assert response.status_code == 404, "Status code != 404"
    assert response.json() == {"detail":"Usuário não encontrado."}, "Retorno diferente do esperado"







