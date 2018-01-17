from flask import Flask, flash, redirect, render_template, request, session, url_for, g, jsonify
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)

@app.route('/')
def index():
	return render_template("index.html")
	
@app.route('/experience')
def experience():
	return render_template("experience.html")
	
@app.route('/hobbies')
def hobbies():
	return render_template("hobbies.html")

@app.route('/personality')
def personality():
	return render_template("personality.html")
	
		
if __name__ == "__main__":
	app.run()
	