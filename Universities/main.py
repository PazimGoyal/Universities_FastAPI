import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .routers import universities,users
from Universities.database import engine, get_db
from Universities.schemas import HashPassword
from . import schemas, models

app = FastAPI()
app.include_router(universities.router)
models.Base.metadata.create_all(bind=engine)




# USER MODEL
@app.post('/user',response_model=schemas.ShowUsers,tags=['User'])
def User(request: schemas.Users, db: Session = Depends(get_db)):
    new_user = models.Users(email=request.email, password=HashPassword(request.password),full_name=request.full_name,disabled=request.disabled)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


if __name__ == '__main__':
    uvicorn.run(app)
