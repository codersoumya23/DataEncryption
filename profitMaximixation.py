import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit

@app.route('/profit-maximization', methods=['POST'])
def profit_maximization():
    try:
        data = request.get_json()
        inputs = data.get("inputs", [])

        results = []
        for input_str in inputs:
            input_list = list(map(int, input_str.split()[1:]))
            profit = calculate_max_profit(input_list)
            results.append(profit)

        return jsonify({"answer": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/profit-maximization', methods=['GET'])
def profit_maximization_get():
    try:
        input_str = request.args.get("input", "")
        input_list = list(map(int, input_str.split()[1:]))
        profit = calculate_max_profit(input_list)

        return jsonify({"answer": profit})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4083,debug=True)
