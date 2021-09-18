from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey
app = Flask(__name__)
app.config['SECRET_KEY']= "secret!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def home_page():
    return render_template("survey_start.html", survey=survey)

@app.route("/begin", methods=["POST"])
def start_survey():

  
    return redirect("/questions/0")

@app.route("/answer",  methods=["POST"])
def questions():
    choice = request.form['answer']
    responses.append(choice)

    if (len(responses)==len(survey.questions)):
        return redirect("/thankyou")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def show_question(qid):

    if (responses is None):
        
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        
        return redirect("/thankyou")

    if (len(responses) != qid):
        
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template(
        "questions.html", question_num=qid, question=question)



@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

