from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user 

from flask import flash

class Tv_shows:
    def __init__(self,data):
        self.id = data['id']
        self.user = user.User.get_by_id({"id": data['user_id']})
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data ['created_at']
        self.udpated_at = data ['updated_at']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO tv_shows (user_id, title, network, release_date, description, created_at, updated_at) VALUES (%(user_id)s, %(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW());"
        return connectToMySQL("tv_shows").query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tv_shows;"
        results = connectToMySQL("tv_shows").query_db(query)

        tv_shows = []
        for row in results:
            tv_shows.append(cls(row))

        return tv_shows


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM tv_shows WHERE id = %(id)s;"
        results = connectToMySQL("tv_shows").query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])



    @classmethod
    def update(cls, data):
        query = "UPDATE tv_shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("tv_shows").query_db(query, data)



    @classmethod
    def delete(cls, data):
        query = "DELETE FROM tv_shows WHERE id = %(id)s;"

        connectToMySQL("tv_shows").query_db(query, data)



    @staticmethod
    def validate(post_data):
        is_valid = True
        
        if len(post_data['title']) < 3:
            flash("Title must be at least 3 characters")
            is_valid = False

        if len(post_data['network']) < 3:
            flash("Network must be at least 3 characters")
            is_valid = False

        if len(post_data['description']) < 3:
            flash("Description must be at least 3 characters")
            is_valid = False

        return is_valid
