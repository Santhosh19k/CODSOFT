import tkinter as tk
from tkinter import ttk, messagebox
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x620")
root.configure(bg="#2FB3B3")
root.resizable(False, False)

p_score=c_score=best_score = 0
roundno = 1
time_left = 30
timer_running = True

def play(p_choice):
    global p_score, c_score, roundno, best_score
    if not timer_running:
        return
    c_choice = random.choice(["Rock", "Paper", "Scissors"])
    computer.config(text=f"Computer chose: {c_choice}")

    if p_choice == c_choice:
        result.set("It's a Tie!")
    elif (p_choice == "Rock" and c_choice == "Scissors") or \
        (p_choice == "Paper" and c_choice == "Rock") or \
        (p_choice == "Scissors" and c_choice == "Paper"):
        p_score += 1
        result.set("You Win!")
    else:
        c_score += 1
        result.set("Computer Wins!")

    if p_score > best_score:
        best_score = p_score
        bs.config(text=f"✨ Best Score: {best_score}")
        if best_score == 5:
            messagebox.showinfo("Badge Unlocked", "🏅 Congratulations! You have earned a Bronze Badge by scoring 5 points!")
        elif best_score == 10:
            messagebox.showinfo("Badge Unlocked", "🥇 Congratulations! You have earned a Silver Badge by scoring 10 points!")
        elif best_score == 15:
            messagebox.showinfo("Badge Unlocked", "🥇 Congratulations! You have earned a Gold Badge by scoring 15 points!")

    scoreboard.insert("", "end", values=(roundno, p_score, c_score))
    scoreboard.yview_moveto(1.0)
    roundno += 1

def reset_score():
    global p_score, c_score, roundno
    p_score = c_score = 0
    roundno = 1
    score.config(text=f"Time Left: {time_left}s")
    computer.config(text="Computer chose:")
    result.set("Let's Play Again!")
    for row in scoreboard.get_children():
        scoreboard.delete(row)

def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        tl.config(text=f"Time Left: {time_left}s")
        time_left -= 1
        root.after(1000, update_timer)
    elif time_left == 0:
        timer_running = False
        messagebox.showinfo("Time's Up", "⏰ 30 seconds Over! Scoreboard will reset.")
        reset_score()
        reset_timer()

def toggle_timer():
    global timer_running
    timer_running = not timer_running
    pause_btn.config(text="▶ Resume Timer" if not timer_running else " Pause Timer")
    if timer_running:
        update_timer()

def reset_timer():
    global time_left, timer_running
    time_left = 30
    tl.config(text=f"Time Left: {time_left}s")
    timer_running = True
    update_timer()

tk.Label(root, text="Rock 🪨 Paper 📃 Scissors ✄", font=("Times New Roman", 22, "bold"), bg="#FFE044").pack(pady=10)
score = tk.Label(root, text="Time Left: 30s", font=("Times New Roman", 14), bg="#FFE044", fg="blue")
score.pack(pady=5)
bs = tk.Label(root, text=" Best Score: 0 ", font=("Times New Roman", 14), bg="#FFE044", fg="green")
bs.pack(pady=5)
computer = tk.Label(root, text="Computer chose:", font=("Times New Roman", 14), bg="#FFE044")
computer.pack(pady=4)
result = tk.StringVar(value="Let's Play! Choose Something!")
tk.Label(root, textvariable=result, font=("Times New Roman", 16, "bold"), bg="#FFE044").pack(pady=10)
frame = tk.Frame(root, bg="#2FB3B3",borderwidth=5)
frame.pack(pady=10,padx=15)
tk.Button(frame, text="🪨", width=10, font=("Times New Roman", 14,"bold"),bg="#FFE044",fg="black",borderwidth=4, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="📃", width=10, font=("Times New Roman", 14,"bold"),bg="#FFE044",fg="black",borderwidth=4, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="✄", width=10, font=("Times New Roman", 14,"bold"),bg="#FFE044",fg="black",borderwidth=4, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)
tk.Button(root, text=" Reset Score", font=("Times New Roman", 12, "bold"), bg="#FF5733", fg="white", command=reset_score).pack(pady=10)
pause_btn = tk.Button(root, text=" Pause Timer", font=("Times New Roman", 12, "bold"), bg="#1282F2", fg="white", command=toggle_timer)
pause_btn.pack()
tk.Label(root, text="📋 Scoreboard : ", font=("Times New Roman", 14, "bold"), bg="#FFE044", anchor="w", justify="left").pack(pady=5, anchor="w", padx=15)
scoreboard = ttk.Treeview(root, columns=("Round", "Player", "Computer"), show="headings", height=8)
scoreboard.heading("Round", text="Round")
scoreboard.heading("Player", text="Your Score")
scoreboard.heading("Computer", text="Computer Score")
scoreboard.column("Round", anchor="center", width=140)
scoreboard.column("Player", anchor="center", width=140)
scoreboard.column("Computer", anchor="center", width=140)
scoreboard.pack(pady=5)
tl = score
update_timer()

root.mainloop()
