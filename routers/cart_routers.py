from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.cart_models import Cart
from schemas.cart_schemas import CartCreate,CartUpdate

router = APIRouter(prefix="/cart", tags=["Cart"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➕ Add to cart
@router.post("/add")
def add_to_cart(data: CartCreate, db: Session = Depends(get_db)):
    cart = Cart(**data.model_dump())
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

# 📦 View cart by user
@router.get("/user/{user_id}")
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(Cart).filter(Cart.user_id == user_id).all()

@router.put("/{cart_id}")
def update_cart(cart_id: int, data: CartUpdate, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart.quantity = data.quantity
    db.commit()
    db.refresh(cart)
    return cart

# ❌ Delete cart item
@router.delete("/{cart_id}")
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(cart)
    db.commit()
    return {"message": "Cart item deleted"}
