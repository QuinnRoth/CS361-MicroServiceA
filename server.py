import zmq
import json
import os

DATA_FILE = "hobbies.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def main():
    context = zmq.Context()
    print("Starting server")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:8888")

    while True:
        message = socket.recv_json()
        command = message.get("command")

        data = load_data()

        if command == "get_all":
            socket.send_json({"status": "success", "hobbies": data})
        elif command == "get_by_name":
            name = message.get("name")
            if name:
                matching = [hobby for hobby in data if hobby["name"] == name]
                socket.send_json({"status": "success", "hobbies": matching})
            else:
                socket.send_json({"status": "error", "message": "Missing 'name' field"})

        elif command == "update":

            name = message.get("name")
            completed = message.get("completed", False)
            if name is None:
                socket.send_json({"status": "error", "message": "Missing 'name' field"})

                continue

            # Check if task already exists
            updated = False
            for hobby in data:

                if hobby["name"] == name:
                    hobby["completed"] = completed

                    updated = True

                    break

            if not updated:
                data.append({"name": name, "completed": completed})

            save_data(data)

            action = "Updated" if updated else "Added"
            socket.send_json({
                "status": "success",
                "message": f"{action} hobby: {{'name': '{name}', 'completed': {completed}}}"})
        else:
            socket.send_json({"status": "error", "message": "Unknown command"})


if __name__ == "__main__":
    main()
