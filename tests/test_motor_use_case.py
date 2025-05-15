import unittest
from domain.entities.motor import Motor
from use_cases.motor_use_case import MotorUseCase

class DummyRepo:
    def __init__(self):
        self.data = []

    def get_all(self):
        return self.data

    def get_by_id(self, id):
        for m in self.data:
            if m.id == id:
                return m
        raise ValueError()

    def add(self, m):
        self.data.append(m)

    def update(self, m):
        for i, x in enumerate(self.data):
            if x.id == m.id:
                self.data[i] = m
                return
        raise ValueError()

    def delete(self, id):
        for i, m in enumerate(self.data):
            if m.id == id:
                del self.data[i]
                return
        raise ValueError()

class TestMotorUseCase(unittest.TestCase):

    def setUp(self):
        self.repo = DummyRepo()
        self.use_case = MotorUseCase(self.repo)

    def test_create_motor(self):
        self.use_case.create_motor(1, "Yamaha", "Aerox", "4-stroke")
        self.assertEqual(len(self.repo.data), 1)

    def test_update_motor_success(self):
        self.use_case.create_motor(2, "Honda", "PCX", "4-stroke")
        self.use_case.update_motor(2, "Honda", "PCX", "eSP+")
        self.assertEqual(self.repo.data[0].engine_type, "eSP+")

    def test_delete_motor_success(self):
        self.use_case.create_motor(3, "Suzuki", "GSX", "DOHC")
        self.use_case.delete_motor(3)
        self.assertEqual(len(self.repo.data), 0)

class TestMotorUseCaseGet(unittest.TestCase):
    def setUp(self):
        self.repo = DummyRepo()
        self.uc = MotorUseCase(self.repo)

    def test_get_motor_success(self):
        self.repo.add(Motor(1,"Yamaha","NMAX","4-stroke"))
        m = self.uc.get_motor(1)
        self.assertEqual(m.model, "NMAX")

    def test_get_motor_not_found(self):
        with self.assertRaises(ValueError):
            self.uc.get_motor(99)

    def test_get_motor_invalid_arg(self):
        with self.assertRaises(TypeError):
            self.uc.get_motor("satu")
