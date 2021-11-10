from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user
from flask_app.models import recipe

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.user = user.User.get_by_id({"id": data['user_id']})
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data ['created_at']
        self.udpated_at = data ['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, date_made, under_thirty, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_thirty)s, NOW(), NOW());"

        return connectToMySQL("recipes").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes").query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))

        return recipes


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("recipes").query_db(query, data)

        if len(results) < 1:
            return False
            
        return cls(results[0])


    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("recipes").query_db(query, data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        connectToMySQL("recipes").query_db(query, data)


    @staticmethod
    def validate(post_data):
        is_valid = True
        
        if len(post_data['name']) < 2:
            flash('Name must be at least 2 characters')
            is_valid = False

        if len(post_data['description']) < 4:
            flash('Description must be at least 4 characters')
            is_valid = False

        if len(post_data['instructions']) < 4:
            flash('Instructions must be at least 4 characters')
            is_valid = False

        return is_valid