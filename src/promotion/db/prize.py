import sqlalchemy
from .database import create_table


prizes = create_table(
    "prizes",
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True)
)
