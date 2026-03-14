from pydantic import BaseModel


class LocationRequest(BaseModel):
    customer_id: str
    latitude: float
    longitude: float


class LocationResponse(BaseModel):
    message: str
    distance: float
    offers: list = []