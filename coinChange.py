from flask import Flask, request, jsonify

app = Flask(__name__)

def max_risk_mitigation(n, m, costs):
    max_mitigation = 0

    for i in range(m):
        for j in range(i + 1, m):
            risk_mitigation = costs[j] - costs[i]

            if risk_mitigation > max_mitigation:
                max_mitigation = risk_mitigation

    return max_mitigation

@app.route('/risk-mitigation', methods=['POST', 'GET'])
def risk_mitigation():
    if request.method == 'POST':
        request_data = request.get_json()

        if "inputs" in request_data:
            inputs = request_data["inputs"]
            results = []
            for input_data in inputs:
                n, m = map(int, input_data[0].split())
                costs = list(map(int, input_data[1].split()))
                result = max_risk_mitigation(n, m, costs)
                results.append(result)
            return jsonify({"answer": results})
        else:
            return jsonify({"error": "Invalid input format"}), 400
    elif request.method == 'GET':
        n = int(request.args.get('n', 0))
        m = int(request.args.get('m', 0))
        costs_str = request.args.get('costs', '')

        try:
            costs = list(map(int, costs_str.split()))
        except ValueError:
            return jsonify({"error": "Invalid input format"}), 400

        result = max_risk_mitigation(n, m, costs)
        return jsonify({"answer": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4089,debug=True)
