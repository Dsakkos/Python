from flask import Flask, render_template, request, redirect
# import the class from users.py
from user import User
app = Flask(__name__)
app.secret_key = "coding dojo"

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users/new')
def index():
    return render_template("new_users.html")



@app.route('/users/new', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users')
def show_users():
    users = User.get_all()
    print(users)
    return render_template('users.html', users = users)


if __name__ == "__main__":
    app.run(debug=True)