from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app=Flask(_name_)


app.config['SQLALCHEMY_DATABASE_URI']=os.environ["DB_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)