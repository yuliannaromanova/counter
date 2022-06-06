from crypt import methods
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0

    return render_template('index.html')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')


@app.route('/add2', methods = ['POST'])
def add2():
    session['count'] +=1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)