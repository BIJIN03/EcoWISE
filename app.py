from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from dotenv import load_dotenv

# Agents
from agents.llm_intent_agent import parse_user_input_llm
from agents.eco_score_agent import get_eco_score
from agents.recommendation_agent import recommend_products
from agents.combo_optimizer_agent import optimize_combo
from agents.llm_explanation_agent import generate_explanation_llm

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")
 

@app.route('/eco_recommend_llm', methods=['POST'])
def eco_recommend_llm():
    try:
        user_input = request.json.get("input", "")

        # Step 1: Parse intent using LLM
        parsed = parse_user_input_llm(user_input)
        intent = {
            "category": parsed.get("product_type"),
            "duration": parsed.get("duration"),
            "preferences": parsed.get("preferences")
        }

        print("Intent :",intent)

        # Step 2: Eco Score Agent
        products = get_eco_score(intent)

        # Step 3: Recommendation Agent
        top_products = recommend_products(products, intent)

        # Step 4: Combo Optimizer Agent
        combo = optimize_combo(top_products, max_items=intent["duration"])

        # Step 5: Explanation Agent
        explanation = generate_explanation_llm(user_input, combo)

        return jsonify({
            "intent": intent,
            "combo": combo,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)