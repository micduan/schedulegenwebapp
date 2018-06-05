import main
from datetime import datetime
from flask_login import UserMixin
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

login = LoginManager(main.app)
login.login_view = 'login'

class professors(main.db.Model):
	id = main.db.Column(main.db.Integer, primary_key=True)
	first = main.db.Column(main.db.String(30))
	last = main.db.Column(main.db.String(30))
	rating = main.db.Column(main.db.Float)
	num_ratings = main.db.Column(main.db.Integer)
	updated = main.db.Column(main.db.DateTime, default=datetime.utcnow)

class User(UserMixin, main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    username = main.db.Column(main.db.String(64), index=True, unique=True)
    email = main.db.Column(main.db.String(120), index=True, unique=True)
    password_hash = main.db.Column(main.db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)   

@login.user_loader
def load_user(id):
    return User.query.get(int(id))