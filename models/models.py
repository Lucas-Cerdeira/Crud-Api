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
    def check_empt_values(cls, value):
        if str(value) == '':
            raise ValueError("Empty values are not aceptable.")
        return value
    
    @validator('day')
    def check_day_value(cls, value):
        if 1 > value > 31:
            raise ValueError("Days can't be greater than 31 and lower than 1.")
        
    @validator('month')
    def check_month_values(cls, value):
        if 1 > value > 12:
            raise ValueError("Months can't be greater than 12 ans lower than 1.")
        
    @validator('year')
    def check_year_value(cls, value):
        current_year = date.today().year
        if value > current_year:
            raise ValueError("Year can't be greater than current year.")
        



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
    
