from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app
from flask import render_template, redirect, request, session, flash

@app.route('/to_list')
def to_list():
    if 'recipe_id' in session:
        session.pop('recipe_id')
    return redirect('/recipes')

@app.route('/create_recipe')
def create_recipe():
    return render_template('recipe_new.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    print(request.form)
    if not Recipe.validate_recipe_entry(request.form):
        return redirect('/create_recipe')
    # add validation for this
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_thirty': request.form['under_thirty'],
        'recipe_date': request.form['recipe_date'],
        'user_id': session['user_id']
    }
    recipe_id = Recipe.save_recipe(data)
    session['recipe_id'] = recipe_id
    return redirect(f'/recipes/{session["recipe_id"]}')

@app.route('/recipes/<int:recipe_id>')
def one_recipe(recipe_id):
    session['recipe_id'] = recipe_id
    recipe_data = {'id': recipe_id}
    recipe = Recipe.retrieve_recipe_by_id(recipe_data)
    user_data = {'id': session['user_id']}
    user = User.get_by_id(user_data)
    return render_template('recipe_single.html', recipe=recipe, user=user)

@app.route('/recipes/edit/<int:recipe_id>')
def make_edit(recipe_id):
    session['recipe_id'] = recipe_id
    recipe_data = {'id': recipe_id}
    recipe = Recipe.retrieve_recipe_by_id(recipe_data)
    return render_template('recipe_edit.html', recipe = recipe)

@app.route('/edit_recipe', methods=['POST'])
def edit_recipe():
    if not Recipe.validate_recipe_entry(request.form):
        return redirect(f'/recipes/edit/{session["recipe_id"]}')
    data = {
        'id': session['recipe_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_thirty': request.form['under_thirty'],
        'recipe_date': request.form['recipe_date']
    }
    Recipe.edit_recipe(data)
    return redirect(f'/recipes/{session["recipe_id"]}')

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {'id': recipe_id}
    Recipe.delete_recipe(data)
    return redirect('/recipes')