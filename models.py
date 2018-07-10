from connection import *
from content_management import *
from passlib.hash import sha256_crypt
from pymysql import escape_string as thwart
from get18_back import *
from wtforms import Form, BooleanField, PasswordField, validators, StringField, TextAreaField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.fields import SelectField, IntegerField


USER_DICT = content()
bloodgroups_lis = bloodgroups()
states = state_list()
gender_lis = gender_list()
cities_dict = cities_list()


def gen_verify_link(username, email):
    link = '127.0.0.1:5000/verify/' + sha256_crypt.encrypt(str(username)) + sha256_crypt.encrypt(str(email))
    return link


def get_name(uid):
    c, conn = connection()
    c.execute("select firstname, lastname from user where uid = '{0}'".format(uid))
    name = c.fetchone()
    name = name[0]+ ' ' + name[1]
    c.close()
    return name

def get_bd_dict():
    c, conn = connection()
    bd_lis = short_bd_list()
    bd_dict = {}
    for i in bd_lis:
        c.execute("select count(*) from userdetails where BloodGroup='{0}'".format(i))
        bd_dict[i] = c.fetchone()[0]
    print(bd_dict)
    c.close()
    return bd_dict


def check_verify_link(urlpath):
    if urlpath:
        c, conn = connection()
        print('127.0.0.1:5000/verify/' + urlpath)
        x = c.execute("UPDATE  user SET emailconfirm = TRUE WHERE email_verification_link=(%s) AND emailconfirm=0",
                  ('127.0.0.1:5000/verify/' + urlpath))
        if x:
            conn.commit()
            return "verification_success.html"
        else:
            return "<div align='middle'>Your verification link is invalid, please check your link and try again</div>"
    else:
        return "Please specify the verification link."


def check_login(request, session, flash):
    error = ''
    c, conn = connection()
    print(1)
    if request.method == "POST":
        x = c.execute("SELECT * FROM user WHERE username = (%s)", thwart(request.form['username']))
        if int(x) == 0:
            error = "Invalid credentials, try again."
            c.close()
            return 1, error
        data_password = c.fetchone()[6]

        if sha256_crypt.verify(request.form['password'], data_password):
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash("Welcome " + session['username'])
            c.close()
            return 0, ''
        else:
            error = "Invalid  credentials, try again."
            c.close()
            return 2, error
    else:
        return 3, error


def registration(request, RegistrationForm, flash, session, send_verification_mail):
    c, conn = connection()
    min_date, max_date = get18_back()

    form = RegistrationForm(request.form)

    print("yesno")

    if request.method == "POST" and form.validate():
        print("yesoo")
        username = thwart(form.username.data)
        firstname = thwart(form.firstname.data)
        lastname = thwart(form.lastname.data)
        phonenumber = thwart(form.phonenumber.data)
        email = thwart(form.email.data)
        address = thwart(form.address.data)
        # city = thwart(form.city.data)
        state = form.state.data
        # country = thwart(form.country.data)
        gender = thwart(form.gender.data)
        date = str(form.date.data)
        age = send_to_find_age(date)
        weight = int(form.weight.data)
        bloodgroup = form.bloodgroup.data
        pdonations = int(form.pdonations.data)
        password = sha256_crypt.encrypt(str(form.password.data))
        city = thwart(request.form['city'])
        x = c.execute("SELECT * FROM user WHERE username = ('{0}')".format(thwart(username)))
        print("yesit")
        if int(x) > 0:
            flash("That username is already taken, please choose another")
            return 1, form, max_date, min_date
            # return render_template('register.html', form=form, cities_dict=cities_dict, min_date=min_date, max_date=max_date)
        else:
            link = gen_verify_link(username, email)
            c.execute(
                "INSERT INTO address(Address, City, State ) VALUES ('{0}','{1}','{2}')".format(address, city, state))
            c.execute("SELECT @last1 := LAST_INSERT_ID()")
            c.execute(
                "INSERT INTO userdetails(DateofBirth, Age, weight, gender, BloodGroup, previousdonations) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
                    date, age, weight, gender, bloodgroup, pdonations))
            c.execute("SELECT @last2 := LAST_INSERT_ID()")
            c.execute(
                "INSERT INTO user (username, firstname, lastname, userpassword, phonenumber, emailid, email_verification_link, user_address,user_details) VALUES ( %s, %s, %s, %s, %s, %s, %s,  @last1,@last2)",
                (
                    username, firstname, lastname, password, phonenumber, email, link))
            conn.commit()
            # c.execute("INSERT INTO user (username,userpassword, emailid, email_verification_link) VALUES (%s, %s, %s, %s)", (thwart(username), thwart(password), thwart(email), link))
            # conn.commit()
            # c.execute("SELECT @last:=LAST_INSERT_ID")
            send_verification_mail(thwart(username), thwart(email), link)

            flash("Thanks for registering, please verify your email id from the mail sent to your mail id!")

            c.close()
            conn.close()
            session['logged_in'] = True
            session['username'] = username
            return 0, form, max_date, min_date
    return 1, form, max_date, min_date


