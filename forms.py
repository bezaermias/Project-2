# Import all the necessary libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Create a class fitnessForm to be used in our main page
class fitnessForm(FlaskForm):
    # For the sign_up page
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    #For the log_in
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])

    # For the second_page
    first_name = StringField('First name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=1, max=20)])
    sex = RadioField('Sex', validators=[DataRequired()], choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')])
    submit = SubmitField('Continue')

    #For the third_page
    height = IntegerField('Height', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    goal = RadioField('What is your Goal?', validators=[DataRequired()],choices=[(1, 'Lose Weight'), (2, 'Gain Weight'), (3, 'Maintain Weight')])
    submit = SubmitField('Finish')




    
