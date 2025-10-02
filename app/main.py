from fastapi import FastAPI
from .models import PriceRequest, PriceResponse
from .price_optimizer import suggest_price

app = FastAPI(title="Dynamic Pricing Engine")

@app.post("/suggest_price", response_model=PriceResponse)
async def suggest_price_endpoint(req: PriceRequest):
    # Example static feature for demo
    features = {
        "product_id": req.product_id,
        "inventory_qty": 50,
        "competitor_price_cents": 950
    }
    if not req.candidate_prices:
        req.candidate_prices = [900, 950, 1000, 1050, 1100]

    price, reason = suggest_price(features, req.candidate_prices)
    return PriceResponse(product_id=req.product_id, suggested_price=price, reason=reason)

@app.get("/")
async def root():
    return {"message": "Dynamic Pricing Engine is running"}
