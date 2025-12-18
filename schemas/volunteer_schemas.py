from pydantic import BaseModel

class VolunteerBase(BaseModel):
    full_name: str
    user_id: int
    email: str
    phone_no: str
    age: int
    location: str


class VolunteerCreate(VolunteerBase):
    pass


class VolunteerUpdate(BaseModel):
    full_name: str | None = None
    phone_no: str | None = None
    age: int | None = None
    location: str | None = None


class VolunteerResponse(VolunteerBase):
    id: int

    class Config:
        from_attributes = True
