from flask import render_template, request
from flask import redirect, url_for

def home():
    return render_template("home.html")

def index():
    return render_template("index.html")

def app():
    return render_template("app.html")