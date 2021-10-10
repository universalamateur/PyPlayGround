from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    """ Returns the render Tenplate Home
    """
    return render_template("home.html")

@app.route("/about/")
def about_page():
    """ Returns an H1 HTML element
    """
    return "<h1>The About Page</h1>"

@app.route('/about/<string:username>')
def about_user(username):
    """ Returns from a dynamic route and escaped Html element
    """
    return f'user {escape(username)}'

if __name__ == '__main__':
    app.run(debug=True)
