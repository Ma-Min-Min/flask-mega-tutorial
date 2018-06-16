from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Min Min'}
    posts = [
            {
                'author': {'username': 'Min'},
                'body': 'Beautiful day in Myanmar'
            },
            {
                'author': {'username': 'Valentine'},
                'body': 'The Catspidy movie was so cool!'
            }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)

