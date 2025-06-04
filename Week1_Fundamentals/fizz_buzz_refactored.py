from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

def fizzbuzz_string(num):
    num_str = str(num)
    fizz_count = num_str.count('5')
    buzz_count = num_str.count('7')
    result = ""

    result += "Fizz" * fizz_count
    result += "Buzz" * buzz_count

    if num % 5 == 0 and num % 7 == 0:
        result += "FizzBuzz"
    elif num % 7 == 0:
        result += "Buzz"
    elif num % 5 == 0:
        result += "Fizz"
    if not result:
        result = str(num)
    return result.lower()

@app.route('/', methods=['GET', 'POST'])
def fizz_buzz():
    feedback = None
    if request.method == 'POST':
        num = session.get('random_num')
        user_input = request.form.get('guess', '').replace(' ', '').lower()
        correct = fizzbuzz_string(num)
        if user_input == correct:
            feedback = f"Correct! {num} -> {correct}"
        else:
            feedback = f"Incorrect. {num} -> {correct}. You entered: {user_input}"
        
        session['random_num'] = random.randint(1, 100)
    else:
        session['random_num'] = random.randint(1, 100)
    return render_template('fizz_buzz_re.html', 
                           random_num=session['random_num'], 
                           feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)