def recommend_products(products, intent, top_k=5):
    """
    Rank products by lowest total eco-impact score.
    """
    def compute_total_score(product):
        return (
            product.get("carbon_score", 0) +
            product.get("water_score", 0) +
            product.get("plastic_score", 0)
        )

    # Rank products
    scored_products = sorted(products, key=compute_total_score)

    # Return top-k
    return scored_products[:top_k]