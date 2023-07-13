# Import all the necessary libraries
from flask import Flask, render_template, url_for, flash, redirect, request, session
from flask_behind_proxy import FlaskBehindProxy
from forms import fitnessForm, log, second, third
from flask_sqlalchemy import SQLAlchemy
from helper import make_google_fitness_tracking_api_request, save_users_to_database

# Create a Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd945cba4a6b3c7a43288ea10bc2e63d7'
proxied = FlaskBehindProxy(app)


# Create a sqlite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#create a manual database
# user_reference_db = [{
#     'name': 
#     'password':
# }]


class User(db.Model):
    login_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

with app.app_context():
    #db.drop_all()
    db.create_all() 

# Associates a URL with a Python function - accesses the root URL "/"
@app.route("/",methods=['GET','POST'])
def home_page():
    forms = fitnessForm()
    if forms.validate_on_submit():
        flash('Welcome to the Fitness Tracker!', 'success')
        return redirect(url_for('log_in'))
    return render_template('index.html', subtitle='Welcome', form=forms)

# Associates a URL with a Python function - accesses the root URL "log_in"
@app.route("/log_in",methods=['GET','POST'])
def log_in():
    forms = fitnessForm()
    if forms.validate_on_submit():
        print("FORM HAS BEEN VALIDATED")
        flash(f'Logged in as {forms.username.data}!', 'success')
        return redirect(url_for('main_page'))

    return render_template('log_in.html', subtitle='Log in', form=forms)

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
    if forms.validate_on_submit():
        flash('Review submitted!', 'success')
        return redirect(url_for('sign_up'))
    return render_template('terms_and_conditions.html', subtitle='Terms and conditons', form=forms) 

# Associates a URL with a Python function - accesses the root URL "contact_us"
@app.route("/contact_us",methods=['GET','POST'])
def contuct_us():
    return render_template('contuct_us.html', subtitle='contuct us')

# Associates a URL with a Python function - accesses the root URL "about_us"
@app.route("/about_us",methods=['GET','POST'])
def about_us():
    return render_template('about_us.html', subtitle='about us') 

# Associates a URL with a Python function - accesses the root URL "sign_up"
@app.route("/sign_up",methods=['GET','POST'])
def sign_up():
    forms = fitnessForm()
    if forms.validate_on_submit():
        print("REGISTRATION HAS BEEEN VALIDATED")
         #db entry
        user_info = User(id='success', username=forms.username.data, password=forms.password.data)
        #print(user_info)
        db.session.add(user_info)
        db.session.commit()
        flash(f'Account created for {forms.username.data}!', 'success')
        return redirect(url_for('second_page'))

    return render_template('sign_up.html', subtitle='sign up', form=forms) 

# Associates a URL with a Python function - accesses the root URL "third_page"
@app.route("/third_page",methods=['GET','POST'])
def third_page():
    forms = third()
    if forms.validate_on_submit():
        return redirect(url_for('main_page'))

    
    return render_template('third_page.html', subtitle='main page', form=forms) 

# Associates a URL with a Python function - accesses the root URL "main_page"
@app.route("/main_page",methods=['GET','POST'])
def main_page():
    workouts = make_google_fitness_tracking_api_request()
    if workouts == None:
        print(workouts)
    print(workouts)
    return render_template('main_page.html', subtitle='Review Page', workouts=[])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")