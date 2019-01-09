from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False') #'sqlite:////var/www/homepage/blog.db?check_same_thread=False'
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, year, finished_lab):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	student_object = Student(
		name=name,
		year=year,
		finished_lab=finished_lab)
	session.add(student_object)
	session.commit()

def query_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	student = session.query(Student).filter_by(
		name=name).first()
	return student

def query_all():
	"""
	Print all the students in the database.
	"""
	students = session.query(Student).all()
	return students

def delete_student(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Student).filter_by(
		name=name).delete()
	session.commit()

def update_lab_status(name, finished_lab):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.finished_lab = finished_lab
	session.commit()
def update_name(name, new_name):
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.name = new_name
	session.commit()
def update_year(name, year):
	student_object = session.query(Student).filter_by(
		name=name).first()
	student_object.year = year
	session.commit()
	
def query_by_id(student_id):
    student = session.query(Student).filter_by(
        student_id=student_id).first()
    return student
