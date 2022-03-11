from fastapi import Form
from pydantic import BaseModel


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
