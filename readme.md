# Calculus

A simple desktop calculator application built with Python and [pywebview](https://pywebview.flowrl.com/). The UI is rendered using HTML/CSS/JS inside a native window, while all the math logic lives on the Python side.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, pywebview |
| Frontend | HTML, CSS, JavaScript |
| Bridge | pywebview JS API (`pywebview.api`) |

## Getting Started

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install pywebview
   ```
4. **Run the app:**
   ```bash
   python main.py
   ```

## Project Structure

```
main.py          # Python backend — calculator logic & webview window
index.html       # Calculator UI
styles.css       # Styling
normalize.css    # CSS reset
transmitter.js   # JS bridge — sends button presses to Python
```

## Roadmap

In future releases the plan is to introduce an **Advanced Functions** extension, which will include:

- Trigonometric functions (sin, cos, tan)
- Logarithms and exponents
- Square root and nth-root
- Power / factorial
- Constants (π, e) etc.