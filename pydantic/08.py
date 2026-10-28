from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price: str # $4.44

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_daterange(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('End date must be greater thar start date')
        return values
        
