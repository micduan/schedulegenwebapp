from flask import Flask, render_template, request, flash, url_for
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, current_user, login_user, login_required
from uwaterlooapi import UWaterlooAPI
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import json
import datetime
import getCourses
import settings
import forms
import models
import scrape
import permute
from Course import Course

app = Flask(__name__, template_folder='Templates')
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
login = LoginManager()
login.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)

@login.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/saved')
def showSavedSchedules():
    return render_template("saved.html")

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def editProfile():
    user = models.User.query.get(current_user.id)

    if request.method == 'POST':
        user.first = request.form['first']
        user.last = request.form['last']
        user.email = request.form['email']
        user.username = request.form['username']
        user.token = request.form['token']
        db.session.merge(user)
        db.session.commit()

    return render_template("profile.html", user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template("index.html")
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return render_template("login.html", title='Sign in', form=form)
        login_user(user, remember=form.remember_me.data)
        return render_template("index.html")
    return render_template("login.html", title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if current_user.is_authenticated:
        return render_template("index.html")
    if form.validate_on_submit():
        user = models.User(username=form.username.data, email=form.email.data, first=form.first.data, last=form.last.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_form = forms.LoginForm()
        login_user(user)
        return render_template("index.html", form=form)
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")

@app.route('/users', defaults={'user_id': None})
@app.route('/users/<user_id>', methods=['GET', 'POST'])
@login_required
def showUsers(user_id):
    
    if user_id:
        user = models.User.query.get(user_id)

        if request.method == 'POST':
            user.first = request.form['first']
            user.last = request.form['last']
            user.email = request.form['email']
            user.username = request.form['username']
            user.token = request.form['token']
            db.session.merge(user)
            db.session.commit()

        return render_template('user.html', user=user)
    else:
        current_user_id = current_user.get_id()
        user_is_valid = models.User.query.filter(models.User.roles.any(id=1)).filter_by(id=current_user_id).first()
        page = request.args.get('page', 1, type=int)
        users = models.User.query.order_by(models.User.id.asc()).paginate(page, 20, False)

        next_url = url_for('showUsers', page=users.next_num) \
            if users.has_next else None
        prev_url = url_for('showUsers', page=users.prev_num) \
            if users.has_prev else None
        
        return render_template('users.html', users=users.items, next_url=next_url, prev_url=prev_url)

@app.route('/profs', defaults={'prof_id': None})
@app.route('/profs/<prof_id>', methods=['GET', 'POST'])
@login_required
def showProfs(prof_id):

    if prof_id:
        prof = models.professors.query.filter_by(id=prof_id).first()

        if request.method == 'POST':
            prof.first = request.form['first']
            prof.last = request.form['last']
            prof.rating = float(request.form['rating'])
            prof.num_ratings = int(request.form['num_ratings'])
            db.session.merge(prof)
            db.session.commit()

        return render_template('prof.html', prof=prof)
    else:
        #user_id = current_user.get_id()
        #user_is_valid = models.User.query.filter(models.User.roles.any(id=1)).filter_by(id=user_id).first()
        page = request.args.get('page', 1, type=int)
        profs = models.professors.query.order_by(models.professors.id.asc()).paginate(page, 20, False)

        next_url = url_for('showProfs', page=profs.next_num) \
            if profs.has_next else None
        prev_url = url_for('showProfs', page=profs.prev_num) \
            if profs.has_prev else None
        
        return render_template('profs.html', profs=profs.items, next_url=next_url, prev_url=prev_url)

@app.route('/roles', defaults={'role_id': None})
@app.route('/roles/<role_id>', methods=['GET', 'POST'])
@login_required
def showRoles(role_id):

    if role_id:
        role = models.Roles.query.filter_by(id=role_id).first()

        if request.method == 'POST':
            role.name = request.form['name']
            role.description = request.form['description']
            db.session.merge(role)
            db.session.commit()

        return render_template('role.html', role=role)
    else:
        #user_id = current_user.get_id()
        #user_is_valid = models.User.query.filter(models.User.roles.any(id=1)).filter_by(id=user_id).first()
        page = request.args.get('page', 1, type=int)
        roles = models.Roles.query.order_by(models.Roles.id.asc()).paginate(page, 20, False)

        next_url = url_for('showRoles', page=roles.next_num) \
            if roles.has_next else None
        prev_url = url_for('showRoles', page=roles.prev_num) \
            if roles.has_prev else None
        
        return render_template('roles.html', roles=roles.items, next_url=next_url, prev_url=prev_url)

@app.route('/token', methods=['POST', 'GET'])
def token():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        if request.form['token'] != "":

            if current_user.is_authenticated:
                user_id = current_user.get_id()
                user = db.session.query(models.User).get(user_id)
                user.token = request.form['token']
                db.session.merge(user)
                db.session.commit()

            uw_api = UWaterlooAPI(api_key=request.form['token'])
            courses = getCourses.generateCourses(uw_api)

            if 'temperature_24hr_min_c' in uw_api.current_weather() and not len(courses) == 0:
                return render_template("select.html", token=request.form['token'], courses=courses)
            else:
                return render_template("error.html", errormsg = "Invalid API Token")
        else:
            return render_template("index.html")

@app.route('/scrape', methods=['POST', 'GET'])
def run_scrape():
    if request.method == 'POST':
        scrape.getRatings()
    return render_template("scrape.html")

@app.route('/schedule', methods=['POST', 'GET'])
def schedule():

    final_list_raw = permute.generateSchedules(request)

    if len(final_list_raw) > 1 and final_list_raw[0] == False:
        return render_template("error.html", errormsg = final_list_raw[1])

    final_list = []

    courses = [Course() for i in range(len(final_list_raw))]
    index = 0
    for course_index in courses:
        course_index.fill_dates(final_list_raw[index])
        final_list.append(course_index.convert_course_to_list())
        index += 1
        del course_index

    return render_template("schedule.html", schedule=final_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)