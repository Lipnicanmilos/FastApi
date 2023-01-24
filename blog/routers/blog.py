from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags = ['_Blogs_']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: session = Depends(get_db)):
    # ---> repository.blog
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: session=Depends(get_db)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: session=Depends(get_db)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: session = Depends(get_db)):
    return blog.show(id, db)
