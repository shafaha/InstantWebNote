from flask import Blueprint
from flask import render_template, request, flash, redirect, abort, url_for
from .forms import SignupForm, LoginForm
from note import AppStarter
from .models import User, Notes
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login/", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if request.method != "GET":
        if form.validate_on_submit():
            print("Control 1")
            print(form.data)
            user = User.query.filter_by(email = form.email.data).first()
            print(user)
            if user and AppStarter.getBcrypt().check_password_hash(user.password, form.password.data): 
                print("Control 2") 
                flash("Login Successful", 'success')
                login_user(user, remember = form.remember.data)
                next_page = request.args.get('next')
                if next_page:
                    print(next_page)
                    return redirect(url_for('signup'))
                else:
                    return redirect(url_for('views.home'))
        else:
            print("Control 3")
            flash("Login Unsuccessful, Please check email and password", 'danger')
            return redirect(url_for('auth.login'))
        
    return render_template('login.html', title ="Login", form = form)


@auth.route("/logout/", methods = ["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup/", methods = ["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method != "GET": 
        print(request.data)
        if form.validate_on_submit():
            password_hash = AppStarter.getBcrypt().generate_password_hash(form.password.data)
            usr = User(form.username.data, form.email.data,password_hash) 
            AppStarter.getDb().session.add(usr)
            AppStarter.getDb().session.commit()
            print(User.query.all())       
            flash("Register Successful", "success")
            return redirect(url_for('auth.login'))
        else:
            flash("Register UNSuccessful,", "dangerous")
            return redirect(url_for('auth.signup'))

    return render_template("signup.html", title = "SignUp", form = form)

@auth.route("/account/", methods = ["GET", "POST"])
@login_required
def account():
    pass

