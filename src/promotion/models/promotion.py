from typing import Optional, List

from fastapi import Form
from pydantic import BaseModel

from .prize import Prize
from .user import User


class Promo(BaseModel):
    id: int
    name: str
    description: Optional[str]


class PromoWithDetails(Promo):
    prizes: Optional[List[Prize]]
    participants: Optional[List[User]]


class PromoCreate(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        description: Optional[str] = Form(None)):
        return cls(name=name, description=description)


class PromoUpdate(PromoCreate):
    pass

