from abc import ABC
from tires.tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, tire_wear: list[float]) -> None:
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3