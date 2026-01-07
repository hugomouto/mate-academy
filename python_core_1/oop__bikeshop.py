from __future__ import annotations


class Bike:
    def __init__(self, brand: str, model: str, max_speed: int):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    @classmethod
    def from_dict(cls, bike_dict: dict) -> Bike:
        return cls(
            brand=bike_dict["brand"],
            model=bike_dict["model"],
            max_speed=bike_dict["max_speed"],
        )

class MountainBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand, model, max_speed)


class RoadBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand, model, max_speed)
