from abc import ABC
from battery.battery import Battery
from datetime import date


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 730