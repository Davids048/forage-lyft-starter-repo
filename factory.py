from datetime import date

import Battery_folder.SpindlerBattery
import Battery_folder.NubbinBattery
import Engine_folder.capulet_engine
import Engine_folder.willoughby_engine
import Engine_folder.sternman_engine
from car import Car


class CarFactory:
    @staticmethod
    def create_calliope( current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        # create a Capulet engine
        engine = Engine_folder.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)

        # create a Spindler battery
        battery = Battery_folder.SpindlerBattery.SpindlerBattery(last_service_date, current_date)

        # create a car
        car = Car(engine,battery)

        return car

    @staticmethod
    def create_glissade( current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        # will engine
        engine = Engine_folder.willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)

        # create a Spindler battery
        battery = Battery_folder.SpindlerBattery.SpindlerBattery(last_service_date, current_date)

        # create a car
        car = Car(engine,battery)

        return car

    @staticmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        # sternman
        engine = Engine_folder.sternman_engine.SternmanEngine(warning_light_on)

        # create a Spindler battery
        battery = Battery_folder.SpindlerBattery.SpindlerBattery(last_service_date, current_date)

        # create a car
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        # will
        engine = Engine_folder.willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)

        # nubbin
        battery = Battery_folder.NubbinBattery.NubbinBattery(last_service_date,current_date)

        # create a car
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        # capulet
        engine = Engine_folder.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)

        # nubbin
        battery = Battery_folder.NubbinBattery.NubbinBattery(last_service_date, current_date)

        # create a car
        car = Car(engine, battery)

        return car



