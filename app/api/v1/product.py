from typing import Any

from app.schema.product import ProductIn, ProductOut
from app.db.models.products import products

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy import select

router = APIRouter(
    prefix= "/products",
    tags=["products"]
)

@router.get("/", response_model=ProductOut)
def get_products(
    skip: int, limit: int = 50, active: bool = True
) -> Any:
    
    try:
        statement = select(products).where(products.c.active == active)
        print(statement)
    except:
        ...

    return 

@router.get("/{id}", response_model=ProductOut)
async def get_product(
    id: int
) -> Any :
    try:
        ...
    except:
        ...
    
    return