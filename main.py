from fastapi import FastAPI, HTTPException, status, Depends
from models import User, User_Update
from utils import validate



app = FastAPI()


users = []



@app.get("/")
async def root():
    return {"mensagem":"Hello World!!!"}



@app.get("/user")
async def show_all_users():
    if not len(users) == 0:
        return users
    
    return {"Mensagem":"Nenhum usuário cadastrado."}


@app.get("/user/{cpf}")
async def user_by_cpf(cpf:str):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')
 
    for user in users:
        if user.cpf == cpf:
            return user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')


@app.post("/user/register", response_model=User)
async def register_user(user:User):
    if not validate(user.cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')

    if user.cpf in map(lambda x:x.cpf, users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Usuário já cadastrado.')
    
    users.append(user)
    
    return user



@app.put("/user/alter_data/{cpf}", response_model=User)#response model
async def alter_user_data(cpf, user_update:User_Update):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')

    for user in users:
        if user.cpf == cpf:
            
            if user_update.first_name:
                user.first_name = user_update.first_name
            if user_update.last_name:
                user.last_name = user_update.last_name
            if user_update.age:
                user.age = user_update.age

            return user 
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')



@app.delete("/user/delete/{cpf}")
async def delete_user(cpf:str):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')
    
    if not cpf in map(lambda x:x.cpf, users):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')
    
    for user in users:
        if user.cpf == cpf:
            users.remove(user)
            return {"Success":"Usuário deletado com sucesso."}
    