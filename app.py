from os import path

from pyJoules.energy_meter import measure_energy

from src.backend.engine import PowerConsumption

directory = path.dirname(path.realpath("__file__"))
app = PowerConsumption(root_path=directory)
app.start()
csv_handler = app.create_csv()


@measure_energy(handler=csv_handler)
def application():
    """Replace code inside with the script you want to run"""
    solution = 0
    for _ in range(50):
        solution = ((1 + 2 + 3) ** 2) ** 2
    print(solution)


for _ in range(100):
    application()

csv_handler.save_data()
app.parse_csv()
