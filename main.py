from fastapi import FastAPI, Request
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name = 'static')

templates = Jinja2Templates(directory = 'templates')

@app.get('/')
def home():
    return 'Hello World!'

# path parameters example
@app.get('/{name}')
def addThem(name: str):
    return {'name': name}

# query parameter example
@app.get('/items/')
async def get_items(first: Optional[str] = None, detail: Optional[str] = None):
    fake_data = {
        'nate':{
            'phone': '555-5555',
            'address': '123 fake street',
            'occupation': 'Teacher',
            'languages': ['Python', 'JS', 'C++', 'TypeScript']
        },
        'brandon':{
            'phone': '555-5555',
            'address': '12345 Real Street',
            'occupation': 'Teacher',
            'languages': ['Python', 'JS', 'Java', 'TypeScript', 'Kotlin']
        }
    }
    details = {'phone', 'address', 'occupation', 'languages'}
    if first and detail:
        if detail not in details:
            return {'error': 'that detail does not exist!'}
        try:
            return fake_data[first][detail]
        except:
            return {'error': 'That person does not exist!'}
    elif first:
        return fake_data.get(first, {'error': 'That Person does not exist!'})
    elif detail and detail in details:
        return {'error': f'Need a person to grab {detail} from!'}
    elif detail and detail not in details:
        return {'error': 'that detail does not exist!'}
    else:
        return {'everyone': fake_data}

@app.get('/items/{name}', response_class=HTMLResponse)
async def read_info(request: Request, name: str):
    fake_data = {
        'nate':{
            'phone': '555-5555',
            'address': '123 fake street',
            'occupation': 'Teacher',
            'languages': ['Python', 'JS', 'C++', 'TypeScript']
        },
        'brandon':{
            'phone': '555-5555',
            'address': '12345 Real Street',
            'occupation': 'Teacher',
            'languages': ['Python', 'JS', 'Java', 'TypeScript', 'Kotlin']
        }
    }
    return templates.TemplateResponse('index.html', {'request': request, 'name': name, 'info': fake_data[name]})
