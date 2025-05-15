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

class TestMotorEntityExtra(unittest.TestCase):

    def test_from_dict_success(self):
        data = {"id":1,"merk":"Yamaha","model":"NMAX","engine_type":"4-stroke"}
        m = Motor.from_dict(data)
        self.assertIsInstance(m, Motor)

    def test_from_dict_missing_key(self):
        data = {"id":2,"merk":"Honda","engine_type":"4-stroke"}  # key 'model' hilang
        with self.assertRaises(KeyError):
            Motor.from_dict(data)

    def test_from_dict_wrong_type(self):
        data = {"id":"tiga","merk":"Suzuki","model":"GSX","engine_type":"4-stroke"}
        with self.assertRaises(TypeError):
            Motor.from_dict(data)
