from automower.services.sEventBus.EventBusServer import EventBusServer

class EventBus:
    """
    Connect to TCP and read/send events. 
    """
    
    def __init__(self, connector = EventBusServer):
        self.connector = connector(self.on_receive)
        self.subscriptions = {}
        self.event_types = {}
        
    def subscribe(self, event_type, on_receive):
        
        self.subscriptions[event_type].append(on_receive)
        def unsubscribe():
            self.subscriptions[event_type].remove(on_receive)
        return unsubscribe
    
    def register_event(self, eventType, serializer, parser):
        self.event_types[eventType] = (serializer, parser)
        self.subscriptions[eventType] = []
    
    def notify(self, event_type, event):
        for sub in self.subscriptions[event_type]:
            sub(event)
    
    def get_connector(self):
        return self.connector
    
    def on_receive(self, event_data):
        # check the type of message
        # parse the message into an event
        # notify all events that have subscribed to that message 
        pass
    
    def send(self, event):
        self.connector.send(event)