import unittest
from domain.entities.motor import Motor

class TestMotorEntity(unittest.TestCase):

    def test_to_dict_output(self):
        motor = Motor(1, "Yamaha", "NMAX", "4-stroke")
        expected = {
            "id": 1,
            "merk": "Yamaha",
            "model": "NMAX",
            "engine_type": "4-stroke"
        }
        self.assertEqual(motor.to_dict(), expected)

    def test_from_dict_valid(self):
        data = {
            "id": 2,
            "merk": "Honda",
            "model": "CBR",
            "engine_type": "4-stroke"
        }
        motor = Motor.from_dict(data)
        self.assertEqual(motor.merk, "Honda")
        self.assertEqual(motor.model, "CBR")

    def test_object_integrity(self):
        motor = Motor(3, "Suzuki", "GSX", "4-stroke")
        self.assertEqual(motor.id, 3)
        self.assertEqual(motor.engine_type, "4-stroke")
