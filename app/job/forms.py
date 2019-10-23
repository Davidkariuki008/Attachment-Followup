from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError,TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Length
from datetime import date


class PostJob(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    category = SelectField('Job Category', choices=[('househelp','Domestic Work'),('coding','Software Developemt'),('coding','Construction'),('coding','Software Developemt'),('coding','Software Developemt'),('coding','Software Developemt')], validators=[DataRequired()])
    date = DateField('Date Posted', default = date.today(), format='%d/%m/%Y')
    jd = TextAreaField('Job Description', validators=[DataRequired()])
    submit = SubmitField('Post Job')

class ReviewForm(FlaskForm):
    username = StringField('User You want to Review', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[('0', '0'),('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5')])
    comment = TextAreaField('Comment about the Worker', validators=[DataRequired()])
    submit = SubmitField('Review')

class ApplyJob(FlaskForm):
    receiver = StringField('To', validators=[DataRequired()])
    sender = StringField('FROM', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('SEND')
    