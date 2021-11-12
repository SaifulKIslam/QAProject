from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Books, Review 

class BooksCheck:
    def __init__(self,message):
        self.message = message

    def __call__(self, form, field):
        all_books = Books.query.all()
        for books in all_nooks:
            if books.name == field.data:
                raise ValidationError(self.message)

class BooksForm(FlaskForm):
    name = StringField('Books name', 
        validators=[
            DataRequired(),
            BooksCheck(message='This book is available on teh Homepgae to add a review.')])
    submit = SubmitField('Add Books')

class ReviewForm(FlaskForm):
    desc = StringField('Review',
        validators=[
            DataRequired()])
    rating = SelectField('Ratings',
        choices=[
            ('5', '5/5'),('4','4/5'),('3','3/5'),('2','2/5'),('1','1/5'), ('0','0/5')])
    submit = SubmitField('Add Review')
