from flask import Flask, render_template
import webjeopardy.jeopardy as jeopardy
import random

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    question = "tests"

    times = 1
    answerscategories = []
    for j in range(5):
        n = random.randint(0, 20000)
        category = n
        answerscategories.append(jeopardy.ask_question(category))
        
    return render_template('hello.html', name=name, answers=answerscategories)

