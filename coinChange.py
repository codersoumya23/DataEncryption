from flask import Flask, request, jsonify

app = Flask(__name__)

def count_ways_to_make_change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is 1 way to make change for amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

@app.route('/coin-change', methods=['GET', 'POST'])
def coin_change():
    if request.method == 'GET':
        try:
            amount = int(request.args.get('amount'))
            num_coins = int(request.args.get('num_coins'))
            coin_values = list(map(int, request.args.get('coins').split()))

            ways = count_ways_to_make_change(amount, coin_values)

            return jsonify({"answer": ways})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            inputs = data.get('inputs', [])

            if not inputs:
                return jsonify({"error": "No inputs provided"}), 400

            results = []
            for input_data in inputs:
                amount, num_coins = map(int, input_data[0].split())
                coin_values = list(map(int, input_data[1].split()))

                ways = count_ways_to_make_change(amount, coin_values)
                results.append(ways)

            return jsonify({"answer": results})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4087,debug=True)