### Test Cases

Basic connection:
- A ServerBus can be created
- A ClientBus can connect to the ServerBus
- Another ClientBus can connect to the ServerBus
- A ClientBus can disconnect from the ServerBus, Server bus will not have error

Failing Connection
- A Client fails to connect to the Server -> Communication error Emergency stop announced. 

Required connections
- Server runs with no clients and no required critical clients -> no emergency stop
- Server runs with Client A, Client A is the only required critical client -> No emergency stop
- Server runs with Client A, Client B is the only required critial client -> Emergency stop
- Server runs with Client A and Client B, Client B is the only required Critial client -> No Emergency Stop
- Server runs with Client A, Client B is the only required client. Client B joins later -> Emergency stop ends when client B joins
- Server runs with Client A and Client B, Client A leaves later Client B is the only required Critial client -> No Emergency Stop
- Server runs with Client A and Client B, Client B leaves later Client B is the only required Critial client -> Emergency Stop Announced

Message Distribution
- Client A connects to server, Client A subscribes to a message type X, Client B sends a message with type X, A receives the message. 
- Client A connects to server, Client A subscribes to a message type X, Client B sends a message with type Y, A does not receive the message.