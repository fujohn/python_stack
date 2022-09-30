from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')
