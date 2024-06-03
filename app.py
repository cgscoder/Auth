#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.authDB

users = db.users

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)