from datetime import datetime
from os import wait

from flask import Flask, redirect, render_template, request, url_for
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


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form.get("data")
        newEntry = SampleEntity(data=data)
        db.session.add(newEntry)
        db.session.commit()
        return redirect(url_for("home"))
    data = SampleEntity.query.all()
    return render_template("home.html", data=data)


@app.route("/timer")
def timer():
    time = datetime.now()
    print(time)
    return render_template("timer.html", time=time)
