from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from . import job
from .forms import PostJob, ReviewForm
from ..models.models import Job, User, Review
from app import db


@job.route('/post-job', methods=['GET','POST'])
def post_job():
    form = PostJob()
    if form.validate_on_submit():
        job = Job(
            job_title = form.job_title.data,
            date_posted = form.date.data,
            location = form.location.data,
            job_description = form.jd.data,
            job_category = form.category.data,
            user_id = current_user.id
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('job.all_jobs'))
    return render_template('post_job.html', form = form)

@job.route('/all-jobs')
@login_required
def all_jobs():
    jobs = Job.query.all()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('jobs.html', jobs=jobs, image_file=image_file)

@job.route('/workers/<username>/review', methods=['GET','POST'])
@login_required
def review(username):
    user= User.query.filter_by(username = username).first_or_404()
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(
            username = form.username.data,
            rate = form.rating.data,
            comment = form.comment.data,
            user_id = current_user.id
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('job.user', username = username))
    return render_template('review.html', form=form, user = user)

@job.route('/workers/')
def workers():
    workers = User.query.all()
    return render_template('workers.html', workers=workers)

@job.route('/workers/<username>')
def user(username):
    sum = 0
    count = 0
    average = 0 
    user= User.query.filter_by(username = username).first_or_404()
    reviews = Review.query.filter_by(username=username).all()
    #getting average of the ratings
    for review in reviews:
        if review.rate:
            sum = sum + review.rate
            count += 1
            average = sum//count
        else:
            average
    
    return render_template('user.html', user = user, reviews = reviews, average =average, count = count)

@job.route('/delete/<int:jobs_id>', methods = ['GET','POST'])
@login_required
def delete(jobs_id):
    job = Job.query.get_or_404(jobs_id)
    db.session.delete(job)
    db.session.commit()
    flash('Your Job has been deleted successfully')
    return redirect(url_for('job.all_jobs'))