from sqlalchemy import func
from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship('RecordModel', back_populates='user', lazy=True)


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    records = db.relationship("RecordModel", back_populates="category", lazy="dynamic")


class RecordModel(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    user = db.relationship('UserModel', back_populates='record')
    category = db.relationship('CategoryModel', back_populates='record')

