from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    product_name: str
    category: int | None = None
    description: str | None = None
    stock: int = 0
    price: float = 0.0

class ProductIn(ProductBase):
    ...

class ProductOut(ProductBase):
    id: int
    active: bool