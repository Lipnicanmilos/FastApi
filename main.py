from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    data = {'name':'Sarthak'}
    return {'data':data}

@app.get('/about')
def about():
    data = {'Hello'}
    return {'data':data}