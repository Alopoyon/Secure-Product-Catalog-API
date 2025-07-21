from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from app.db.models import metadata_obj, products
from app.db.products import new_product
from app.schema.product import ProductIn


def init_db():
    engine = create_engine("sqlite:///test.db", echo=True, echo_pool="debug")
    metadata_obj.create_all(bind=engine)

    with engine.connect() as conn:
        data = []
        try:
            with open("app/db/MOCK_PRODUCTS.csv", "r", newline='', encoding='utf-8') as products_csv:
                for line in products_csv:
                    data.append(products_csv.readline().strip().split(","))
            for row in data:
                # print("data: ",data)
                _obj = ProductIn(
                    name=row[0],
                    product_name=row[1],
                    category=int(row[2] or 0),
                    description=row[3],
                    stock=int(row[4]),
                    price=float(row[5])
                )
                # t = open(".t.txt","w")
                # t.write(repr(_obj))
                # t.write("\n")
                if ProductIn.model_validate(_obj):
                    new_product(product=_obj, conn=conn)
        except:
            print("Error")