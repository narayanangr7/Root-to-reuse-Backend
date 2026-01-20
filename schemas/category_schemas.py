from pydantic import BaseModel

class CategoryBase(BaseModel):

    name:str
    content:str

class CategoryUpdate(BaseModel):
    name: str | None = None
    content: str | None = None