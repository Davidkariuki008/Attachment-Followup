import os
import secrets
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from run import app


from . import auth
from .forms import RegistrationForm, LoginForm, UpdateAccountForm
from ..models.models import User
from app import db


@auth.route('/')
def index():
    return render_template('index.html')

# register route
@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

# login route  
@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('job.all_jobs'))  
        else:
            flash('Check on Your email or password and try again!')
    return render_template('login.html', form=form)

# logout route
@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out')
    return render_template('logout.html')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@auth.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone_no = form.phone.data
        current_user.employment_status = form.employment_status.data
        current_user.worker_description = form.worker_description.data
        db.session.commit()
        flash('Your account has been updated successfully')
        return redirect(url_for('auth.account'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone.data = current_user.phone_no
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form = form)