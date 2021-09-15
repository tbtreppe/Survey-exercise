from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey
app = Flask(__name__)
app.config['SECRET_KEY']= "name"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/homepage')
def home_page():
    return render_template("homepage.html", survey=survey)

@app.route('/questions/0')
def questions():
    return render_template("questions0.html")

@app.route('/answers')
def answers():
    return responses.append("answers")

@app.route('/')
def redirect_to_next_question():
    return redirect("questions1.html") 