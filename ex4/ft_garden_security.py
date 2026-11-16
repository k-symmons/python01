class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, amount: float) -> None:
        self.set_height(self._height + amount)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height():.0f}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    if not rose.set_height(-1):
        print("Height update rejected")
    if not rose.set_age(-1):
        print("Age update rejected")
    print("Current state: ", end="")
    rose.show()
