import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def longest_palindrome_length(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_count = 0

    for count in char_count.values():
        length += (count // 2) * 2
        if count % 2 == 1:
            odd_count = 1

    return length + odd_count

@app.route('/file-reorganization', methods=['GET', 'POST'])
def file_reorganization():
    if request.method == 'GET':
        try:
            sample_json_data_param = request.args.get('inputs')
            if sample_json_data_param:
                sample_json_data = json.loads(sample_json_data_param)
                inputs = sample_json_data.get("inputs", [])
                results = [longest_palindrome_length(file_labels) for file_labels in inputs]
                return jsonify({"answer": results})
            else:
                return jsonify({"status": "error", "message": "No inputs provided in the GET request."})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    elif request.method == 'POST':
        try:
            data = request.get_json()
            inputs = data.get("inputs", [])
            results = [longest_palindrome_length(file_labels) for file_labels in inputs]
            return jsonify({"answer": results})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

if __name__== "__main__":
    app.run(host='0.0.0.0', port=4082,debug=True)