from flask_app.models.account import Account
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'account_id' in session:
        return render_template('/dashboard')
    else:
        return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'account_id' in session:
        data = {'id': session['account_id']}
        account = Account.get_by_id(data)
        return render_template('dashboard.html', account = account)
    else:
        return redirect('/')

@app.route('/register_account', methods=['POST'])
def register_account():
    session.clear()
    print(request.form)
    if not Account.validate_account_registration(request.form):
        print('validation issue')
        session['registration_failed'] = True
        return redirect('/')
    pw_hash =  bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password_hash': pw_hash
    }
    account_id = Account.save_account(data)
    print(account_id)
    session['account_id'] = account_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    session.clear()
    print(request.form)
    data = {'email': request.form['email']}
    account_in_db = Account.get_by_email(data)
    if not account_in_db:
        flash('Email has no account.')
        session['login_failed'] = True
        return redirect('/')
    if not bcrypt.check_password_hash(account_in_db.password_hash, request.form['password']):
        flash('Invalid Email/Password')
        session['login_failed'] = True
        return redirect('/')
    session['account_id'] = account_in_db.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

