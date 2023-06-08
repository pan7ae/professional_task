import sqlalchemy
from .database import metadata

promotions = sqlalchemy.Table(
    "promotions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("prizes", sqlalchemy.ARRAY(sqlalchemy.Integer), nullable=True),
    sqlalchemy.Column("participants", sqlalchemy.ARRAY(sqlalchemy.Integer), nullable=True)
)
