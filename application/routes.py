# homepage - all books
    # -> view reviews
    # -> add book
        # input book name
            # if book name exists return them to index
            # if book name does not exits them submit
        # -> edit book
            # get book if exists from index
            # return update page
        # -> delte a review
from flask import render_template, redirect, url_for, request

@app.route('/', methods = ['POST', 'GET'])
def index():
    all_books = Books.query.all()
    return render_template('index.html', all_books=all_books)

@app.route('/addBook', methods = ['GET', 'POST'])
def add():
    form = BooksForm()
    if form.validate_on_submit():
        new_books = Books(name=form.name.data)
        db.session.add(new_books)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addbook.html', form=form)

@app.route('/update/<int:ifNum>', methods=['GET', 'POST'])
def update(idNum):
    form = BooksForm()
    books_update = Books.query,get(idNum)
    if form.validate_on_submit():
        books_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('delete/<int:idNum>')
def delete(idNum):
    books_delete = Books.query.get(idNum)
    db.session.delete(books_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addReview/<int:idNum>', methods=['GET', 'POST'])
def addReview(idNum):
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(desc=form.desc.data,
            rating=form.rating.data,
            books_id=idNum)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('Reviewpage', idNum=idNum))
    return render_template('addReview.html', form=form, books = Books.query.get(idNum))

@app.route('/Reviewpage/<int:idNum>', methods=['GET','POST'])
def Reviewpage(idNum):
    review_page = Review.query.filter_by(books_id=idNum).all()
    return render_template('Reviewpage.html', review_page=review_page)
