from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# Auth token used to authorize requests

AUTH_TOKEN = '123456789'

# Init example DB

MACHINES = {
    'bosch_1000': {'price': 9999.0, 'reservations': 0},
}


def abort_if_machine_doesnt_exist(machine_id):
    if machine_id not in MACHINES:
        abort(404, message="Machine {} doesn't exist".format(machine_id))


def abort_if_unauthorized(token):
    if token != AUTH_TOKEN:
        abort(401, message='Unauthorized')


# Add argument variables

parser = reqparse.RequestParser()
parser.add_argument('auth_token')
parser.add_argument('new_price')
parser.add_argument('reservations')
parser.add_argument('add_reservations')
parser.add_argument('set_reservations')


# Shows a single item based on it's ID

class Machine(Resource):
    def get(self, machine_id):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_machine_doesnt_exist(machine_id)
        return {machine_id: MACHINES[machine_id]}


# Shows the price of a single item based on it's ID, and allows for updating the price 

class Price(Resource):

    def get(self, machine_id):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_machine_doesnt_exist(machine_id)
        return {machine_id: {'price': MACHINES[machine_id]['price']}}

    def put(self, machine_id):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_machine_doesnt_exist(machine_id)
        try:
            new_price = float(args['new_price'])
            MACHINES[machine_id]['price'] = new_price
            return {machine_id: {'price': MACHINES[machine_id]['price']}}, 200
        except:
            abort(400,
                  message=f"Something went wrong. Could not update the price for {machine_id}. Make sure it's an int or float.")


# Shows the number of reservations of a single item based on it's ID, and allows for updating the number of reservations

class Reservations(Resource):

    def get(self, machine_id):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_machine_doesnt_exist(machine_id)
        return {machine_id: {'reservations': MACHINES[machine_id]['reservations']}}

    def put(self, machine_id):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_machine_doesnt_exist(machine_id)
        if (args['add_reservations']):
            try:
                reservations_to_be_added = int(args['add_reservations'])
                MACHINES[machine_id]['reservations'] += reservations_to_be_added
                return {machine_id: {'reservations': MACHINES[machine_id]['reservations']}}, 200
            except:
                abort(400,
                      message=f"Something went wrong. Could not update the number of reservations for {machine_id}. Make sure it's an int.")

        elif (args['set_reservations']):
            try:
                reservations = int(args['set_reservations'])
                MACHINES[machine_id]['reservations'] = reservations
                return {machine_id: {'reservations': MACHINES[machine_id]['reservations']}}, 200
            except:
                abort(400,
                      message=f"Something went wrong. Could not update the number of reservations for {machine_id}. Make sure it's an int.")


# Setup the Api resource routing

api.add_resource(Machine, '/machines/<machine_id>')
api.add_resource(Price, '/machines/<machine_id>/price')
api.add_resource(Reservations, '/machines/<machine_id>/reservations')

if __name__ == '__main__':
    app.run(debug=True)

