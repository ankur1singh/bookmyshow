from flask import Blueprint
from flask_restful import Resource, Api, request
from .api import Users, Login, Movielist, Theaterlist, Screenlist, Bookinglist, Paymentlist, Verify, Image, Actorlist, Crewlist


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)
api = Api(main_bp)


api.add_resource(Users, "/Register")
api.add_resource(Verify, "/verify")
api.add_resource(Login, "/login/<id>")
api.add_resource(Movielist, '/movies/')
api.add_resource(Image, "/image/")
api.add_resource(Theaterlist, '/theater/<id>')
api.add_resource(Screenlist, '/screen/<id>')
api.add_resource(Bookinglist, '/booking/<id>')
api.add_resource(Paymentlist, '/payment/<id>')
api.add_resource(Actorlist, '/actor/<id>')
api.add_resource(Crewlist, '/crew/<id>')




