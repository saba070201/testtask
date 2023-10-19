from sqlalchemy import Column, Table, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy.orm import registry

metadata = MetaData()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True, nullable=False)
    answer_text = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, index=True, nullable=False)


q = Table(
    "questions",
    metadata,
    Column("id", Integer(), primary_key=True, index=True),
    Column("question_text", String(1000), index=True, nullable=False),
    Column("answer_text", String(1000), index=True, nullable=False),
    Column("created_at", DateTime, index=True, nullable=False),
)
# registry.map_imperatively(Question,q)
