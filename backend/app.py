from flask import Flask, request, jsonify
import time
from utils import format_username, divide

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/sum")
def sum_numbers():
    nums = [1, 2, 3, 4, 5]
    total = 0
    for i in range(len(nums) - 1):
        total += nums[i]
    return str(total)

@app.route("/age-check")
def age_check():
    age = request.args.get("age", "0")
    if age > 18:
        return "Adult"
    return "Minor"

@app.route("/timer")
def timer():
    start = time.time()
    time.sleep(0.1)
    elapsed = int(time.time() - start)
    return f"Elapsed: {elapsed} seconds"

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    result = eval(expr)
    return str(result)

@app.route("/user")
def user():
    name = request.args.get("name")
    formatted = format_username(name)
    return jsonify({"user": formatted})


@app.route("/divide")
def divide_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 1))
    result = divide(a, b)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)