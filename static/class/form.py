from flask_wtf import Form
from wtforms import TextField, TextAreaField, IntegerField, SubmitField, SelectField,RadioField
from wtforms import validators,ValidationError

class ContactForm(Form):
    name = TextField('Name of Student',[validators.Required("Please enter your name")])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    address = TextAreaField('Address')
    email = TextField('Email',[validators.Required('Please enter your email'), validators.Email("Email seems incorrect")])
    age = IntegerField('Age')
    language= SelectField('Languages',choices=[('cpp','C++'),('py','Python')])
    submit = SubmitField('Send')
