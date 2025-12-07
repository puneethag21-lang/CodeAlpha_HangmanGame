import random
import tkinter as tk
from tkinter import messagebox

words = ["python", "program", "laptop", "science", "internet"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

def update_word_display():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)

def guess_letter():
    global attempts

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message_label.config(text="❌ Enter a valid letter!")
        return

    if letter in guessed_letters:
        message_label.config(text="⚠️ Already guessed!")
        return

    guessed_letters.append(letter)

    if letter in secret_word:
        message_label.config(text="✔️ Correct guess!")
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts Left: {attempts}")
        message_label.config(text="❌ Wrong guess!")

    update_word_display()

    # Win condition
    if all(l in guessed_letters for l in secret_word):
        messagebox.showinfo("Hangman", f"🎉 You Win! Word: {secret_word}")
        root.destroy()

    # Lose condition
    if attempts == 0:
        messagebox.showinfo("Hangman", f"💀 Game Over! Word was: {secret_word}")
        root.destroy()

def restart_game():
    global secret_word, guessed_letters, attempts
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    attempts_label.config(text="Attempts Left: 6")
    message_label.config(text="")
    update_word_display()

# GUI Setup
root = tk.Tk()
root.title("Hangman Game (Python GUI)")
root.geometry("400x300")

title_label = tk.Label(root, text="🎯 Hangman Game", font=("Arial", 18))
title_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack()

attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Arial", 14))
attempts_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 16), width=5)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=guess_letter)
guess_button.pack()

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("Arial", 12), command=restart_game)
restart_button.pack(pady=10)

update_word_display()

root.mainloop()
