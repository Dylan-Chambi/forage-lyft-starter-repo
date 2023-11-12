import unittest
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 0.5, 0.9, 0.8]
        tires = OctoprimeTires(tire_wear)
        assert tires.needs_service()

    def test_needs_service_true(self):
        tire_wear = [1, 1, 0.5, 0.5]
        tires = OctoprimeTires(tire_wear)
        assert tires.needs_service()

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.1, 0.4, 0.8]
        tires = OctoprimeTires(tire_wear)
        assert not tires.needs_service()

    def test_needs_service_false(self):
        tire_wear = [1, 1, 0.4, 0.5]
        tires = OctoprimeTires(tire_wear)
        assert not tires.needs_service()