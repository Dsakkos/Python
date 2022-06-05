from flask import Flask, render_template# Import Flask to allow us to create our app

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html", times=3)	

@app.route('/play/<int:num>')
def number(num):
    return render_template("index.html", times=num)


@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("index2.html", times=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

