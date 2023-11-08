from flask import Flask, request, render_template, redirect
from surveys import surveys, Question
# from flask_debugtoolbar import DebugToolbarExtension
from flask import session
# from tkinter import *
# from tkinter.ttk import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
# debug= DebugToolbarExtension(app)

responses=[]

@app.route('/')
def start_survey():
    return render_template('home.html')

@app.route('/satisfaction-questions/<int:num>')
def display(num):
    q= surveys['satisfaction'].questions[num]
    ans=Question(q, choices=None)

    return render_template('/questions.html', survey_q=q.question, answer0=ans.choices[0], 
            answer1=ans.choices[1])

@app.route('/satisfaction-questions/<int:num>', methods=['POST'])
def answer(num):
    session['response']=request.form['tally']
    responses.append(session['response'])
    print(responses)
    return redirect('/satisfaction-questions/{}'.format(num+1))

@app.route('/satisfaction-questions/2')
def show():
    stuff=Question(question="On average, how much do you spend a month on frisbees?", choices=[['Less than $10,000'], ['$10,000 or more']])
    return render_template('oddQ.html', odd_q= stuff.question, answer2=stuff.choices[0], answer3=stuff.choices[1] )

@app.route('/satisfaction-questions/4')
def end():
    return render_template('thank_you.html')
    


##### HERE IS THE CODE FOR PERSONALITY SURVEY #####

@app.route('/personality-questions/<int:num>')
def display1(num):
    q= surveys['personality'].questions[num]
    ans=Question(q, choices=None)
    return render_template('/questions.html', survey_q=q.question, answer0=ans.choices[0], 
            answer1=ans.choices[1])

@app.route('/personality-questions/<int:num>', methods=['POST'])
def answer1(num):
    session['response']=request.form['tally']
    responses.append(session['response'])
    print(responses)
    return redirect('/personality-questions/{}'.format(num+1))
@app.route('/personality-questions/2', methods=['POST'])
def answer2(num):
    q=surveys['personality'].questions[num]
    ans=Question(q[0])
    ans2=Question(q[1])
    return redirect('/personality-questions/{}'.format(num+1), ans)
@app.route('/personality-questions/3', methods=['POST'])
def answer3(num):
    
    session['response']=request.form['tally']
    responses.append(session['response'])
    print(responses)
    return redirect('/personality-questions/{}'.format(num))
