import main
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

class professors(main.db.Model):
	id = main.db.Column(main.db.Integer, primary_key=True)
	first = main.db.Column(main.db.String(30))
	last = main.db.Column(main.db.String(30))
	rating = main.db.Column(main.db.Float)
	num_ratings = main.db.Column(main.db.Integer)
	updated = main.db.Column(main.db.DateTime, default=datetime.utcnow)

user_roles = main.db.Table('user_roles',
    main.db.Column('user_id', main.db.Integer, main.db.ForeignKey('user.id')),
    main.db.Column('role_id', main.db.Integer, main.db.ForeignKey('roles.id'))
)

class User(UserMixin, main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    username = main.db.Column(main.db.String(64), unique=True)
    first = main.db.Column(main.db.String(30))
    last = main.db.Column(main.db.String(30))
    email = main.db.Column(main.db.String(120), index=True, unique=True)
    password_hash = main.db.Column(main.db.String(128))
    token = main.db.Column(main.db.String(50))
    roles = relationship("Roles", secondary=user_roles, backref=main.db.backref('users'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 

    def is_admin(self):
        
        user_is_valid = User.query.filter(User.roles.any(id=1)).filter_by(id=self.id).first()

        if user_is_valid:
            return True
        return False

class Roles(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    name = main.db.Column(main.db.String(15), unique=True, nullable=False)
    description = main.db.Column(main.db.String(100))


