from pydantic import BaseModel, validator
from typing import Optional, Union
from datetime import date


class User(BaseModel):
    first_name: str
    last_name: str
    day: int
    month: int
    year: int
    job_role: str | None = None
    cpf: str



    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'
    
    
    @property
    def data_nascimento(self):
        return date(year=self.year, month=self.month, day=self.day).isoformat()


    @property
    def age(self) -> int:
        data_atual = date.today()
        age = data_atual.year - self.data_nascimento.year

        # Verifica se a data de nascimento já ocorreu este ano
        if (data_atual.month, data_atual.day) < (self.data_nascimento.month, self.data_nascimento.day):
            age -= 1

        return age
    
    @validator('*')
    def check_empt_values(cls, values):
        if str(values) == '':
            raise ValueError("Empty values are not aceptable.")
        return values



class User_Update(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    job_role: Optional[str] = None


    @property
    def data_nascimento(self):
        return date(year=self.year, month=self.month, day=self.day).isoformat()
    
