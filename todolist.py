from tkinter import *
from tkinter import messagebox
from tkinter import ttk

t_list = []

def input_err():
    if b.get() == "":
        messagebox.showerror("Input Error", "Please enter a task.")
        return 0
    return 1

def clear_t() :
    b.delete(0, END)

def insert_t():
    if input_err():
        content = b.get().strip()
        t_list.append({'text': content, 'done': False})
        ta.yview_moveto(1)
        update_t()
        clear_t()
        update_progress()

def update_t():
    ta.delete(0, END)
    for a,i in enumerate(t_list, start=1):
        display_t = i['text']
        if i['done']:
            display_t = f"{display_t} ✅"
        ta.insert(END, f" {a} . {display_t}")
        if i['done']:
            ta.itemconfig(a - 1, {'fg': 'gray'})
    ta.yview_moveto(1)
    update_progress()

def update_progress():
    if len(t_list) == 0:
        progress['value'] = 0
        return
    completed = sum(bool(task['done']) for task in t_list)
    progress['value'] = (completed / len(t_list)) * 100

def delete():
    if not ta.curselection():
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    if ta.curselection():
        index = ta.curselection()[0]
        del t_list[index]
        update_t()
        update_progress()

def delete_all():
    if not t_list:
        messagebox.showinfo("Nothing to delete", "There are no tasks to delete.")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
    if confirm:
        t_list.clear()
        update_t()

def mark_t(event):
    if not ta.curselection():
        return
    index = ta.curselection()[0]
    if t_list[index]['done']:
        messagebox.showinfo("Already Completed", "This task is already marked as completed.")
        return
    t_list[index]['done'] = True
    update_t()
    update_progress()

root = Tk()
root.title("To-Do-List")
root.geometry("665x400+550+250")
root.resizable(0, 0)

bg = PhotoImage(file="bgimage.gif")
canvas1 = Canvas(root, width=665, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

tdl = Label(root, text="To-Do List", font=("Times New Roman", 15, "bold"),height=1, width=15, borderwidth=2, relief="solid")
t = Label(root, text="Task :-", font=("Times New Roman", 11, "bold"),bg="#FFB300", height=1, width=9, borderwidth=1, relief="solid")
b = Entry(root, width=75, borderwidth=1, relief="solid")
add_t = Button(root, text="Add task", font=("Times New Roman", 10, "bold"),fg="black", bg="#66FF00", borderwidth=1, relief="solid",height=1, width=10, command=insert_t)
del_t = Button(root, text="Delete task", font=("Times New Roman", 10, "bold"), fg="white", bg="#FF0303", borderwidth=1, relief="solid", height=1, width=10, command=delete)
ta = Listbox(root, width=45, height=8, font="bold", selectmode='SINGLE',bg="WHITE", fg="BLACK", selectbackground="#02CCF0", selectforeground="BLACK",borderwidth=1, relief="solid")
ta.bind("<Double-Button-1>", mark_t)
scrollbar = Scrollbar(root, orient=VERTICAL, command=ta.yview)
scrollbar.place(x=210 + 50 * 7.3, y=115, height=199)
scrollbar.config(command=ta.yview)
del_all = Button(root, text="Delete All", font=("Times New Roman", 9, "bold"),fg="white", bg="#FF8000", borderwidth=1, relief="solid",height=1, width=10, command=delete_all)
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=270, mode='determinate')

canvas1.create_window(330, 30, window=tdl)
canvas1.create_window(50, 80, window=t)
canvas1.create_window(334, 80, window=b)
canvas1.create_window(615, 79, window=add_t)
canvas1.create_window(330, 215, window=ta)
canvas1.create_window(151, 350, window=del_t)
canvas1.create_window(525, 350, window=del_all)
canvas1.create_window(338, 350, window=progress)
root.mainloop()
