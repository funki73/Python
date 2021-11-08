from flask import Flask, render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def dojohome():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)

    return redirect ('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('/dojo_show.html', dojo = Dojo.get_dojos_with_ninjas(data))

# @app.route("/dojos/<int:dojo_id>")
# def display_ninjas(dojo_id):
#     return render_template("dojo.html", dojo = Dojo.get_dojos_with_ninjas({"id": dojo_id}))

#     return redirect ('/')