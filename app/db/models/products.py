from app.db.models import metadata_obj
from sqlalchemy import Table, Column, Integer, String, Boolean, Computed, ForeignKeyConstraint, Float


products = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(150), nullable=False),
    Column("product_name", String(150), nullable=False, unique=True),
    Column("category", Integer, nullable=True),
    Column("description", String(500), nullable=True),
    Column("stock", Integer, nullable=False),
    Column("price", Float, nullable=False),
    Column("active", Boolean, Computed("stock <= 0 || price <= 0")),

    ForeignKeyConstraint(["category"], ["categories.id"], 
                         name="fk_category", 
                         ondelete="CASCADE", 
                         onupdate="CASCADE"
                         )

)