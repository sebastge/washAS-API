# Wash AS API

###### The python modules flask, flask_restful, uuid, random, string and requests are all needed to run this code (sorry).

To run the API locally you need to clone the repo and run the following command

```sh
python3 api.py
```
The server should now run on

```sh
http://localhost:5000
```

Run the following script in a new terminal window to populate the database with examples, as per the instructions

```sh
python3 update_db.py
```


A small database with a single product, customer and reservation is created when running the code. The info found in these can be used to test the API as decribed lower down. The example DB isa as follows:

```sh
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

```

## The API has the following features:
###### (The variable auth_token can be set programmatically in the file api.py)

- ##### Return all the products in the DB

```sh
curl --location --request GET 'http://localhost:5000/machines/?auth_token=123456789&type=all'
```

- ##### Return a product's info based on its ID, including the price and number of reservations it has (replace <product_id> below)

```sh
curl --location --request GET 'http://localhost:5000/machines/?auth_token=123456789&type=single&product_id=<product_id>'
```

- ##### Create a new object (replace <product_description>, <product_price> and <product_name> below.)
```sh
curl --location --request POST 'http://localhost:5000/machines/?auth_token=123456789&product_name=<product_name>&product_description=<product_description>&product_price=<product_price>'
```

- ##### Update an object's attibutes based on its ID (replace <product_id>, <product_description>, <product_price> and <product_name> below. (Remove the variable from the URL if not updating it...))
```sh
curl --location --request PUT 'http://localhost:5000/machines/?auth_token=123456789&product_id=<product_id>&product_description=<product_description>&product_price=<product_price>&product_name=<product_name>'
```


- ##### Create a new reservation based on the product's ID and the customer's ID (replace <product_id>, <customer_id> below.)

```sh
curl --location --request POST 'http://localhost:5000/machines/reservations/?auth_token=123456789&customer_id=<customer_id>&product_id=<product_id>'

```

- ##### Get the number of reservations belonging to a specific product based on the product's ID (replace <product_id> below)

```sh
curl --location --request GET 'http://localhost:5000/machines/reservations/?auth_token=123456789&type=get_product_reservations&product_id=<product_id>'
```

- ##### Get the number of reservations belonging to a specific customer based on the customer's ID (replace <customer_id> below)

```sh
curl --location --request GET 'http://localhost:5000/machines/reservations/?auth_token=123456789&type=get_customer_reservations&customer_id=<customer_id>'
```

