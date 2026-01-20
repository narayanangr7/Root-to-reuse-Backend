from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.product_models import Product
from schemas.prodect_schema import ProductCreate, ProductOut,ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_product")
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get("/{id}", operation_id="get_product_by_id")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product:
        return product
    return {"error": "Product not found"}

@router.get("/category/{category_id}", operation_id="get_products_by_category")
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category_id == category_id).all()

    if not products:
        raise HTTPException(status_code=404, detail="No products found for this category")

    return products


@router.put("/{id}",operation_id="update_product")
def update_product(id:int,data:ProductUpdate,db:Session=Depends(get_db)):
    rtr_product= db.query(Product).filter(Product.id == id).first()
    if not rtr_product:
        return {"error":"Product not found"}
    
    update_data = data.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(rtr_product,key,value)

    db.commit()
    db.refresh(rtr_product)
    return{"message":"Product updated successfully!","product":rtr_product}



@router.put("/{id}", response_model=ProductOut, operation_id="update_product")
def update_product(id: int, data: ProductCreate, db: Session = Depends(get_db)):
    p = db.query(Product).filter(Product.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    update_data = data.model_dump(exclude_unset=True)
    for k, v in update_data.items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p

@router.delete("/{id}", operation_id="delete_product")
def delete_product(id: int, db: Session = Depends(get_db)):
    p = db.query(Product).filter(Product.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(p)
    db.commit()
    return {"message": "Product deleted"}
