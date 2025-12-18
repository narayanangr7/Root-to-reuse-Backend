from pydantic import BaseModel

class SingUpBase(BaseModel):
    username:str
    password:str
    phone_no:int
    email:str

class loginUser(BaseModel):
    id:int
    username:str
    Password:str