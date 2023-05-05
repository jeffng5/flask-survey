from flask import Flask, request, render_template, redirect
from surveys import surveys, Question
from flask_debugtoolbar import DebugToolbarExtension
# from tkinter import *
# from tkinter.ttk import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug= DebugToolbarExtension(app)



responses=[]

@app.route('/')
def start_survey():
    return render_template('home.html')

@app.route('/questions/<int:num>')
def display(num):
    q= surveys['satisfaction'].questions[num]
    ans=Question(q, choices=None)
    return render_template('/questions.html', survey_q=q.question, answer0=ans.choices[0], 
            answer1=ans.choices[1])

@app.route('/questions/<int:num>', methods=['POST'])
def answer(num):
    num=0
    responses.append(request.form['tally'])
    num+=1
    print(responses)
    return redirect('/questions/{}'.format(num)), responses

@app.route('/questions/2')
def show():
    stuff=Question(question="On average, how much do you spend a month on frisbees?", choices=[['Less than $10,000'], ['$10,000 or more']])
    return render_template('oddQ.html', odd_q= stuff.question, answer2=stuff.choices[0], answer3=stuff.choices[1] )


    
     