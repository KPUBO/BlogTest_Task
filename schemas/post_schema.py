from fastapi.openapi.models import Schema
from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(..., title="Заголовок поста", max_length=200)
    content: str = Field(..., title="Содержание поста", max_length=1000)


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    amounts_of_likes: int
