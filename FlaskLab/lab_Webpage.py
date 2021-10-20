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

def create_sql_conection():
    return ""

def run_query(query):
    """ Returns the results from a SQL query
    """
    connection = create_sql_conection()
    result = connection.execute(query)
    return result

@app.route('/about/<string:username>')
def about_user(username):
    """ Returns the users profile from the database to the web front end
    """
    sql_query = f'SELECT * FROM profiles WHERE user_id = {username}'
    result = run_query(sql_query)
    return f'<p>{result}</p>'

if __name__ == '__main__':
    app.run(debug=True)
