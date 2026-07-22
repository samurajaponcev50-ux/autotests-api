import httpx

login_payload = {
    "email": "user2807@example.com",
    "password": "Qwerty123!"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_me_response_data = user_me_response.json()

print("User me response:", user_me_response_data)
print("User me status code:", user_me_response.status_code)