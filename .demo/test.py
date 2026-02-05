from flask import Flask, render_template


#instantiating the application
app = Flask(__name__) 

# home route
@app.route('/')

def hello_world():
  return "Hello, world!"


# settings route
@app.route('/settings')

def settings():
  return "This is the settings page"



# dynamic routes
@app.route("/post/<int:post_id>")

def show_post(post_id):
  return 'Post %d' % post_id

# rendering a template
@app.route("/hello/<name>")

def hello(name=None):
  return render_template('index.html', name=name)

if __name__ == '__main__':
  app.run(debug=True)

