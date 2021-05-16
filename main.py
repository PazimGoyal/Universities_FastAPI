from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel

app= FastAPI()



@app.get('/about')
def about():
    return {'data':12}


class MyModel(BaseModel):
    id:Optional[int]
    no:Optional[int]
    name:Optional[str]

@app.get('/{id}')
def index(id:int,limit:int=0):
    return {'data':id,'limit':limit}

if __name__=='__main__':
    uvicorn.run(app)