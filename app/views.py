# from flask import Flask, request
from app import app
from app import data
# from flask import request
# from flask import Response
from flask import render_template
from flask import url_for

# app = Flask(__name__)

@app.route('/')
def home(): 
	tplvars = get_tplvars()
	return render_template("home.jinja", **tplvars) 

@app.route('/characters/<string:charname>')
def singlechar(charname): 
	charname = charname.replace("-"," ")
	char = data.import_charsheet(charname)
	tplvars = get_tplvars()
	if None == char:
		return render_template("character_404.jinja", **tplvars) 
	tplvars ['character'] = char
	tplvars ['title'] = f"{charname} &larr; Mothership Character Sheets"
	tplvars ['skills'] = data.load_skills()
	return render_template("charsheet.jinja", **tplvars) 

@app.route('/characters')
def chars(): 
	chars = data.get_all_chars()
	tplvars = get_tplvars()
	tplvars['chars'] = chars
	tplvars['title'] =  "Mothership Character Sheets"
	return render_template("characters.jinja", **tplvars) 

def get_tplvars():
	return {
		'stylesheet' : url_for('static', filename='style.css'),
		'title' : "Mothership characters"
	}