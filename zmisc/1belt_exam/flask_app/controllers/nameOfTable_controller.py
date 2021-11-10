from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User

# Add new controller name to server.py file

# Above was moved from user_controller.py file
@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect ("/")

    return render_template(
        "dashboard.html", 
        user = User.get_by_id({"id": session['uuid']})),
        #example all_food_trucks = FoodTruck.get_all()
        #all_nameOfTable (plural) = nameOfTable<class_name>."get_all_query"
