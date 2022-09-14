from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def root_route():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def with_x(x):
    return render_template('index.html', x=x, y=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def with_x_y(x, y):
    return render_template('index.html', x=x, y=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def with_x_y_colors(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.