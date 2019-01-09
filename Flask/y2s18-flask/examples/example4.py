from flask import Flask, render_template
app = Flask(__name__)

# Flask app with template and variables
@app.route('/')
def hello_world(year='y2'):
    return render_template("hello_vars.html",
    	year=year)

if __name__ == '__main__':
   app.run(debug = True)