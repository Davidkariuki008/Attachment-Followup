from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create a table for the workers
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    phone_no = db.Column(db.String(12), unique=True)
    password_hash = db.Column(db.String(128))
    employment_status = db.Column(db.String())
    worker_description = db.Column(db.String())
    job = db.relationship('Job', backref='user', lazy=True)
    review = db.relationship('Review', backref='user', lazy=True)


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Worker: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# jobs table
class Job(db.Model):

    __tablename__ = 'jobs'
    jobs_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(60), index=True)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    job_description = db.Column(db.Text, nullable=False)
    job_category = db.Column(db.String, nullable=False)
    location = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

    def __repr__(self):
        return '<Job: {}>'.format(self.job_description)

class Review(db.Model):

    __tablename__ = 'reviews'


    review_id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer)
    comment = db.Column(db.Text)
    username = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Review: {}>'.format(self.comment)