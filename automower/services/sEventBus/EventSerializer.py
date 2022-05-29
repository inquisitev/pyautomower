

class EventSerializer:
    def serialize(self) -> str:
        raise NotImplementedError()

    def get_args(self) -> list:
        raise NotImplementedError()
