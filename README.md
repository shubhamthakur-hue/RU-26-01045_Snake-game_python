# Snake Game (Python + Pygame)

A simple Snake game with a 10 × 10 grid, score tracking, food collection, collision detection, console test scenarios, and a graphical interface built with Pygame.

## Disclaimer

**This project is intended to run only with Python 3.13.** Use the Python 3.13 launcher commands below to install Pygame and run the program. Although Python 3.14 may also be installed on your computer, these instructions explicitly select Python 3.13.

## Requirements

- Windows with the Python launcher (`py`)
- Python 3.13 installed
- Pygame installed for Python 3.13

> Python 3.14 is assumed to be already installed. Installing Python 3.13 alongside Python 3.14 allows both versions to coexist; use `py -3.13` to select Python 3.13.

## 1. Check the currently selected Python version

Open **Command Prompt** or **PowerShell** and run:

```bat
py --version
```

This reports the default Python version selected by the launcher. It may show Python 3.14 if that is your default.

## 2. Install Python 3.13 alongside Python 3.14

1. Visit the official Python downloads page: <https://www.python.org/downloads/>.
2. Find the Python 3.13 release and download the Windows installer appropriate for your computer.
3. Run the installer. If available, select **Add Python to PATH**. You can leave Python 3.14 installed; the two versions can coexist.
4. Complete the installation.

If Python 3.13 is already installed, skip this installation step.

## 3. Verify that Python 3.13 is installed

Run:

```bat
py -3.13 --version
```

The output should identify Python 3.13, for example `Python 3.13.x`. If the launcher reports that the requested version cannot be found, check that Python 3.13 was installed successfully.

## 4. Install Pygame for Python 3.13

Run:

```bat
py -3.13 -m pip install pygame
```

This installs Pygame into the Python 3.13 environment. Using `py -3.13 -m pip` helps avoid accidentally installing Pygame only for Python 3.14.

If `pip` needs updating, you can run:

```bat
py -3.13 -m pip install --upgrade pip
```

Then repeat the Pygame installation command.

## 5. Save the game file

Save the supplied Python code in a file named `snake_game.py` (or use your chosen filename). Open Command Prompt or PowerShell and change to the directory containing that file. For example:

```bat
cd path\to\your\project
```

Replace `path\to\your\project` with the actual folder path.

## 6. Run the graphical game

Run the following command, replacing `file_name.py` with the actual name of your Python file:

```bat
py -3.13 file_name.py
```

For example, if the file is named `snake_game.py`:

```bat
py -3.13 snake_game.py
```

### Controls

- **Arrow keys** — change the snake's direction
- **Space** — restart after game over
- **Esc** — quit the game

The snake cannot reverse directly into the opposite direction. The game ends if the snake hits a wall or itself.

## 7. Run the console test scenarios

The program includes four console test scenarios. Run them with:

```bat
py -3.13 file_name.py --test
```

For example:

```bat
py -3.13 snake_game.py --test
```

This runs the built-in test routine instead of opening the graphical game.

## Quick command reference

Run these commands in order from Command Prompt or PowerShell:

```bat
py --version
py -3.13 --version
py -3.13 -m pip install pygame
py -3.13 file_name.py
```

To run the tests:

```bat
py -3.13 file_name.py --test
```

## Troubleshooting

- **Python 3.13 is not found:** Install Python 3.13 and then retry `py -3.13 --version`.
- **`No module named pygame`:** Install Pygame using `py -3.13 -m pip install pygame`.
- **Pygame installed for the wrong Python version:** Run the installation command with `py -3.13 -m pip` exactly as shown.
- **The game file cannot be found:** Change to the folder containing the file, or provide the full path to the file.
- **The window does not open:** Confirm that you ran the script without the `--test` argument and that Pygame installed successfully.

## Notes

The game starts with the snake at `(5, 5)` and initially places food at `(7, 5)`. It awards 10 points for each item of food eaten. The first food locations are fixed for the assignment's test behavior; later food locations are selected randomly.
