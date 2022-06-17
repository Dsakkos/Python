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
    return render_template("new_users.html" )


@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    id = User.create(data)
    return redirect(f'/users/{id}')


@app.route('/users/<int:id>')
def show_user(id):
    return render_template('show_user.html', user = User. 
    get_user_by_id({"id": id}))

@app.route('/users')
def show_users():
    return render_template('users.html', all_user = User.
    get_all_users())


@app.route('/users/edit/<int:id>')
def edit_user(id):
    return render_template('edit_user.html', user = User. 
    get_user_by_id({"id": id}))

@app.route('/users/update', methods = ['POST'])
def update_user():
    data = {
        "id": request.form['id'],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    User.update_user(data)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete_user(id):
    User.delete({"id": id})
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)