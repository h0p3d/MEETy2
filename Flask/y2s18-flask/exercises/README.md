### Y2 2018 Summer: Basic Flask Lab

Welcome to the Intro to Flask lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

Throughout this lab, you should be editing `app.py`.

### Part 1: First web page!

Edit the `home_page` function, using just Python, to return your favorite sport.
A stub for this function can be found in `app.py`.

Make sure you run `python app.py` to see your favorite sport
printed in your browser.

### Part 2: Adding a Template!

Add your first HTML template in `templates/index.html`.
This template should have
- A heading, h1 tag, with your favorite sport
- A paragraph about why it's the best sport.

Now, use the `render_template` function to see your
HTML page in the browser!

### Part 3: Adding CSS

Add a new rule in `static/style.css` to make the background color in
your website green.

Then, import this file in your HTML template. Open your HTML page
in the browser, to check that the background is green.

If you have extra time, build a color scheme for your website.

### Part 4: Using Loops and Conditionals!

- First, add a for loop into your template, to print a list
of your favorite players. This list should be defined
inside your Python `home_page` function.

- Use an if-statement, to check if a variable `likes_same_sport`, which
should be defined in your Python file, is True. If it is True,
render the whole website, as before.

- If it's False, just print the header and the paragraph explaining why you
think that it's the best sport. The list of best players should not be seen here.


### Part 5: Extras

If you finish any of the previous parts early, you can work
on some extra tasks, including:

Part 2 Extras:
- Organize your website using divs in `index.html`
- Adding images to your website
- Finding and importing more complex templates from W3

Part 3 Extras:
- Add a header to your website, and make sure to use margins and padding
to separate the header from the content on the website
- Adding a sidebar to your website, that doesn't move when you scroll

Part 4 Extras:
- Add a table to the website, with pictures and quotes from the most
memorable players or games.,
- Adding more complex if-statements into your website - for instance, checking
if the user likes the same sport as you, and how many players they would like to
see information about. This should determine the length of the list you show.
- Instead of specifying exactly how many players
the user wants to see, the template should accept a variable `users_favorite_player`.
The website should print all the players, until we print their favorite player. If this
is the first player, we only need to print one player. If their favorite player isn't
in the list of best players, then the entire list is printed.


