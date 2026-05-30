import tkinter as tk
from tkinter import messagebox
import re
import random
import string

def check_password():
    password = entry.get()

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 20
    else:
        suggestions.append("Add special characters")

    if score < 50:
        strength = "Weak"
        color = "red"
    elif score < 80:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    result_label.config(
        text=f"Strength: {strength} ({score}%)",
        fg=color
    )

    if suggestions:
        suggestion_label.config(
            text="Suggestions:\n" + "\n".join(suggestions)
        )
    else:
        suggestion_label.config(
            text="Excellent Password!"
        )

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(12))
    messagebox.showinfo(
        "Suggested Strong Password",
        password
    )

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x400")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

entry = tk.Entry(
    root,
    width=35,
    show="*",
    font=("Arial", 14)
)
entry.pack(pady=10)

check_btn = tk.Button(
    root,
    text="Check Strength",
    command=check_password,
    font=("Arial", 12)
)
check_btn.pack(pady=10)

generate_btn = tk.Button(
    root,
    text="Generate Strong Password",
    command=generate_password,
    font=("Arial", 12)
)
generate_btn.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
suggestion_label.pack(pady=10)

root.mainloop()
