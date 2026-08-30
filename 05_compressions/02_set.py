menu = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["ginger", "cardamom", "elachi"],
    "Kadak Chai": ["ginger", "balck pepper", "elachi"],
}

unique_spices = {spice for spices in menu.values() for spice in spices}

print(f"Unique Spices: {unique_spices}")