import sqlalchemy
from .database import metadata

prizes = sqlalchemy.Table(
    "prizes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True)
)
