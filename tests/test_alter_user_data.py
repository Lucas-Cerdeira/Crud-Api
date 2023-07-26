from fastapi.testclient import TestClient
import pytest
from pytest import mark
import main
from models.models import User, User_Update

client = TestClient(main.app)





def test_alter_user_data_when_cpf_invalido():
    cpf = "897.789.610-10"
    user = {
    "name": "Marcos",
    "last_name": "Vinicius",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": cpf
}
    
    response = client.put(f"/user/alter_data/{cpf}", json=user)

    assert response.status_code == 409, "Status code != 409"
    assert response.json() == {"detail":"Cpf inválido."}, "Cpf é válido"




def test_alter_user_first_name():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)
    
    expected_user = {
    "first_name": "Gabriel",
    "last_name": "Vinicius",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "897.789.610-00"
}
        
    new_firs_name = {
        "first_name": "Gabriel",
}
    
    response = client.put(f"/user/alter_data/{cpf}", json=new_firs_name)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)



def test_alter_user_last_name():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)
    
    new_last_name = {
    "last_name": "Lobato"
}
    
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Lobato",
    "day": 19,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "897.789.610-00"
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_last_name)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)



### Criar test_alter_user_Day
def test_alter_user_day():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)
    
    new_day = {
    "day": 25
}
    
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "day": 25,
    "month": 8,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "897.789.610-00"
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_day)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)

    
### Criar test_alter_user_Month
def test_alter_user_month():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)
    
    new_month = {
    "month": 5
}
    
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "day": 19,
    "month": 5,
    "year": 2005,
    "job_role": "Intern Assosiate",
    "cpf": "897.789.610-00"
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_month)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)

### Criar test_alter_user_Year
def test_alter_user_year():
    cpf = "897.789.610-00"
    user_1 = User(first_name="Marcos", last_name="Vinicius", day=19, month=8, year=2005, job_role="Intern Assosiate", cpf="897.789.610-00")
    main.users.append(user_1)
    
    new_year = {
    "year": 2004
}
    
    expected_user = {
    "first_name": "Marcos",
    "last_name": "Vinicius",
    "day": 19,
    "month": 8,
    "year": 2004,
    "job_role": "Intern Assosiate",
    "cpf": "897.789.610-00"
}

    response = client.put(f"/user/alter_data/{cpf}", json=new_year)

    assert response.status_code == 200, "Status code != 200"
    assert response.json() == expected_user, "Diferente do retorno esperado"
    main.users.remove(user_1)

