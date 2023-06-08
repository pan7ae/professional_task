import sqlalchemy
from .database import create_table

users = create_table(
    "users",
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True),
)
