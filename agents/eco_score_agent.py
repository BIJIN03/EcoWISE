import pandas as pd

def get_eco_score(intent):
    df = pd.read_csv('data/products.csv')
    category = intent["category"]
    return df[df["category"] == category].to_dict(orient='records')
