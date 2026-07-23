import httpx

from tools.fakers import get_random_email
from tools.fakers import get_random_last_name
from tools.fakers import get_random_first_name
from tools.fakers import get_random_middle_name

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": get_random_last_name(),
    "firstName": get_random_first_name(),
    "middleName": get_random_middle_name()
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
