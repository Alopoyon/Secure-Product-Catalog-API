from models import metadata_obj
from sqlalchemy import Table, Column, String, Integer, ForeignKeyConstraint

categories = Table(
    "categories",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("parent_id", Integer),
    Column("description", String(200)),

    ForeignKeyConstraint(["parent_id"], ["categories.id"],
                         name="fk_sub_categories",
                         ondelete="CASCADE",
                         onupdate="CASCADE"
                         )
)
