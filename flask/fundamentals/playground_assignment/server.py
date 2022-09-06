from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def create_boxes_1():
    return render_template('play.html', x=3, color='red')

@app.route('/play/<int:x>')
def create_boxes_2(x):
    return render_template('play.html', x=x, color='blue')


@app.route('/play/<int:x>/<string:color>')
def create_boxes_3(x, color):
    return render_template('play.html', x=x, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.