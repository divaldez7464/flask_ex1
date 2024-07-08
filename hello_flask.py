
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

#Task 2
# @app.route('/')
# def hello():
#   return '<p>Diego Valdez: LMAO</p>'

#Task 4
@app.route('/')
def hello():
  return render_template('index.html')

#Task 3
@app.route('/diego')
def ac():
    return '<p>LMAO</p>'