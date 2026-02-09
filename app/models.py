from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username

# inserting data
new_user = User(username='johndoe', email='johndoe@gitforgits.com')
db.session.add(new_user)
db.session.commit()

# querying data
user = User.query.filter_by(username='johndoe').first()
print(user.email)

# updating data
user = User.query.filter_by(username='johndoe').first()
user.email = 'newemail@gitforgits.com'
db.session.commit()

# deleting data
user = User.query.get(1) #Assumes '1' is the ID of the user
db.session.delete(user)
db.session.commit()

# handling relationships
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  user = db.relationship('User',backref=db.backref('posts', lazy=True))


#retrieving related data
user = User.query.get(1) #get the user with id=1
posts = user.posts #access all posts made by this user

for post in posts:
  print(post.title)

#eager loading example
user = User.query.options(joinedload(User.posts)).filter_by(username='johndoe').first()

for post in user.posts:
  print(post.title)

