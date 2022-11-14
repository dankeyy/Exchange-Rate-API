import sys
import json
import os
from typing import Optional
import requests


def low_rates(prod=False) -> Optional[list]:
    payload = {}
    filtered = lambda payload: [name for name, rate in payload["rates"].items() if rate < 10]

    if prod:
        url = "https://api.apilayer.com/exchangerates_data/latest?"

        key = os.getenv("EXCHANGERATES_APIKEY_PROD")
        if key is None:
            raise ValueError("Could not find key")

        headers = {
        "apikey": key
        }

        response = requests.request("GET", url, headers=headers)
        payload = json.loads(response.text)
        status_code = response.status_code
        if status_code == 200:
            return filtered(payload)

    else:
        with open("mock.json") as f:
            payload = json.load(f)
        return filtered(payload)


if __name__ == '__main__':

    if sys.argv[1] == "prod":
        res = low_rates(prod=True)
        print(res) # might wanna comment it, do something else with res, idk

    elif sys.argv[1] == "dev":
        res = low_rates(prod=False)
        print(res) # might wanna comment it, do something else with res, idk

    else:
        print("bad argument, specify dev or prod")
        exit(1)
