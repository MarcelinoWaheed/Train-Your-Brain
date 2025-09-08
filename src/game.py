# game.py
import tkinter as tk
from tkinter import messagebox
import random

from constants import (
    BG_COLOR, PRIMARY_FONT, TITLE_FONT, NUMBER_FONT,
    COLOR_SUCCESS, COLOR_SUCCESS_HOVER,
    COLOR_WARN, COLOR_WARN_HOVER,
    COLOR_DANGER, COLOR_DANGER_HOVER,
    COLOR_INFO, COLOR_INFO_HOVER,
    COLOR_QUIT, COLOR_QUIT_HOVER,
)
from storage import load_highscore, save_highscore
from ui import add_hover_effect


class MemoryGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Train Your Brain: Bit by Bit")
        root.geometry("400x380")
        root.config(bg=BG_COLOR)

        self.score = 0
        self.attempts = 0
        self.time_left = 0
        self.timer_id = None
        self.highscore = load_highscore()
        self.current_number = ""

        # INTRO FRAME
        self.intro_frame = tk.Frame(root, bg=BG_COLOR)
        self.intro_frame.pack(expand=True)

        tk.Label(
            self.intro_frame,
            text="Welcome to the Memory Challenge!\n\n"
                 "A number will flash briefly.\n"
                 "Type it correctly before time runs out!\n",
            bg=BG_COLOR,
            font=("Arial", 13),
            justify="center"
        ).pack(pady=20)

        tk.Button(
            self.intro_frame,
            text="Start",
            command=self.show_difficulty,
            bg=COLOR_SUCCESS,
            fg="white",
            activebackground=COLOR_SUCCESS_HOVER,
            activeforeground="white",
            font=("Arial", 12),
            width=12,
            bd=0
        ).pack()

        # DIFFICULTY FRAME
        self.diff_frame = tk.Frame(root, bg=BG_COLOR)

        tk.Label(
            self.diff_frame,
            text="Choose your challenge!",
            font=TITLE_FONT,
            bg=BG_COLOR
        ).pack(pady=15)

        difficulties = [
            ("Easy (3 digits)", 3, COLOR_SUCCESS, COLOR_SUCCESS_HOVER),
            ("Medium (5 digits)", 5, COLOR_WARN, COLOR_WARN_HOVER),
            ("Hard (7 digits)", 7, COLOR_DANGER, COLOR_DANGER_HOVER),
        ]

        for text, digits, color, hover in difficulties:
            btn = tk.Button(
                self.diff_frame,
                text=text,
                command=lambda d=digits: self.start_round(d),
                bg=color,
                fg="white",
                activebackground=hover,
                activeforeground="white",
                font=("Arial", 12, "bold"),
                width=20,
                bd=0
            )
            btn.pack(pady=8)
            add_hover_effect(btn, color, hover)

        # GUESS FRAME
        self.guess_frame = tk.Frame(root, bg=BG_COLOR)

        self.number_label = tk.Label(
            self.guess_frame,
            font=NUMBER_FONT,
            bg=BG_COLOR
        )
        self.number_label.pack(pady=10)

        self.timer_label = tk.Label(
            self.guess_frame,
            text="",
            font=TITLE_FONT,
            bg=BG_COLOR,
            fg="red"
        )
        self.timer_label.pack()

        tk.Label(
            self.guess_frame,
            text="Enter the number:",
            bg=BG_COLOR,
            font=PRIMARY_FONT
        ).pack()

        self.entry = tk.Entry(
            self.guess_frame,
            font=("Arial", 16),
            justify="center"
        )
        self.entry.pack(pady=5)

        tk.Button(
            self.guess_frame,
            text="Check Answer",
            command=self.check_answer,
            bg=COLOR_INFO,
            fg="white",
            activebackground=COLOR_INFO_HOVER,
            activeforeground="white",
            font=("Arial", 12),
            width=12,
            bd=0
        ).pack(pady=10)

        # RESULT FRAME
        self.result_frame = tk.Frame(root, bg=BG_COLOR)

        self.result_label = tk.Label(
            self.result_frame,
            font=PRIMARY_FONT,
            bg=BG_COLOR
        )
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(
            self.result_frame,
            font=PRIMARY_FONT,
            bg=BG_COLOR
        )
        self.score_label.pack(pady=5)

        self.highscore_label = tk.Label(
            self.result_frame,
            text=f"High Score: {self.highscore}",
            font=("Arial", 12, "bold"),
            bg=BG_COLOR,
            fg="blue"
        )
        self.highscore_label.pack(pady=5)

        tk.Button(
            self.result_frame,
            text="Play Again",
            command=self.show_difficulty,
            bg=COLOR_SUCCESS,
            fg="white",
            activebackground=COLOR_SUCCESS_HOVER,
            activeforeground="white",
            font=("Arial", 12),
            width=12,
            bd=0
        ).pack(pady=5)

        tk.Button(
            self.result_frame,
            text="Show Score",
            command=self.show_score,
            bg=COLOR_INFO,
            fg="white",
            activebackground=COLOR_INFO_HOVER,
            activeforeground="white",
            font=("Arial", 12),
            width=12,
            bd=0
        ).pack(pady=5)

        tk.Button(
            self.result_frame,
            text="Quit",
            command=root.quit,
            bg=COLOR_QUIT,
            fg="white",
            activebackground=COLOR_QUIT_HOVER,
            activeforeground="white",
            font=("Arial", 12),
            width=12,
            bd=0
        ).pack(pady=5)

    def show_difficulty(self) -> None:
        self.hide_frames()
        self.diff_frame.pack(expand=True)

    def start_round(self, digits: int) -> None:
        self.hide_frames()
        number = random.randint(10 ** (digits - 1), 10 ** digits - 1)
        self.current_number = str(number)
        self.number_label.config(text=self.current_number)
        self.guess_frame.pack(expand=True)
        self.root.after(1200, lambda: self.number_label.config(text=""))
        self.entry.delete(0, tk.END)
        self.start_timer(10)

    def start_timer(self, seconds: int) -> None:
        self.time_left = seconds
        self.update_timer()

    def update_timer(self) -> None:
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.check_answer(timeout=True)

    def check_answer(self, timeout: bool = False) -> None:
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        guess = self.entry.get().strip()
        self.attempts += 1

        if not timeout and guess == self.current_number:
            self.score += 1
            result = "Correct answer!"
            color = "green"
        else:
            result = f"Wrong! It was {self.current_number}"
            color = "red"

        if self.score > self.highscore:
            self.highscore = self.score
            save_highscore(self.highscore)

        self.result_label.config(text=result, fg=color)
        self.score_label.config(text=f"Score: {self.score}/{self.attempts}")
        self.highscore_label.config(text=f"High Score: {self.highscore}")
        self.hide_frames()
        self.result_frame.pack(expand=True)

    def show_score(self) -> None:
        messagebox.showinfo(
            "Score",
            f"You have {self.score} correct out of {self.attempts} attempts.\n"
            f"High Score: {self.highscore}"
        )

    def hide_frames(self) -> None:
        for f in [
            self.intro_frame,
            self.diff_frame,
            self.guess_frame,
            self.result_frame
        ]:
            f.pack_forget()