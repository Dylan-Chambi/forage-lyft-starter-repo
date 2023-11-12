import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-11-12")
        last_service_date = date.fromisoformat("2020-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        assert battery.needs_service()

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-11-12")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        assert not battery.needs_service()