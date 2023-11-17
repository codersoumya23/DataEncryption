from flask import Flask, request, jsonify

app = Flask(__name__)

def get_intervals(inputs):
    result = []
    for input_set in inputs:
        n = int(input_set[0])
        employees = input_set[1].split()
        shifts = [(int(input_set[i]), int(input_set[i+1])) for i in range(2, 2*n+1, 2)]

        intervals = []
        for i in range(len(shifts)):
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

@app.route('/time-intervals', methods=['POST'])
def time_intervals():
    data = request.json
    inputs = data['inputs']
    response = get_intervals(inputs)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4085,debug=True)



