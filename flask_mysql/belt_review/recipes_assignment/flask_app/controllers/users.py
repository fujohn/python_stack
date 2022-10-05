from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/recipes')
    else:
        return render_template('index.html')

@app.route('/recipes')
def recipes():
    print(session['user_id'])
    data = {'id': session['user_id']}
    user = User.get_by_id(data)
    all_recipes = Recipe.get_all_recipes_with_user()
    return render_template('recipes_list.html', user = user, all_recipes = all_recipes)

@app.route('/register_user', methods=['POST'])
def register():
    session.clear()
    print(request.form)
    if not User.validate_registration(request.form):
        print('validation error')
        session['registration_failed'] = True
        return redirect('/') # with all the flash messages
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.save(data)
    print(user_id)
    session['user_id'] = user_id
    return redirect('/recipes')


@app.route('/login', methods=['POST'])
def login():
    session.clear()
    print(request.form)
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Email not registered.', 'login')
        session['login_failed'] = True
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        session['login_failed'] = True
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
