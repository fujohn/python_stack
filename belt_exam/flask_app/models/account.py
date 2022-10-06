from flask_bcrypt import Bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
bcrypt = Bcrypt(app)    # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument



from flask import flash
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Account:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password_hash = data['password_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f"{self.first_name} {self.last_name}'s account information"

    # validate inputs
    @staticmethod
    def validate_account_registration(account):
        email_list_query = 'SELECT * FROM accounts WHERE email = %(email)s'
        email_list = connectToMySQL('accounts_schema').query_db(email_list_query, account)
        is_valid = True
        if len(account['email']) == 0:
            flash("Please enter email.", 'empty')
            is_valid = False
        elif not EMAIL_REGEX.match(account['email']): 
            flash("Invalid email address!", 'invalid')
            is_valid = False
        elif email_list: # create email_list to select list of email? or if select works
            flash("Email already in use.")
            is_valid = False
        if not account['first_name'].isalpha():
            flash("Please use only alphabetic characters in first name.")
            is_valid = False
        elif len(account['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if not account['last_name'].isalpha():
            flash("Please use only alphabetic characters in last name.")
            is_valid = False
        elif len(account['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(account['password']) < 8:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if account['password'] != account['confirm_password']:
            flash("Passwords do not match.")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM accounts WHERE id = %(id)s;"
        result = connectToMySQL('accounts_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        result = connectToMySQL('accounts_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save_account(cls, data):
        query = 'INSERT INTO accounts (first_name, last_name, email, password_hash) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        return connectToMySQL('accounts_schema').query_db(query, data)
