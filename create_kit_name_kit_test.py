import pytest
from data import get_kit_body
from sender_stand_request import get_new_user_token, post_new_client_kit

@pytest.fixture
def auth_token():
    return get_new_user_token()

def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_name_min_length(auth_token):
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_name_max_length(auth_token):
    kit_body = get_kit_body("A" * 511)
    positive_assert(kit_body, auth_token)

def test_name_empty(auth_token):
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)
