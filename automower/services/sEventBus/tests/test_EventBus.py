import sys
from unittest.mock import Mock, call
sys.path.append(".")
from automower.services.sEventBus.EventBus import EventBus

class EventBusServerFake:
  def __init__(self, on_rec):
    self.on_rec = on_rec

def test_init():
  bus = EventBus(connector = EventBusServerFake)
  
def test_subscribe_unsubscribe():
  
  bus = EventBus(connector = EventBusServerFake)
  bus.register_event("IMU-Update", None, None)
  mock = Mock()
  unsub_func = bus.subscribe("IMU-Update", mock.imu_update)
  assert "IMU-Update" in bus.subscriptions.keys()
  bus.notify("IMU-Update", "data")
  mock.imu_update.assert_called_once()
  
  unsub_func()
  
  bus.notify("IMU-Update", "data")
  mock.imu_update.assert_called_once()
  
  
  bus.register_event("IMU-Update", None, None)
  assert len(mock.imu_update.calls) == 2
  
  
  