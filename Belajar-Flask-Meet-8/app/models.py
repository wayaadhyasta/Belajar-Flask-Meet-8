from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return '<User {}>' .format(self.name)
    
class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id), nullable=False)

    def __repr__(self):
        return '<Todo {}>' .format(self.todo)
    
class CategoryProduct(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    # Relationship
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return '<CategoryProduct {}>' .format(self.name)

class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    category_id = db.Column(db.BigInteger, db.ForeignKey(CategoryProduct.id), nullable=False)

    def __repr__(self):
        return '<Product {}>' .format(self.name)
