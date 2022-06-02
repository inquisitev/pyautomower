### Requirements

- [ ] Cap'n proto shall be used to serialize data. https://github.com/capnproto/pycapnp
- [ ] There shall be a single central node
- [ ] A service shall be able to connect to the central node
- [ ] A service shall be able to send a message to the central node
- [ ] A service shall be able to subscribe to a message type
- [ ] Cap'n proto structures shall be registered as a white-list of valid nodes. 
- [ ] Clients can disconnect from Server
- [ ] Multiple Clients can connect to the server
- [ ] Clients shall address claim
- [ ] If critical components fail to join, or the connection fails, the system shall emergency stop
- [ ] Clients shall send a unique Identity object, or they will be kicked. 
