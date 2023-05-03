from voluptuous import Schema, PREVENT_EXTRA, Length, All

cat = Schema({
    "length": str,
    "origin": str,
    "image_link": str,
    "family_friendly": int,
    "shedding": int,
    "general_health": int,
    "playfulness": int,
    "children_friendly": int,
    "grooming": int,
    "intelligence": int,
    "other_pets_friendly": int,
    "min_weight": float,
    "max_weight": float,
    "min_life_expectancy": float,
    "max_life_expectancy": float,
    "name": str
}, extra=PREVENT_EXTRA, required=True)

cats_list = Schema(All([cat], Length(min=1)), extra=PREVENT_EXTRA, required=True)
