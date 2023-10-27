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
    
    @validator('first_name')
    def check_empt_first_name(cls, value):
        if value.strip() == '':
            raise ValueError("Empty values are not aceptable.")
        return value
    
    
    @validator('last_name')
    def check_empt_last_name(cls, value):
        if value.strip() == '':
            raise ValueError("Empty values are not aceptable.")
        return value
    
    
    @validator('job_role')
    def check_empt_job_role(cls, value):
        if value.strip() == '':
            raise ValueError("Empty values are not aceptable.")
        return value
    
    
    @validator('cpf')
    def check_empt_values(cls, value):
        if value.strip() == '':
            raise ValueError("Empty values are not aceptable.")
        return value
    

    @validator('day')
    def check_day_value(cls, value):
        if 1 > value or value > 31:
            raise ValueError("Days can't be greater than 31 and lower than 1.")
        return value

    @validator('month')
    def check_month_values(cls, value):
        if 1 > value or value > 12:
            raise ValueError("Months can't be greater than 12 ans lower than 1.")
        return value
        
    @validator('year')
    def check_year_value(cls, value):
        current_year = date.today().year
        if not len(str(value)) == 4:
            raise ValueError("Invalid year.")
        if value > current_year:
            raise ValueError("Year can't be greater than current year.")
        return value
        



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
    
