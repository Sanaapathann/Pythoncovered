from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fizz_buzz():
    result = ""
    if request.method == 'POST':
        num = int(request.form["number"])
        num_str = str(num)
        
        fizz_count = 0
        buzz_count = 0

        for ch in num_str:
            if ch == '5':
                fizz_count += 1
            elif ch == '7':
                buzz_count += 1
        
        for _ in range(fizz_count):
            result += "Fizz "

        for _ in range(buzz_count):
            result += "Buzz "

        if num % 5 == 0 and num % 7 == 0:
            result += "Fizz Buzz "
        elif num % 7 == 0:
            result += "Buzz "
        elif num % 5 == 0:
            result += "Fizz "
        elif num % 7 != 0 and num % 5 != 0:
            result += str(num)
        else:
            result = "Enter a valid number"

        return render_template('fizz_buzz.html', result=result)

    return render_template('fizz_buzz.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

