# Y2 2018 Summer: Routing Lab

Welcome to the routing lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Setup

Before you start coding, make sure you fork and clone the repository
for this lab:
```
cd ~/Desktop
git clone https://github.com/YOUR_GITHUB_USERNAME/y2s18-routing.git
```

## Lecture Exercises

**Important**: Work in the `exercises` folder!

### Part 1: Basic routing

In `app.py`, change the route for `/` to display the `home.html`
template. You can open `home.html` in Sublime to see what the template
looks like. Remember that templates are in the `templates` folder!

*Hint*: Remember functions you've learned in earlier lectures, like
`render_template`.

You can go back to the command line now and start the server, using
`python app.py`. In the browser, go to `http://127.0.0.1:5000` to
see what it looks like so far.

### Part 2: Variable Routes

In `app.py`, add a route and call the function for this route
`display_student(student_id)`. When you navigate to
`http://127.0.0.1:5000/student/4`, for example, you should see the
`student.html` template where `student_id` is 4.

*Hint*: The variable `student_id` should have type `int`.

### Part 3: URL Building

In `student.html`, add a link to the home page.

*Hint*: Remember how to use `url_for()`.

## Independent Lab: Displaying student information

**Important**: Work in the `lab` folder!

### Part 1

In `student.html`, add some text and the templating elements
`{{ student.name }}`, `{{ student.year }}`, and `{{ student.finished_lab }}`.
*Hint*: `student.name` returns the `name` attribute of `student`.

### Part 2

In `app.py`, in the `return` statement of `display_student(student_id)`,
change the parameters of `render_template()` for the template to display
the information of the student with `student_id`.
*Hint*: In `databases.py`, there is a function called `query_by_id(id)` that
returns the Student object with the given `id`, which is an `int`.
*Hint*: You can set `student=query_by_id(student_id)` as the second
parameter of `render_template()`.
 is `student_id`.

### Part 3

Refresh your webpage in the browser to make sure everything works as
expected. If there are errors and the server goes down, you can restart
the server from the command line with `python app.py` again.

### Part 4

In all the files in the `templates` folder, change the `href` attribute
of the `<link>` tag to be `{{url_for('static', filename='style.css')}}`.
Add your own CSS and additional templating like you've learned in the
past few days!

## Lab Bonus: Listing all students

### Part 1

In `home.html`, add templating code to display the name, year, and
finished_lab status of each student, using `{% for %}` and `{% endfor %}`.

### Part 2

Edit the route to the home page to give `home.html` all the information
it needs. *Hint*: You'll want to use `query_all()`.

### Part 3

In the `home.html` template, add a link in the same `for` loop which will
bring you to the page for each student.

### Part 4

Again, check that everything works in the browser. Restart your server if
it goes down again, with `python app.py`.


## Additional bonuses

1. Add a new page with all the students from a given year, with a home page
for each year.

2. Figure out a way to add a photo to each student's page.

3. Incorporate a color scheme.
