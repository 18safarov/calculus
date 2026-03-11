import webview
import sympy

frontend = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

  <title>Calculus</title>

  <link rel="icon" href="toti.ico">
  <link rel="stylesheet" href="normalize.css">
  <link rel="stylesheet" href="styles.css">

  <style>
    body { 
        font-family: sans-serif; 
        display: flex; 
        justify-content: center; 
        align-items: center;
        background-color: black; 
        height: 100vh;
        margin: 0; 
        overflow: hidden; /* - scrollbar */
    }

    .container {
        display: flex;
        flex-direction: row;
    }

    .calculator { 
        position: relative;
        background-color: #ecf0f1; 
        padding: 20px; 
        border-radius: 10px;
        width: 250px; 
    }

    .advanced-window.open + .calculator {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
    }

    #display { 
        width: 100%; 
        height: 50px; 
        margin-bottom: 15px; 
        font-size: 24px; 
        text-align: right; 
        border: 1px solid #bdc3c7; 
        border-radius: 5px; 
        box-sizing: border-box; 
        padding: 5px; 
    }

    #display::placeholder {
        color: #000000;
        opacity: 1;
    }

    .buttons { 
        display: grid; 
        grid-template-columns: 1fr 1fr 1fr 1fr; 
        gap: 10px; 
    }

    .transfer-function,
    .zero {
        grid-column: span 2;
    }

    .equal {
        grid-column: span 2;
        background-color: #e74c3c;
        color: white;
    }

    button { 
        padding: 15px 0; 
        font-size: 18px; 
        cursor: pointer; 
        border: none; 
        border-radius: 5px; 
        background-color: #bdc3c7; 
        transition: background-color 0.2s; 
    }

    button:hover { 
        background-color: #95a5a6; 
    }

    .operator { 
        background-color: #e74c3c; 
        color: white; 
    }

    .operator:hover { 
        background-color: #c0392b; 
    }

    .clear { 
        grid-column: span 2; 
        background-color: #3498db; 
        color: white; 
    }

    .clear:hover { 
        background-color: #2980b9; 
    }

    .opener {
        position: absolute;
        top: 3px;
        left: 10px;
        padding: 0;
        font-size: 15px;
        cursor: pointer;
        background: none;
        border: none;
    }

    .opener:hover {
        background: none;
    } 

    .advanced-window {
        background-color: #ecf0f1; 
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px; 
        width: 0;
        padding: 0;
        overflow: hidden;
        opacity: 0;
        transition: width 0.3s ease, padding 0.3s ease, opacity 0.3s ease;
        display: grid; 
        grid-template-columns: 1fr 1fr 1fr 1fr; 
        gap: 10px; 
        align-content: start;
    }

    .advanced-window.open {
        width: 250px;
        padding: 20px;
        opacity: 1;
    }
  </style>

</head>
<body>
  <div class="container">

    <div class="advanced-window">

      <button onclick="send('(')">(</button>
      <button onclick="send(')')">)</button>
      <button onclick="send('E')">e</button>
      <button onclick="send('pi')">π</button>

      <button onclick="send('sin(')">sin</button>
      <button onclick="send('cos(')">cos</button>
      <button onclick="send('tan(')">tan</button>
      <button onclick="send('cot(')">cot</button>

      <button onclick="send('log(')">log</button>
      <button onclick="send('ln(')">ln</button>

      <button onclick="send('!')">x!</button>
      <button onclick="send('sqrt(')">√</button>
      <button onclick="send('cbrt(')">∛</button>
      <button id="rootBtn" onclick="sendRootButton()">ʸ√x</button>
      
      <button onclick="send('**2')">x²</button>
      <button onclick="send('**')">xʸ</button>

      <button class="transfer-function" onclick="send('km_to_mi')">km → mi</button>
      <button class="transfer-function" onclick="send('mi_to_km')">mi → km</button>
      <button class="transfer-function" onclick="send('c_to_f')">°C → °F</button>
      <button class="transfer-function" onclick="send('f_to_c')">°F → °C</button>

    </div>

    <div class="calculator">

      <input type="text" id="display" placeholder="0">

      <button class="opener" id="openerId">&lt;&lt;</button>

      <div class="buttons">
        <button onclick="send('7')">7</button>
        <button onclick="send('8')">8</button>
        <button onclick="send('9')">9</button>
        <button class="operator" onclick="send('/')">÷</button>

        <button onclick="send('4')">4</button>
        <button onclick="send('5')">5</button>
        <button onclick="send('6')">6</button>
        <button class="operator" onclick="send('*')">×</button>

        <button onclick="send('1')">1</button>
        <button onclick="send('2')">2</button>
        <button onclick="send('3')">3</button>
        <button class="operator" onclick="send('-')">-</button>

        <button class="zero" onclick="send('0')">0</button>
        <button onclick="send('.')">.</button>
        <button class="operator" onclick="send('+')">+</button>

        <button class="clear" onclick="send('C')">C</button>
        <button class="equal" onclick="send('=')">=</button>
      </div>

    </div>

  </div>

  <script>
    // state for the ʸ√x button: cycle through two pieces each click
    const _rootStates = ['root(', ', '];
    let _rootStateIndex = 0;

    function send(button_value) {
    // reset helper state when starting over or calculating result
    if (button_value === '=' || button_value === 'C') {
        _rootStateIndex = 0;
        // restore original button label
        const rootbtn = document.getElementById('rootBtn');
        if (rootbtn) rootbtn.textContent = 'ʸ√x';
    }

    pywebview.api.button_pressed(button_value).then(function(result) {
        document.getElementById('display').value = result;
    });
    }

    // wrapper called by the root button in html
    function sendRootButton() {
    const token = _rootStates[_rootStateIndex];
    send(token);
    // update button text so user knows what next click will insert
    const rootbtn = document.getElementById('rootBtn');
    if (rootbtn) {
        // show next token or keep original symbol if clearing
        const next = _rootStates[(_rootStateIndex + 1) % _rootStates.length];
        rootbtn.textContent = next === 'root(' ? 'ʸ√x' : ',';
    }
    // advance index in circular fashion
    _rootStateIndex = (_rootStateIndex + 1) % _rootStates.length;
    }

    const opener = document.getElementById('openerId');

    // toggles advanced operations window and resizes webview
    opener.addEventListener('click', function() {
    pywebview.api.toggle_advanced().then(function(is_open) {
        document.querySelector('.advanced-window').classList.toggle('open', is_open);
    });
    if (opener.textContent === '<<') {
        opener.textContent = '>>';
    } else {
        opener.textContent = '<<';
    }
    });

    // allow pressing Enter when typing in the display to evaluate
    const display = document.getElementById('display');
    display.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        pywebview.api.evaluate(display.value).then(function(result) {
        display.value = result;
        });
        e.preventDefault();
    }
    });
  </script>

