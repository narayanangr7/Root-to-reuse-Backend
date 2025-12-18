from pydantic import BaseModel

class CampBase(BaseModel):
    event_name: str
    full_name: str
    volunteer_id: int
    email: str
    phone: str
    address: str
    hours: int
    message: str | None = None


class CampCreate(CampBase):
    pass


class CampUpdate(BaseModel):
    event_name: str | None = None
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    hours: int | None = None
    message: str | None = None


class CampResponse(CampBase):
    id: int

    class Config:
        from_attributes = True
