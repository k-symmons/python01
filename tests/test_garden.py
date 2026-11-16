from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]


def check() -> None:
    output = StringIO()
    with redirect_stdout(output):
        security = runpy.run_path(str(ROOT / "ex4/ft_garden_security.py"))
        types = runpy.run_path(str(ROOT / "ex5/ft_plant_types.py"))
        analytics = runpy.run_path(str(ROOT / "ex6/ft_garden_analytics.py"))
    assert output.getvalue() == ""

    with redirect_stdout(output):
        plant = security["Plant"]("Rose", -2.0, -1)
        assert (plant.get_height(), plant.get_age()) == (0.0, 0)
        assert plant.set_height(1.25)
        assert plant.set_age(3)
        assert not plant.set_height(-1.0)
        assert not plant.set_age(-1)
        plant.grow(-2.0)
    assert (plant.get_height(), plant.get_age()) == (1.25, 3)

    tomato = types["Vegetable"]("Tomato", 5.0, 10, "April")
    tomato.grow(0.25)
    assert tomato.nutritional_value == 1
    tomato.age()
    assert (tomato.get_height(), tomato.get_age()) == (5.25, 11)
    assert tomato.nutritional_value == 2

    assert not analytics["Plant"].is_older_than_year(365)
    assert analytics["Plant"].is_older_than_year(366)
    seed = analytics["Seed"]("Sunflower", 80.0, 45, "yellow")
    oak = analytics["Tree"]("Oak", 200.0, 365, 5.0)
    unknown = analytics["Plant"].anonymous()
    output = StringIO()
    with redirect_stdout(output):
        seed.show()
        seed.grow(0.25)
        seed.age()
        seed.bloom(42)
        seed.show()
        analytics["show_statistics"](seed)
        oak.produce_shade()
        oak.produce_shade()
        analytics["show_statistics"](oak)
        unknown.show()
        analytics["show_statistics"](unknown)
    result = output.getvalue()
    assert "Sunflower: 80.2cm, 46 days old" in result
    assert "Seeds: 42" in result
    assert "Stats: 1 grow, 1 age, 2 show" in result
    assert "2 shade" in result
    assert "Unknown plant: 0.0cm, 0 days old" in result
    assert "Stats: 0 grow, 0 age, 1 show" in result


if __name__ == "__main__":
    check()
