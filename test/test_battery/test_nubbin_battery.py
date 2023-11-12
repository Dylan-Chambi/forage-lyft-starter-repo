import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-11-12")
        last_service_date = date.fromisoformat("2018-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        assert battery.needs_service()

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-11-12")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        assert not battery.needs_service()