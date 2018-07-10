from flask import Flask, render_template, flash, url_for, redirect, request, session, send_file, send_from_directory, jsonify
from content_management import *
from passlib.hash import sha256_crypt
from wtforms import Form, BooleanField, PasswordField, validators, StringField, TextAreaField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.fields import SelectField, IntegerField
from pymysql import escape_string as thwart
from connection import *
import gc
from flask_mail import Mail, Message
import os
from get18_back import *
from wrappers import *
import models

app = Flask(__name__, instance_path="/home/sriteja/PycharmProjects/Blood Bank/protected")
app.secret_key = 'sriteja_charan'
app.config.update(
    DEBUG=True,
    MAIL_SERVER='students.iiit.ac.in',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='sriteja.sugoor@students.iiit.ac.in',
    MAIL_PASSWORD='Mail Password'
    )
mail = Mail(app)


USER_DICT = content()
bloodgroups_lis = bloodgroups()
states = state_list()
gender_lis = gender_list()
cities_dict = cities_list()


#Required Classes
class RequestForm(Form):
    bloodgroup = SelectField('Blood Group', [validators.InputRequired()], coerce=str, choices=bloodgroups_lis,
                             render_kw={"placeholder": "Select blood group"})
    state = SelectField('State or Union Teritorry', [validators.InputRequired()], coerce=str, choices=states)


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)], render_kw={"placeholder": "Unique username"})
    firstname = StringField('First Name', [validators.InputRequired()])
    lastname = StringField('Last Name')
    email = StringField('Email Address', [validators.Email()], render_kw={"placeholder": "Eg: email@example.etc"})
    phonenumber = StringField('Phone Number', [validators.InputRequired()], render_kw={"placeholder": "Indian mobile number"})
    date = DateField('Date Of Birth', [validators.InputRequired()], render_kw={"placeholder": "Format: YYYY-MM-DD"})
    #  age = IntegerField('Age', [validators.InputRequired()], render_kw={"placeholder":">16 to donate blood"})
    weight = IntegerField('Weight in kgs', [validators.InputRequired()], render_kw={"placeholder": "50<yourWeight<150"})
    bloodgroup = SelectField('Blood Group', [validators.InputRequired()], coerce=str, choices=bloodgroups_lis, render_kw={"placeholder": "Select blood group"})
    gender = SelectField('Gender', [validators.InputRequired()], coerce=str, choices=gender_lis)
    pdonations = IntegerField('Previous Donations', default=0)
    address = TextAreaField('Address', [validators.InputRequired()])
    # city = SelectField('City',[validators.Length(max=30),validators.InputRequired()])
    # state = StringField('State', [validators.Length(max=30),validators.InputRequired()], render_kw={"placeholder":"Please select presently statying State or Union Territory"})
    state = SelectField('State or Union Teritorry', [validators.InputRequired()], coerce=str, choices=states)
    password = PasswordField('Password', [validators.Length(min=7), validators.InputRequired(), validators.EqualTo('confirm', message="Passwords must match.")], render_kw={"placeholder": "Min-7, 1 Upper, 1 lower, 1 spec char"})
    confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Must be equal to previoius field"})
    accept_tos = BooleanField('I accept the <a href="/tos">Terms of Service</a> and <a href="/privacy/">Privacy Notice</a> (Last Updated Apr 6 2018)', [validators.InputRequired()], id='accept_tos',render_kw={"required":"", "onclick": "check_selected()"})


def get_name(uid):
    c,conn = connection()
    c.execute("select firstname, lastname from user where uid = '{0}'".format(uid))
    name = c.fetchone()
    name = name[0]+ ' ' + name[1]
    c.close()
    return name


# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(405)
def method_not_found(e):
    try:
        return render_template("405.html")
    except Exception as e:
        return render_template("500.html")


@app.errorhandler(500)
def internal_server():
    return render_template("500.html")


# @app.route('/<path:url_path>/')
# @app.route('/')
# def home_page(url_path='/'):
#     return render_template('main.html')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/contributions/')
def contributions():
    bd_dict = models.get_bd_dict()
    return render_template('about-us.html', bd_dict=bd_dict)


@app.route('/reg/')
def reg():
    return render_template('registeration_form.html')


@app.route('/faq/')
def faq():
    return render_template("faq.html")


@app.route('/precautions/')
def precautions():
    return render_template("precautions.html")


@app.route('/temp/')
@logout_required
def heck():
    print(request.path)
    return request.path


@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = RequestForm(request.form)
    exit_status, data_list, city, state, blood_group, notifications, names = models.make_dashboard(form, request, flash, session)
    if exit_status is 0:
        return render_template("find_donors.html", user_list=data_list, city=city, state=state, blood_group=blood_group)
    elif exit_status is 1:
        return render_template("dashboard.html", USER_DICT=USER_DICT, cities_dict=cities_dict, states=states,
                               bloodgroups_lis=bloodgroups_lis, form=form, noti_names=zip(notifications, names))



@app.route('/make_a_request/', methods=['GET', 'POST'])
def make_request():
    models.make_blood_request(request, flash, session)
    return redirect(url_for('dashboard'))


@app.route('/return-file/')
def return_file():
    return send_file('/home/sriteja/PycharmProjects/Blood Bank/logo.png', attachment_filename='logo.png')


@app.route('/filedown/')
def file_downloads():
    return render_template('downloads.html')


