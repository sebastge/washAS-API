# Wash AS API

To run the API locally you need to clone the repo and run the following command

```sh
python3 api.py
```
The server should now run on

```sh
http://localhost:5000
```

The following object is initialised for the machine Bosch 1000

```sh
{
    'bosch_1000': {'price': 9999.0, 'reservations': 0}
}
```
## The API has the following features:

- ##### Return an object based on its ID (bosch_1000 in this case)

```sh
curl http://localhost:5000/machines/bosch_1000?auth_token=123456789
```

- ##### Return only the price for an object based on its ID (bosch_1000 in this case)

```sh
curl http://localhost:5000/machines/bosch_1000/price?auth_token=123456789
```

- ##### Return only the number of reservations for an object based on its ID (bosch_1000 in this case)

```sh
curl http://localhost:5000/machines/bosch_1000/reservations?auth_token=123456789
```

- ##### Update the price for an object based on its ID (bosch_1000 in this case)
```sh
curl http://localhost:5000/machines/bosch_1000/price -d "new_price=5999&auth_token=123456789" -X PUT -v
```

- ##### Update the number of reservations for an object based on its ID (bosch_1000 in this case)

This can be done in two different ways. The first command adds a number of reservations to the number of reservations. I.e. number_of_reservations = existing_number_of_reservations + new_number_of_reservations

```sh
curl http://localhost:5000/machines/bosch_1000/reservations -d "add_reservations=5&auth_token=123456789" -X PUT -v
```

The second command sets a new number of reservations, irregardless of how many reservations were in the database already. I.e. number_of_reservations = new_number_of_reservations

```sh
curl http://localhost:5000/machines/bosch_1000/reservations -d "set_reservations=39&auth_token=123456789" -X PUT -v
```
