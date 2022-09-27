from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    session.clear()
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
    new_id = User.show_newest()[0]['MAX(id)']
    print(new_id)
    return redirect(f'/show/{new_id}')

@app.route('/show/<int:id>')
def show_user(id):
    data = {
        'id': id
    }
    user = User.retrieve_user(data)[0]
    print(user)
    return render_template('profile.html', user=user)

@app.route('/edit/<int:id>')
def go_to_edit(id):
    session['edit'] = True
    data = {
        'id': id
    }
    user = User.retrieve_user(data)[0]
    return render_template('create.html', user=user)

@app.route('/edit_user/<int:id>', methods=['POST'])
def edit_user(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.edit_user(data)
    session.clear()
    return redirect(f'/show/{id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/')
