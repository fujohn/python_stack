from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return redirect('/dojos')

@app.route('/dojos')
def dojos_page():
    dojos = Dojo.get_all_dojos()
    session.clear()
    print(dojos)
    return render_template('dojos.html', all_dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    data = {
        'name': request.form['name']
    }
    Dojo.save_dojo(data)
    return redirect('/dojos')

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template('ninja_info.html', all_dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.save_ninja(data)
    return redirect(f'/dojos/{data["dojo_id"]}')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    print(dojo.ninjas)
    return render_template('dojo_ninjas.html', dojo = dojo)

@app.route('/edit/<int:id>')
def go_to_edit(id):
    session['edit'] = True
    data = {
        'id':id
    }
    ninja = Ninja.retrieve_ninja(data)[0]
    return render_template('ninja_info.html', ninja=ninja)

@app.route('/edit_ninja', methods=['POST'])
def edit_ninja():
    print(request.form)
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    Ninja.edit_user(data)
    ninja = Ninja.retrieve_ninja(data)[0]
    print(ninja)
    return redirect(f'/dojos/{ninja["dojo_id"]}')
