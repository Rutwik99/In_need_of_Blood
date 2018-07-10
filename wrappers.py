from functools import wraps
from flask import session, redirect, url_for, flash, render_template


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session['logged_in'] is True:
                return f(*args, **kwargs)
            else:
                return redirect(url_for("login_page"))
        else:
            flash("You need to login first")
            return redirect((url_for("login_page")))
    return wrap


def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' not in session:
                return f(*args, **kwargs)
        else:
            flash("You need to logout first")
            return render_template("header.html")
    return wrap
