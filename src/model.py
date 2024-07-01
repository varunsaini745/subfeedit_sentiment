from pydantic import BaseModel
from typing import List


class Comment(BaseModel):
    id: int
    text: str
    polarity: float
    classification: str
    created_time: int


class CommentsResponse(BaseModel):
    comments: List[Comment]
