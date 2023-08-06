from pydantic import BaseModel

class Sunglass(BaseModel):
    id: int
    brand: str
    shape: str
    price: int
