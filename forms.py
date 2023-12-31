# Import all the necessary libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Create a class fitnessForm to be used in our main page
class fitnessForm(FlaskForm):

    def register_check(username):
        user = User.filter_by(username=username).first()
        if user == username:
            return False
        else:
            return True

    # For the sign_up page
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20), 
   # register_check(username)
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

  
        
class log(FlaskForm):

    def login_check(username):
        user = User.filter_by(username=username).first()
        if user == username:
            return True
        else:
            return False
        
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20), 
    #login_check(username)
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')




class second(FlaskForm):
    # For the second_page
    first_name = StringField('First name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=1, max=20)])
    sex = RadioField('Sex', validators=[DataRequired()], choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')])
    submit = SubmitField('Continue')

class third(FlaskForm):
    #For the third_page
    height = IntegerField('Height', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    goal = RadioField('What is your Goal?', validators=[DataRequired()],choices=[(1, 'Lose Weight'), (2, 'Gain Weight'), (3, 'Maintain Weight')])
    submit = SubmitField('Continue')

class mainForm(FlaskForm):
    muscle = SelectField('Muscle', choices=[('biceps', 'Biceps'), ('triceps', 'Triceps'), ('chest', 'Chest'), ('back', 'Back'), ('legs', 'Legs'), ('shoulders', 'Shoulders'), ('abs', 'Abs')])
    submit = SubmitField('Search')

    


    


    
