from models import metadata_obj
from sqlalchemy import Table, Column, Integer, String, Boolean, Computed, ForeignKeyConstraint, Float


product = Table(
    "product",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(150)),
    Column("category", Integer),
    Column("stock", Integer),
    Column("price", Float),
    Column("active", Boolean, Computed("stock > 0 || price <0")),

    ForeignKeyConstraint(["category"], ["categories.id"], 
                         name="fk_category", 
                         ondelete="CASCADE", 
                         onupdate="CASCADE"
                         )

)