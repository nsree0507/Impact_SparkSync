from pydantic import BaseModel
from datetime import datetime


class Offer(BaseModel):
    customer_id: str
    product: str
    discount: str
    stock_available: int
    created_at: datetime | None = None


class OfferResponse(BaseModel):
    customer_id: str
    product: str
    discount: str