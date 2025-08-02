import zmq
import json
from time import sleep

def send_request(message):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8888")
    socket.send_json(message)
    response = socket.recv_json()
    return response

def getHobby(hobby):
    print(f"Getting hobby: {hobby}")
    message = {"command": "get_by_name", "name": hobby}
    response = send_request(message)
    if response.get("status") == "success":
        return response.get("tasks", [])
    else:
        print(f"Error: {response.get('message', 'Unknown error')}")
        return []

def getAllHobbies():
    print("Getting all hobbies")
    message = {"command": "get_all"}
    response = send_request(message)
    if response.get("status") == "success":
        return response.get("tasks", [])
    else:
        print(f"Error: {response.get('message', 'Unknown error')}")
        return []

def updateHobby(hobby, status):
    print(f"Updating hobby: {hobby} to status: {status}")
    message = {"command": "update", "name": hobby, "completed": status}
    response = send_request(message)
    if response.get("status") == "success":
        return response.get("message", {})
    else:
        print(f"Error: {response.get('message', 'Unknown error')}")
        return {}


def main():

    print(json.dumps(getAllHobbies(), indent=2))

    sleep(2)

    print(json.dumps(updateHobby("running", False), indent=2))
    sleep(2)

    print(json.dumps(getHobby("running"), indent=2))
    sleep(2)


if __name__ == "__main__":
    main()
