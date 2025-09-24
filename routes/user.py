from flask import Blueprint, render_template, redirect, url_for, session

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def login():
    return "Welcome to the User Page!"
    #return render_template("auth/login.hrml")

@user_bp.route('/settings')
def settings():
    return "Welcome to the Settings Page!"

@user_bp.route('/dashboard')
def dashboard():
    name = session['email']
    return render_template('dashboard.html', name=name)

@user_bp.before_request
def check_autentication():
    if 'token' not in session:
        return redirect(url_for('auth.login'))