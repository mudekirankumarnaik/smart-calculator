import tkinter

from calculator import add, subtract, multiply, divide
from history import save_history, show_history

window = tkinter.Tk()

window.title("Smart Calculator")
window.geometry("400x600")


# Calculator memory
current = ""
first_number = None
operator = ""


# ---------------- FUNCTIONS ----------------

def number_clicked(number):
    global current

    current = current + str(number)

    display.config(text=current)


def operator_clicked(op):
    global current
    global first_number
    global operator

    if current == "":
        return

    first_number = float(current)
    operator = op
    current = ""

    display.config(text=f"{first_number} {operator}")

def equals_clicked():
    global current
    global first_number
    global operator

    second_number = float(current)

    if operator == "+":
        answer = add(first_number, second_number)

    elif operator == "-":
        answer = subtract(first_number, second_number)

    elif operator == "*":
        answer = multiply(first_number, second_number)

    elif operator == "/":

        if second_number == 0:
            display.config(text="Cannot divide by 0")
            return

        answer = divide(first_number, second_number)

    current = str(answer)

    display.config(text=current)

    history_text = f"{first_number} {operator} {second_number} = {answer}"

    save_history(history_text)

def clear_clicked():
    global current
    global first_number
    global operator

    current = ""
    first_number = None
    operator = ""

    display.config(text="0")

def decimal_clicked():
    global current

    if "." not in current:

        if current == "":
            current = "0."

        else:
            current = current + "."

    display.config(text=current)

def history_clicked():

    history = show_history()

    history_window = tkinter.Toplevel(window)

    history_window.title("Calculation History")
    history_window.geometry("400x400")

    history_textbox = tkinter.Text(
        history_window,
        font=("Arial", 14)
    )

    history_textbox.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    history_textbox.insert(
        "1.0",
        history
    )

    history_textbox.config(
        state="disabled"
    )

# ---------------- DISPLAY ----------------

display = tkinter.Label(
    window,
    text="0",
    font=("Arial", 30),
    anchor="e",
    height=2
)

display.pack(
    fill="x",
    padx=20,
    pady=20
)


# ---------------- BUTTON FRAME ----------------

button_frame = tkinter.Frame(window)
button_frame.pack()

equals_button = tkinter.Button(
    button_frame,
    text="=",
    width=5,
    height=2,
    font=("Arial", 18),
    command=equals_clicked
)


equals_button.grid(
    row=3,
    column=2,
    padx=5,
    pady=5
)

clear_button = tkinter.Button(
    button_frame,
    text="C",
    width=5,
    height=2,
    font=("Arial", 18),
    command=clear_clicked
)

clear_button.grid(
    row=4,
    column=0,
    padx=5,
    pady=5
)

decimal_button = tkinter.Button(
    button_frame,
    text=".",
    width=5,
    height=2,
    font=("Arial", 18),
    command=decimal_clicked
)

decimal_button.grid(
    row=3,
    column=1,
    padx=5,
    pady=5
)

history_button = tkinter.Button(
    button_frame,
    text="History",
    width=5,
    height=2,
    font=("Arial", 18),
    command=history_clicked
)

history_button.grid(
    row=4,
    column=1,
    columnspan=3,
    padx=5,
    pady=5,
    sticky="nsew"
)


# ---------------- NUMBER BUTTONS ----------------

numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]

for index, number in enumerate(numbers):

    row = index // 3
    column = index % 3

    button = tkinter.Button(
    button_frame,
    text=str(number),
    width=5,
    height=2,
    font=("Arial", 18),
    command=lambda n=number: number_clicked(n)
)

    button.grid(
    row=row,
    column=column,
    padx=5,
    pady=5
)


# ---------------- OPERATOR BUTTONS ----------------

operators = ["+", "-", "*", "/"]

for index, op in enumerate(operators):

    button = tkinter.Button(
    button_frame,
    text=op,
    width=5,
    height=2,
    font=("Arial", 18),
    command=lambda o=op: operator_clicked(o)
)

    button.grid(
    row=index,
    column=3,
    padx=5,
    pady=5
)


# ---------------- START GUI ----------------

window.mainloop()
