import requests

url = 'http://127.0.0.1:8100'

print("Test 1:")
print("Sending an empty request - no type specified. Response in JSON format: ")
request = {}
response = requests.post(url, json=request)
print(response.json(), "\n")

print("Test 2:")
print("Sending an invalid request that does not use json format. Response: ")
response = requests.post(url, data=request)
print(response.json(), "\n")

print("Test 3:")
print("Sending a request for type: goal. Response: ")
request = {"type": "goal"}
response = requests.post(url, json=request)
print(response.json(), "\n")

print("Test 4:")
print("Sending a request for type: streak. Response: ")
request = {"type": "streak"}
response = requests.post(url, json=request)
print(response.json(), "\n")

print("Example parsed data: ")
if "author" in response.json():
    print(response.json()["message"], "-", response.json()["author"])
else:
    print(response.json()["message"])
