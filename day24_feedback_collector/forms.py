from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    feedback = TextAreaField("Feedback", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Submit Feedback")
