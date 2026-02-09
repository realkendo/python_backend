from app import app 
from flask import render_template
from flask import request, redirect, url_for, allowed_file
# file import
import os
from werkzeug.utils import secure_filename

# home route
@app.route('/')
def index():
  return render_template('index.html', title='Home Page', name='Ken Dough', messages=["Hello", "Hi", "Hey"])

# contact form route
@app.route('/contact')
def contact():
  return render_template('contact.html')

# route to handle the form post request
@app.route('/handle_form', methods=['POST'])
def handle_form():
  name = request.form['name']
  email = request.form['email']
  # process or store the form data here
  return redirect(url_for("Thank you"))

# file upload route
@app.route('/handle_file_upload', methods=['POST'])
def handle_file_upload():
  file = request.file['file']
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return "File upload successful"



