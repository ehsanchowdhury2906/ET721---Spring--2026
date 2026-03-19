"""
ehsan chowdhury
lab14, mini blog app using flask
march 19, 2026
"""
from flask import flask, render template, redirect, url_for, request
from flask_sqlalchemy import SQLalchemy

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')



if _name_ == '__main'