from models import metadata_obj
from sqlalchemy import Table, Column, VARCHAR, Integer, ForeignKeyConstraint, ARRAY

from uuid import uuid4

orders = Table(
    "orders",
    metadata_obj,
    Column("id", VARCHAR(36), nullable=False, default=uuid4),
    Column("product_id", ARRAY(Integer), nullable=False),
    # Column("user_id", VARCHAR(36), nullable=False),

    ForeignKeyConstraint(
        ["product_id"],
        ["products.id"],
        name="fk_product_id",
        ondelete="CASCADE",
        onupdate="CASCADE"
    )
)