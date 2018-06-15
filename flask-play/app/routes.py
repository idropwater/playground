from app import app
from flask import render_template, request, redirect, session
from app.forms import LoginForm

@app.route('/')
def hello_world():
    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        form = LoginForm()
        if form.validate_on_submit():
            return 'success'

    return render_template('login.html')

@app.route('/logout')
def logout():
    return session['username']

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 400
