import json
import os
from domain.entities.motor import Motor
from domain.repositories.motor_repository import MotorRepository

class MotorRepositoryJSON(MotorRepository):
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump([], f)

    def _load_data(self):
        with open(self.filepath, 'r') as f:
            return [Motor.from_dict(item) for item in json.load(f)]

    def _save_data(self, motors):
        with open(self.filepath, 'w') as f:
            json.dump([motor.to_dict() for motor in motors], f, indent=2)

    def get_all(self) -> list[Motor]:
        return self._load_data()

    def get_by_id(self, motor_id: int) -> Motor:
        motors = self._load_data()
        for m in motors:
            if m.id == motor_id:
                return m
        raise ValueError("Motor not found")

    def add(self, motor: Motor) -> None:
        motors = self._load_data()
        motors.append(motor)
        self._save_data(motors)

    def update(self, motor: Motor) -> None:
        motors = self._load_data()
        for i, m in enumerate(motors):
            if m.id == motor.id:
                motors[i] = motor
                self._save_data(motors)
                return
        raise ValueError("Motor not found")

    def delete(self, motor_id: int) -> None:
        motors = self._load_data()
        new_motors = [m for m in motors if m.id != motor_id]
        if len(new_motors) == len(motors):
            raise ValueError("Motor not found")
        self._save_data(new_motors)
