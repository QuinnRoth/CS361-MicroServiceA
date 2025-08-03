Prerequisites:
  Install Python Packages
  The client must connect to localhost:8888
  The message must be in the format: {command: "<command>", "name": <hobby>, "completed": <status>}
  The name and completed arguments may remain empty depending on the command
  <status> is a boolean (True or False)
  Send using 'socket.send_json(message)'
  Save response using socket.recv_json()
  
Request hobby by name:
    The 'message' must follow this format: {command: "get_by_name", "name": <hobby>}
    The server will respond with {"status": "<status>", "hobbies": matching}
    Where matching is the hobbies data in JSON format. This may be multiple if there are duplicate hobbies.
    <status> signals whether or not the command was successful.

Request all hobbies:
    The 'message' must follow this format: {command: "get_all"}
    The server will respond with {"status": "<status>", "hobbies": data}
    Where data is a JSON-formatted list of all hobbies currently saved in the JSON file.
    <status> signals whether or not the command was successful.

Update or Add a hobby:
    The 'message' must follow this format: {command: "update", "name": <hobby>, "completed": <status>}
    The server will respond with {"status": "<status>", "message": f"{action} hobby: {{'name': '{name}', 'completed': {completed}}}"}
    <status> signals whether or not the command was successful.
    action will be either added or updated
    
Receiving data from the server:
  response.get(<key>) to get the value/data paired with the key

Example call:
    message = {"command": "update", "name": hobby, "completed": status}
    socket.send_json(message)
    response = socket.recv_json()

UML SEQUENCE DIAGRAM:
https://github.com/QuinnRoth/CS361-MicroServiceA/blob/main/Sequence%20diagram-1.pdf
