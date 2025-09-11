from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth # package for HTTP authorization 

app = Flask (__name__)
api = Api (app)
auth = HTTPBasicAuth() # create a HTTPBasicAuth() object and assign it to auth.

USER_DATA = {
    "admin": "atch_5K}?g" # create a dictionary containing user data which has a username and password as key and value
}

@auth.verify_password 
def verify (username, password): # verify function which takes the username and password as arguments that 
    if not (username and password): # returns True if the value of the dictionary call using the username gives the password we have
        return False
    return USER_DATA.get (username) == password # use get method of the dictionary so we don't get a key error

class HelloWorld (Resource):
    @auth.login_required # decorator auth.login_required on our get method
    def get (self):
        return {"Hello": "World"} # must be logged in to get the return of the HelloWorld class

api.add_resource (HelloWorld, '/hello_world')

app.run(debug=False)