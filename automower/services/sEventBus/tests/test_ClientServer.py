import sys, threading, pytest,time
sys.path.append(".")
from automower.services.sEventBus.EventBusClient import EventBusClient
from automower.services.sEventBus.EventBusServer import EventBusServer

latest_client_recv = ""
latest_server_recv = ""

def set_latest_server(x):
  global latest_server_recv
  latest_server_recv = x
  
  
def set_latest_client(x):
  global latest_client_recv
  latest_client_recv = x

eBusServer = EventBusServer(set_latest_server)
x = threading.Thread(target=eBusServer._server_thread, daemon=True)
eBusClient = EventBusClient(set_latest_client)
y = threading.Thread(target=eBusClient._client_thread, daemon=True)

@pytest.fixture(autouse=True)
def run_around_tests():
  
    x.start()
    y.start()
    
    yield
    
    eBusClient.terminate()
    eBusServer.terminate()
    


def test_server():
  """
  cant really test the functionality between the two, but this just doese a quick test for any bad errors in the thread.
  """
  eBusServer.send("message")
  eBusClient.send("message")
  