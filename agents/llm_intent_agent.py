import os
import json
from dotenv import load_dotenv
from google import genai


load_dotenv()

def parse_user_input_llm(user_message):
    prompt = f"""
    You are an AI agent who helps recommend the customers for selecting eco friendly products for their needs and purposes.
    
Extract the following from the message, by analyzing the customer needs and requirements:
- product_type (e.g., toiletries, groceries) : should be one of the following categories - 
    Water Bottle
    Toothbrush
    Shopping Bag
    Phone Case
    Trash Bag
    Toothbrush (Electric)
    Paper Towel
    Bedsheet
    Cutlery Set
    Cleaning Product
    Laundry Detergent
    Charger
    Food Wrap
    Notebook
    Light Bulb
    Coffee Cup
    Clothing
    Storage Container
    Meat Alternative
    Plate Set
    Car
    Deodorant
    Tea
    Showerhead
    Furniture
    Makeup
    Pet Waste Bag
    Dish Soap
    Kettle
    Diaper
    Toilet Paper
    Cotton Round
    Wet Wipe
    Sponges
    Shampoo Bar
    Towel
    Notepad
    Coconut Oil
    Honey
    Vinegar
    Spice
    Baking Mat
    Essential Oil
    Diffuser
    Coconut Flour
    Nail Polish
    Storage Jar
    Dish Brush
    Candle
    Ice Pack
    Aluminum Foil
    Shampoo
    Hair Care
    Salt
    Pepper
    Coffee Pod
    Wrapping Paper
    Glass Jar
    Toothpaste
    Soap
- duration (number of days)
- preferences (list of eco constraints like plastic-free, low carbon)

Respond only as valid JSON like:
{{
  "product_type": "toiletries",
  "duration": 3,
  "preferences": ["plastic-free", "low carbon"]
}}

Message: "{user_message}"
"""

    try:
        

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        content = response.text.strip()
        # print("Gemini response :",content)
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()
        elif content.startswith("```"):
            content = content.replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        print("Gemini Intent Parse Error:", e)
        return {
            "product_type": "general",
            "duration": 3,
            "preferences": []
        }
