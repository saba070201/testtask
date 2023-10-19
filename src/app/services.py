import requests
from . import schemas
from . import models
from sqlalchemy.orm import Session


def get_data_from_api(q: schemas.Query, db: Session):
    i = 0
    result = []
    times = q.question_num
    while i < times:
        response = requests.get("https://jservice.io/api/random?count=1").json()[0]
        q_obj = schemas.Question(
            id=response["id"],
            question_text=response["question"],
            answer_text=response["answer"],
            created_at=response["created_at"],
        )
        if db.query(models.Question).get(q_obj.id):
            continue
        else:
            q_item = models.Question(**q_obj.dict())
            db.add(q_item)
            db.commit()
            db.refresh(q_item)
            result.append(q_obj)
            i += 1
    return result
