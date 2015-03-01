from app import app
from flask import request, render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Oakland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was awesome!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/spec', methods=['GET', 'POST'])
def spec_get():
    return "{'event': 'Landing', 'properties': ['Version]}"

@app.route('/set', methods=['POST'])
def spec_set():
    return "THANKS!"
