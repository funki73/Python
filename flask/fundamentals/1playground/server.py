from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template('level1.html')

@app.route('/play/<int:num>')
def level2(num):
    return render_template('level2.html', times = num)

@app.route('/play/<int:num>/<string:color>')
def level3(num, color):
    return render_template('level3.html', times=num, color=color)



if __name__=="__main__":
    app.run(debug=True)