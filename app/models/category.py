from models import metadata_obj
from sqlalchemy import Table, Column, String, Integer

categories = Table(
    "categories",
    metadata_obj,
    Column("category_id", Integer, primary_key=True),
    Column("category_name", String(50)),
    Column("description", String(200))
)