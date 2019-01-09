from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/add', methods = ["GET", "POST"])
def add_student_route():
	if request.method == "GET":
		return render_template("add.html")
	else:
		student_name = request.form['Name']
		student_year = request.form['Year']
		add_student(student_name, student_year, False)
		return render_template("response.html", action = "adding", name = student_name)

@app.route("/delete", methods = ["GET", "POST"])
def delete_student_route():
	if request.method == "GET":
		return render_template("delete.html")
	else:
		id = int(request.form["id"])
		student = query_by_id(id)
		if student == None:
			return "Action failed. ID does not exist."
		name = student.name
		delete_student(name)
		return render_template("response.html", action = "deleting", name = name)

@app.route("/remove/<string:id>") #if you are just getting or just posting you don't need to list multiple methods
def remove_student_route(id):
	id = int(id)
	student = query_by_id(id)
	if student == None:
			return "Action failed. ID does not exist."
	name = student.name
	delete_student(name)
	return render_template("response.html", action = "removing", name = name)

@app.route("/edit", methods = ["GET", "POST"])
def edit_student_route():
	if request.method == "GET":
		return render_template("edit.html")
	else:
		change = request.form['change']
		value = request.form['new_value']
		id = int(request.form['id'])
		student = query_by_id(id)
		if change == "year":
			if "2" in value:
				update_year(student.name,"Year 2")
			elif "1" in value:
				update_year(student.name,"Year 1")
			else:
				update_year(student.name,"Year 3")
		elif change == "name":
			update_name(student.name, value)
		else:
			update_lab_status(student.name, value != "False")
		return render_template("response.html", action = "editing", name = student.name)


@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)
