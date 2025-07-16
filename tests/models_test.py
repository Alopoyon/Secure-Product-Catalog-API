from app.db.models import products, orders, categories
from sqlalchemy import select

# def test_product_creation(db_session):
#     test_product = insert(products).values(
#         name = "Test Product 1",
#         category = "Test Category 1",
#         stock = 20,
#         price = 44.35
#     )

def test_category_table(db_session):
    test_category_insert_statement = categories.insert().values(
        name = "Test Category 1",
        description = "The first category created as for testing"
    )
    test_category_select_statement = select(categories)
    with db_session as session:
        session.execute(test_category_insert_statement)
        session.commit()

        result = session.execute(test_category_select_statement).all()
        print([i for i in result])