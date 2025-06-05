from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def todo():
    todo_list = session.get('todo_list', [])
    if request.method == 'POST':
        task = request.form["task"]
        if task:
            todo_list.append(task)
            session['todo_list'] = todo_list
        elif len(todo_list) >= 5:
                error = "You can only have up to 5 tasks."
        else:
            return render_template('todo.html', error="Please enter a task", todo_list=todo_list)
        
    return render_template('todo.html', todo_list=todo_list)

if __name__ == '__main__':
    app.run(debug=True)