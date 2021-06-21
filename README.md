# washAS-API

# curl http://localhost:5000/machines/bosch_1000/price -d "new_price=1337&auth_token=123456789" -X PUT -v
# curl http://localhost:5000/machines/bosch_1000/reservations -d "add_reservations=5&auth_token=123456789" -X PUT -v
# curl http://localhost:5000/machines/bosch_1000/reservations -d "set_reservations=39&auth_token=123456789" -X PUT -v

# curl 'http://localhost:5000/machines/bosch_1000?auth_token=123456789'
# curl 'http://localhost:5000/machines/bosch_1000/price?auth_token=123456789'
# curl 'http://localhost:5000/machines/bosch_1000/reservations?auth_token=123456789'
