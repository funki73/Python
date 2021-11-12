import re
from flask import render_template, redirect, request, session
import flask

from flask_app import app

from flask_app.models.user import User

from flask_app.models.tv_show import Tv_shows


# Above was moved from user_controller.py file
@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect ("/")

    return render_template(
        "dashboard.html", 
        logged_in_user = User.get_by_id({"id": session['uuid']}),
        all_tv_shows = Tv_shows.get_all()
    )

@app.route("/tv_shows/add")
def new_tv_show():
    return render_template("new_tv_show.html")


@app.route("/tv_shows/<int:id>")
def display_tv_show(id):
    return render_template(
        "tv_show.html",
        logged_in_user = User.get_by_id({"id": session['uuid']}),
        tvshow = Tv_shows.get_one({"id": id})
    )

@app.route("/tv_shows/<int:id>/edit")
def update_tv_show(id):
    return render_template(
        "edit_tv_show.html",
        tvshow = Tv_shows.get_one({"id": id})
    )

@app.route("/tv_shows/<int:id>/edit", methods = ["POST"])
def edit_tv_show(id):
    if not Tv_shows.validate(request.form):
        return redirect(f"/tv_shows/{id}/edit")

    data ={
        **request.form,
        "id": id
    }

    Tv_shows.update(data)

    return redirect("/dashboard")


@app.route("/tv_shows/add", methods=["POST"])
def add_tv_show():
    if not Tv_shows.validate(request.form):
        return redirect("/tv_shows/add")

    data = {
        **request.form,
        "user_id": session["uuid"]
    }

    Tv_shows.create(data)

    return redirect("/dashboard")

@app.route("/tv_shows/<int:id>/delete")
def delete_tv_show(id):
    Tv_shows.delete({"id": id})

    return redirect("/dashboard")