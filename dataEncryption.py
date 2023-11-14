import json
import math
import re
from flask import Flask
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

# @app.route('/data-encryption',methods=['GET'])
def data_encryption():
    url = "http://127.0.0.1:5000/data-encrpytion"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

@app.route('/data-encryption',methods=['POST'])
def main():
    json_data=data_encryption()
    #json_data='{"inputs":["coding","its harder to read code than to write it"]}'
    data_dict=json.loads(json_data)
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




