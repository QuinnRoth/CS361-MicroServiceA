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

Mitigation Plan/Communication Contract:
   A. For which teammate did you implement “Microservice A”?
        Gabriel Lee
   B. What is the current status of the microservice? Hopefully, it’s done!
        Completed
   C. How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is        your microservice hosted somewhere? Etc.
        Get the code from GitHub and run it locally. 
   D. If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
        Just message me on Teams if you have any questions, and I will try to respond ASAP. 
   E. If your teammate cannot access/call your microservice, by when do they need to tell you? Provide a specific date to ensure they have a clear deadline.
        Please let me know as soon as you find out. The microservice works, so it will just be teaching you how to properly call it.
   F. Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to              discuss with your teammate?
        I don't think so.


UML SEQUENCE DIAGRAM:
https://github.com/QuinnRoth/CS361-MicroServiceA/blob/main/Sequence%20diagram-1.pdf
