from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "clickmeat"

@app.route('/')
def counterme():
    if 'clickme' in session:
        session['clickme'] += 1
    else:
        session['clickme'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)