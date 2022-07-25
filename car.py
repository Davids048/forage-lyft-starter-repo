from abc import ABC, abstractmethod
import Servicable

class Car(Servicable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

