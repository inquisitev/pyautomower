import sys
from unittest.mock import Mock, call
sys.path.append(".")
from automower.services.sEventBus.EventBus import EventBus
from automower.services.sEventBus.BaseEvent import BaseEvent

class EventBusServerFake:
  def __init__(self, on_rec):
    self.on_rec = on_rec

class FakeEvent(BaseEvent):

  def __init__(self, arg):
    self.arg = arg
    self.id = "FakeEvent"

  def serialize(self):
    return f"FakeEvent, {self.arg}"

  def parse( args):
    arg = args[1]
    return FakeEvent(arg)
  
  

def test_init():
  bus = EventBus(connector = EventBusServerFake)
  
def test_subscribe_unsubscribe():
  
  bus = EventBus(connector = EventBusServerFake)
  bus.register_event("IMU-Update", FakeEvent)
  mock = Mock()
  unsub_func = bus.subscribe("IMU-Update", mock.imu_update)
  assert "IMU-Update" in bus.subscriptions.keys()
  bus.notify("IMU-Update", "data")
  mock.imu_update.assert_called_once()
  
  unsub_func()
  
  bus.notify("IMU-Update", "data")
  mock.imu_update.assert_called_once()
  bus.register_event("IMU-Update", FakeEvent)
  mock.imu_update.assert_has_calls([call("data")])

def test_subscribe_unsubscribe_multiple():
  
  bus = EventBus(connector = EventBusServerFake)
  bus.register_event("IMU-Update", FakeEvent)
  mock = Mock()
  unsub_func1 = bus.subscribe("IMU-Update", mock.imu_update1)
  unsub_func2 = bus.subscribe("IMU-Update", mock.imu_update2)
  assert "IMU-Update" in bus.subscriptions.keys()
  bus.notify("IMU-Update", "data")
  mock.imu_update1.assert_called_once()
  
  unsub_func1()
  
  bus.notify("IMU-Update", "data")
  mock.imu_update1.assert_called_once()
  bus.register_event("IMU-Update", FakeEvent)
  mock.imu_update1.assert_has_calls([call("data")])
  mock.imu_update2.assert_has_calls([call("data"),call("data")])

def test_on_receive():
  bus = EventBus(connector = EventBusServerFake)
  bus.register_event("FakeEvent", FakeEvent)
  mock = Mock()
  unsub_func = bus.subscribe("FakeEvent", mock.fake_event)

  bus.on_receive("FakeEvent, 1")
  mock.fake_event.assert_called_once()
  arg = mock.fake_event.call_args.args[0]
  assert arg.serialize() == "FakeEvent, 1"


  bus.on_receive("NotAnEvent, 1,2,3,45,")
  mock.fake_event.assert_called_once()


  unsub_func = bus.subscribe("FakeEvent1", mock.fake_event1)

  bus.on_receive("FakeEvent1,1")
  mock.fake_event.assert_called_once()
  arg = mock.fake_event.call_args.args[0]
  assert arg.serialize() == "FakeEvent, 1"
  
  
  