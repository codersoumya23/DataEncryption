from flask import Flask, request, jsonify

app = Flask(__name__)

def is_eligible_transaction(n, transfers):
    # Create a dictionary to store the net asset change for each client
    net_assets = {i: 0 for i in range(n)}

    # Calculate net asset change for each client based on transfers
    for transfer in transfers:
        sender, receiver = transfer
        net_assets[sender] -= 1
        net_assets[receiver] += 1

    # Check if any client indirectly receives assets from themselves
    visited = set()

    def dfs(client):
        visited.add(client)
        for i in range(n):
            if net_assets[i] < 0 and i not in visited:
                if dfs(i):
                    return True
            elif i == client and net_assets[i] > 0:
                return True
        return False

    for client in range(n):
        if client not in visited and dfs(client):
            return "Ineligible"

    return "Eligible"

@app.route('/fraudulent-transactions', methods=['POST'])
def fraudulent_transactions():
    try:
        data = request.get_json()

        # Extract inputs from JSON
        inputs = data.get("inputs", [])

        results = []

        for inp in inputs:
            n, l = map(int, inp[0].split())
            transfers = [list(map(int, t.split())) for t in inp[1:]]
            result = is_eligible_transaction(n, transfers)
            results.append(result)

        return jsonify({"answer": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/fraudulent-transactions', methods=['GET'])
def fraudulent_transactions_get():
    try:
        # Extract inputs from query parameters
        n = int(request.args.get("n"))
        l = int(request.args.get("l"))
        transfers = [list(map(int, request.args.get(f"transfers[{i}]").split())) for i in range(l)]

        # Check eligibility
        result = is_eligible_transaction(n, transfers)

        # Return the result in JSON format
        return jsonify({"answer": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4082, debug=True)
