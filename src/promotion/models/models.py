from typing import Optional, List

from fastapi import Form
from pydantic import BaseModel


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


class User(BaseModel):
    user_id: int
    name: str


class UserCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

    @classmethod
    def as_form(
        cls,
        name: str = Form(...)):
        return cls(name=name)


class Prize(BaseModel):
    prize_id: int
    description: Optional[str]


class PrizeCreate(BaseModel):
    description: Optional[str]

    class Config:
        orm_mode = True

    @classmethod
    def as_form(
        cls,
        description: str = Form(None)):
        return cls(name=description)


class Result(BaseModel):
    winner: User
    prize: Prize
