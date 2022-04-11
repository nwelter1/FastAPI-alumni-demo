from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return 'Hello World!'

@app.get('/{name}')
def addThem(name: str):
    return {'name': name}