from pydantic import BaseModel

class Address(BaseModel):
    pincode: int
    city: str
    state: str

class User(BaseModel):
    id: int
    name: str
    address: Address

user_data = {
    "id": 1,
    "name": "Pradipta Das",
    "address": {
        "pincode": 751020,
        "city": "Cuttack",
        "state": "Odisha"
    }
}

user = User(**user_data)
print(user)