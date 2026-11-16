class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self, amount: float) -> None:
        self.height += amount

    def age(self) -> None:
        self.days_old += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    starting_height = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()
    print(f"Growth this week: {rose.height - starting_height:.1f}cm")
