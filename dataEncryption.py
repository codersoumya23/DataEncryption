import json
import math
import re
from flask import Flask, request

app=Flask(__name__)
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



@app.route('/data-encryption',methods=['POST'])
def main():

        json_data=request.get_json()
        #json_data='{"inputs":["coding","its harder to read code than to write it"]}'
        data_dict=json.loads(json_data)
        my_list=data_dict['inputs']
        List=[]
        for x in my_list:
            calc(x,List)
        print(List)
        json_data={"answer":List}
        json_format=json.dumps(json_data,indent=2)
        print(json_format)
        return json_format

if __name__=="__main__":
    #main()
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)





