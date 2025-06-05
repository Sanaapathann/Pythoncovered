from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def todo():
    todo_dict = session.get('todo_dict', {})

    error = None
    if request.method == 'POST':
         if 'remove' in request.form:
            # Remove the selected task
            task_to_remove = request.form['remove']
            if task_to_remove in todo_dict:
                del todo_dict[task_to_remove]
                session['todo_dict'] = todo_dict
            return redirect(url_for('todo'))
         else:
            task = request.form["task"].strip()
            if task:
                if task in todo_dict:
                    error = "Task already exists!"
                elif len(todo_dict) >= 5:
                    error = "You can only have up to 5 tasks."
                else:
                    todo_dict[task] = True  
                    session['todo_dict'] = todo_dict
            else:
                error = "Please enter a task"
        
    return render_template('todo1.html', error=error, todo_list=list(todo_dict.keys()))

if __name__ == '__main__':
    app.run(debug=True)