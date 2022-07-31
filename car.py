from abc import ABC, abstractmethod
import Servicable

class Car(Servicable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def need_service(self):
        return self.engine.need_service() or self.battery.need_service()

