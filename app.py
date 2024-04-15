from flask import Flask,request,render_template


app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal',methods=['GET'])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number2"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    return result

if __name__=='__main__':
    app.run(debug=True)