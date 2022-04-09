from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.sql import func

db = SQLAlchemy()


class BaseMixin(object):
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

class User_Account(BaseMixin, db.Model):
    __tablename__ = "user_account"
    id = db.Column(
        db.Integer,
        unique=True,
        nullable=False,
        primary_key=True,
    )
    username = db.Column(db.String, nullable=False)

    @staticmethod
    def update_username(username, userId):
        userIdMatches = User_Account.query.filter_by(user_id=userId).all()
        matchFound = False
        for each in userIdMatches:
            if each.username != username:
                db.session.delete(each)
            else:
                matchFound = True

        if not matchFound:
            User_Account.create(user_id=userId, username=username)

        db.session.commit()