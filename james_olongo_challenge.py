# -*- coding: utf-8 -*-
"""James_Olongo_challenge.ipynb

Automatically generated by Colaboratory.

"""

import requests
import json


def fetch_json_content(url):
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # check erros HTTP

        return response.json()  # return content of response
    except requests.exceptions.RequestException as e:
        return {"error": f"Une erreur s'est produite : {e}"}


# URL initiale
url = "https://www.letsrevolutionizetesting.com/challenge"

iteration = 1

while True:  # Continue until you get a different message
    print(f"Iteration {iteration}:")

    response_data = fetch_json_content(url)
    print("Response JSON:", response_data)

    message = response_data.get("message")
    if message != "This is not the end":
        print("Message is different. Stopping loop.")
        break

    follow_url = response_data.get("follow")
    if follow_url:
        url = follow_url
        print(f"Updating URL to: {follow_url}")
    else:
        print("Follow URL not found. Stopping loop.")
        break

    iteration += 1
