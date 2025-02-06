import requests
from requests.exceptions import HTTPError

url = "https://api.themoviedb.org/3/configuration"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMzYzYzI0MjRkZDI0ZGIxM2UwZDQ3OWIxYzExODA3NSIsIm5iZiI6MTczODgyNTA2Ny4zNjksInN1YiI6IjY3YTQ1ZDZiNzdiOGNlZDQ1NjY2ZDkzZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Xsx_gDaxIxH5l1bugdVbRPfuqJa5Y0NxivSwEIM7gSg",
    "accept": "application/json"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')
    data = response.json()
    print(data)