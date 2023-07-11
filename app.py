# Import all the necessary libraries
from flask import Flask, render_template, url_for, flash, redirect, request, session
from flask_behind_proxy import FlaskBehindProxy
from forms import fitnessForm
from flask_sqlalchemy import SQLAlchemy


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
@app.route("/log_in",methods=['GET','POST'])
def log_in():
    if forms.validate_on_submit():
        flash(f'Logged in as {forms.username.data}!', 'success')
        return redirect(url_for('main_page'))

    return render_template('log_in.html', subtitle='Log in', form=forms)

#Associates a URL with a Python function - accesses the root URL "second_page"
@app.route("/second_page",methods=['GET','POST'])
def second_page():
    if forms.validate_on_submit():
        flash(f'Account created for {forms.username.data}!', 'success')
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
def contact_us():
    return render_template('contact_us.html', subtitle='contuct us')

# Associates a URL with a Python function - accesses the root URL "about_us"
@app.route("/about_us",methods=['GET','POST'])
def about_us():
    return render_template('about_us.html', subtitle='about us') 

# Associates a URL with a Python function - accesses the root URL "sign_up"
@app.route("/sign_up",methods=['GET','POST'])
def sign_up():
    if forms.validate_on_submit():
        flash(f'Account created for {fitnessform.username.data}!', 'success')
        return redirect(url_for('second_page'))

    return render_template('sign_up.html', subtitle='sign up', form=forms) 

# Associates a URL with a Python function - accesses the root URL "third_page"
@app.route("/third_page",methods=['GET','POST'])
def third_page():
    forms = fitnessForm()
    if form.validate_on_submit():
        return redirect(url_for('main_page'))

    
    return render_template('third_page.html', subtitle='main page', form=forms) 

# Associates a URL with a Python function - accesses the root URL "main_page"
@app.route("/main_page",methods=['GET','POST'])
def main_page():
    if forms.validate_on_submit():
        return redirect(url_for('main_page')) 
    return render_template('main_page.html', subtitle='Review Page', form=forms) 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")