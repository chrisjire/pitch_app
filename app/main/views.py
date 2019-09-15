from flask import render_template, request, redirect, url_for,abort
from .forms import RegistrationForm, LoginForm
from . import main
from .. import db

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
    return redirect(url_for('home'))
    return render_template('register.html', title = Register, form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
