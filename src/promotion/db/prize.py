import sqlalchemy as sa
from .database import metadata

prizes = sa.Table(
    "prizes",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("description", sa.String, nullable=True)
)
