import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    # Makes sure the columns are added to the end of the table
    created_at._creation_order = 9998
    updated_at._creation_order = 9999

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def deleteOne(cls, **kw):
        obj = cls.query.filter_by(**kw).first()
        if obj:
            db.session.delete(obj)
            db.session.commit()
    
    @classmethod
    def getOne(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def getAll(cls):
        return cls.query.all()

class User_Account(BaseMixin, db.Model):
    __tablename__ = "user_account"
    username = db.Column(db.String, nullable=False)
    test = db.Column(db.String, nullable=True)

    @staticmethod
    def createUser(username):
        result = User_Account(username=username)
        db.session.add(result)
        db.session.commit()
        return result

    @staticmethod
    def update(id, **kw):
        user = User_Account.query.filter_by(id=id).first()
        for key in kw:
            if key != "id":
                setattr(user, key, kw[key])
        db.session.commit()
    
    @staticmethod
    def delete(id, **kw):
        user = User_Account.query.filter_by(id=id).first()
        user.deleteOne()