from pydantic import BaseModel

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartResponse(BaseModel):

    quantity: int

class CartUpdate(BaseModel):
    quantity: int


    class Config:
        from_attributes = True
