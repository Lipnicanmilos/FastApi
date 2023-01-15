from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# @my_app.get('/blog')
# ak sa budem dotazovat po velkych datach bude to neefektivne
# preto pouzijem obmedzenie
@app.get('/blog?limit=10&published=true')
def index():
    data = {'name':'Sarthak'}
    return {'data':data}

@app.get('/blog/1')
def show():
    data = {'Hello'}
    id = 1
    return {'data': str(1)}

@app.get('/post/unpublished')
def unpublished():
    return {'data': 'all unpublished'}

@app.get('/post/{id}')
def post(id: int):
    # data = {'Hello'}
    # id = 1
    return {'data': id}

@app.get('/post/{id}/comments')
def comments(id):
        data = {'1', '2', '3' }
        return {'data':data}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f"Blog is created with title as {blog.title}"}
    
# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", port=5000, log_level="info")
#     server = uvicorn.Server(config)
#     server.run()