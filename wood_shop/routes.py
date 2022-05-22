from flask import render_template, request
from wood_shop import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')  