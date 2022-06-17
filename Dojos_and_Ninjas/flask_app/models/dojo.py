from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"

        results = connectToMySQL(cls.db).query_db(query)
        dojos = []

        for row in results:
            dojos.append( cls(row) )
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojo (name) VALUES (%(name)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojo LEFT JOIN ninjas on dojo.id = ninjas.dojo_id WHERE dojo.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(data) )
        return dojo