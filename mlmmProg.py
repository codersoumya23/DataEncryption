import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def count_book_of_works(inputs):
    result = []
    for input_data in inputs:
        cutoff = int(input_data[0])
        num_scores = int(input_data[1])
        performance_scores = list(map(int, input_data[2].split()))

        total = 0
        count = 0

        for score in performance_scores:
            total += score
            if total <= cutoff:
                count += 1
            else:
                break

        result.append(count)

    return result

@app.route('/mlmm-program', methods=['GET', 'POST'])
def mlmm_program():
    if request.method == 'GET':
        try:
            inputs_str = request.args.get('inputs')
            inputs = eval(inputs_str)  # Convert string representation to a list of lists

            if not inputs:
                return jsonify({"error": "No inputs provided"}), 400

            output = count_book_of_works(inputs)
            return jsonify({"answer": output})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            inputs = data.get('inputs', [])

            if not inputs:
                return jsonify({"error": "No inputs provided"}), 400

            output = count_book_of_works(inputs)
            return jsonify({"answer": output})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4084,debug=True)
