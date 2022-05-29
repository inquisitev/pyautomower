
# https://gist.github.com/logasja/97bddeb84879b30519efb0c66b4db159 - thanks jacob
import socket, select
from automower.services.sEventBus.EventBusSocketBase import EventBusSocketBase, PORT, ADDRESS, RECEIVE_BUFFER_SIZE


class EventBusServer(EventBusSocketBase):
  
  def __init__(self, receive_callback):
    super().__init__(receive_callback)
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind((ADDRESS, PORT))
    self.server_socket.listen(10) # up to 10 clients can listen simutaneously
    self.add_connection(self.server_socket)    
    
  def _server_thread(self):
    while not self.should_end:
      read_sockets, write_sockets, error_sockets = select.select(self.connection_list, self.connection_list, [])
      
      for sock in read_sockets:
        if sock == self.server_socket:
          new_socket, addr = self.server_socket.accept()
          self.add_connection(new_socket)
        else:
          try:
            data = sock.recv(RECEIVE_BUFFER_SIZE)
            self.receive(data)
          except:
            sock.close()
            self.remove_connection(sock)
        
      self.try_send([sock.send for sock in write_sockets])
      
            
            