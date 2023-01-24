from fastapi import FastAPI
from . import models
from .database import SessionLocal, engine
from .routers import blog, user

app = FastAPI()
# models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)
db=SessionLocal()

app.include_router(blog.router)
app.include_router(user.router)

# -----------------------------------------
# from sqlalchemy.sql import text

# @app.get('/delete', tags=['SqlQuery'])
# def sql(db: session = Depends(get_db)):
#     query = db.query(text("""
#     drop table users
#     """))

#     return 'delete'

# @app.get('/show')
# def get_all():
#     blogs=db.query(models.Blog).all()
#     return blogs