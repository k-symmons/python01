class Plant:
    __slots__ = ("name", "height", "plant_age")

    def __init__(self, name: str,plant_age: int,height: float) -> None:
        self.name = name
        self.plant_age = plant_age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self, amount: float) -> None:
        self.height = round(self.height + amount,1)

    def age(self) -> None:
        self.plant_age += 1

if __name__ == "__main__":

    print("=== Garden Plant Growth ===")
    initial_height = 25
    flower = Plant("Rose", 30, initial_height)
    flower.show()
    i = 1
    while(i <= 7):
        print(f"=== Day {i} ===")
        flower.grow(0.8)
        flower.age()
        flower.show()
        i += 1
    print(f"Growth this week: {round(flower.height - initial_height, 2)}cm")
