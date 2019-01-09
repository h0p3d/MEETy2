from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/hello')
def hello_route(name='Emily'):
    return render_template('hello.html', n=name)

@app.route('/hello/<string:name>')
def hello_name_route(name='Emily'):
    return render_template('hello.html', n=name)

# Comment out the two previous routes and show
# that this combined route does the same thing
# @app.route('/hello')
# @app.route('/hello/<string:name>')
# def hello_route(name='Emily'):
#     return render_template('hello.html', n=name)

app.run(debug=True)
