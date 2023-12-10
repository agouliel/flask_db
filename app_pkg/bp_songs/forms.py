from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SongForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist')
    album = StringField('Album')
    composer = StringField('Composer')
    comment = StringField('Comment')
    submit = SubmitField('Add')