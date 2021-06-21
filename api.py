import uuid

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# Auth token used to authorize requests

AUTH_TOKEN = '123456789'

# Init example DB with one customer, one product, and one reservation of said product by said customer

MACHINES = [
    {'product_id': 'ed8d410c-5a32-4b70-bd86-7f5a7ec06538', 'product_name': 'Bosch 1000',
     'product_description': 'The best washer',
     'product_price': 4999}]

CUSTOMERS = [{
    'customer_id': '0b93985f-20cc-41d9-8148-75fcd71514e3', 'name': 'Sebastian', 'reservations': []
}]

RESERVATIONS = [
    {'customer_id': '0b93985f-20cc-41d9-8148-75fcd71514e3', 'product_id': 'ed8d410c-5a32-4b70-bd86-7f5a7ec06538',
     'reservation_id': '6d90fe20-4269-4927-993a-56c9efd28f53'}]


def abort_if_product_doesnt_exist(product_id):
    machine_exists = False
    for machine in MACHINES:
        if product_id == machine['product_id']:
            machine_exists = True
    if not machine_exists:
        abort(404, message="Machine {} doesn't exist".format(product_id))


def abort_if_customer_doesnt_exist(customer_id):
    customer_exists = False

    for customer in CUSTOMERS:
        if customer_id == customer['customer_id']:
            customer_exists = True
    if not customer_exists:
        abort(404, message="Customer {} doesn't exist".format(customer_id))


def abort_if_unauthorized(token):
    if token != AUTH_TOKEN:
        abort(401, message='Unauthorized')


def get_customer_reservations(customer_id):
    customer_reservations = []
    for reservation in RESERVATIONS:
        if customer_id == reservation['customer_id']:
            for machine in MACHINES:
                if reservation['product_id'] == machine['product_id']:
                    machine['reservation_id'] = reservation['reservation_id']
                    customer_reservations.append(machine)

    return customer_reservations


def get_product_reservations(product_id):
    product_reservations = []
    for reservation in RESERVATIONS:
        if product_id == reservation['product_id']:
            for machine in MACHINES:
                if reservation['product_id'] == machine['product_id']:
                    machine['reservation_id'] = reservation['reservation_id']
                    product_reservations.append(machine)

    return product_reservations


def get_number_of_product_reservations(product_id):
    num_reservations = 0
    for reservation in RESERVATIONS:
        if product_id == reservation['product_id']:
            num_reservations += 1
    return num_reservations


# Add argument variables

parser = reqparse.RequestParser()
parser.add_argument('auth_token')
parser.add_argument('reservations')
parser.add_argument('add_reservations')
parser.add_argument('set_reservations')
parser.add_argument('size')
parser.add_argument('name')
parser.add_argument('customer_id')
parser.add_argument('product_id')
parser.add_argument('product_name')
parser.add_argument('product_description')
parser.add_argument('product_price')
parser.add_argument('type')


# Shows a single item based on it's ID

class Machine(Resource):

    def post(self):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        product_id = str(uuid.uuid4())
        MACHINES.append({'product_id': product_id, 'product_name': args['product_name'],
                         'product_description': args['product_description'], 'product_price': args['product_price']})
        return {'product_id': product_id, 'product_name': args['product_name'],
                'product_description': args['product_description'], 'product_price': args['product_price']}, 201

    def get(self):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        if args['type'] == 'all':
            return MACHINES
        elif args['type'] == 'single':
            abort_if_product_doesnt_exist(args['product_id'])
            for machine in MACHINES:
                if args['product_id'] == machine['product_id']:
                    machine['number_of_reservations'] = get_number_of_product_reservations(args['product_id'])
                    return machine, 200

    def put(self):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_product_doesnt_exist(args['product_id'])
        for machine in MACHINES:
            if args['product_id'] == machine['product_id']:
                if args.get('product_price'):
                    MACHINES[MACHINES.index(machine)]['product_price'] = int(args['product_price'])
                if args.get('product_name'):
                    MACHINES[MACHINES.index(machine)]['product_name'] = str(args['product_name'])
                if args.get('product_description'):
                    MACHINES[MACHINES.index(machine)]['product_description'] = str(args['product_description'])
                return machine, 200


# Shows the number of reservations of a single item based on it's ID, and allows for updating the number of reservations

class Reservations(Resource):

    def post(self):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        abort_if_product_doesnt_exist(args['product_id'])
        abort_if_customer_doesnt_exist(args['customer_id'])
        reservation_id = str(uuid.uuid4())
        RESERVATIONS.append({'reservation_id': reservation_id, 'customer_id': args['customer_id'],
                             'product_id': args['product_id']})
        return {'reservation_id': reservation_id, 'customer_id': args['customer_id'],
                'product_id': args['product_id']}, 201

    def get(self):
        args = parser.parse_args()
        abort_if_unauthorized(args['auth_token'])
        if args['type'] == 'get_product_reservations':
            abort_if_product_doesnt_exist(args['product_id'])
            for machine in MACHINES:
                if args['product_id'] == machine['product_id']:
                    return {'product_id': args['product_id'],
                            'reservations': get_product_reservations(args['product_id'])}

        elif args['type'] == 'get_customer_reservations':
            abort_if_customer_doesnt_exist(args['customer_id'])
            for customer in CUSTOMERS:
                if args['customer_id'] == customer['customer_id']:
                    return {'customer_id': args['customer_id'],
                            'reservations': get_customer_reservations(args['customer_id'])}


# Setup the Api resource routing

api.add_resource(Machine, '/machines/')
api.add_resource(Reservations, '/machines/reservations/')

if __name__ == '__main__':
    app.run(debug=True)
