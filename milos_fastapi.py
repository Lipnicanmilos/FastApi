from fastapi import FastAPI

my_app = FastAPI()

# @my_app.get('/blog')
# ak sa budem dotazovat po velkych datach bude to neefektivne
# preto pouzijem obmedzenie
@my_app.get('/blog?limit=10&published=true')
def index():
    data = {'name':'Sarthak'}
    return {'data':data}

@my_app.get('/blog/1')
def show():
    data = {'Hello'}
    id = 1
    return {'data': str(1)}

@my_app.get('/post/unpublished')
def unpublished():
    return {'data': 'all unpublished'}

@my_app.get('/post/{id}')
def post(id: int):
    # data = {'Hello'}
    # id = 1
    return {'data': id}

@my_app.get('/post/{id}/comments')
def comments(id):
        data = {'1', '2', '3' }
        return {'data':data}