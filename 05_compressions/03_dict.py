price_in_inr = {
    "Chai": 45,
    "Coffee": 45,
    "Cold Coffee": 90
}

price_in_usd = {item:price / 90 for item, price in price_in_inr.items() }

print(f"price in usd {price_in_usd}")