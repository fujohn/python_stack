from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hi(name):
    try:
        return f'Hi {name.capitalize()}!'
    except: 
        return 'Sorry! No response. Try again.'


@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    try:
        output = ''

        for i in range(num):
            output += f"<p>{word}</p>"

        return output
    except:
        return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.