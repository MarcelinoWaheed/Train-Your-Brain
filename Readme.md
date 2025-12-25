# Train Your Brain: Bit by Bit 🧠

A dynamic Tkinter memory game designed to test and improve your short-term memory. A number flashes briefly—type it before the time runs out! Now featuring player profiles, detailed statistics, and a robust **SQL database** backend.

## ✨ Features

- **Multiple Difficulty Levels:**
  - 🟢 Easy (3 digits)
  - 🟡 Medium (5 digits)
  - 🔴 Hard (7 digits)
- **Player Profiles:** Create your own profile and track your progress.
- **Detailed Statistics:** View your accuracy, total games played, and performance breakdown by difficulty.
- **Interactive UI:** Clean Tkinter interface with visual feedback.
- **Robust Database:** Utilizes **SQLite** for efficient, persistent data storage.

## 🎮 How to play

1. **Start:** Run the game and enter your name (defaults to "Player 1").
2. **Choose Difficulty:** Select between Easy, Medium, or Hard.
3. **Memorize:** A number will appear briefly on the screen.
4. **Type:** Enter the number correctly before the timer runs out.
5. **Track:** Check "My Profile" to see your stats loaded directly from the database.

## 📂 Project Structure

```text
.
├─ src/
│  ├─ main.py         # App entry point
│  ├─ game.py         # Game logic & Screens management
│  ├─ ui.py           # UI components & styling
│  ├─ storage.py      # Database Manager (SQLite Connection & Queries)
│  ├─ constants.py    # Configuration & Asset paths
│  └─ show_db.py      # Utility script to query the database
├─ Screenshots/       # Images for README
│  ├─ Intro.png
│  ├─ Difficulty.png
│  ├─ Player Details.png
│  ├─ Result for correct answer.png
│  └─ Result for wrong answer.png
└─ arcade.db          # SQLite Database (Auto-generated)
```

## 🛠️ Requirements

- **Python 3.10+**
- **SQLite3** (Included with Python standard library)
- No external packages required

## 🚀 Run the Game

**Windows / macOS / Linux:**

Make sure you are in the project folder, then run:

```bash
python src/main.py
```

## 🛠️ Utility: View Database

To inspect the SQL data directly in the terminal:

```bash
python src/show_db.py
```

## 📸 Screenshots

| Intro | Difficulty Selection |
|:---:|:---:|
| ![Intro](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/203c4a82c11f97a2379ee20b9cba8853e8a29264/Screenshots/Intro.png?raw=true) | ![Difficulty](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/203c4a82c11f97a2379ee20b9cba8853e8a29264/Screenshots/Difficulty.png?raw=true) |

| Player Stats (SQL Data) | Correct Result |
|:---:|:---:|
| ![Stats](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/7ef06f31cbb0bd51bab9498b5aeb77e00cf04010/Screenshots/Player%20Details.png?raw=true) | ![Correct](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/c8e7c0eaf504bdd833948b22b74b69f194c40ffc/Screenshots/Result%20for%20correct%20answer.png?raw=true) |

| Wrong Result |
|:---:|
| ![Wrong](https://github.com/MarcelinoWaheed/Train-Your-Brain/blob/c8e7c0eaf504bdd833948b22b74b69f194c40ffc/Screenshots/Result%20for%20wrong%20answer.png?raw=true) |

## ⚙️ Technologies Used

- **Python** – Core logic.
- **Tkinter** – GUI Framework.
- **SQLite** – Relational Database Management System (RDBMS).

---
**Feel free to contribute and enhance the project! 🚀**
