from flask import render_template, request, redirect, url_for,abort
from forms import RegistrationForm, LoginForm
from . import main
from .. import db

@main.route('/')
def index():
    return '<h1> Hello World </h1>'
