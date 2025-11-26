import requests
import json
import random
import string

#base url:
base_url = "https://gorest.co.in"

#authorization
auth_token = "Bearer 4d10ef7527d6f8e3f5a961df8d074dc2df34d6de7f36edff5efb026b65ec26c6"

#generate Random Email
def generate_random_email():
    domain = "example.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#GET Request
def test_get_request():
    url = base_url + "/public/v2/users"
    headers = {
        "Authorization": auth_token
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("JSON Response Body: ", json_str)

#POST Request
def test_post_request():
    url = base_url + "/public/v2/users"
    headers = {
        "Authorization": auth_token
    }
    payload = {
        "name": "Foo Bar",
        "email": generate_random_email(),
        "gender": "female",
        "status": "active"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("JSON Response Body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Foo Bar"
    return user_id

#PUT Request
def test_put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {
        "Authorization": auth_token
    }
    payload = {
        "name": "Foo Bar",
        "email": generate_random_email(),
        "gender": "female",
        "status": "inactive"
    }
    response = requests.put(url, json=payload, headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("JSON Response Body: ", json_str)
    assert user_id == json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Foo Bar"

#DELETE Request
def test_delet_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {
        "Authorization": auth_token
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("User Is Removed")


#API Tests
test_get_request()
user_id = test_post_request()
test_put_request(user_id)
test_delet_request(user_id)