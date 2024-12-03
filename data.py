from copy import deepcopy

BASE_KIT_BODY = {
    "name": ""
}

def get_kit_body(name):
    body = deepcopy(BASE_KIT_BODY)
    body["name"] = name
    return body
