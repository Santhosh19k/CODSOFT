import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#DA1818')
root.resizable(0, 0)
entry = tk.Entry(root, bg='#FFF5CC', fg='black',font=('Times New Roman', 25),borderwidth=10, justify="right")
entry.grid(row=0, columnspan=10, padx=10, pady=10, sticky='nsew')

def press(n):
    entry.insert(tk.END, str(n))
def operate(x):
    entry.insert(tk.END, x)
def clear():
    entry.delete(0, tk.END)
def equal():
    a = entry.get()
    if a.strip() == "":
        mb.showerror("Error", "Empty input! Please enter the number")
        clear()
        return
    try:
        res = eval(a)
        clear()
        entry.insert(tk.END,str(res))
    except:
        mb.showerror("Error", "Invalid expression! Please enter the correct expression")
        clear()

btns = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 1)
]
for (num, row, col) in btns:
    tk.Button(root, text=str(num), width=5, height=1,font=('Times New Roman', 20),bg='#FFF5CC', fg='black',command=lambda x=num: press(x)).grid(row=row, column=col, padx=10, pady=5)  

tk.Button(root, text='+', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=lambda: operate('+')).grid(row=1, column=3, padx=5, pady=5)
tk.Button(root, text='-', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=lambda: operate('-')).grid(row=2, column=3, padx=5, pady=5)
tk.Button(root, text='*', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=lambda: operate('*')).grid(row=3, column=3, padx=5, pady=5)
tk.Button(root, text='/', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=lambda: operate('/')).grid(row=4, column=3, padx=5, pady=5)
tk.Button(root, text='C', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=clear).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text='=', width=5, height=1,font=('Times New Roman', 18),borderwidth=5,bg='#FFD700', fg='black',command=equal).grid(row=4, column=2, padx=5, pady=5)
root.mainloop()
