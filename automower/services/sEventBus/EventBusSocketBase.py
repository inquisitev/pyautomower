import socket

PORT = 5001 # TODO: read environemnt var
ADDRESS = socket.gethostname() # TODO: read environemnt var
RECEIVE_BUFFER_SIZE = 4096 # TODO: does this need to be so big? or can it be bigger
MESSAGE_TERMINATOR = '\\-|-/' #trying to use something that wont be acceidetally used elsewhere
LOBBY_MAX_SIZE = 10 #trying to use something that wont be acceidetally used elsewhere

class EventBusSocketBase:
  
  def __init__(self, receive_callback):
    
    self.receive_callback = receive_callback
    self.should_end = False
    self.send_queue = []
    self.connection_list = []
    
  def send(self, message):
    self.send_queue.append(self.encode_message(message))
  
  def receive(self, message):
    for decoded_message in self.decode_message(message):
      self.receive_callback(decoded_message)
  
  def encode_message(self, message):
    return f"{message}{MESSAGE_TERMINATOR}".encode()
  
  def decode_message(self, message):
    messages = message.decode().split(MESSAGE_TERMINATOR)
    if '' in messages:
      messages.remove('')
    return messages
    
  def terminate(self):
    self.should_end = True
  
  def add_connection(self, connection):
    self.connection_list.append(connection)
  
  def remove_connection(self, connection):
    self.connection_list.remove(connection)
    
  def try_send(self, notifiers):
    while len(self.send_queue) > 0:
      if isinstance(notifiers, list):
        msg = self.send_queue.pop()
        for notifier in notifiers:
          notifier(msg)
      else:
          notifiers(self.send_queue.pop())