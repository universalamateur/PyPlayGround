from app import app
from flask import render_template
import datetime

@app.route('/', methods=["GET"])
def homr():
    date_string = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    return f"<h1>First Try on API Design</h1><p>This site is a prototype API.</p><b>There has been a change {date_string}</b>"

@app.route('/template')
def template():
    return render_template('home.html')