from flask import Flask, render_template, request, redirect

from flask import app

from models.ninja import Ninja

from models.dojo import Dojo

app = Flask(__name__)
app.secret_key = "keep it safe, keep it secure"

@app.route('/')
def dojohome():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)

    return redirect ('/')

@app.route('/ninjas')
def ninjas():

    return render_template("ninja.html", dojos = Dojo.get_dojos_with_ninjas())

@app.route('/ninja/add', methods=["POST"])
def add_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/')

@app.route("/dojos/<int:dojo_id>")
def display_ninjas(dojo_id):
    return render_template("dojo.html", dojo = Dojo.get_dojos_with_ninjas({"id": dojo_id}))

if __name__=="__main__":
    app.run(debug=True)