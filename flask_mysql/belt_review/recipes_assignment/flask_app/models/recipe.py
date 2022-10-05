from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.recipe_date = data['recipe_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user_info = None

    def __repr__(self):
        return f'Recipe for {self.name}'

    def add_creator(self, user):
        self.user_info = user

    @classmethod
    def get_all_recipes_with_user(cls):
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id'
        results = connectToMySQL('recipes_schema').query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipe_class = cls(recipe)
            user_data = {
                'id': recipe['users.id'],
                'first_name': recipe['first_name'],
                'last_name': recipe['last_name'],
                'email': recipe['email'],
                'password': recipe['password'],
                'created_at': recipe['users.created_at'],
                'updated_at': recipe['users.updated_at']
            }
            recipe_class.add_creator(user.User(user_data))
            recipes.append(recipe_class)
        return recipes # a list of recipe instances

    @staticmethod
    def validate_recipe_entry(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Name must have at least 3 characters.', 'recipe_entry')
            is_valid = False
        if len(recipe['description']) < 3:
            flash('Description must have at least 3 characters.', 'recipe_entry')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Instructions must have at least 3 characters.', 'recipe_entry')
            is_valid = False
        if len(recipe['recipe_date']) < 1:
            flash('Please choose a valid date.', 'recipe_entry')
            is_valid = False
        if not 'under_thirty' in recipe:
            flash('Please select whether it takes less than 30 minutes.', 'recipe_entry')
            is_valid = False
        return is_valid

    @classmethod
    def save_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, under_thirty, recipe_date, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(recipe_date)s, %(user_id)s)'
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def retrieve_recipe_by_id(cls, data):
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s'
        result = connectToMySQL('recipes_schema').query_db(query, data)[0]
        print(result)
        recipe_data = {
                'id': result['id'],
                'name': result['name'],
                'description': result['description'],
                'instructions': result['instructions'],
                'under_thirty': result['under_thirty'],
                'recipe_date': result['recipe_date'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at'],
                'user_id': result['user_id']
        }
        recipe = cls(recipe_data)
        user_data = {
                'id': result['users.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'email': result['email'],
                'password': result['password'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at']
            }
        recipe.add_creator(user.User(user_data))
        return recipe

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_thirty = %(under_thirty)s, recipe_date = %(recipe_date)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s'
        return connectToMySQL('recipes_schema').query_db(query, data)