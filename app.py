# Import all the necessary libraries
from flask import Flask, render_template, url_for, flash, redirect, request, session
from flask_behind_proxy import FlaskBehindProxy
from forms import fitnessForm, log, second, third, mainForm
from flask_sqlalchemy import SQLAlchemy
from helper import make_google_fitness_tracking_api_request


# Create a Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd945cba4a6b3c7a43288ea10bc2e63d7'
proxied = FlaskBehindProxy(app)

# Create a sqlite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Associates a URL with a Python function - accesses the root URL "/"
@app.route("/",methods=['GET','POST'])
def home_page():
    forms = fitnessForm()
    if forms.validate_on_submit():
        flash('Welcome to the Fitness Tracker!', 'success')
        return redirect(url_for('log_in'))
    return render_template('index.html', subtitle='Welcome', form=forms)

# Associates a URL with a Python function - accesses the root URL "log_in"
@app.route("/log_in", methods=['GET', 'POST'])
def log_in():
    #create an instance of the log class
    form = log()
    if form.validate_on_submit():
        # This queries in the database to find the username and password with the provided username and password
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        # if the username is found stores the user ID in the session and will be redirected to the main page  
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main_page'))
        # if the username is not found then flash the message below
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('log_in.html', subtitle='Log In', form=form)



#Associates a URL with a Python function - accesses the root URL "second_page"
@app.route("/second_page",methods=['GET','POST'])
def second_page():
    forms= second()
    if forms.validate_on_submit():
        return redirect(url_for('third_page'))
    return render_template('second_page.html', subtitle='sign up', form=forms)


# Associates a URL with a Python function - accesses the root URL "terms_and_conditon"
@app.route("/terms_and_condtions",methods=['GET','POST'])
def terms_and_conditions():
    return render_template('terms_and_condtions.html', subtitle='Terms and conditons') 


# Associates a URL with a Python function - accesses the root URL "contact_us"
@app.route("/contact_us",methods=['GET','POST'])
def contuct_us():
    return render_template('contuct_us.html', subtitle='contuct us')


# Associates a URL with a Python function - accesses the root URL "about_us"
@app.route("/about_us",methods=['GET','POST'])
def about_us():
    return render_template('about_us.html', subtitle='about us') 


# Associates a URL with a Python function - accesses the root URL "sign_up"
@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    # make an instance of the fitnessForm class for the sign up
    form = fitnessForm()
    if form.validate_on_submit():
        #checks if a user with the same username exists in the User database
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            # if it does show this message
            flash('Username is already taken. Please choose a different username.', 'danger')
        else:
            #check if a user withe a specific email exists in User database
            existing_email = User.query.filter_by(email=form.email.data).first()
            if existing_email:
                flash('Email is already taken. Please choose a different email.', 'danger')
            else:
                # if the username and the email does not exist a new User object is created
                new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
                # the new user is added to the database session
                db.session.add(new_user)
                # the changes are commited to the dabase
                db.session.commit()
                # display the following message
                flash('Account created successfully!', 'success')
                # redirect user to the next page
                return redirect(url_for('second_page'))
    return render_template('sign_up.html', subtitle='Sign Up', form=form)


# Associates a URL with a Python function - accesses the root URL "third_page"
@app.route("/third_page",methods=['GET','POST'])
def third_page():
    forms = third()
    if forms.validate_on_submit():
        return redirect(url_for('main_page'))
    return render_template('third_page.html', subtitle='main page', form=forms) 


@app.route("/main_page", methods=['GET', 'POST'])
def main_page():
    # an instance of th mainForm class
    form = mainForm()
    # The function is called to retrieve a list of workouts from the ninja exercise API
    workouts = make_google_fitness_tracking_api_request()
    if form.validate_on_submit():
        # retrieve the selected msucle value
        muscle = form.muscle.data.lower()
        # filter the lsit of workouts based on the selected muscle and store it in a list using list comprehension
        #by checking if the selected muscle is contatined in the "muscles" attribute of each workout
        filtered_workouts = [workout for workout in workouts if muscle in workout['muscle'].lower()]
        # pass the filtered workouts to the main_page
        return render_template('main_page.html', subtitle='Review Page', form=form, workouts=filtered_workouts)
    return render_template('main_page.html', subtitle='Review Page', form=form, workouts=workouts)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")