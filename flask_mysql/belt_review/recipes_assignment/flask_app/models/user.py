from flask_bcrypt import Bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import recipe
from flask import flash
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password'] # will only stored the hashed version of pw
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'
    
    # validate registration
    def validate_registration(user):
        email_query = 'SELECT * FROM users WHERE email = %(email)s'
        email_exists = connectToMySQL('recipes_schema').query_db(email_query, user) # None if no data is found
        is_valid = True
        if len(user['email']) == 0:
            flash("Please enter email.", 'register')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        elif email_exists: 
            flash("User already exists.", 'register')
            is_valid = False
        if not user['first_name'].isalpha():
            flash("Please use only alphabetic characters in first name.", 'register')
            is_valid = False
        elif len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.", 'register')
            is_valid = False
        if not user['last_name'].isalpha():
            flash("Please use only alphabetic characters in last name.", 'register')
            is_valid = False
        elif len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.", 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters long.", 'register')
            is_valid = False
        if user['password'] != user['password_conf']:
            print('mismatch pw')
            flash("Passwords do not match.", 'register')
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])