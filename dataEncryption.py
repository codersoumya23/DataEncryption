import json
import math
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def string_to_matrix(input, row, col, List):
    matrix = [[' ' for _ in range(col)] for _ in range(row)]
    for index in range(len(input)):
        matrix[index // col][index % col] = input[index]

    matrix1 = [list(row) for row in zip(*matrix)]
    res = ' '.join([''.join(row) for row in matrix1])
    List.append(res)




def calc(input_str, List):
    input = ''.join(re.findall(r'[a-zA-Z]+', input_str))
    num = len(input)
    n = math.sqrt(num)
    row = math.floor(n)
    col = math.ceil(n)
    if (row * col < num):
        row = row + 1

    string_to_matrix(input, row, col, List)

@app.route('/data-encryption', methods=['GET', 'POST'])
def main():
    List = []
    json_response={}
    if request.method == 'GET':
        # Extract sample JSON data from the query parameter
        sample_json_data_param = request.args.get('inputs')

        if sample_json_data_param:
            try:
                sample_json_data = json.loads(sample_json_data_param)
                data_dict = sample_json_data
            except json.JSONDecodeError as e:
                return jsonify({"status": "error", "message": f"Invalid JSON data: {e}"})
        else:
            return jsonify({"status": "error", "message": "No sample_data query parameter provided for GET request."})
    elif request.method == 'POST':
        json_data = request.get_json()
        if json_data is None:
            return jsonify({"status": "error", "message": "No JSON data in the request."})

        data_dict = json_data

    my_list = data_dict.get('inputs', [])
    for x in my_list:
        calc(x, List)

    if request.method == 'POST':
        json_response = {"answer": List}
        # return jsonify(json_response)

    return jsonify(json_response)


    # return jsonify({"status": "success", "message": "GET request processed."})

if __name__ == "__main__":
    app.run(host='127.2.3.1', port=4080, debug=True)
