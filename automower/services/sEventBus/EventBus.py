from automower.services.sEventBus.EventBusServer import EventBusServer
from automower.services.sEventBus.BaseEvent import BaseEvent
from typing import Type, Callable
class EventBus:
    """
    Connect to TCP and read/send events. 
    """
    
    def __init__(self, connector = EventBusServer, echo=False):
        self.connector = connector(self.on_receive)
        self.echo = echo
        self.subscriptions = {}
        self.event_types = {}
        
    def subscribe(self, event_type: str, on_receive: Callable[[Type[BaseEvent]], None]):
        if event_type not in self.event_types:
            return
        self.subscriptions[event_type].append(on_receive)
        def unsubscribe():
            self.subscriptions[event_type].remove(on_receive)
        return unsubscribe
    
    def register_event(self, eventType, event_class):
        self.event_types[eventType] = event_class
        self.subscriptions[eventType] = []
    
    def notify(self, event_type: str, event: Type[BaseEvent]):
        print("notifying")
        if event_type not in self.event_types:
            return
        if self.echo:
            self.send(event)
        else:
            for sub in self.subscriptions[event_type]:
                sub(event)
    
    def get_connector(self):
        return self.connector
    
    def on_receive(self, event_data):
        event_data = [e.strip() for e in event_data.split(',')]
        event_type = event_data[0]
        if event_type in self.event_types:
            event = self.event_types[event_type].parse(event_data)
            self.notify(event_type, event)
            return event
    
    def send(self, event: Type[BaseEvent]):
        self.connector.send(event.serialize())