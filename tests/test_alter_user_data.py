from fastapi.testclient import TestClient
import pytest
from pytest import mark
import main
from models import User, User_Update

client = TestClient(main.app)



#Fazer um mock
def test_alter_user_data_when_cpf_invalido():
    cpf = "897.789.610-10"
    user = {
    "first_name": "Gabriel",
    "last_name": "Cerdeira",
    "age": 20,
    "cpf": "897.789.610-10"
}
    response = client.put(f"/user/alter_data/{cpf}", json=user)

    assert response.status_code == 409, "Status code != 409"
    assert response.json() == {"detail":"Cpf inválido."}, "Cpf é válido"



@mark.first_name_test
@mark.put
def test_alter_user_first_name():
    cpf = "897.789.610-00"
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf=cpf)
    main.users.append(user_1)
    
    expected_user = {
    "first_name": "Gabriel",
    "last_name": "Cerdeira",
    "age": 20,
    "cpf": "897.789.610-00"
}
    
    new_firs_name = {
    "first_name": "Gabriel",
    "last_name": None,
    "age": None,
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_firs_name)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)


@mark.last_name_test
@mark.put
def test_alter_user_last_name():
    cpf = "897.789.610-00"
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf=cpf)
    main.users.append(user_1)
    
    new_last_name = {
    "first_name": None,
    "last_name": "Lobato",
    "age": None,
}
    
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Lobato",
    "age": 20,
    "cpf": "897.789.610-00"
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_last_name)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)



@mark.age
def test_alter_user_age():
    cpf = "897.789.610-00"
    user_1 = User(first_name='Gabriel', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    main.users.append(user_1)

    expected_user = {
    "first_name": "Gabriel",
    "last_name": "Cerdeira",
    "age": 25,
    "cpf": "897.789.610-00"
}
    
    new_age = {
    "first_name": None,
    "last_name": None,
    "age": 25,
    }
    
    response = client.put(f"/user/alter_data/{cpf}", json=new_age)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)





