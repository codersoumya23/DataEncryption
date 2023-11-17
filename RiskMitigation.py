from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_total_risk_mitigation(n, m, costs):
    strategies = []

    for i in range(m):
        for j in range(i + 1, m):
            risk_mitigation = costs[j] - costs[i]
            strategies.append((i, j, risk_mitigation))

    # Sort strategies based on risk mitigation in descending order
    sorted_strategies = sorted(strategies, key=lambda x: x[2], reverse=True)

    # Choose the top N strategies
    selected_strategies = sorted_strategies[:n]

    # Calculate total risk mitigation for the selected strategies
    total_risk_mitigation = sum(strategy[2] for strategy in selected_strategies)

    return total_risk_mitigation

def validate_inputs(inputs):
    for input_data in inputs:
        if len(input_data) != 2:
            return False
        try:
            n, m = map(int, input_data[0].split())
            costs = list(map(int, input_data[1].split()))
            if n < 0 or m < 0 or len(costs) != m:
                return False
        except ValueError:
            return False

    return True

@app.route('/risk-mitigation', methods=['POST', 'GET'])
def risk_mitigation():
    if request.method == 'POST':
        request_data = request.get_json()

        if "inputs" in request_data:
            inputs = request_data["inputs"]

            if not validate_inputs(inputs):
                return jsonify({"error": "Invalid input format"}), 400

            total_max_risks = [calculate_total_risk_mitigation(int(input_data[0].split()[0]), len(input_data[1].split()), list(map(int, input_data[1].split()))) for input_data in inputs]

            return jsonify({"answer": total_max_risks})
        else:
            return jsonify({"error": "Invalid input format"}), 400
    elif request.method == 'GET':
        n = int(request.args.get('n', 0))
        m = int(request.args.get('m', 0))
        costs_str = request.args.get('costs', '')

        try:
            costs = list(map(int, costs_str.split()))
            if n < 0 or m < 0 or len(costs) != m or m < n:
                return jsonify({"error": "Invalid input format"}), 400
        except ValueError:
            return jsonify({"error": "Invalid input format"}), 400

        result = calculate_total_risk_mitigation(n, m, costs)
        return jsonify({"answer": result})


if __name__== "__main__":
    app.run(host='0.0.0.0', port=4081,debug=True)