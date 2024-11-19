import random
from flask import Flask, request, jsonify
app = Flask(__name__)

########################
# Microservice IP and Port Configurations
########################
SERVER_ADDRESS = "127.0.0.1"
PORT_NUMBER = 8100

# Message Data
messages = {
            "streak": [
                {
                    "message": "Success isn't always about 'greatness', it's about consistency.",
                    "author": "The Rock",
                },
                {
                    "message": "You just can’t beat the person who never gives up.",
                    "author": "Babe Ruth",
                },
                {
                    "message": "New streak, way to go!",
                },
                {
                    "message": "New streak! Keep up that momentum!",
                }
            ],
            "goal": [
                {
                    "message": "Good Job!"
                },
                {
                    "message": "Keep it up!"
                },
                {
                    "message": "You smashed that goal!"
                },                
                {
                    "message": "Everything is impossible until it is done.",
                    "author": "Robert H. Goddard"
                },
                {
                    "message": "No matter how many goals you have achieved, you must set your sights on a higher one.",
                    "author": "Jessica Savitch"
                },
                {
                    "message": "Goals are the road maps that guide you to your destination.",
                    "author": "Roy T. Bennett"
                },
                {
                    "message": "No matter how many goals you have achieved, you must set your sights on a higher one.",
                    "author": "Jessica Savitch"
                },
                {
                    "message": "Goals are the road maps that guide you to your destination.",
                    "author": "Roy T. Bennett"
                },
                {
                    "message": "Everything is impossible until it is done.",
                    "author": "Robert H. Goddard"
                }
            ]
        }

########################
# Microservice functions
########################
def random_message(type=None):
    """Chooses a random mesage based on streak or goal type requested. If no type is passed, a goal type is selected. """
    rand_int = random.randrange(1, 99999999)
    if type == "streak":
        rand_index = rand_int % len(messages["streak"])
        return jsonify(messages["streak"][rand_index])
    else:   #  type is None or type == "goal":
        rand_index = rand_int % len(messages["goal"])
        return jsonify(messages["goal"][rand_index])

########################
# REST API Routes
########################

@app.get("/")
def show_all_messages():
    return jsonify(messages), 201

@app.post("/")
def post_message():
    if request.is_json:
        request_data = request.get_json()
        if "type" not in request_data:
            return random_message(), 201
        elif request_data["type"] == "goal":
            return random_message("goal")
        elif request_data["type"] == "streak":
            return random_message("streak")
        else:
            return jsonify({"error": "Type variable not valid"}), 400
    return {"error": "Request must be JSON format"}, 415

if __name__ == '__main__':
    app.run(host=SERVER_ADDRESS, port=PORT_NUMBER)