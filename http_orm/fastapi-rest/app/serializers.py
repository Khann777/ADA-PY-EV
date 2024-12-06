from pydantic import BaseModel

class ProductSerializer(BaseModel):
    title: str
    price: float
    quantity: int
    description: str

class ProductListSerializer(BaseModel):
    title: str
    price: float

class ProductDetailSerializer(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    description: str

