import requests
from requests.exceptions import HTTPError

try:
    response=requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=41.311081&lon=69.240562&appid=0c5557c89dc8128646577917380776f3')
    response.raise_for_status()
except HTTPError as http_err:
    print(f'http error was occured: {http_err}')
except Exception as err:
    print(f'Other error occured: {err}')
else:
    print('Success!')
data = response.json()
temperature = data['list'][0]['main']['temp']     
humidity = data['list'][0]['main']['humidity']  
print(f'temperature={temperature}')
print(f'humidity={humidity}')
