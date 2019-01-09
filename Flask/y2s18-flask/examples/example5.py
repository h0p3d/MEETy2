from flask import Flask, render_template
app = Flask(__name__)

# Flask app with template and loops!
@app.route('/')
def hello_world():
    pets = ["Rocky Rooster", "Lauren Llama", "Alice Alpaca"]
    
    return render_template("hello_loop.html",
    	pets=pets)

if __name__ == '__main__':
   app.run(debug = True)