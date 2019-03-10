from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'RangDipkin'}
    posts = [
        {
            'author': {'username': 'Max'},
            'body': 'This blog is dumb.'
        },
        {
            'author': {'username': 'Rang'},
            'body': 'No you\'re dumb!'
        }
    ]
    return render_template('index.html', title='Flask Blog', user=user, posts=posts)
