from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal', methods=['GET','POST'])
def math_operation():
    data = request.get_json()
    operation = data.get("operation")
    number1 = float(data.get("number1"))
    number2 = float(data.get("number2"))

    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    else:
        result = number1/number2
        
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
