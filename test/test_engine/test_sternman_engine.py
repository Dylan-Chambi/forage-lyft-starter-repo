import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        assert engine.needs_service()


    def test_needs_service_true(self):
        current_mileage = 50000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        assert engine.needs_service()

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        assert not engine.needs_service()

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        assert not engine.needs_service()
