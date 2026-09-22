def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets" or unit == "grams" or unit == "area":
        if unit == "packets":
            print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
        if unit == "grams":
            print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
        if unit == "area":
            print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
     print("Unknown unit type")