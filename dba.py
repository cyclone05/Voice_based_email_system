import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




engine=pyttsx3.init()
engine.setProperty('rate',130)

r = sr.Recognizer()

with sr.Microphone() as source:
    
    pyttsx3.speak("speak your voice ID")
    print("\nSpeak your voice ID:")

    iD_audio = r.listen(source)
    pyttsx3.speak("we got your voice ID")
    print("\nwe got your voice ID")


print("\n\n--------------------------------------------------------------------------------------------")

global ID

ID = r.recognize_google(iD_audio)
pyttsx3.speak("you said {}".format(ID))
print("\n you said",ID)


pyttsx3.speak("To use function of this program enter valid voice password")
print("\n\n-----------------------To use function of this program enter  voice password--------------")


print("\n\n-------------------------------------------------------------------------------------------")
r=sr.Recognizer()

with sr.Microphone() as source:
    
    pyttsx3.speak("speak your voice password")
    print("\nSpeak your voice password:")

    pass_audio=r.listen(source)
    pyttsx3.speak("we got your voice password")
    print("\nwe got your voice password")


print("\n\n--------------------------------------------------------------------------------------------")

global q

q=r.recognize_google(pass_audio)
pyttsx3.speak("you said {}".format(q))
print("\n you said",q)



app=Flask("dbproject")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'


db=SQLAlchemy(app)

class myclass(db.Model):
    userid = db.Column(db.Text, primary_key = True)
    password = db.Column(db.Text)

    def __init__(self,userid,password):
        self.userid = userid
        self.password = password


userid=ID
userpass=q

db.create_all()



userinfo=myclass(userid,userpass)
db.session.add(userinfo)
db.session.commit()

"""
readinfo = myclass.query.all()
readuser=readinfo[0].userid
readpass=readinfo[0].password
print(readuser)
print(readpass)
"""

User=myclass.query.filter_by(userid=userid).first()

print(User)
