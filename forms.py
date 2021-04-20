from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# WTForm
class InsertText(FlaskForm):
    text = TextAreaField("Insert text to convert to mp3", validators=[DataRequired()])
    save_as = StringField("Save as:", validators=[DataRequired()])
    submit = SubmitField("Convert to Mp3")
