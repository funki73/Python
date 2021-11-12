
from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User
from flask_app.models.tv_show import Tv_shows

from types import MethodDescriptorType
import re
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "uuid" in session:
        return redirect("dashboard")

    return render_template("index.html")



@app.route("/register", methods = ["POST"])
def register():
    if not User.register_validator(request.form):
        return redirect("/")

    hash_browns = bcrypt.generate_password_hash(request.form['password'])
    data ={
        **request.form,
        "password": hash_browns
    }

    user_id = User.create(data)

    session["uuid"] = user_id

    return redirect("/dashboard")


@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect ("/")

    user = User.get_by_email({"email": request.form["email"]})

    session["uuid"] = user.id

    return redirect ("/dashboard")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")

