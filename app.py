from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def survey_start():
    """Returns Landing Page"""
    # initialize session dictionary
    session["responses"] = []
    session.pop("_flashes", None)
    return render_template('survey_start.html', 
    title = survey.title, 
    instructions = survey.instructions)

@app.route('/begin', methods = ['POST'])
def begin_survey():
    """Redirects to the questions landing page"""

    return redirect('/questions/0')   

@app.route('/questions/<int:question_num>')
def ask_questions(question_num):
    """Handles questions and sends request to answer"""

    # Handle users trying to skip or repeat questions 
    response_length = len(session["responses"])
    if question_num != response_length:
        question_num = response_length 
        flash("You are trying to access an invalid question")
        return redirect(f'/questions/{response_length}')

    elif question_num > len(survey.questions) and response_length == len(survey.response):
        # Handles users trying to access completed questions
        flash('You have already completed the survey')
        # return redirect('/completion')
        return redirect('/completion')
        

    if question_num < len(survey.questions):
        # TODO: ADD FLASH MESSAGES TO THE TEMPLATE
        return render_template('question.html', 
        question = survey.questions[question_num].question, 
        choices = survey.questions[question_num].choices,
        question_num = question_num + 1)

    # Loop through each survey question, once complete
    # send to completion page        
    return redirect('/completion')



    

@app.route('/answer/<int:question_num>', methods = ['POST']) # 
def update_answer(question_num):
    """Updates answer list and redirects to next question"""

    # get answers from form
    answer = request.form['answer']
    responses = session["responses"]
    # add responses to session 
    responses.append(answer)
    session['responses'] = responses   # sesson['responses'] + [answer]  -- only changes cookie when session changes
    return redirect(f'/questions/{question_num}')

@app.route('/completion')
def survey_complete():
    """Page to show user that survey has been completed"""
    return render_template('completion.html')

