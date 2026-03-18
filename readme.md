# Calculus

A desktop calculator application built with Python ([pywebview](https://pywebview.flowrl.com/) and [sympy](https://www.sympy.org/)). The UI is rendered using HTML/CSS/JS inside a native window, while all the math logic lives on the Python side.

Fully portable: **no installation required!**

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, pywebview, sympy |
| Frontend | HTML, CSS, JavaScript |
| Bridge | pywebview JS API (`pywebview.api`) |

## Features

- **Standard & Advanced Math:** Trigonometric functions (sin, cos, tan), logarithms, square/nth roots, and factorials etc.
- **Smart Constants:** Built-in support for constants like π and e.
- **Unit Conversions:** Easily convert length and temperature.
- **Keyboard Support:** Fully functional keyboard inputs (Press `Enter` to calculate).

## Download & Run (For Users)

You don't need to install Python or any dependencies to use Calculus. Just download the ready-to-use file for your operating system from the [Latest Release](https://github.com/safarsin/calculus/releases/latest) page!

## Development Setup (For Developers)

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/safarsin/calculus.git
   ```
2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install pywebview sympy
   ```

4. **Run the app:**
   ```bash
   python main.py
   ```

## Project Structure

```
calculus/
├──  main.py          # Python backend — calculator logic & webview window
├──  index.html        # Calculator UI
├──  styles.css        # Styling
├──  normalize.css    # CSS reset
└──  transmitter.js   # JS bridge — sends button presses to Python
```
