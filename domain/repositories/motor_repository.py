from abc import ABC, abstractmethod
from domain.entities.motor import Motor

class MotorRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Motor]:
        pass

    @abstractmethod
    def get_by_id(self, motor_id: int) -> Motor:
        pass

    @abstractmethod
    def add(self, motor: Motor) -> None:
        pass

    @abstractmethod
    def update(self, motor: Motor) -> None:
        pass

    @abstractmethod
    def delete(self, motor_id: int) -> None:
        pass
