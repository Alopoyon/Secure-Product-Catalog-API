from sqlalchemy import insert, select, update, delete

from fastapi.exceptions import HTTPException

from app.db.models import products
from app.schema.product import ProductIn, ProductOut

def new_product(product: ProductIn, conn):
    insert_stmt = insert(products).values(
        name = product.name,
        product_name = product.product_name, 
        category = product.category,
        description = product.description,
        stock = product.stock,
        price = product.price
        )
    
    try:
        conn.execute(insert_stmt)
        conn.commit()
    except Exception as e:
        print(e)

    return

def get_products(skip:int, limit:int, order:str, conn):
    if order in ("id","name","stock","price"):
        return HTTPException(status_code=404, detail=f"You cannot order by: {order}")
    select_stmt = select(products).offset(skip).limit(limit).order_by(products.c.name)
    
    try:
        conn.execute(select_stmt)
        # conn.commit()
    except Exception as e:
        print(e)


    return

def get_product(id: int, conn):
    select_stmt = select(products).where(products.c.id == id)
    
    try:
        conn.execute(select_stmt)
        # conn.commit()
    except Exception as e:
        print(e)

    return