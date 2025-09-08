# main.py
import tkinter as tk
from game import MemoryGame

if __name__ == "__main__":
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()