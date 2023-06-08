import sqlalchemy
from .database import create_table


promotions = create_table(
    "promotions",
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("prizes", sqlalchemy.ARRAY(sqlalchemy.Integer), nullable=True),
    sqlalchemy.Column("participants", sqlalchemy.ARRAY(sqlalchemy.Integer), nullable=True)
)