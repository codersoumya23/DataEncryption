from flask import Flask, request, jsonify

app = Flask(__name__)

def max_profit(inputs):
    results = []
    for input_data in inputs:
        n, m, max_sum = map(int, input_data[0].split())
        a = list(map(int, input_data[1].split()))
        b = list(map(int, input_data[2].split()))

        max_profit = 0
        a_sum, b_sum = 0, 0
        a_pointer, b_pointer = 0, 0

        while a_pointer < n and a_sum + a[a_pointer] <= max_sum:
            a_sum += a[a_pointer]
            a_pointer += 1

        max_profit = a_pointer

        while b_pointer < m and a_pointer >= 0:
            b_sum += b[b_pointer]
            b_pointer += 1

            while b_sum + a_sum > max_sum and a_pointer > 0:
                a_pointer -= 1
                a_sum -= a[a_pointer]

            if a_sum + b_sum <= max_sum:
                max_profit = max(max_profit, a_pointer + b_pointer)

        results.append(max_profit)

    return {"answer": results}

@app.route('/portfolio-operations', methods=['POST'])
def portfolio_operations():
    try:
        data = request.get_json()
        inputs = data["inputs"]
        result = max_profit(inputs)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4081,debug=True)