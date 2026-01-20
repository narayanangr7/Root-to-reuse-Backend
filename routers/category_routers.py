from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.category_models import Category
from schemas.category_schemas import CategoryBase,CategoryUpdate

router = APIRouter(prefix="/catagory",tags=["catagory"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    db.commit()

@router.get("/")
def get_all_category(db: Session = Depends(get_db)):
    new_category = db.query(Category).all()
    return new_category

# CREATE PRODUCT
@router.post("/", operation_id="create_Catagory")
def create_product(data: CategoryBase, db: Session = Depends(get_db)):
    new_catagory = Category(**data.model_dump())
    db.add(new_catagory)
    db.commit()
    db.refresh(new_catagory)
    return {"message": "Product added successfully!", "product": new_catagory}

@router.put("/{id}", operation_id="update_category")
def update_category(id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)

    return {
        "message": "Category updated successfully",
        "category": category
    }