from flask_app.config.mysqlconnection import connectToMySQL

from .ninja import Ninja


class Dojo:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        alldojos = []
        for dojo in dojos:
            alldojos.append(cls(dojo))
        return alldojos
    
    @classmethod
    def create_dojo( cls , data ):
        query = "INSERT INTO dojos (name , created_at , updated_at ) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result

    @classmethod
    def get_dojos_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos_id WHERE dojo_id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( cls( ninja_data ) )
        return dojo