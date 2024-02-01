from typing import TypeVar, Generic
from dataclasses import dataclass


@dataclass(kw_only=True)
class Vehicle:
    name: str

    def display(self) -> None:
        print(f"Vehicle Name: {self.name}")


class Boat(Vehicle):
    def display(self) -> None:
        print(f"Boat Name: {self.name}")


class Plane(Vehicle):
    def display(self) -> None:
        print(f"Plane Name: {self.name}")


class Car(Vehicle):
    def display(self) -> None:
        print(f"Car Name: {self.name}")


class Registry[T: (Car, Boat)]:
    def __init__(self) -> None:
        self.vehicles: list[T] = []

    def add(self, v: T) -> None:
        self.vehicles.append(v)

    def display_all(self) -> None:
        for v in self.vehicles:
            v.display()


registry = Registry[Car, Boat]()
registry.add(Car(name="Jeep"))
registry.add(Boat(name="Yacht"))
registry.add()
registry.display_all()
