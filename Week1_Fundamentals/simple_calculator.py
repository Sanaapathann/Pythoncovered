from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y'])
        operation = request.form['operation']

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x / y
        else:
            result = "Operation Error"

        return render_template('simple_calculator.html', result=result)

    return render_template('simple_calculator.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)