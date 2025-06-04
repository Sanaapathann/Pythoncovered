from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def adv_calculator():
    result = None                                                
    x = ''                                                      
    y = ''                                                       
    operation = ''                                               
    if request.method == 'POST':                                 
        try:
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
                if y == 0:
                    result = "Division by zero error"
                else:
                    result = x / y
            else:
                result = "Operation Error"

            x = result                                            
            y = ''                                                
        except ValueError:
            result = "Please enter valid numbers"
        except Exception as e:
            result = f"Error: {e}"

    return render_template('advanced_calculator.html', result=result, x=x, y=y, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)


