from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')