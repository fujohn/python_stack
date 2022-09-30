# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# model the class after the friend table from our database
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query) # yields a list of dictionaries (1 dict per row)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def show_newest(cls):
        query = 'SELECT MAX(id) FROM users'
        return connectToMySQL('users_schema').query_db(query)

    @classmethod
    def retrieve_user(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def edit_user(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s'
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('users_schema').query_db( query, data )

    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if len(user['email']) == 0:
            flash("Please enter email.", 'empty')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'invalid')
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        return is_valid