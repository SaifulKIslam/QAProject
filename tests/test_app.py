import unittest 
from flask import url_for
from flask_testing import TestCase
from application.models import Review, Books 
from application import app, db 


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
			SECRET_KEY='TEST_SECRET_KEY',
			DEBUG=True
			)
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        #Create Test registree
        books = Books(name='Fantastic Mr Fox')
        review = Review(desc='a great adventure and great read')
        
        #Save Books & Review to the database
        db.session.add(books)
        db.session.add(review)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', idNum=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('index', idNum=1))
        self.assertEqual(response.status_code, 200)

    def test_addReview_get(self):
        response = self.client.get(url_for('addReview', idNum=1))
        self.assertEqual(response.status_code, 200)

    def test_Reviewpage_get(self):
        response = self.client.get(url_for('Reviewpage', idNum=1))
        self.assertEqual(response.status_code, 200)

#Test Adding a books name
class TestAdd(TestBase):
    def test_add_books(self):
        response = self.client.post(
		url_for('add', idNum=1),
		data = dict(name='Fantastic Mr Fox')
	)
        self.assertIn(b'Fantastic Mr Fox', response.data)

#Test Updating a books name
class TestUpdate(TestBase):
    def test_update_books(self):
        response = self.client.post(
		url_for('update', idNum=1),
                data = dict(oldname='Fantastic Mr Fox', newname='Harry Potter'),
		follow_redirects=True
        	)
        self.assertEqual(response.status_code, 200)

#Test Deleting a books
class TestDelete(TestBase):
    def test_delete_books(self):
        response = self.client.post(
		url_for('index', idNum=1),
		data = dict(name='Fantastic Mr Fox'),
		follow_redirects=True
		)
        self.assertEqual(response.status_code,200)

#Test Adding a review
class TestAddreview(TestBase):
    def test_add_review(self):
        response = self.client.post(
		url_for('addReview', idNum=1),
		data = dict(desc='Great read')
		)
        self.assertIn(b'Great read', response.data)

#Test Reviewpage
class TestReviewpage(TestBase):
    def test_reviewpage(self):
        response = self.client.post(
                url_for('Reviewpage', idNum=1),
                data = dict(name='Fantastic Mr Fox'),
                follow_redirects=True
                )
        self.assertEqual(response.status_code,200)