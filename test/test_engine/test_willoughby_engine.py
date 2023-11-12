import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        assert engine.needs_service()

    def test_needs_service_true(self):
        current_mileage = 80000
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        assert not engine.needs_service()

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        assert not engine.needs_service()

    def test_needs_service_false(self):
        current_mileage = 20000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        assert not engine.needs_service()