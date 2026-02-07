from app import app 
from flask import render_template

# home route
@app.route('/')
def index():
  return render_template('index.html', title='Home Page', name='Ken Dough', messages=["Hello", "Hi", "Hey"])


