import uuid

import requests

from app.utils.config import auth_data

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = 'scope=GIGACHAT_API_PERS'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': str(uuid.uuid4()),
    'Authorization': 'Basic ' + auth_data,
}


def get_token():
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.json()['access_token']
