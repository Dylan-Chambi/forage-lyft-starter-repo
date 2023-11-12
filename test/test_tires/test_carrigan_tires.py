import unittest
from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.4, 0.5, 0.9, 0.8]
        tires = CarriganTires(tire_wear)
        assert tires.needs_service()

    def test_needs_service_true(self):
        tire_wear = [0, 1, 0, 0]
        tires = CarriganTires(tire_wear)
        assert tires.needs_service()

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.1, 0.4, 0.8]
        tires = CarriganTires(tire_wear)
        assert not tires.needs_service()

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.8, 0.8, 0.8]
        tires = CarriganTires(tire_wear)
        assert not tires.needs_service()