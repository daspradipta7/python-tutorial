from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalze(cls, v):
        if not v.istitle():
            raise ValueError("Name must be capitalized")
        return v

data = {
     "first_name": "pradipta", 
    "last_name":"Das"
}
person = Person(**data)

print(person)