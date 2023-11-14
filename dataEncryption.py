import json
import math
import re
from flask import Flask, request
from urllib.request import urlopen
def string_to_matrix(input,row,col,List):
    matrix=[[' ' for _ in range(col)] for _ in range(row)]
    for index in range(len(input)):
        matrix[index//col][index%col]=input[index]

    matrix1=[list(row) for row in zip(*matrix)]

    res=' '.join([''.join(row) for row in matrix1])
    List.append(res)

def calc(input_str,List):
    input=''.join(re.findall(r'[a-zA-Z]+',input_str))
    num=len(input)
    n=math.sqrt(num)
    row=math.floor(n)
    col=math.ceil(n)
    if(row*col<num):
        row=row+1

    string_to_matrix(input,row,col,List)

app=Flask(__name__)

@app.route('/data-encryption',methods=['POST'])
def read_json_from_url(url):
    try:
        # Make an HTTP GET request to the URL
        response = request.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content
            json_data = response.json()
            return json_data
        else:
            # Print an error message if the request was not successful
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        # Handle exceptions
        print(f"Error: {e}")
        return None

# Example URL with JSON data
url = "http://127.0.0.1:5000"

# Read JSON from the given URL
json_data = read_json_from_url(url)



def main():
    url = "http://127.0.0.1:5000"

# Read JSON from the given URL
    json_data = read_json_from_url(url)
    #json_data=data_encryption()
    #json_data='{"inputs":["coding","its harder to read code than to write it"]}'
    json_string= json.dumps(json_data)
    data_dict=json.loads(json_string)
    my_list=data_dict['json_data']
    List=[]
    for x in my_list:
        calc(x,List)
    print(List)
    json_data={"answer":List}
    json_format=json.dumps(json_data,indent=2)
    print(json_format)
    return json_format

if __name__=="__main__":
    main()
    app.run(debug=True)




