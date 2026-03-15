# main.py
from typing import Optional, Union

class Vehicle:

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0) -> None:

        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year}, mileage={self._mileage})"

    def drive(self, distance: float) -> str:
        self._mileage += distance
        return f"Транспортное средство проехало {distance} км. Общий пробег: {self._mileage} км"

    def get_mileage(self) -> float:

        return self._mileage


class Car(Vehicle):

    def __init__(self, brand: str, model: str, year: int,
                 body_type: str, doors_count: int, mileage: float = 0) -> None:

        super().__init__(brand, model, year, mileage)
        self.body_type = body_type
        self.doors_count = doors_count

    def __str__(self) -> str:

        return f"Легковой автомобиль: {self.brand} {self.model} ({self.year}), кузов: {self.body_type}"

    def __repr__(self) -> str:

        return (f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"body_type='{self.body_type}', doors_count={self.doors_count}, mileage={self._mileage})")

    def drive(self, distance: float, passengers: Optional[int] = 1) -> str:

        if passengers > 5:
            return "Ошибка: слишком много пассажиров для легкового автомобиля"

        self._mileage += distance
        return (f"Легковой автомобиль проехал {distance} км с {passengers} пассажиром(ами). "
                f"Общий пробег: {self._mileage} км")

    def honk(self) -> str:

        return "Бип-бип!"


class Truck(Vehicle):


    def __init__(self, brand: str, model: str, year: int,
                 capacity: float, mileage: float = 0) -> None:

        super().__init__(brand, model, year, mileage)
        self.capacity = capacity
        self._current_load = 0.0

    def __str__(self) -> str:

        return f"Грузовик: {self.brand} {self.model} ({self.year}), грузоподъёмность: {self.capacity}т"

    def __repr__(self) -> str:

        return (f"Truck(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"capacity={self.capacity}, mileage={self._mileage})")

    def drive(self, distance: float) -> str:

        if self._current_load == 0:
            return "Предупреждение: грузовик едет порожняком!"

        self._mileage += distance
        return (f"Грузовик проехал {distance} км с грузом {self._current_load}т. "
                f"Общий пробег: {self._mileage} км")

    def load(self, weight: float) -> str:

        if self._current_load + weight > self.capacity:
            return f"Ошибка: превышение грузоподъёмности! Максимум {self.capacity}т"

        self._current_load += weight
        return f"Груз загружен. Текущая загрузка: {self._current_load}т"

    def unload(self, weight: float) -> str:

        if weight > self._current_load:
            return f"Ошибка: нельзя снять больше, чем загружено (текущий груз: {self._current_load}т)"

        self._current_load -= weight
        return f"Груз снят. Текущая загрузка: {self._current_load}т"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, "sedan", 4, 15000)
    truck = Truck("Volvo", "FH16", 2020, 20, 50000)

    print(car)
    print(repr(car))
    print(car.drive(100, 3))
    print(car.honk())

    print("\n" + "=" * 50 + "\n")

    print(truck)
    print(repr(truck))
    print(truck.load(15))
    print(truck.drive(200))
    print(truck.unload(10))
