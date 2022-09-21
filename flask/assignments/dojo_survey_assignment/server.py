from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret' # set a secret key for security purposes

@app.route('/')
def index():
    session.clear() # if you are back at the home page, we default you back to nothing in session
    return render_template('index.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    print('back_end' in request.form)
    ends = []
    for end in ['front_end', 'back_end', 'database']:
        if end in request.form:
            ends.append(request.form[end])
    session['ends'] = ends
    print(session[ends])
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)