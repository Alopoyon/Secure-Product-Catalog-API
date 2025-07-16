from models import metadata_obj
from sqlalchemy import Table, Column, String, Integer, ForeignKeyConstraint, Text

categories = Table(
    "categories",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement="auto"),
    Column("name", String(50), unique=True, index=True, nullable=False),
    Column("parent_id", Integer, nullable = True),
    Column("description", String(200), nullable = True),

    ForeignKeyConstraint(["parent_id"], ["categories.id"],
                         name="fk_sub_categories",
                         ondelete="CASCADE",
                         onupdate="CASCADE"
                         )
)
