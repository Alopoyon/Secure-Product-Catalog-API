from app.models import products, orders, categories
from sqlalchemy import insert

# def test_product_creation(db_session):
#     test_product = insert(products).values(
#         name = "Test Product 1",
#         category = "Test Category 1",
#         stock = 20,
#         price = 44.35
#     )

def test_category_creation(db_session):
    test_category_statement = insert(categories).values(
        name = "Test Category 1",
        description = "The first category created as for testing"
    )
    with db_session() as session:
        result = session.execute(test_category_statement)
        session.commit()