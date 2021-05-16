from fastapi import APIRouter, Depends, HTTPException
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette import status

from .. import models, schemas
from ..database import get_db

router=APIRouter({
'tags':['Private']
})

@router.get('/all')
def index(db: Session = Depends(get_db)):
    """
    return all the Universities
    :param db:
    :return:
    """
    all = db.query(models.Universities).all()
    return all


@router.get('/university',tags=['Public'])
def get_university(response: Response, id: int, db: Session = Depends(get_db), name: str = '',
                   status_code=status.HTTP_201_CREATED):
    """
    return all the Universities
    :param db:
    :return:
    """
    uni = db.query(models.Universities).filter(models.Universities.id == id).first()
    if not uni:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"University with ID {id} not available")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'Error':f"University with ID {id} not available"}
    return uni


@router.post('/new',tags=['Private'])
def new_university(request: schemas.MyModel, db: Session = Depends(get_db)):
    new_uni = models.UniversitiesList(name=request.name, country=request.country)
    db.add(new_uni)
    db.commit()
    db.refresh(new_uni)
    return new_uni
