"""
Ehsan chowdhury
March 9, 2026
lab 11, intro to flask
"""
from flask import Flask, render_template

""" 
creating a object from the flask module 
"""

app = Flask(__name__)

#set the routng to the main page
# route ' decorator' is used to access a root url
@app.route('/')
def index():
    name = "ehsan chowdhury"
    fruits = ['apple', 'orange', 'grapes']
    fruit = 'orange'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit)

#endpoints refer to the name of the view in an app
@app.route('/about')
def about():
    images = ['birdinsky.jpg', 'nature.jpg', 'nicesky.jpg']
    
    return render_template('about.html', image_list=images)

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

#set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)