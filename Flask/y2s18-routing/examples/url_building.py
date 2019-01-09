from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('home_with_link.html')

@app.route('/hello')
@app.route('/hello/<string:name>')
def hello_route(name="Default Name"):
    return render_template('hello_with_link.html', n=name)

app.run(debug=True)
