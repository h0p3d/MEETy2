from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/student/<int:id>')
def display_student(id):
	student = query_by_id(id)
	return render_template("student.html", student_id = id, student = student, year = student.year, name = student.name)

app.run(debug=True)
