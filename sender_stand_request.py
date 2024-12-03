import requests
from configuration import URL_SERVICE, CREATE_USER_PATH , KITS_PATH

def get_new_user_token():
    response = requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}")
    response.raise_for_status()
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", json=kit_body, headers=headers)
    return response
