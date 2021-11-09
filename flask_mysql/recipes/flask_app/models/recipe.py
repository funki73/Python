from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user
from flask_app.models import recipe

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.user = user.User.get_by_id({"id": data['user_id']})
        self.name = data['name']
        self.description = data['description']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data ['created_at']
        self.udpated_at = data ['updated_at']

    @classmethod
    def create(cls,data):
        pass


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes").query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))

        return recipes


    @classmethod
    def get_one(cls,data):
        pass


    @classmethod
    def update(cls,data):
        pass


    @classmethod
    def update(cls,data):
        pass


    @classmethod
    def delete(cls,data):
        pass


    @staticmethod
    def validate(post_data):
        pass