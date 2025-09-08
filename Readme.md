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

> Place the images in `assets/` with the following names for the links to work.

![Intro screen](./assets/intro.png)

![Difficulty selection](./assets/difficulty.png)

![Result screen](./assets/result.png)

<!-- HTML fallbacks for viewers that block Markdown image rendering -->
<p>
  <img src="./assets/intro.png" alt="Intro screen" width="360" />
</p>
<p>
  <img src="./assets/difficulty.png" alt="Difficulty selection" width="360" />
</p>
<p>
  <img src="./assets/result.png" alt="Result screen" width="360" />
</p>

If images do not appear:

- Confirm files exist at `assets/intro.png`, `assets/difficulty.png`, `assets/result.png`.
- Ensure the file is saved as `Readme.md` or `README.md`.
- Some previews require reopening the Markdown preview after saving.
