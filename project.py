import tkinter as tk

class Calculator:
    def __init__(self, cal):
        self.cal = cal
        cal.title("Calculator")

        # Entry widget to display the input and results
        self.display = tk.Entry(cal, width=20, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            ('9', 1, 0), ('8', 1, 1), ('7', 1, 2), ('+', 1, 3),
            ('6', 2, 0), ('5', 2, 1), ('4', 2, 2), ('-', 2, 3),
            ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        # Create buttons and add them to the grid
        for (text, row, col) in buttons:
            tk.Button(cal, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, value):
        if value == 'C':
            self.display.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + value)

# Create the main application window
root = tk.Tk()
calculator_app = Calculator(root)

# Run the application
root.mainloop()