import numpy as np
from .ml_model import load_model

model = load_model()

def suggest_price(features: dict, candidate_prices: list[float]):
    best_price = candidate_prices[0]
    max_revenue = 0
    best_prob = 0

    for price in candidate_prices:
        features_copy = features.copy()
        features_copy["price_cents"] = price
        X = np.array([list(features_copy.values())])
        prob = model.predict_proba(X)[:,1][0]
        revenue = price * prob
        if revenue > max_revenue:
            max_revenue = revenue
            best_price = price
            best_prob = prob

    reason = f"Max expected revenue: {max_revenue:.2f} (prob: {best_prob:.2f})"
    return best_price, reason
