from passlib.context import CryptContext
from pydantic.main import BaseModel, Optional


class MyModel(BaseModel):
    id: int
    name: str
    country: Optional[str]


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users(BaseModel):
    email: str
    password: str
    full_name: str
    disabled: Optional[bool] = False

class ShowUsers(BaseModel):
    email: str
    full_name: str
    class Config():
        orm_mode=True

def HashPassword(password):
    return pwd_context.hash(password)
