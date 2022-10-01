# from flask_app.models.user import User
# from flask_app import app
# from flask import render_template,redirect,request,session,flash

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
#         # we redirect to the template with the form.
#         return redirect('/')
#     # ... do other things
#     return redirect('/dashboard')

# # bcrypt (register)
# @app.route('/register/user', methods=['POST'])
# def register():
#     # validate the form here ...
#     # create the hash
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)
#     # put the pw_hash into the data dictionary
#     data = {
#         "username": request.form['username'],
#         "password" : pw_hash
#     }
#     # Call the save @classmethod on User
#     user_id = User.save(data)
#     # store user id into session
#     session['user_id'] = user_id
#     return redirect("/dashboard")

# # login
# @app.route('/login', methods=['POST'])
# def login():
#     # see if the username provided exists in the database
#     data = { "email" : request.form["email"] }
#     user_in_db = User.get_by_email(data)
#     # user is not registered in the db
#     if not user_in_db:
#         flash("Invalid Email/Password")
#         return redirect("/")
#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         # if we get False after checking the password
#         flash("Invalid Email/Password")
#         return redirect('/')
#     # if the passwords matched, we set the user_id into session
#     session['user_id'] = user_in_db.id
#     # never render on a post!!!
#     return redirect("/dashboard")