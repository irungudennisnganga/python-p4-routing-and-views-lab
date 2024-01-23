#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return 'hello'
    

@app.route("/count/<parameter>")
def count(parameter):
    # print('hello')
    new=[]
    for n in range(int(parameter)):
        new.append(n)
    return [w for w in new]

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1,operation,num2):
    
    if operation == '+' :
        total=num1 + num2
        # print(total)

    elif operation == '-'  :
        total=num1 - num2
        # print(total)
        
    elif operation == '*' :
        total=num1 * num2
        print(total)
        
    elif operation == 'div' :
        total=num1 / num2
        # print(total)    
    
    elif operation == '%' :
        total=num1 % num2
        # print(total)
        
    return str(total)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
