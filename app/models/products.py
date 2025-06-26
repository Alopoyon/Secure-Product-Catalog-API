from models import metadata_obj
from sqlalchemy import Table, Column, Integer, String, Boolean, Computed, ForeignKeyConstraint


product = Table(
    "product",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(150)),
    Column("stock", Integer), 
    Column("active", Boolean, Computed("stock > 0")),
    Column("category"),

    ForeignKeyConstraint(["category"], ["categories.category_id"], name="fk_category", ondelete="CASCADE")


)