@app.route('/slashboard/')
def slashboard():
    try: pass
    # return render_template("dashboard.html", USER_DICT=HFS)
    except Exception as e:
        return render_template("500.html", error=e)


@app.route('/verify', methods=['GET'])
@app.route('/verify/<path:urlpath>', methods=['GET'])
def verify_email(urlpath=0):
    try:
        temp = models.check_verify_link(urlpath)

        if temp == "verification_success.html":
            return render_template("verification_success.html")
        else:
            return "temp"
    except Exception as e:
        return str(e)


@app.route('/sendmail/')
def send_mail():
    try:
        send_verification_mail('teja', 'sriteja.sugoor@students.iiit.ac.in', "https://www.google.com")
        # msg = Message("Success",
        #               sender=("Blood Bank", "sriteja.sugoor@students.iiit.ac.in"),
        #               recipients=['sritejakittu777@gmail.com', 'sriteja.sugoor@students.iiit.ac.in'])
        # msg.html = render_template("Welcome to Republic.html", username = "teja", link = "google.com")
        # mail.send(msg)
        return render_template('Welcome to Blood Bank.html', username='teja', link='https://www.google.com')
    except Exception as e:
        return str(e)


def gen_verify_link(username, email):
    link = '127.0.0.1:5000/verify/' + sha256_crypt.encrypt(str(username)) + sha256_crypt.encrypt(str(email))
    return link


def send_verification_mail(username, email, link):
    try:
        msg = Message("Account verification",
                      sender=("Blood Bank", "sriteja.sugoor@students.iiit.ac.in"),
                      recipients=[email, 'sritejakittu777@gmail.com'])
        msg.body = "Hello " + username +\
                   ",\n   Thanks for registering as a blood donor. To avoid spam," \
                   "please verify your email account by clicking on this link" + link

        msg.html = render_template("Welcome to Blood Bank.html", username=username, link=link)
        mail.send(msg)
        return 'Mail sent'
    except Exception as e:
        return str(e)


def send_mail_change(username, email, link):
    try:
        print("came_here")
        msg = Message("Email Changed",
                      sender=("Blood Bank", "sriteja.sugoor@students.iiit.ac.in"),
                      recipients=['sritejakittu777@gmail.com', email])
        msg.body = "Hello" + username +\
                   ",\n    As you updated your email id, you need to your email," \
                   "please verify it by clicking on this link" + link
        msg.html = render_template("email_changed.html", username=username, link=link)
        mail.send(msg)
        return 'Mail sent'
    except Exception as e:
        return str(e)


@app.route('/sve/')
def sev():
    try:
        send_verification_mail('teja', 'sritejakittu777@gmail.com',
                               gen_verify_link('teja', 'sritejakittu777@gmail.com'))
        return "mail_sent"
    except Exception as e:
        return str(e)


@app.route('/include/')
def include_example():
    try:
        replies = {'sri': 'cool',
                   'teja': 'good',
                   'chinni': 'nice',
                   'charan': 'super'}
        return render_template('include.html', replies=replies)
    except Exception as e:
        return str(e)


def special_requirement(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            if 'sriteja' == session['username']:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('dashboard'))
        except Exception as e:
            return redirect(url_for('dashboard'))
    return wrap


@app.route('/secret/<path:filename>')
@special_requirement
def protected(filename):
    try:
        return send_from_directory(os.path.join(app.instance_path, ''), filename)
    except Exception as e:
        return redirect(url_for('dashboard'))


@app.route('/interactive/')
def interactive():
    try:
        return render_template("interactive.html")
    except Exception as e:
        return str(e)


@app.route('/jinjaman/')
def jinja_tem():
    try:
        gc.collect()
        data = [15, '15', 'Python is gd', 'python, java, c, c++', '<p><strong>hello</strong></p>']
        return render_template("jinja_tem.html", data=data)
    except Exception as e:
        return str(e)


@app.route('/converters/')
@app.route('/converters/<path:page>')
@app.route('/converters/<page>')
def convert_url(page=1):
    try:
        gc.collect()
        return render_template("convert_url.html", page=page)
    except Exception as e:
        return str(e)


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash("You have been logged out")
    gc.collect()
    return redirect(url_for('index'))


@app.route('/update/', methods=['GET', 'POST'])
@login_required
def update_details():
    exit_status, error, form, min_date, max_date, data_dict = models.update_user_details(request, session, flash, send_mail_change)
    return render_template('update.html', cities_dict=cities_dict, states=states, form=form, min_date=min_date, max_date=max_date, data_dict=data_dict, error=error)


@app.route('/login/', methods=['GET', 'POST'])
@logout_required
def login_page():
    error = ''
    try:
        exit_status, error = models.check_login(request, session, flash)
        print(exit_status, error)
        if not exit_status:
            return redirect(url_for('dashboard'))
        gc.collect()
        return render_template("login.html",  error=error)
    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


@app.route('/state/')
def state_select():
    return render_template('cs.html', states=state_list(), cities_dict=cities_list())


@app.route('/check/')
def check():
    return render_template('temp2.html')


@app.route('/register/', methods=["GET", "POST"])
@logout_required
def register_page():
    exit_status, form, max_date, min_date = models.registration(request, RegistrationForm, flash, session, send_verification_mail)
    if not exit_status:
        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form, max_date=max_date, min_date=min_date, cities_dict=cities_dict)


if __name__ == '__main__':
    app.run(debug=True)
