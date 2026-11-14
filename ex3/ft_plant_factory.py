class Plant:
    __slots__ = ("name", "height", "plant_age", "initial_age")

    def __init__(self, name: str,plant_age: int,height: float) -> None:
        self.name = name
        self.plant_age = plant_age
        self.height = height
        self.initial_age = self.plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self, amount: float) -> None:
        self.height = self.height + amount
        self.height = round(self.height)

    def age(self) -> None:
        self.plant_age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = {Plant("Rose", 25, 30), Plant("Oak",height = 200.0,plant_age = 365), Plant("Cactus", height = 5.0, plant_age = 90), Plant("Sunflower", height = 80.0, plant_age = 45),Plant("Fern", height = 15.0, plant_age = 120)}
    for plant in plants:
        print(f"Created: ", end = "")
        plant.show()
