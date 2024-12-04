import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH
import data

def get_new_user_token():
    response = requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}")
    response.raise_for_status()
    return response.json()["authToken"]

def post_new_user(body):
    return requests.post(
        f"{URL_SERVICE}{CREATE_USER_PATH}",
        json=body,
        headers=data.headers
    )

def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = f"Bearer {auth_token}"
    return requests.post(
        f"{URL_SERVICE}{KITS_PATH}",
        json=kit_body,
        headers=headers_dict
    )
