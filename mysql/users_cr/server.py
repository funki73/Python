from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User

app = Flask(__name__)
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

def update_form():
    pass

def update_user():
    pass

def delete_user():
    pass
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)