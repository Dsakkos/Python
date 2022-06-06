from flask import Flask, redirect, session


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return 'Counter: '+str(session['counter'])

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)



