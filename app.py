from flask import Flask, flash, redirect, render_template, request, session, url_for, g, jsonify
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)

@app.route('/')
def index():
	return render_template("index.html")
	
@app.route('/bouldering')
def bouldering():
	return render_template("bouldering.html")
	
@app.route('/badminton')
def badminton():
	return render_template("badminton.html")

@app.route('/personality')
def personality():
	return render_template("personality.html")
	
		
if __name__ == "__main__":
	app.run(debug=True)
	