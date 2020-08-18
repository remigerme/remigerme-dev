from flask import render_template

from remigermedev import app

@app.route('/')
@app.route('/<name>')
@app.route('/<name>/')
def index(name='world'):
	return render_template('index.html', name=name)
