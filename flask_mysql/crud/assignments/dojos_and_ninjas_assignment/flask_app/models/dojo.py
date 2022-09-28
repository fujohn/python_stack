# import the function that will return an instance of a connection
from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# model the class after the friend table from our database

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    def __repr__(self):
        return f'{self.id} {self.name}'

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query) # yields a list of dictionaries (1 dict per row)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0]) # create class of given dojo id
        for one_ninja in results:
            ninja_data = {
                'id': one_ninja['ninjas.id'],
                'first_name': one_ninja['first_name'],
                'last_name': one_ninja['last_name'],
                'age': one_ninja['age'],
                'dojo_id': one_ninja['dojo_id'],
                'created_at': one_ninja['created_at'],
                'updated_at': one_ninja['updated_at'],
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data)) # add each ninja in corresponding dojo id
        return dojo


    # @classmethod
    # def show_newest(cls):
    #     query = 'SELECT MAX(id) FROM users'
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query)

    # @classmethod
    # def retrieve_user(cls, data):
    #     query = "SELECT * FROM users WHERE id=%(id)s"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    # @classmethod
    # def edit_user(cls, data):
    #     query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s'
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id=%(id)s"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )