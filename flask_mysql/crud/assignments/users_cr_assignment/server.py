from operator import methodcaller
from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/move_to_create')
def create_user():
    return render_template('create.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)