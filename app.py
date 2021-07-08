from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []  # variable to store user responses to question

@app.route('/')
def survey_start():
    """Returns Landing Page"""

    return render_template('survey_start.html', 
    title = survey.title, 
    instructions = survey.instructions)


@app.route('/begin', methods = ['POST'])
def begin_survey():
    """Redirects to the questions landing page"""

    flash('Starting first question')
    return redirect('/questions/0')   


@app.route('/questions/<int:question_num>', methods = ['GET', 'POST'])
def ask_questions(question_num):
    """Handles questions and sends request to answer"""

    # print(request.args)

    if question_num < len(survey.questions):

        breakpoint()
        return render_template('question.html', 
        question = survey.questions[question_num].question, 
        choices = survey.questions[question_num].choices,
        question_num = question_num + 1)
        # answer = request.args['answer']

        # NEXT: debug answer 

    # breakpoint()

    return 'Survey complete!'
    

@app.route('/answer/<int:question_num>', methods = ['GET', 'POST']) # 
def update_answer(question_num): # question_num, answer
    """Updates answer list and redirects to next question"""

    answer = request.form['answer']

    breakpoint()

    responses.append(answer)

    print('Should append answer', answer)
    print(responses)

    return redirect(f'{question_num}')
    # return redirect('/questions/<int:questions_num>')





# @app.route('<question_num>/<answer>') # /answer/<int:question_num>
# def update_answer(question_num, answer):
#     """Updates answer list and redirects to next question"""

#     # session['']

#     responses.append(answer)

#     return redirect(f'questions/{question_num}')
    
    

