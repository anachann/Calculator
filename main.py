import tkinter as tk

calculation = ""

def add_to_calculation(symbol):     #adding new symbols to the equasion string
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():         #Evaluating the equasion string provided in GUI
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():                  #clearing the string provided in GUI
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("480x320")

text_result = tk.Text(root, height=2, width=26, font=("Arial",24))
text_result.grid(columnspan=5)

button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=10, font=("Arial",14))
button_9.grid(row=2,column=0)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=10, font=("Arial",14))
button_8.grid(row=2,column=1)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=10, font=("Arial",14))
button_7.grid(row=2,column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=10, font=("Arial",14))
button_6.grid(row=3,column=0)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=10, font=("Arial",14))
button_5.grid(row=3,column=1)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=10, font=("Arial",14))
button_4.grid(row=3,column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=10, font=("Arial",14))
button_3.grid(row=4,column=0)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=10, font=("Arial",14))
button_2.grid(row=4,column=1)
button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=10, font=("Arial",14))
button_1.grid(row=4,column=2)
button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=10, font=("Arial",14))
button_0.grid(row=5,column=1)
button_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=10, font=("Arial",14))
button_division.grid(row=2,column=4)
button_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=10, font=("Arial",14))
button_multiplication.grid(row=3,column=4)
button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=10, font=("Arial",14))
button_minus.grid(row=4,column=4)
button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=10, font=("Arial",14))
button_plus.grid(row=5,column=4)

button_open = tk.Button(root, text="(", command=lambda: add_to_calculation(")"), width=10, font=("Arial",14))
button_open.grid(row=5,column=0)
button_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=10, font=("Arial",14))
button_close.grid(row=5,column=2)
button_equals = tk.Button(root, text="=", command=evaluate_calculation, width=10, font=("Arial",14))
button_equals.grid(row=6,column=2)
button_reset = tk.Button(root, text="C", command=clear_field, width=10, font=("Arial",14))
button_reset.grid(row=6,column=1)
root.mainloop() 