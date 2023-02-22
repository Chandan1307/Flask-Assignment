from flask import Flask

# Q1. What is Flask Framework? What are the advantages of Flask Framework?
'''
Flask is a micro web framework written in Python. It is designed to be simple, lightweight, and easy to use. 
Flask is often used for building small to medium-sized web applications and APIs.


Some of the advantages of using Flask are:
Lightweight: Flask is a minimalistic framework and does not require any external libraries or tools. This makes it easy to use and reduces the overhead of the application.

Easy to learn: Flask has a simple and easy-to-understand API that makes it easy for developers to get started with the framework.

Flexible: Flask is a flexible framework and can be easily extended to meet the needs of different projects.

Large community: Flask has a large community of developers and users who are constantly contributing to the framework and developing new features and plugins.

Python integration: Flask is written in Python and integrates well with other Python libraries and tools.

Good for small to medium-sized projects: Flask is ideal for small to medium-sized projects that do not require a lot of complexity and can be easily managed with a minimalistic framework.
'''

# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in jupyter Notebook.
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()


'''

# Q3. What is App routing in Flask? Why do we use app routes?

'''
App routing in Flask refers to the process of mapping URLs or routes to functions in a Flask application. When a user visits a specific URL, 
Flask routes the request to the appropriate function based on the URL pattern.

In Flask, app routing is done using the @app.route() decorator. 
This decorator is used to specify the URL pattern and the associated function that should be called when the pattern is matched.

In this example, we have defined two routes - '/' and '/about'. The @app.route() decorator is used to specify the URL patterns for these routes, and the associated functions index() and about() are called when the respective URLs are visited.

We use app routes in Flask to handle incoming requests and direct them to the appropriate function. 
App routing allows us to define multiple routes in a single Flask application, making it easy to create complex web applications with multiple pages and functions.

Additionally, app routes allow us to create dynamic web pages that respond to user input. 
For example, we could define a route that takes a user ID as a parameter and returns information about the user. This allows us to create personalized and dynamic web applications that are tailored to the needs of individual users.

'''
# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
# route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999

'''
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return 'Company Name: ABC Corporation<br>Location: India<br>Contact Detail: 999-999-9999'

if __name__ == '__main__':
    app.run()

'''
# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
'''
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

with app.test_request_context():
    print(url_for('hello')) # Outputs: /hello
    print(url_for('show_user_profile', username='chandan')) # Outputs: /user/John Doe
    print(url_for('show_post', post_id=123)) # Outputs: /post/123

'''