from app import app 
from flask import url_for

# home route
@app.route('/')
def index():
  return "index"

# login route
@app.route('/login')
def login():
  return "login"

# user's route
@app.route('/users/<username>')
def profile(username):
  return f'{username}\'s profile'

with app.test_request_context():
  print(url_for('index'))
  print(url_for('login'))
  print(url_for('login', next='/'))
  print(url_for('profile', username="John Doe"))

# error handling
@app.errorhandler(404)
def page_not_found(error):
  return "This page does not exist.", 404

@app.errorhandler(500)
def internal_server_error(error):
  return "Internal server error.", 500



