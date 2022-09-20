from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'q1w2e3r4t5y6' # set a secret key for security purposes

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0

    if 'visited' not in session:
        session['visited'] = 1
    else:
        session['visited'] += 1

    return render_template('index.html')



@app.route('/increase_counter', methods=['POST'])
def increase_counter():
    session['counter'] += 1
    return redirect("/")	 

@app.route('/increase_counter_2', methods=['POST'])
def increase_counter_2():
    session['counter'] += 2
    return redirect("/")	 

@app.route('/increase_counter_custom', methods=['POST'])
def increase_counter_custom():
    print(request.form)
    session['amount'] = int(request.form['custom_increment'])
    session['counter'] += session['amount']
    return redirect("/")	 

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()		# clears all keys
    # session.pop('counter')		# clears a specific key
    return redirect("/")	 

if __name__ == "__main__":
    app.run(debug=True)

# import base64
# base64.urlsafe_b64decode('eyJjb3VudGVyIjowLCJ2aXNpdGVkIjoxfQ===')

