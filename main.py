from fastapi import FastAPI


app= FastAPI()
@app.get('/')
def index():
    return {'data':12}


@app.get('/about')
def about():
    return {'data':12}
