import requests
import json

BASE_PATH = 'https://data.fixer.io/api/latest?access_key='


def get_data(api_key):
    try:
        response = requests.get(BASE_PATH + api_key)
    except Exception as e:
        print(f"Error: {e}")
    else:
        return json.loads(response.text)

