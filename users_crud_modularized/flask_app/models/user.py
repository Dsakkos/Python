
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES ( %(fname)s , %(lname)s , %(email)s);"
        return connectToMySQL(cls.db).query_db( query, data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db( query)
        user_list = []
        for row in results:
            user_list.append( cls(row))
        return user_list




    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db( query, data)
        return cls(results[0])

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s WHERE id=%(id)s"
        connectToMySQL(cls.db).query_db( query, data )
        return

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        connectToMySQL(cls.db).query_db(query,data)