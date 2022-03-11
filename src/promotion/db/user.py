import sqlalchemy as sa
from .database import metadata

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("name", sa.String, unique=True),
)
