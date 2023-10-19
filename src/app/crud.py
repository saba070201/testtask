from sqlalchemy.orm import Session

from . import models, schemas

from . import services


def get_questions(db: Session):
    return db.query(models.Question).all()


def create_question(db: Session, q: schemas.Query):
    return services.get_data_from_api(q=q, db=db)
