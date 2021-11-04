from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "eatmeat"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/form_submit", methods = ["POST"])
def form_submit():
    print(request.form)

    session["yourname"] = request.form ["yourname"]
    session["city"] = request.form ["city"]
    session["language"] = request.form ["language"]
    session["comment"] = request.form ["comment"]

    return redirect("/results")

@app.route("/results")
def new_route():
    print(request.form)
    return render_template(
        "results.html",
        yourname = session["yourname"],
        city = session["city"],
        language = session["language"],
        comment = session["comment"]
)


if __name__=="__main__":
    app.run(debug=True)