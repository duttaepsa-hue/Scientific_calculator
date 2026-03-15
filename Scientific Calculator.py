import tkinter as tk
import math

# ---------------- WINDOW SETUP ---------------- #
root = tk.Tk()
root.title("Scientific Calculator by Epsa")
root.geometry("350x700")
root.resizable(True, True)

# ---------------- STATE VARIABLES ---------------- #
equation = ""
input_text = tk.StringVar()

# ---------------- FUNCTIONS ---------------- #
def press(symbol):
    global equation
    equation += str(symbol)
    input_text.set(equation)


def clear():
    global equation
    equation = ""
    input_text.set(equation)


def delete():
    global equation
    equation = equation[:-1]
    input_text.set(equation)


def calculate():
    global equation
    try:
        expr = equation

        # Replace mathematical symbols
        expr = expr.replace("^", "**")
        expr = expr.replace("√", "math.sqrt(")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")

        # Fix missing closing brackets
        open_br = expr.count("(")
        close_br = expr.count(")")
        if open_br > close_br:
            expr += ")" * (open_br - close_br)

        result = str(eval(expr, {"math": math, "__builtins__": None}))
        input_text.set(result)
        equation = result

    except Exception:
        input_text.set("Error")
        equation = ""


def key_event(event):
    key = event.char
    if key in "0123456789.+-*/":
        press(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        delete()
    elif key.lower() == "c":
        clear()


root.bind("<Key>", key_event)

# ---------------- DISPLAY ---------------- #
entry = tk.Entry(
    root,
    textvariable=input_text,
    justify='right',
    font=('Consolas', 32),
    bd=8,
    relief=tk.RIDGE
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# ---------------- BUTTON CREATION ---------------- #
def create_button(text, row, col, cmd=None, colspan=1, bg="#333", fg="white"):
    button = tk.Button(
        root,
        text=text,
        font=("Arial", 18, "bold"),
        bg=bg,
        fg=fg,
        bd=3,
        relief=tk.RAISED,
        command=cmd
    )
    button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
    return button

# Colors
num_color = "#1C1C1F"
op_color = "#E74C3C"
sci_color = "#164885"
eq_color = "#F39C12"

# ROW 1
create_button("C", 1, 0, clear, bg=sci_color)
create_button("DEL", 1, 1, delete, bg=sci_color)
create_button("(", 1, 2, lambda: press("("), bg=sci_color)
create_button(")", 1, 3, lambda: press(")"), bg=sci_color)

# ROW 2
create_button("7", 2, 0, lambda: press("7"), bg=num_color)
create_button("8", 2, 1, lambda: press("8"), bg=num_color)
create_button("9", 2, 2, lambda: press("9"), bg=num_color)
create_button("/", 2, 3, lambda: press("/"), bg=op_color)

# ROW 3
create_button("4", 3, 0, lambda: press("4"), bg=num_color)
create_button("5", 3, 1, lambda: press("5"), bg=num_color)
create_button("6", 3, 2, lambda: press("6"), bg=num_color)
create_button("*", 3, 3, lambda: press("*"), bg=op_color)

# ROW 4
create_button("1", 4, 0, lambda: press("1"), bg=num_color)
create_button("2", 4, 1, lambda: press("2"), bg=num_color)
create_button("3", 4, 2, lambda: press("3"), bg=num_color)
create_button("-", 4, 3, lambda: press("-"), bg=op_color)

# ROW 5
create_button("0", 5, 0, lambda: press("0"), bg=num_color)
create_button(".", 5, 1, lambda: press("."), bg=num_color)
create_button("=", 5, 2, calculate, bg=eq_color)
create_button("+", 5, 3, lambda: press("+"), bg=op_color)

# ROW 6
create_button("√", 6, 0, lambda: press("√("), bg=sci_color)
create_button("sin", 6, 1, lambda: press("sin("), bg=sci_color)
create_button("cos", 6, 2, lambda: press("cos("), bg=sci_color)
create_button("tan", 6, 3, lambda: press("tan("), bg=sci_color)

# ROW 7
create_button("log", 7, 0, lambda: press("log("), bg=sci_color)
create_button("ln", 7, 1, lambda: press("ln("), bg=sci_color)
create_button("^", 7, 2, lambda: press("^"), bg=sci_color)
create_button("π", 7, 3, lambda: press("3.14159"), bg=sci_color)

# ---------------- GRID CONFIG ---------------- #
for i in range(8):
    root.rowconfigure(i, weight=1)

for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
