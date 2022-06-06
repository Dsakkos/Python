from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'coding dojo'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def user_survey():
    print("Got Post Info")
    session['fullname'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['Comments'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def show_survey():
    return render_template('survey.html')


if __name__ == '__main__':
    app.run(debug=True)