from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: str
    name: str
    email: str


class CustomerLoyaltyResponse(BaseModel):
    customer_id: str
    score: int
    level: str


class CustomerOfferResponse(BaseModel):
    customer_id: str
    offers: list