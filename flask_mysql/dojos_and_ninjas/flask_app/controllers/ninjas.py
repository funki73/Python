from flask import Flask, render_template, request, redirect

from flask_app import app

from flask_app.models.ninja import Ninja

from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html", dojos = Dojo.get_all_dojos())

@app.route('/ninja/add', methods=["POST"])
def add_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/')
