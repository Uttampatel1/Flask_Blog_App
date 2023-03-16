from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from sqlalchemy import create_engine
from models import db, User, Post


# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# replace DATABASE_URI with the path to your SQLite database file
DATABASE_URI = 'sqlite:///project.db'

engine = create_engine(DATABASE_URI)

# initialize the app with the extension
db.init_app(app)


posts = [
    {
        'author' : 'Uttam pipaliya',
        'title' : 'Blog post 1',
        'content' : 'first post Content',
        'date_posted' : 'march 3, 2023'
    },
    {
        'author' : 'Ayush patel',
        'title' : 'Blog post 2',
        'content' : 'second post Content',
        'date_posted' : 'march 4, 2023'
    },
    {
        'author' : 'Dhruv patel',
        'title' : 'Blog post 3',
        'content' : 'three post Content',
        'date_posted' : 'march 4, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)

