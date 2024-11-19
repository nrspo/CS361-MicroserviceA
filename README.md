This microservice is a REST API to provide an inspirational quote for a workout app.

Application dependencies:
Flask: To install: py -m pip install flask
requests: py -m pip install requests

Flask instructions to start the application:
    1. environment: adjust SERVER_ADDRESS and PORT_NUMBER if needed. Default is 127.0.0.1:8100
    2. Run the inspirational_quote_server.py microservice app

Requests handled:
GET "/": Responds with a JSON including all messages. 
POST "/": POSTS formatted with json body {"type": "message_type"}. Supported types are "goal" and "streak".
            Responds with a JSON formatted {"message": "A message", "author": "An Author"}. "author" key is only present if a message is a quote.

COMMUNICATION CONTRACT
EXAMPLE REQUEST AND RECEIVE (Python 3.13):
See client_example.py for more examples.

# import standard library requests
import requests
# use json syntax
request = {"type": "goal"}
# use requests.post(url, json=) to request the microservice with json format
response = requests.post('http://127.0.0.1:8100', json=request)    
# call .json() on the response to parse the data
print(response.json(), "\n")     
print(response.json()["message"])              

UML Sequence Diagram
![alt text](<microservice uml.png>)