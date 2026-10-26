from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    userId: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    imageURL: Optional[str] = None

cart_details = {
    "userId": "123456789",
    "items": ["Laptop", "Mouse"],
    "quantities": {
        "Laptop": 1,
        "Mouse": 1
    }
}

cart = Cart(**cart_details)

print(f"Cart items: {cart}")