</body>
</html>
"""

class CalculatorAPI:
    def __init__(self):
        self.advanced_open = False  # flag for calculator state
        self.current_value = ""     # what see user on screen
        self.stored_value = None    # save number for next operation
        self.reset_next = False     # flag to reset current_value on next input

    # --- toggle advanced panel and resize window ---
    def toggle_advanced(self):
        self.advanced_open = not self.advanced_open
        if self.advanced_open:
            webview.windows[0].resize(894, 450)
        else:
            webview.windows[0].resize(300, 450)
        return self.advanced_open

    def button_pressed(self, char):

        match char:
            case 'C':
                self.current_value = ""
                return self.current_value
            
            # kilometer to mile
            case 'km_to_mi':
                try:
                    km = float(self.current_value)
                    mi = km * 0.62137119    
                    self.current_value = f"{mi:.13g}"
                except ValueError:
                    self.current_value = "Error"
                self.reset_next = True
                return self.current_value
            
            # mile to kilometer
            case 'mi_to_km':
                try:
                    mi = float(self.current_value)
                    km = mi * 1.609344
                    self.current_value = f"{km:.13g}"
                except ValueError:
                    self.current_value = "Error"
                self.reset_next = True
                return self.current_value
            
            # celsius to fahrenheit
            case 'c_to_f':
                try:
                    c = float(self.current_value)
                    f = c * 9/5 + 32
                    self.current_value = f"{f:.13g}"
                except ValueError:
                    self.current_value = "Error"
                self.reset_next = True
                return self.current_value
            
            # fahrenheit to celsius
            case 'f_to_c':
                try:
                    f = float(self.current_value)
                    c = (f - 32) * 5/9
                    self.current_value = f"{c:.13g}"
                except ValueError:
                    self.current_value = "Error"
                self.reset_next = True
                return self.current_value

            case '=':
                try:
                    expr = sympy.sympify(self.current_value)        # string → expression
                    self.current_value = str(sympy.N(expr))         # result
                except Exception:
                    self.current_value = "Error"
                self.reset_next = True

                try:
                    result = float(self.current_value)
                    if result.is_integer():
                        self.current_value = str(int(result))  # 5.0 -> 5
                    else:
                        self.current_value = f"{result:.13g}"  # limit to 13 significant digits
                except ValueError:
                    self.current_value = "Error"

                return self.current_value

        # or just add the button text to the string
        if self.reset_next:
            self.current_value = ""
            self.reset_next = False

        self.current_value += char
        
        return self.current_value   

    # called when the user edits the input and hits Enter
    def evaluate(self, text: str):
        self.current_value = text
        return self.button_pressed('=')

if __name__ == '__main__':
    api = CalculatorAPI()
    window = webview.create_window(
        title='Calculus', 
        html=frontend,
        js_api=api, 
        width=300, 
        height=450, 
        resizable=False,
        min_size=(300, 450)
    )
    webview.start(icon='toti.ico')