from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.volunteer_models import Volunteer
from schemas.volunteer_schemas import VolunteerBase,VolunteerCreate,VolunteerResponse,VolunteerUpdate

router = APIRouter(prefix="/volunteers", tags=["Volunteers"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    db.commit()


@router.post("/", response_model=VolunteerResponse)
def create_volunteer(data: VolunteerCreate, db: Session = Depends(get_db)):
    volunteer = Volunteer(**data.dict())
    db.add(volunteer)
    db.commit()
    db.refresh(volunteer)
    return volunteer


@router.get("/", response_model=list[VolunteerResponse])
def get_all_volunteers(db: Session = Depends(get_db)):
    return db.query(Volunteer).all()


@router.get("/{volunteer_id}", response_model=VolunteerResponse)
def get_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer


@router.put("/{volunteer_id}", response_model=VolunteerResponse)
def update_volunteer(
    volunteer_id: int,
    data: VolunteerUpdate,
    db: Session = Depends(get_db)
):
    volunteer = db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(volunteer, key, value)

    db.commit()
    db.refresh(volunteer)
    return volunteer


@router.delete("/{volunteer_id}")
def delete_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    db.delete(volunteer)
    db.commit()
    return {"message": "Volunteer deleted successfully"}
