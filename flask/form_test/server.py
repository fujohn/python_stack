from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
<<<<<<< HEAD

=======
app.secret_key = 'keep it secret, keep it safe' # set a secret key for session to work
>>>>>>> 7abaeca36fd9ab3a8120ad0b2e9bc4a6d9948325
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name = request.form['name']
#     email = request.form['email']
#     return redirect("/show")	 

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')
    
# # adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html")

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# # Session data is also available directly in our templates. That means we can do this:
# @app.route('/show')
# def show_user():
#     return render_template('show.html')

@app.route('/process', methods=['POST'])
def process():
    if request.form['which_form'] == 'register':
        print('REGISTERING')
        print(request.form)
    elif request.form['which_form'] == 'login':
        print('LOGGING IN')
        print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)