import re
import random
import string
import tkinter as tk
from tkinter import messagebox


COMMON_PASSWORDS = {
    "123456", "password", "qwerty", "123456789",
    "admin", "letmein", "welcome", "123123"
}


def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # Character variety checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This password is too common and insecure.")

    # Repeated patterns detection
    if re.search(r"(.)\1\1", password):
        score -= 1
        feedback.append("Avoid repeated characters.")

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, score, feedback, color


def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(14))


def check_password():
    password = entry.get()

    if not password:
        messagebox.showwarning("Input Required", "Please enter a password.")
        return

    strength, score, feedback, color = analyze_password(password)

    result_var.set(f"Strength: {strength} | Score: {score}/6")
    result_label.config(fg=color)

    feedback_box.delete("1.0", tk.END)

    if feedback:
        for item in feedback:
            feedback_box.insert(tk.END, f"- {item}\n")
    else:
        feedback_box.insert(tk.END, "Your password meets strong security standards.")


def generate_and_fill():
    password = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, password)


# ---------------- GUI ----------------
app = tk.Tk()
app.title("Password Security Analyzer")
app.geometry("520x460")
app.resizable(False, False)

title = tk.Label(app, text="Password Security Analyzer", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(app, font=("Arial", 14), width=35, show="*")
entry.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack()

tk.Button(button_frame, text="Analyze", width=12, command=check_password).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Generate", width=12, command=generate_and_fill).grid(row=0, column=1, padx=5)

result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var, font=("Arial", 12, "bold"))
result_label.pack(pady=10)

feedback_box = tk.Text(app, height=12, width=60)
feedback_box.pack(pady=10)

app.mainloop()
