from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/<int:num>')
def index2(num):
    return render_template('index2.html', times = num)


if __name__=="__main__":
    app.run(debug=True)