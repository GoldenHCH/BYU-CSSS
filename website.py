from flask import FLask, render_template, request
import flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_']

class person:
    def __init__(self, first_name, last_name, dob, major, location, company=None, email, wechat):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.major = major
        self.location = location
        self.company = company
        self.email = email
        self.wechat = wechat

    def update(self, first_name, last_name, dob, major, location, company=None, email, wechat)
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.major = major
        self.location = location
        self.company = company
        self.email = email
        self.wechat = wechat


    