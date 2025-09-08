# ui.py
import tkinter as tk

def add_hover_effect(button: tk.Button, normal_color: str, hover_color: str) -> None:
    def on_enter(_):
        button.config(bg=hover_color, fg="white")
    def on_leave(_):
        button.config(bg=normal_color, fg="white")
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)