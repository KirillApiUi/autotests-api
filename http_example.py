import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed" : False,
    "userid": 1
}
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.json())

data = {"username": "test_user", "password": "12345"}
response = httpx.post("https://postman-echo.com/post", data=data)

print(response.status_code)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://postman-echo.com/get", headers=headers)

print(response.request.headers)
print(response.json())