def update_user_details(request, session, flash, send_mail_change):
    error = ''
    c, conn = dict_connection()
    min_date, max_date = get18_back()
    c.execute(
        "select * from ((user inner join userdetails on userdetails.userdetilsid = user.user_details)"
        "inner join address on address.Addressid=user.user_address) where username = '{0}'".format(
            thwart(session['username'])))
    data_dict = c.fetchone()

    print(data_dict)

    class UpdateForm(Form):
        username = StringField('Username', render_kw={"readonly": ""})
        firstname = StringField('First Name', render_kw={"readonly": ""})
        lastname = StringField('Last Name', render_kw={"readonly": ""})
        email = StringField('Update Email Address', [validators.Email()])
        phonenumber = StringField('Update Phone Number', [validators.InputRequired()])
        date = DateField('Date Of Birth', [validators.InputRequired()], render_kw={"readonly": ""})
        weight = IntegerField('Weight in kgs', [validators.InputRequired()],
                              render_kw={"placeholder": "50<yourWeight<150"})
        bloodgroup = StringField('Blood Group', render_kw={"readonly": ""})
        gender = StringField('Gender', render_kw={"readonly": ""})
        pdonations = IntegerField('Previous Donations', default=data_dict['previousdonations'])
        address = TextAreaField('Address', [validators.InputRequired()])
        state = SelectField('State or Union Teritorry', [validators.InputRequired()], coerce=str,
                            choices=states, default=data_dict['State'])
        present_password = PasswordField('Present Password', [validators.InputRequired()])
        new_password = PasswordField('Update Password',
                                     [validators.EqualTo('confirm', message="Passwords must match.")],
                                     render_kw={"placeholder": "Min-7, 1 Upper, 1 lower, 1 spec char"})
        confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Must be equal to previoius field"})

    form = UpdateForm(request.form)

    if request.method == "POST" and form.validate():
        print("yesoo")
        phonenumber = thwart(form.phonenumber.data)
        email = thwart(form.email.data)
        address = thwart(form.address.data)
        state = form.state.data

        weight = int(form.weight.data)
        pdonations = int(form.pdonations.data)
        city = thwart(request.form['city'])
        c.execute("SELECT userpassword FROM user WHERE username = ('{0}')".format(data_dict['username']))
        data = c.fetchone()
        print(data['userpassword'])

        if sha256_crypt.verify(form.present_password.data, data['userpassword']):
            print("yes it")
            if form.new_password.data:
                password = sha256_crypt.encrypt(str(form.new_password.data))
                c.execute(
                    "UPDATE user SET userpassword = '{0}' WHERE username = '{1}'".format(password,
                                                                                         data_dict['username']))

            if email == data_dict['emailid']:
                pass
            else:
                print('camed ')
                link = gen_verify_link(session['username'], email)
                send_mail_change(session['username'], email, link)
                flash("Please verify your changed mail id by the verification link  sent to your new mail id")
                c.execute(
                    "UPDATE user SET email_verification_link = '{0}', emailid = '{1}', emailconfirm = 0 WHERE username = '{2}'".format(
                        link, email, data_dict['username']))

            c.execute(
                "UPDATE user SET phonenumber = '{0}' WHERE username = '{1}'".format(phonenumber, data_dict['username']))
            c.execute(
                "UPDATE address SET city='{0}', state='{1}', address='{2}' WHERE Addressid = '{3}'".format(city, state,
                                                                                                           address,
                                                                                                           data_dict[
                                                                                                               'Addressid']))
            c.execute(
                "UPDATE userdetails SET previousdonations = '{0}', weight = '{1}' WHERE userdetilsid='{2}'".format(
                    pdonations, weight, data_dict['userdetilsid']))

            flash("Details Updated Successfully")
            conn.commit()
            c.close()
            conn.close()
            return 0, '', form, min_date, max_date, data_dict
        else:
            error = 'Wrong password, please try again.'
    return 1, error, form, min_date, max_date, data_dict


