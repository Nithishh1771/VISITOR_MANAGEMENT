from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import column,String

db=SQLAlchemy()


class Visitor_pass(db.Model):
    __tablename__ = "Visitor_pass"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    uname = db.Column(String(10))
    mobile = db.Column(String(10))
    gender= db.Column(String(20))
    pvisit = db.Column(String(50))
    Email_ID = db.Column(String(100))
    proof = db.Column(String(255))
    date=db.Column(String(30))
    time=db.Column(String(40))


    