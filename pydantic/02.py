from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

input_data = {
    "id": 123,
    "name": "Anderson Smith",
    "is_active": True,
}

user = User(**input_data)

print(user)

input_data2 = {
    "id": "123",
    "name": "John Doe",
    "is_active": False,
}

user2 = User(**input_data2)

print(user2)


input_data3 = {
    "id": "123a",
    "name": "John Doe",
    "is_active": "False",
}

try:
    user3 = User(**input_data3)
    print(user3)
except Exception as e:
    print(f"Error creating user3: {e}")


