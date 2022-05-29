import socket, os
from automower.services.sEventBus.EventBusSocketBase import EventBusSocketBase, PORT, ADDRESS, RECEIVE_BUFFER_SIZE

class EventBusClient(EventBusSocketBase):
  
  def __init__(self, receive_callback):
    super().__init__(receive_callback)
    
    self.client_socket = socket.socket()  # instantiate
    self.client_socket.connect((ADDRESS, PORT))  # connect to the server
    self.add_connection(self.client_socket)

  def _client_thread(self):
    while not self.should_end:
      self.try_send(self.client_socket.send) # send message
      data = self.client_socket.recv(RECEIVE_BUFFER_SIZE).decode()  # receive response
      self.receive_callback(data)
      
      
    