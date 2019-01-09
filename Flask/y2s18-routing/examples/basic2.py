from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/hello')
def hello_route():
    return render_template('hello.html', n = 'Emily')

app.run(debug=True)