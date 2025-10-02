from pydantic import BaseModel
from typing import List, Optional

class PriceRequest(BaseModel):
    product_id: int
    user_id: Optional[int] = None
    candidate_prices: Optional[List[float]] = None

class PriceResponse(BaseModel):
    product_id: int
    suggested_price: float
    reason: str
