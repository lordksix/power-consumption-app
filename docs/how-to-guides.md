This part of the project documentation focuses on a **problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code provided in this project.

## How is it structured?

Clone the code from this [GitHub repository](https://github.com/lordksix/power-consumption-app)
 on your preferred directory and following structure will be downloaded:

    power-consumption-app/
    ├───app.py
    ├── docs/
    │   |── explanation.md
    │   |── index.md
    │   ├── how-to-guides.md
    |   └── reference.md
    └── src/
        │
        ├── backend/
        │   ├── bash.py
        │   ├── engine.py
        │   └── __init__.py
        └── pyproject.toml

## How to start

After cloning the project run the following command to install the necessary dependencies.

```sh
    cd power-consumption-app
    pip install power-consumption
```

## How to configure

In the `app.py` file you will find the follow function:

    @measure_energy(handler=csv_handler)
    def application():
        """Replace code inside with the script you want to run"""
        solution = 0
        for _ in range(50):
            solution = ((1 + 2 + 3) ** 2) ** 2
        print(solution)

Replace the code inside the function block with your prefer code.

## How to use it

Run

```sh
    python3 app.py
```

The console inside the function application() will run 100 times and the results will be saved in a file
called `result.csv` or the name you have chosen.

First column: timestamp -> Timestamp of the start of the iteration
Second column: tag -> Name of the function running
Third column: duration -> Duration of the iteration
Forth column: package_0 -> Total energy in uJ consumed by CPU during the iteration
Fifth column: nvidia_gpu_0 -> Total energy in uJ consumed by GPU during the iteration

## How to read the final result

The application will print in the console:
- How much energy was consume in total
- Total duration of all iterations
- How much power the application consumes
