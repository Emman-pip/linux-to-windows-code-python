from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=base)


class SampleEntity(db.Model):
    id = Column(Integer, primary_key=True)
    data = Column(String)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db.init_app(app)
