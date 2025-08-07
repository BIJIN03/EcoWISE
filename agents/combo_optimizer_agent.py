def optimize_combo(products, max_items=3):
    """
    From recommended products, generate an optimized combo (kit).
    Aim: Minimize total eco-impact score.
    """

    def total_eco_score(product):
        return (
            product.get("carbon_score", 0) +
            product.get("water_score", 0) +
            product.get("plastic_score", 0)
        )

    # Sort by total score
    sorted_products = sorted(products, key=total_eco_score)

    # Select top 'max_items' products
    optimized_kit = sorted_products[:max_items]

    return optimized_kit