from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    total_price: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    total_price: int

    class Config:
        from_attributes = True
