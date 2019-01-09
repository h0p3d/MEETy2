from flask import Flask, render_template
app = Flask(__name__)

# Flask app with "Coming Soon" template from W3
# https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_coming_soon&stacked=h
@app.route('/')
def hello_world():
    return render_template("blog_template.html")

if __name__ == '__main__':
   app.run(debug = True)