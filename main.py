import webview
import sympy

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
        if char == 'C':
            self.current_value = ""
            return self.current_value

        if char == '=':
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
                pass

            return self.current_value

        # or just add the button text to the string
        if self.reset_next:
            self.current_value = ""
            self.reset_next = False

        self.current_value += char
        
        return self.current_value   

if __name__ == '__main__':
    api = CalculatorAPI()
    window = webview.create_window(
        title='Calculus', 
        url='index.html', 
        js_api=api, 
        width=300, 
        height=450, 
        resizable=False,
        min_size=(300, 450)
    )
    webview.start(icon='toti.ico')