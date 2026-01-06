from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.camp_models import Camp
from schemas.camp_schemas import CampCreate, CampUpdate, CampResponse

router = APIRouter(prefix="/camp", tags=["Camp"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    db.commit()

@router.post("/create", response_model=CampResponse)
def create_camp(data: CampCreate, db: Session = Depends(get_db)):
    camp = Camp(**data.model_dump())
    db.add(camp)
    db.commit()
    db.refresh(camp)
    return camp


@router.get("/all", response_model=list[CampResponse])
def get_all_camps(db: Session = Depends(get_db)):
    return db.query(Camp).all()


@router.get("/{camp_id}", response_model=CampResponse)
def get_camp_by_id(camp_id: int, db: Session = Depends(get_db)):
    camp = db.query(Camp).filter(Camp.id == camp_id).first()
    if not camp:
        raise HTTPException(status_code=404, detail="Camp not found")
    return camp


@router.get("/volunteer/{volunteer_id}", response_model=list[CampResponse])
def get_camps_by_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    camps = db.query(Camp).filter(Camp.volunteer_id == volunteer_id).all()
    return camps


@router.put("/update/{camp_id}", response_model=CampResponse)
def update_camp(
    camp_id: int,
    data: CampUpdate,
    db: Session = Depends(get_db)
):
    camp = db.query(Camp).filter(Camp.id == camp_id).first()
    if not camp:
        raise HTTPException(status_code=404, detail="Camp not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(camp, key, value)

    db.commit()
    db.refresh(camp)
    return camp


@router.delete("/delete/{camp_id}")
def delete_camp(camp_id: int, db: Session = Depends(get_db)):
    camp = db.query(Camp).filter(Camp.id == camp_id).first()
    if not camp:
        raise HTTPException(status_code=404, detail="Camp not found")

    db.delete(camp)
    db.commit()
    return {"message": "Camp deleted successfully"}
