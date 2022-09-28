# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def retrieve_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def edit_user(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s'
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
