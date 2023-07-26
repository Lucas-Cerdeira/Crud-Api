from pydantic import BaseModel, validator
from typing import Optional
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


    
    @validator('day')
    def day_out_of_range(cls, value):
        if not 1 <= value <= 31:
            raise ValueError("Dia deve estar entre 1 e 31.")
        return value
    
    @validator('month')
    def month_out_of_range(cls, value):
        if not 1 <= value <= 12:
            raise ValueError("Mês deve estar entre 1 e 12.")
        return value
    
    @validator('year')
    def year_out_of_range(cls, value):
        from datetime import datetime
        ano_atual = datetime.today().year

        if not value < ano_atual:
            raise ValueError("Ano deve ser menor que o atual.")
        return value



class User_Update(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    job_role: Optional[str] = None


    @validator('day')
    def day_out_of_range(cls, value):
        if not 1 <= value <= 31:
            raise ValueError("Dia deve estar entre 1 e 31.")
        return value
    
    @validator('month')
    def month_out_of_range(cls, value):
        if not 1 <= value <= 12:
            raise ValueError("Mês deve estar entre 1 e 12.")
        return value
    
    @validator('year')
    def year_out_of_range(cls, value):
        from datetime import datetime
        ano_atual = datetime.today().year

        if not value < ano_atual:
            raise ValueError("Ano deve ser menor que o atual.")
        return value

    @property
    def data_nascimento(self):
        return date(year=self.year, month=self.month, day=self.day).isoformat()
    
