from flask import Flask, request, jsonify

app = Flask(__name__)

def get_intervals(n, employees, shifts):
    result = []

    intervals = []
    for i in range(n):
        for j in range(shifts[i][0], shifts[i][1]):
            intervals.append((j, i, employees[i]))

    intervals.sort()

    output_intervals = []
    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] != current_interval[0]:
            output_intervals.append(current_interval)
            current_interval = intervals[i]
        else:
            current_interval = (current_interval[0], current_interval[1], current_interval[2] + " " + intervals[i][2])

    output_intervals.append(current_interval)

    result.append([len(output_intervals)] + [" ".join(map(str, interval)) for interval in output_intervals])

    return {"answer": result}

@app.route('/time-intervals', methods=['GET', 'POST'])
def time_intervals():
    if request.method == 'GET':
        n = int(request.args.get('n'))
        employees = request.args.get('employees').split()
        shifts = [(int(request.args.get(f'shifts[{i}][0]')), int(request.args.get(f'shifts[{i}][1]'))) for i in range(n)]

        response = get_intervals(n, employees, shifts)
        return jsonify(response)

    if request.method == 'POST':
        data = request.json
        inputs = data.get('inputs')
        if not inputs:
            return jsonify({"error": "Invalid data format."}), 400

        response = get_intervals(inputs[0], inputs[1].split(), [(int(inputs[i]), int(inputs[i+1])) for i in range(2, 2*int(inputs[0])+1, 2)])
        return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4088,debug=True)