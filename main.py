import tkinter as tk

root = tk.Tk()
root.geometry("303x450")
root.title("Калькулятор")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

def add_symbol(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

btnc = tk.Button(root, text="C", command=clear, font=("Arial", 20))
btnc.grid(row=5, column=0, columnspan=4, sticky="nsew")

btns = ["7","8","9","/", "4","5","6","*", "1","2","3","-", "0",".","=","+"]

row, col = 1, 0
for b in btns:
    if b == "=":
        cmd = calculate
    else:
        cmd = lambda x=b: add_symbol(x)

    tk.Button(root, text=b, width=4, height=2, font=("Arial", 20), command=cmd).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()