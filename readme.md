# Calculus

A desktop calculator application built with Python ([pywebview](https://pywebview.flowrl.com/) and [sympy](https://www.sympy.org/)). The UI is rendered using HTML/CSS/JS inside a native window, while all the math logic lives on the Python side.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, pywebview, sympy |
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
   pip install pywebview sympy
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

- Trigonometric functions (sin, cos, tan) - done
- Logarithms and exponents - done
- Square root and nth-root functions - done
- Power / factorial functions - done
- Constants (π, e) - done 
- Unit conversions (length, temperature) - done
- Custom function definitions - done
- Add keyboard support and show result by pressing Enter - done
- User interface improvements (themes, responsive design)