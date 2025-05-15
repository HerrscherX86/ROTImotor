from domain.entities.motor import Motor
from domain.repositories.motor_repository import MotorRepository

class MotorUseCase:
    def __init__(self, repo: MotorRepository):
        self.repo = repo

    def list_motors(self):
        return self.repo.get_all()

    def get_motor(self, motor_id: int):
        if not isinstance(motor_id, int):
            raise TypeError("motor_id must be int")
        return self.repo.get_by_id(motor_id)

    def create_motor(self, id: int, merk: str, model: str, engine_type: str):
        motor = Motor(id, merk, model, engine_type)
        self.repo.add(motor)

    def update_motor(self, id: int, merk: str, model: str, engine_type: str):
        motor = Motor(id, merk, model, engine_type)
        self.repo.update(motor)

    def delete_motor(self, motor_id: int):
        if not isinstance(motor_id, int):
            raise TypeError("motor_id must be int")
        self.repo.delete(motor_id)

