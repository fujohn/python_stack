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
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''

    for i in range(num):
        output += f"<p>{word}</p>"

    return output


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.