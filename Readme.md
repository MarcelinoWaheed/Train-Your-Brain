# Train Your Brain: Bit by Bit 🧠

A dynamic Tkinter memory game designed to test and improve your short-term memory. A number flashes briefly—type it before the time runs out! Now featuring player profiles, statistics, and multiple difficulty levels.

## ✨ Features

- **Multiple Difficulty Levels:**
  - 🟢 Easy (3 digits)
  - 🟡 Medium (5 digits)
  - 🔴 Hard (7 digits)
- **Player Profiles:** Create your own profile and track your progress.
- **Detailed Statistics:** View your accuracy, total games played, and performance breakdown by difficulty.
- **Interactive UI:** Clean Tkinter interface with visual feedback.
- **Persistent Storage:** Saves player data and high scores locally to `player_data.json`.

## 🎮 How to play

1. **Start:** Run the game and enter your name (defaults to "Player 1").
2. **Choose Difficulty:** Select between Easy, Medium, or Hard.
3. **Memorize:** A number will appear briefly on the screen.
4. **Type:** Enter the number correctly before the timer runs out.
5. **Track:** Check "My Profile" to see your stats.

## 📂 Project Structure

```text
.
├─ src/
│  ├─ main.py         # App entry point
│  ├─ game.py         # Game logic & Screens management
│  ├─ ui.py           # UI components & styling
│  ├─ storage.py      # Data management (Load/Save JSON)
│  ├─ constants.py    # Configuration & Asset paths
│  └─ show_db.py      # Utility script to view saved data
├─ Screenshots/       # Images for README
│  ├─ intro.png
│  ├─ difficulty.png
│  ├─ player_details.png
│  ├─ result_correct.png
│  └─ result_wrong.png
└─ player_data.json   # Stores player stats (Auto-generated)
```

## 🛠️ Requirements

- **Python 3.10+** (Tkinter usually ships with the official installer)
- No external packages required

## 🚀 Run the Game

**Windows / macOS / Linux:**

Make sure you are in the project folder, then run:

```bash
python src/main.py
```

## 🛠️ Utility: View Database

If you want to check the saved data (JSON) directly in the terminal without opening the game:

```bash
python src/show_db.py
```

## 📸 Screenshots

| Intro | Difficulty Selection |
|:---:|:---:|
| ![Intro](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/203c4a82c11f97a2379ee20b9cba8853e8a29264/Screenshots/Intro.png) | ![Difficulty](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/203c4a82c11f97a2379ee20b9cba8853e8a29264/Screenshots/Difficulty.png) |

| Player Stats | Correct Result |
|:---:|:---:|
| ![Stats](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/7ef06f31cbb0bd51bab9498b5aeb77e00cf04010/Screenshots/Player%20Details.png) | ![Correct](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/c8e7c0eaf504bdd833948b22b74b69f194c40ffc/Screenshots/Result%20for%20correct%20answer.png) |

| Wrong Result |
|:---:|
| ![Wrong](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/c8e7c0eaf504bdd833948b22b74b69f194c40ffc/Screenshots/Result%20for%20wrong%20answer.png) |

## ⚙️ Technologies Used

- **Python** – Core logic.
- **Tkinter** – GUI Framework.
- **JSON** – Data persistence.

---
**Feel free to contribute and enhance the project! 🚀**



