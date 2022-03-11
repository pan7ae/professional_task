from .promotion import promotions
from .prize import prizes
from .user import users
from .database import metadata, engine

metadata.create_all(bind=engine)
