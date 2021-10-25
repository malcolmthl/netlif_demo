from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'https://bcancer-fastapi.herokuapp.com'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['GET'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {'calculation: 123123123'}