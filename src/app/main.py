from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/questions/", response_model=list[schemas.Question])
def get_questions(db: Session = Depends(get_db)):
    questions = crud.get_questions(db)
    return questions


@app.post("/add-question/", response_model=list[schemas.Question])
def create_questions(q: schemas.Query, db: Session = Depends(get_db)):
    questions = crud.create_question(db, q)
    return questions
