from abc import ABC, abstractmethod
from domain.entities.motor import Motor

class MotorRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Motor]:
        """Return a list of all motors."""
        pass # pragma: no cover

    @abstractmethod
    def get_by_id(self, motor_id: int) -> Motor:
        """Return a single motor by its ID."""
        pass # pragma: no cover

    @abstractmethod
    def add(self, motor: Motor) -> None: # pragma: no cover
        """Add a new motor."""
        pass # pragma: no cover

    @abstractmethod
    def update(self, motor: Motor) -> None:
        """Update an existing motor."""
        pass # pragma: no cover

    @abstractmethod
    def delete(self, motor_id: int) -> None:
        """Delete a motor by its ID."""
        pass # pragma: no cover
