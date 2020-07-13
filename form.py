from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, email_validator

class ContactForm(FlaskForm):
    charityName = StringField('Name', [DataRequired()])
    charityEmail = StringField('Email', [DataRequired(), Email()])
    category = StringField('Category', [DataRequired()])
    tagLine = StringField('Tagline', [DataRequired()])
    mission = TextAreaField('Mission', [DataRequired()])
    charityWebsite = StringField('Charity Website', [DataRequired()])