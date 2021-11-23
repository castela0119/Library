from sqlalchemy.orm import defaultload
from app import db
from datetime import *

'''
model.py
이 파일은 데이터베이스의 제약 조건을 명시하는 파일입니다.
관계형 데이터베이스의 데이터를 객체랑 연결 시켜주는 것을 ORM (Object Relational Mapping) 이라고 불러요.
즉, 이 파일은 외부에 존재하는 DB를 서버에서 사용하기 위해, DB와 동일한 제약조건을 객체에 걸어버리는 겁니다.
'''

class lib_books(db.Model):

    __tablename__ = 'lib_books'

    book_id             = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True,)
    book_name           = db.Column(db.String(30), nullable=False)
    publisher           = db.Column(db.String(50),)
    author              = db.Column(db.String(30),)
    publication_date    = db.Column(db.Integer,)
    pages               = db.Column(db.Integer,)
    isbn                = db.Column(db.Integer, nullable=False)
    description         = db.Column(db.String(255),)
    img_path            = db.Column(db.String(255),)
    book_counts         = db.Column(db.Integer,)
    book_stars          = db.Column(db.Integer,)
    book_reviews        = db.Column(db.String(255),)

class lib_status(db.Model):

    __tablename__ = 'lib_status'

    status_no           = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True,)
    img_path            = db.Column(db.String(255), db.ForeignKey('lib_books.img_path'))
    book_id             = db.Column(db.Integer, db.ForeignKey('lib_books.book_id'), nullable=False,)
    user_email          = db.Column(db.String(40), db.ForeignKey('lib_users.user_email'), nullable=False,)
    book_name           = db.Column(db.String(30), db.ForeignKey('lib_books.book_name'), nullable=False,)
    avg              = db.Column(db.Float, nullable=False)
    book_start          = db.Column(db.Date, default = date.today)
    book_end            = db.Column(db.Date, default = date.today() + timedelta(days=14))
    book_return         = db.Column(db.Date)

    def __init__(self, status_no, book_id, user_email, img_path, book_name, avg, book_start, book_end, book_return):
        self.status_no      = status_no
        self.book_id        = book_id
        self.user_email     = user_email
        self.img_path       = img_path
        self.book_name      = book_name
        self.avg            = avg
        self.book_start     = book_start
        self.book_end       = book_end
        self.book_return    = book_return

class lib_users(db.Model):

    __tablename__ = 'lib_users'

    user_no             = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True,)
    user_email          = db.Column(db.String(40), nullable=False)
    user_pw             = db.Column(db.Integer, nullable=False)
    user_name           = db.Column(db.String(40), nullable=False)

class lib_reviews(db.Model):

    __tablename__ = 'lib_reviews'

    review_id           = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True,)
    user_email          = db.Column(db.String(40), db.ForeignKey('lib_users.user_email'), nullable=False)
    book_id             = db.Column(db.Integer, db.ForeignKey('lib_books.book_id'), nullable=False)
    rating              = db.Column(db.Float, nullable=False)
    content             = db.Column(db.Text())