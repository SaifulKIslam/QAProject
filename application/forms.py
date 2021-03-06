from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Books, Review 

class BooksCheck:
    def __init__(self,message):
        self.message = message

    def __call__(self, form, field):
        all_books = Books.query.all()
        for books in all_books:
            if books.name == field.data:
                raise ValidationError(self.message)

class BooksForm(FlaskForm):
    name = StringField('Books name', 
		validators=[
			DataRequired(),
			BooksCheck(message='This book already exists')])
    submit = SubmitField('Add Books')

class ReviewForm(FlaskForm):
    desc = StringField('Review',
		validators=[
			DataRequired()])
    
    submit = SubmitField('Add Review')