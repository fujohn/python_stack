from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'q1w2e3r4t5y6' # set a secret key for security purposes

@app.route('/')
def index():
    if 'counter' in session:
        print('key exists!')
        return render_template("index.html")
    else:
        print("key 'counter' does NOT exist")
        session['counter'] = 0
        return render_template("index.html")


@app.route('/increase_counter', methods=['POST'])
def increase_counter():
    session['counter'] += 1
    return redirect("/")	 

@app.route('/increase_counter_2', methods=['POST'])
def increase_counter_2():
    session['counter'] += 2
    return redirect("/")	 

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    # session.clear()		# clears all keys
    session.pop('counter')		# clears a specific key
    return redirect("/")	 

if __name__ == "__main__":
    app.run(debug=True)