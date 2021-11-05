from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route("/create")
def create():
    return render_template("create.html")

# relevant code snippet from server.py
@app.route('/create', methods=["POST"])
def create_sub():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/users/<int:user_id>')
def display_user(user_id):
    return render_template("user.html", user = User.get_one({"id": user_id}))

@app.route("/users/<int:user_id>/edit")
def edit_form(user_id):
    return render_template("edit.html", user = User.get_one({"id": user_id}))

@app.route('/users/<int:user_id>/update', methods=["POST"])
def update_user(user_id):
    print (request.form)
    data={
        **request.form,
        "id":user_id
    }
    User.update(data)

    return redirect('/')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete({"id": user_id})

    return redirect('/')