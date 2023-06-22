from pydantic import BaseModel, validator
from typing import Optional



class User(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    age: int
    cpf: str


class User_Update(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None





