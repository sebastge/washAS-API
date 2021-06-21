import requests
import random
import string

api_url = 'http://localhost:5000/machines/'

for i in range(1001, 2001):
    create_row_data = {'auth_token': '123456789', 'product_name': f'Bosch {i}', 'product_description': ''.join(random.choices(string.ascii_lowercase, k=20)), 'product_price': random.randint(1000,5000)}
    r = requests.post(url=api_url, data=create_row_data)
    print(r.status_code, r.reason, r.text)