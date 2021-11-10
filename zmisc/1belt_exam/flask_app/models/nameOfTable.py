from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import user 
# //add into "NameOfTable" from flask_app.models import "NameOfTable".  Remove this line when completed.

# //add from flask import flash when updating the static method

# class "NameOfTable"
    def __init__(self,data):
        self.xxx = data['xx']
        # self.user = user.User.get_by_id({"id: data['user_id"]}) may need to update


@classmethod
def create(cls, data):
    pass



@classmethod
def get_all(cls):
    pass



@classmethod
def get_one(cls,):
    pass



@classmethod
def update(cls, data):
    pass



@classmethod
def delete(cls, data):
    pass



@staticmethod
def validate(post_data):
    pass
