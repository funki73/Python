from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times=5)
    # return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/flask')
def flask():
    return f'Hi Flask!'

@app.route('/say/michael')
def michael():
    return f'Hi Michael!'

@app.route('/say/john')
def john():
    return f'Hi John!'

@app.route('/repeat/hello/<name>/<int:num>')
def hi(name,num):
    return f'{name * num}'

@app.route('/repeat/bye/<name>/<int:num>')
def bye(name,num):
    return f'{name * num}'

@app.route('/repeat/dogs/<name>')
def dogs(name):
    return f'{name * 85}'

if __name__=="__main__":
    app.run(debug=True)


