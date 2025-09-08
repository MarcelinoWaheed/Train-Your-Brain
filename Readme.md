# Train Your Brain: Bit by Bit

A tiny Tkinter memory game: a number flashes briefly—type it before time runs out. Your best streak is saved to `highscore.txt`.

Features:

- Clean Tkinter UI with difficulty levels (3/5/7 digits)
- Countdown timer and instant feedback
- Persistent high score stored locally

How to play:

1. Click Start → pick a difficulty.
2. Memorize the shown number. It disappears quickly.
3. Type the number before the timer ends. Earn a point for each correct round.

Project structure:

```
.
├─ main.py         # App entry point
├─ game.py         # Game logic + Tkinter screens
├─ ui.py           # UI helpers (hover effects, etc.)
├─ storage.py      # Load/save high score
├─ constants.py    # Shared constants (optional)
└─ highscore.txt   # Highest score (plain text)
```

Requirements:

- Python 3.10+ (Tkinter ships with the official installer on Windows/macOS)
- No external packages

Run:

- Windows (PowerShell) or macOS/Linux (Terminal):

```
python main.py
```

Tips:

- Reset high score: clear or delete `highscore.txt` (it will be recreated).
- Single-file version: run with `python <filename>.py`.

Troubleshooting:

- "tkinter not found": ensure you installed the official Python from python.org. On Linux, install Tk packages (e.g., `sudo apt install python3-tk`).
- Multiple Python versions: try `python3 main.py`.

Screenshots:

![image alt](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/af3594c4c3cc9c1950cf79163750feed7a114b97/Screenshots/intro.png)

![image alt](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/f3e692643beb24eb6f8d80064dd4f29b901fd0fb/Screenshots/difficulty.png)

![image alt](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/f3e692643beb24eb6f8d80064dd4f29b901fd0fb/Screenshots/result.png)

## ⚙️ Technologies Used

- **Python** – Core programming language.
- **Tkinter** – GUI framework.

**Feel free to contribute and enhance the project! 🚀**
