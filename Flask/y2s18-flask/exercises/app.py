from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	show_more = True
	fav_players = ["Barney", "Taylor Swift", "David Guetta", "Imagine Dragons"]
	return render_template("temp1.html", show_more = show_more, fav_players=fav_players)

if __name__ == '__main__':
   app.run(debug = True)