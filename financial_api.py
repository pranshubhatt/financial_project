from flask import Flask, request, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load your data
data_path = "dataset.xlsx"  # Make sure this file exists in the same directory or provide a valid path
df = pd.read_excel(data_path)

# Function to calculate the financial score
def calculate_financial_score(family_data):
    savings_income_ratio = family_data['Savings'] / family_data['Income']
    expenses_income_ratio = family_data['Monthly Expenses'] / family_data['Income']
    loan_income_ratio = family_data['Loan Payments'] / family_data['Income']
    credit_card_spending_ratio = family_data['Credit Card Spending'] / family_data['Income']
    financial_goals_met = family_data['Financial Goals Met (%)'] / 100

    # Calculate the score with weights
    score = (
        0.3 * savings_income_ratio +
        0.2 * (1 - expenses_income_ratio) +
        0.2 * (1 - loan_income_ratio) +
        0.2 * (1 - credit_card_spending_ratio) +
        0.1 * financial_goals_met
    ) * 100

    return max(0, min(100, score))  # Ensure score is between 0 and 100

# Route to calculate financial score
@app.route('/financial-score', methods=['POST'])
def financial_score():
    try:
        # Get input JSON
        data = request.get_json()
        family_id = data.get("family_id")

        # Filter family data
        family_data = df[df['Family ID'] == family_id].iloc[0]  # Assumes unique Family ID
        score = calculate_financial_score(family_data)

        # Generate insights
        insights = []
        if family_data['Savings'] < 0.2 * family_data['Income']:
            insights.append("Increase savings to at least 20% of your income.")
        if family_data['Monthly Expenses'] > 0.5 * family_data['Income']:
            insights.append("Reduce monthly expenses to below 50% of your income.")
        if family_data['Loan Payments'] > 0.3 * family_data['Income']:
            insights.append("Minimize loan payments to improve your financial health.")
        if family_data['Credit Card Spending'] > 0.2 * family_data['Income']:
            insights.append("Reduce credit card spending to less than 20% of your income.")
        if not insights:
            insights.append("Your financial health is excellent. Keep up the good work!")
        return jsonify({
            "family_id": family_id,
            "financial_score": score,
            "insights": insights
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to list available routes (for debugging)
@app.route('/routes', methods=['GET'])
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        output.append(f"{rule} -> {rule.endpoint}")
    return jsonify(output)

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the Financial Insights API!"

if __name__ == '__main__':
    app.run(debug=True)
