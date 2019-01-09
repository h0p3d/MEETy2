from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<int:student>')
def display_student(student):
    return render_template('student.html', student_id=student)

app.run(debug=True)
