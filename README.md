# Growing Code

Python fundamentals through community garden data.

Each exercise is one function that reads input and prints a result. The series starts with a print statement and ends with a typed function that formats seed inventory. There is no program entry point in the exercise files.

Requires Python 3.10+.

## Layout

```
ex0/ft_hello_garden.py
ex1/ft_garden_name.py
ex2/ft_plot_area.py
ex3/ft_harvest_total.py
ex4/ft_plant_age.py
ex5/ft_water_reminder.py
ex6/ft_count_harvest_iterative.py
ex6/ft_count_harvest_recursive.py
ex7/ft_seed_inventory.py
main.py
```

`main.py` is a test helper. It imports a function by filename and runs it. Exercise 7 is called with sample arguments; the others wait for keyboard input.

The helper looks for each module on the current path, so run it from the exercise directory (or copy that exercise’s file next to `main.py`):

```bash
cd ex2
cp ../main.py .
python3 main.py
```

Choose `0`–`7` to test one exercise, or `a` to run them all.

## Exercises

| Exercise | Function | What it does |
| --- | --- | --- |
| 0 | `ft_hello_garden` | Prints `Hello, Garden Community!` |
| 1 | `ft_garden_name` | Asks for a garden name and prints it with a fixed status line |
| 2 | `ft_plot_area` | Reads length and width, prints the rectangular area |
| 3 | `ft_harvest_total` | Adds three daily harvest weights |
| 4 | `ft_plant_age` | Ready to harvest if the age is strictly more than 60 days |
| 5 | `ft_water_reminder` | Water the plants if more than 2 days have passed |
| 6 | `ft_count_harvest_iterative` / `ft_count_harvest_recursive` | Count from day 1 to the given day, then print `Harvest time!` |
| 7 | `ft_seed_inventory` | Format a seed type, quantity, and unit (`packets`, `grams`, or `area`) |

Exercise 7 must use this signature:

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

Unknown units print `Unknown unit type`. Type hints are optional in exercises 0–6 and required in exercise 7 (`mypy`). Style is checked with `flake8`.
