from flask import Blueprint, render_template, redirect, url_for, request, session

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == "mauro@gmail.com" and password == '123':
            session['email'] = email
            session["token"] = 123
            return redirect(url_for('user.dashboard'))
        else:
            return "Credenciais invalidas!", 401
 
    return render_template("auth/login.html")