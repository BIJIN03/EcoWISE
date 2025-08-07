import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_explanation_llm(user_input, recommendations):
    product_names = ", ".join([p["name"] for p in recommendations])
    
    prompt = f"""
The user said: "{user_input}"

You selected these products:
{product_names}

Explain why these are eco-friendly in a friendly, human tone, in about 10 - 20 words. 
Mention if they reduce carbon emissions, avoid plastic, use biodegradable materials, etc.
Use simple language and motivate the user to choose sustainability.
Do not generate texts like "Okay", "Oops" etc. Respond only in standard way.
If you are unaware of the products or the inputs are empty, just mention that.
Also, mention some of the Product Brands of these eco frieandly products.
If you don't know the answer, say so and respond that you does'nt have answers for that right now and ask whether the user want to know about specific products in your perspective.
Do not generate text in Markdown format.
Do not generate any other content.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini Explanation Error:", e)
        return "These products are chosen for their sustainability and environmental benefits."
