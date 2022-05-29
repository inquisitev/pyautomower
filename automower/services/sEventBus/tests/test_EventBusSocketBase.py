import sys
from unittest.mock import Mock, call
sys.path.append(".")
from automower.services.sEventBus.EventBusClient import EventBusSocketBase

def test_init():
  base = EventBusSocketBase(lambda x: print(x))
  assert base.should_end == False
  assert len(base.send_queue) == 0
  assert len(base.connection_list) == 0
  
def test_send():
  base = EventBusSocketBase(lambda x: print(x))
  base.send("message")
  
  assert len(base.send_queue) == 1
  
  mock = Mock()
  base.try_send(mock.send)
  mock.send.assert_called_with(b"message\\-|-/")

  assert len(base.send_queue) == 0
  
  
  base.send("message")
  base.try_send([mock.send1, mock.send2, mock.send3])
  
  mock.send1.assert_called_once_with(b"message\\-|-/")
  mock.send2.assert_called_once_with(b"message\\-|-/")
  mock.send3.assert_called_once_with(b"message\\-|-/")
  
def test_receive():
  mock = Mock()
  base = EventBusSocketBase(mock.recv_callback)
  base.receive(b"message\\-|-/message2\\-|-/message3")
  
  mock.assert_has_calls
  mock.recv_callback.assert_has_calls([call("message"), call("message2"), call("message3")])
  
def test_add_remove_connection():
  base = EventBusSocketBase(lambda x: print(x))
  base.add_connection(1)
  base.add_connection(2)
  base.add_connection(3)
  assert len(base.connection_list) == 3
  base.remove_connection(1)
  assert len(base.connection_list) == 2
  base.remove_connection(2)
  assert len(base.connection_list) == 1
  
def test_terminae():
  base = EventBusSocketBase(lambda x: print(x))
  assert base.should_end == False
  base.terminate()
  assert base.should_end == True