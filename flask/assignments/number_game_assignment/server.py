from flask import Flask, render_template, request, redirect, session
import random # import the random module



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100) # random number between 1-100
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    # Here we add two properties to session to store the name and email
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)