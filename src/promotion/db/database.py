from databases import Database
from sqlalchemy import create_engine, MetaData
from ..config import DATABASE_URL

database = Database(DATABASE_URL, min_size=1, max_size=20, timeout=60)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=200
)
