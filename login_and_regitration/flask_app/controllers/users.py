from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user

@app.route('/')
def home():
    return render_template('new_users.html')

@app.route('/users/register', methods=['POST'])
def register_user():
    if user.User.create_user(request.form):
        return redirect('/users/profile')
    return redirect('/')

@app.route('/users/profile')
def profile():
    return render_template('profile.html')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/users/login', methods = ['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/users/profile')
    return redirect('/')