from datetime import datetime
from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question_text: str
    answer_text: str
    created_at: datetime

    class Config:
        from_attributes = True


class Query(BaseModel):
    question_num: int

    class Config:
        from_attributes = True
