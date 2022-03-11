from pydantic import BaseModel

from .prize import Prize
from .user import User


class Result(BaseModel):
    winner: User
    prize: Prize
