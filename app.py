#-*- coding:utf8 -*-
from flask import Flask, render_template, redirect, url_for
from ajax import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60

# import routes
app.register_blueprint(ajax)



@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html', page='home.html')

@app.route('/load')
def load():
	return render_template('index.html', page='load.html')

@app.route('/show')
def show():
	return render_template('index.html', page='show.html')


if __name__ == '__main__':
	app.run(port=5000)
