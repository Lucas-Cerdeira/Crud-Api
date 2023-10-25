from fastapi import HTTPException, status, APIRouter
from utils import validate
from models.models import User, User_Update

users = []

router = APIRouter()

@router.get("/user")
async def show_all_users():
    if not len(users) == 0:
        return users
    
    return {"Mensagem":"Nenhum usuário cadastrado."}


@router.get("/user/{cpf}")
async def user_by_cpf(cpf:str):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')
 
    for user in users:
        if user.cpf == cpf:
            return user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')



@router.post("/user/register", response_model=User)
async def register_user(user:User):
    if not validate(user.cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')

    if user.cpf in map(lambda x:x.cpf, users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Usuário já cadastrado.')
    
    users.append(user)
    
    return user



@router.put("/user/alter_data/{cpf}", response_model=User)#response model
async def alter_user_data(cpf, user_update:User_Update):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')

    for user in users:
        if user.cpf == cpf:
            
            if user_update.first_name:
                user.first_name = user_update.first_name
            if user_update.last_name:
                user.last_name = user_update.last_name
            if user_update.day:
                user.day = user_update.day
            if user_update.month:
                user.month = user_update.month
            if user_update.year:
                user.year = user_update.year
            if user_update.job_role:
                user.job_role = user_update.job_role

            return user 
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')



@router.delete("/user/delete/{cpf}")
async def delete_user(cpf:str):
    if not validate(cpf):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Cpf inválido.')
    
    if not cpf in map(lambda x:x.cpf, users):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado.')
    
    for user in users:
        if user.cpf == cpf:
            users.remove(user)
            return {"Success":"Usuário deletado com sucesso."}
    