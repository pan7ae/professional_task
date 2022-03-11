import sqlalchemy as sa
from .database import metadata

promotions = sa.Table(
    "promotions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("description", sa.String, nullable=True),
    sa.Column("prizes", sa.ARRAY(sa.Integer), nullable=True),
    sa.Column("participants", sa.ARRAY(sa.Integer), nullable=True)
)
