from fastapi.testclient import TestClient
import pytest
from pytest import mark
import main
from models import User, User_Update

client = TestClient(main.app)



#Fazer um mock
def test_alter_user_data_when_cpf_invalido():
    user = {
    "first_name": "Gabriel",
    "last_name": "Cerdeira",
    "age": 20,
    "cpf": "897.789.610-10"
}
    response = client.put("/user/alter_data/897.789.610-10", json=user)

    assert response.status_code == 409
    assert response.json() == {"detail":"Cpf inválido."}



@mark.first_name_test
@mark.put
def test_alter_user_first_name():
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf='897.789.610-00')
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

    response = client.put("/user/alter_data/897.789.610-00", json=new_firs_name)

    assert response.status_code == 200
    assert response.json() == expected_user
    assert user_1 in main.users
    main.users.remove(user_1)

@mark.first_name_test
@mark.put
def test_alter_first_name_when_igual_o_anterior():
    user_1 = User(first_name='Gabriel', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    main.users.append(user_1)
    
    new_firs_name = {
    "first_name": "Gabriel",
    "last_name": None,
    "age": None,
}

    response = client.put("/user/alter_data/897.789.610-00", json=new_firs_name)

    assert response.status_code == 409
    assert response.json() == {"detail":"Nome não alterado, novo name não pode ser igual o anterior."}
    main.users.remove(user_1)


@mark.last_name_test
@mark.put
def test_alter_user_last_name():
    user_1 = User(first_name='Marcos', last_name='Cerdeira', age=20, cpf='897.789.610-00')
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

    response = client.put("/user/alter_data/897.789.610-00", json=new_last_name)

    assert response.status_code == 200
    assert response.json() == expected_user
    assert user_1 in main.users
    main.users.remove(user_1)


@mark.last_name_test
@mark.put
def test_alter_last_name_when_igual_o_anterior():
    user_1 = User(first_name='Gabriel', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    main.users.append(user_1)
    
    new_last_name = {
    "first_name": None,
    "last_name": "Cerdeira",
    "age": None,
}

    response = client.put("/user/alter_data/897.789.610-00", json=new_last_name)

    assert response.status_code == 409
    assert response.json() == {"detail":"Nome não alterado, novo sobrenome não pode ser igual o anterior."}
    main.users.remove(user_1)

@mark.age
def test_alter_user_age():
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
    
    response = client.put("/user/alter_data/897.789.610-00", json=new_age)

    assert response.status_code == 200
    assert response.json() == expected_user
    main.users.remove(user_1)

@mark.age
def test_alter_user_age_when_igual_o_anterior():
    user_1 = User(first_name='Gabriel', last_name='Cerdeira', age=20, cpf='897.789.610-00')
    main.users.append(user_1)

    new_age = {
    "first_name": None,
    "last_name": None,
    "age": 20
    }

    response = client.put("/user/alter_data/897.789.610-00", json=new_age)

    assert response.status_code == 409
    assert response.json() == {"detail":"Idade não alterada, idade não pode ser igual o anterior."}
    main.users.remove(user_1)




