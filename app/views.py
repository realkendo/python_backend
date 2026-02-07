from app import app 

@app.route('/')
def index():
  return "Hello Flask"

@app.route('/user/<username>')
def show_user_profile(username):
  '''
  Docstring for show_user_profile
  
  :param username: Description
  '''
  return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
  '''
  show the post with given ID, the IS is an interger 
  '''
  return f'Post {post_id}'


# dynamic routes
@app.route('/login', method=['GET', 'POST'])

def login():
  if request.method == 'POST':
    return do_the_login()
  else:
    return show_the_login_form()


# constructing URLs
from flask import url_for

