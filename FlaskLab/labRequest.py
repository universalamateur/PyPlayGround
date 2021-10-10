from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/index')
def index():
    # Returns the index page
    return 'index'

@app.route('/login')
def login():
    # Returns the Login Page
    return 'login'

@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'user {escape(username)}'
    #return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('show_user_profile', username='John Doe', query='Search query parameter'))

#if __name__ == '__main__':
#    app.run(debug=True)
