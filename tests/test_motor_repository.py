import unittest
import os
from data.motor_repository_json import MotorRepositoryJSON
from domain.entities.motor import Motor

TEST_JSON_FILE = "data/test_motors.json"

class TestMotorRepositoryJSON(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_JSON_FILE):
            os.remove(TEST_JSON_FILE)
        self.repo = MotorRepositoryJSON(TEST_JSON_FILE)

    def tearDown(self):
        if os.path.exists(TEST_JSON_FILE):
            os.remove(TEST_JSON_FILE)

    def test_add_and_get_all(self):
        motor = Motor(1, "Yamaha", "NMAX", "4-stroke")
        self.repo.add(motor)
        all_motors = self.repo.get_all()
        self.assertEqual(len(all_motors), 1)
        self.assertEqual(all_motors[0].merk, "Yamaha")

    def test_get_by_id_valid(self):
        motor = Motor(2, "Honda", "CBR", "4-stroke")
        self.repo.add(motor)
        result = self.repo.get_by_id(2)
        self.assertEqual(result.model, "CBR")

    def test_update_motor(self):
        self.repo.add(Motor(3, "Suzuki", "GSX", "DOHC"))
        self.repo.update(Motor(3, "Suzuki", "GSX-R", "DOHC"))
        updated = self.repo.get_by_id(3)
        self.assertEqual(updated.model, "GSX-R")

class TestMotorRepositoryDelete(unittest.TestCase):
    def setUp(self):
        # pastikan file JSON baru
        if os.path.exists(TEST_JSON_FILE): os.remove(TEST_JSON_FILE)
        self.repo = MotorRepositoryJSON(TEST_JSON_FILE)

    def tearDown(self):
        if os.path.exists(TEST_JSON_FILE): os.remove(TEST_JSON_FILE)

    def test_delete_success(self):
        self.repo.add(Motor(1,"Yamaha","NMAX","4-stroke"))
        self.repo.delete(1)
        self.assertEqual(self.repo.get_all(), [])

    def test_delete_not_found(self):
        with self.assertRaises(ValueError):
            self.repo.delete(2)

    def test_delete_empty_file(self):
        # file baru, belum ada data
        with self.assertRaises(ValueError):
            self.repo.delete(1)
