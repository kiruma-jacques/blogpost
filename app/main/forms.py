from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class NewBlogForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    content=TextAreaField('Post something', validators=[Required()])
    author=StringField('Your Name', validators=[Required()])
    submit =SubmitField('Submit')

class UpdateBlogForm(FlaskForm):
    title=StringField('Change your title', validators=[Required()])
    content=TextAreaField('Change your content', validators=[Required()])
    submit =SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Your Comment', validators=[Required()])
    user=StringField('Your Name', validators=[Required()])
    submit=SubmitField('Submit')
