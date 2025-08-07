from tkinter import *
import random
import tkinter.messagebox as tmsg

# ---------------------------- Easy Word List ---------------------------- #
words = {
    'book': 'Used for reading',
    'code': 'Set of programming instructions',
    'fish': 'Lives in water',
    'game': 'Played for fun',
    'lamp': 'Gives light',
    'ring': 'Worn on a finger',
    'tree': 'Has leaves and grows tall',
    'frog': 'Jumps and lives near water',
    'cake': 'Sweet baked dessert',
    'milk': 'White dairy drink'
}

word = ''
jumbled_word = ''
hint = ''
score = 0
attempts = 0

# ---------------------------- Game Logic ---------------------------- #
def get_new_word():
    global word, jumbled_word, hint
    word, hint = random.choice(list(words.items()))
    jumbled_word = ''.join(random.sample(word, len(word)))
    word_label.config(text=f"🔤 Jumbled Word: {jumbled_word}")
    hint_label.config(text="💡 Hint: ???")
    guess_entry.delete(0, END)

def show_hint():
    hint_label.config(text=f"💡 Hint: {hint}")

def check_answer():
    global score, attempts
    guess = guess_entry.get().strip().lower()
    attempts += 1
    if guess == word:
        score += 1
        tmsg.showinfo("Correct ✅", f"🎉 Great! Your score is: {score}")
    else:
        tmsg.showerror("Wrong ❌", f"Oops! The correct word was: {word}")
    update_score()
    get_new_word()

def update_score():
    score_label.config(text=f"🏆 Score: {score} | 🎯 Attempts: {attempts}")

def clear_input():
    guess_entry.delete(0, END)

# ---------------------------- GUI Setup ---------------------------- #
root = Tk()
root.title("🧠 Easy Jumbled Word Game")
root.geometry("800x600")
root.config(bg="#fef9e7")
root.resizable(False, False)

# ---------------------------- GUI Design ---------------------------- #
title = Label(root, text="🎯 Easy Jumbled Word Puzzle", font=("Comic Sans MS", 28, "bold"),
              bg="#fef9e7", fg="#6c3483")
title.pack(pady=20)

frame = Frame(root, bg="#ffffff", bd=4, relief=RIDGE)
frame.pack(pady=20, padx=20)

word_label = Label(frame, text="", font=("Helvetica", 24, "bold"),
                   bg="#d5f5e3", fg="#154360", pady=10, padx=20, width=20)
word_label.pack(pady=20)

guess_entry = Entry(frame, font=("Arial", 20), justify="center", width=30, bg="#fcf3cf")
guess_entry.pack(pady=10)

btn_frame = Frame(frame, bg="#ffffff")
btn_frame.pack(pady=20)

submit_btn = Button(btn_frame, text="✅ Submit", font=("Arial", 16), width=12,
                    bg="#27ae60", fg="white", command=check_answer)
submit_btn.grid(row=0, column=0, padx=10, pady=5)

next_btn = Button(btn_frame, text="🔄 Next Word", font=("Arial", 16), width=12,
                  bg="#2980b9", fg="white", command=get_new_word)
next_btn.grid(row=0, column=1, padx=10, pady=5)

hint_btn = Button(btn_frame, text="💡 Show Hint", font=("Arial", 16), width=12,
                  bg="#f39c12", fg="white", command=show_hint)
hint_btn.grid(row=1, column=0, padx=10, pady=5)

clear_btn = Button(btn_frame, text="🧼 Clear", font=("Arial", 16), width=12,
                   bg="#7f8c8d", fg="white", command=clear_input)
clear_btn.grid(row=1, column=1, padx=10, pady=5)

hint_label = Label(frame, text="💡 Hint: ???", font=("Arial", 16, "italic"),
                   bg="#ffffff", fg="#2d3436")
hint_label.pack(pady=10)

score_label = Label(root, text="🏆 Score: 0 | 🎯 Attempts: 0", font=("Arial", 16, "bold"),
                    bg="#fef9e7", fg="#2d3436")
score_label.pack(pady=10)

# ---------------------------- Start Game ---------------------------- #
get_new_word()
root.mainloop()