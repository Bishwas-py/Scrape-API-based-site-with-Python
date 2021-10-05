import requests
import bs4
import json

url = 'https://nepsealpha.com/nepse-data'

session = requests.Session()

response = session.get(url)

soup = bs4.BeautifulSoup(response.text, 'html5lib')
form = soup.find('form', {'id': 'logout-form'})
token = form.find('input', {'name':'_token'})['value']

data_response = session.post(url,
    {
        'symbol': 'NEPSE',
        'specific_date': '2021-10-05',
        'start_date': '2021-09-15',
        'end_date': '2021-10-05',
        'filter_type': 'date-range',
        '_token': token
    }
)
print(
    json.dumps(data_response.json(), indent=4)
    )