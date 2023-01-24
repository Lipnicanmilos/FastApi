from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from ..hashing import Hash
from sqlalchemy.orm import session

router = APIRouter(
    prefix='/users',
    tags = ['_Users_']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int, db: session = Depends(get_db)):
    user =  db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroyUser(id: int, db: session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateUser(id: int, request: schemas.ShowUser, db: session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} not found")   
    user.update(request.dict())
    db.commit()
    return 'updated'
