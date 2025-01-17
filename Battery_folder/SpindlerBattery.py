from battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self):
        date_battery_should_get_service_by = add_years_to_date(self.last_service_date, 2)
        if date_battery_should_get_service_by < self.current_date:
            return True
        else:
            return False
