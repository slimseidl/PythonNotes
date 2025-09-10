from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# reqparse is an argument parser that processes arguments with with web requests to an API 

app = Flask (__name__)
api = Api (app)

film_dict = {
'1': {'Name': 'Avengers: Infinity War', 'Year': 2018, 'Month': 'March'},
'2': {'Name': 'Ant Man and the Wasp', 'Year': 2018, 'Month': 'August'}
}

def abort_if_todo_doesnt_exist (film_id):
    if film_id not in film_dict:
        abort (404, message="Film {} doesn't exist". format (film_id))
    # abort import is used in a custom function that we use to send an appropriate message if the film_id doesn't exist
    # pass the film_id as an argument and if the id doesn't exist in the dictionary then a 404 is given with a custom message relating to the film that doesn't exist

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('year')
parser.add_argument('month')

# Films Class defines methods to get, delete, and put a film in our dictionary
# If film doesnt exist it aborts 
# delete and put methods return status codes 
class Films (Resource):
    def get (self, film_id):
        abort_if_todo_doesnt_exist (film_id)
        return film_dict [film_id]

    def delete (self, film_id):
        abort_if_todo_doesnt_exist (film_id)
        del film_dict [film_id]
        return '', 204

    def put (self, film_id):
        args = parser.parse_args() # Parses arguments from the request parser and stores them in a dictionary
        task = {'Name': args['name'],
        'Year': args['year'],
        'Month': args['month']}
        film_dict [film_id] = task
        return task, 201

# Class Film Dictionary returns the entire database of films 
class FilmDict (Resource):
    def get (self):
        return film_dict

# http://127.0.0.1:5000 will generate a NOT FOUND error. need to use /films or /films/<film_id>
api.add_resource (FilmDict, '/films')
api.add_resource (Films, '/films/<film_id>')

if __name__ == '__main__':
    app.run(debug=False)