def make_blood_request(request, flash, session):
    notification = thwart(request.form.get('notification', None))
    user_list = request.form.get('user_list', None)
    subject = thwart(request.form.get('Subject', None))
    print(notification)
    print(user_list)
    strs = user_list.replace('(', '').replace(')', '')
    list = strs.split(',')
    print(strs)
    print(list)

    print(list[5::6])
    c, conn = connection()
    # for i in list[5::6]:
    #     c.execute("INSERT INTO Notifications_data (notification, user_id) values ('''{0}''', '{1}')".format(notification,int(i)))
    # conn.commit()
    c.execute("select uid from user where username='{0}'".format(thwart(session['username'])))
    user_id = c.fetchone()
    c.execute(
        "INSERT INTO Notification_data (notification, created_by, subject) VALUES ('''{0}''', '{1}', '''{2}''')".format(
            notification, user_id[0], subject))
    c.execute("SELECT @last := LAST_INSERT_ID()")
    for i in list[5::6]:
        c.execute("INSERT INTO Notification_users (notification_id, to_user) VALUES (@last,'{0}')".format(int(i)))
    conn.commit()
    c.close()
    flash('Your request has been successsfully sent, wait until the respective user confirms')
    return 0


def make_dashboard(form, request, flash, session):
    try:
        try:
            if 'logged_in' not in session:
                flash("Welcome Guest!")
            print("niced")

            if request.method == 'POST' and form.validate():
                blood_receive_dict = who_can_donate()
                print("veryniced")
                c, conn = connection()
                blood_group = form.bloodgroup.data
                city = request.form['city']
                state = form.state.data
                data_user_list = []
                c.execute("select firstname, lastname, phonenumber, emailid, Address, uid from (select user.username, user.firstname, user.lastname, user.phonenumber, user.emailid, user.uid, address.city, address.state, address.Address, userdetails.BloodGroup from ((user inner join address on user.user_address = address.Addressid) inner join userdetails on user.user_details = userdetails.userdetilsid)) as t where Bloodgroup = '{0}' and state = '{1}' and city = '{2}' and username != '{3}' ".format(blood_group, state, city, thwart(session['username'])))
                data_user_list = c.fetchall()
                print(data_user_list)
                print(blood_receive_dict)
                data_list = ()
                for i in blood_receive_dict[blood_group]:
                    c.execute(
                        "select firstname, lastname, phonenumber, emailid, Address, uid  from (select user.username, user.firstname, user.lastname, user.phonenumber, user.emailid, user.uid, address.city, address.state, address.Address, userdetails.BloodGroup from ((user inner join address on user.user_address = address.Addressid) inner join userdetails on user.user_details = userdetails.userdetilsid)) as t where Bloodgroup = '{0}' and state = '{1}' and city = '{2}' and username != '{3}' ".format(
                            i, state, city, thwart(session['username'])))
                    temp_list = c.fetchall()
                    for j in temp_list:
                        data_list = data_list + (j,)
                print(data_list)
                c.close()
                print("veryveryniced")
                # return render_template("find_donors.html", user_list=data_list, city=city, state=state, blood_group=blood_group)
                return 0, data_list, city, state, blood_group, '', ''
            c, conn = connection()
            print("good")
            c.execute("select uid from user where username = '{0}'".format(thwart(session['username'])))
            user_id = c.fetchone()
            c.close()
            print("ggood")
            c,conn=dict_connection()
            # c.execute("select Notification_data.notification from Notifications_data inner join Notiwhere user_id = '{0}'".format(user_id[0]))
            c.execute("select notification, created_by, subject from Notification_data inner join Notification_users on  id= Notification_users.notification_id where to_user='{0}'".format(user_id[0]))

            notifications = c.fetchall()
            names = []
            for i in notifications:
                names.append(get_name(i['created_by']))
            c.close()
            print(names)
            print(notifications)

            print("notnice")
        except Exception as e:
            flash(e)
        return 1, '', '', '', '', notifications, names
    except Exception as e:
        return 2, '', '', '', '', '', ''
