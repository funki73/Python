from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self , data ):
        self.dojo_id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query)
    
    @classmethod
    def add_ninja( cls, data ):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)