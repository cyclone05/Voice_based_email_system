
from flask import Flask
from flask_sqlalchemy import SQLAlchemy





app=Flask("dbproject")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'


db=SQLAlchemy(app)

class myclass(db.Model):
    userid = db.Column(db.Text, primary_key = True)
    password = db.Column(db.Text)

    def __init__(self,userid,password):
        self.userid = userid
        self.password = password

"""
userid="deepak"
userpass="Khette"

db.create_all()

userinfo=myclass(userid,userpass)
db.session.add(userinfo)
db.session.commit()

"""

userid="poonam"
userpass="bankar"
uname=myclass.query.filter_by(userid=userid).first()
if uname:
	print("user is valid")
"""
else:
	userinfo=myclass(userid,userpass)
	db.session.add(userinfo)
	db.session.commit()
"""