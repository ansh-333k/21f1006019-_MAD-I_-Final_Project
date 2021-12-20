from main import app, db
from applications.models import *
from flask import render_template
from flask import redirect
from flask import session
from flask import request
from flask import flash
from random import sample
from random import shuffle

tables = ['users']

@app.route("/")
def index():
	session.pop('username', None)
	return render_template('index.html')

@app.route("/admin_login", methods = ["GET", "POST"])
def admin_login():
	if request.method == 'GET':
		return render_template('admin_login.html')
	elif request.method == 'POST':
		if request.form['admin_pass'] == 'P@ssw0rd':
			session['username'] = 'Admin'
			return redirect('/admin_dashboard')
		else:
			flash('Password Incorrect !!! Try Again ...')
			return redirect('/admin_login')

@app.route("/user_login", methods = ["GET", "POST"])
def user_login():
	if request.method == 'GET':
		return render_template('user_login.html')
	elif request.method == 'POST':
		d = dict()
		for u in users.query.all():
			d[u.username] = u.password
		if request.form['username'] in d.keys():
			if d[request.form['username']] == request.form['password']:
				session['username'] = request.form['username']
				return redirect(f"/{request.form['username']}/dashboard")
			else:
				flash('Password Incorrect !!! Try Again ...')
				return redirect('/user_login')
		else:
			user = users(username = request.form['username'], password = request.form['password'])
			db.session.add(user)
			db.session.commit()
			session['username'] = request.form['username']
			return redirect(f"/{request.form['username']}/dashboard")

@app.route("/logout")
def logout():
	return redirect('/')

@app.route("/admin_dashboard")
def admin_dashboard():
	return render_template('admin_dashboard.html')

@app.route("/<user>/dashboard")
def user_dashboard(user):
	user = users.query.filter(users.username == user).one()
	return render_template('user_dashboard.html', user = user)

@app.route("/users")
def user():
	if session['username'] != 'Admin':
		return render_template('error.html')
	else:
		user = users.query.all()
		return render_template('users.html', users = user)

@app.route("/decks")
def deck():
	if session['username'] != 'Admin':
		return render_template('error.html')
	else:
		return render_template('decks.html')

@app.route("/decks/<level>")
def decks_level(level):
	if session['username'] != 'Admin':
		return render_template('error.html')
	else:
		if level == 'easy':
			deck = easy.query.all()
		elif level == 'medium':
			deck = medium.query.all()
		elif level == 'hard':
			deck = hard.query.all()
		return render_template('decks_level.html', decks = deck, level = level)

@app.route("/<user>/play")
def play(user):
	user = users.query.filter(users.username == user).one()
	return render_template('play.html', user = user)

@app.route("/<user>/play/<level>", methods = ["GET", "POST"])
def play_level(user, level):
	if level == 'easy':
		deck = easy.query.all()
	elif level == 'medium':
		deck = medium.query.all()
	elif level == 'hard':
		deck = hard.query.all()
	quiz = list()
	questions = sample(deck, 10)
	options = list(set(deck).difference(set(questions)))
	for question in questions:
		temp = list()
		temp.append(question.synonyms)
		option = sample(options, 3)
		for i in option:
			temp.append(i.synonyms)
		shuffle(temp)
		temp.insert(0, question.word)
		quiz.append(temp)
	user = users.query.filter(users.username == user).one()
	if request.method == 'GET':
		return render_template('play_level.html', quiz = quiz, user = user, level = level)
	elif request.method == 'POST':
		for k, v in request.form.items():
			if level == 'easy':
				que = easy.query.filter(easy.word == k).one()
			elif level == 'medium':
				que = medium.query.filter(medium.word == k).one()
			elif level == 'hard':
				que = hard.query.filter(hard.word == k).one()
			if que.synonyms == v:
				user.score += 1
			db.session.commit()
		return redirect(f"/{user.username}/dashboard")