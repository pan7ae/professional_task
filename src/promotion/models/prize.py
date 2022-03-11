from typing import Optional

from fastapi import Form
from pydantic import BaseModel


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
