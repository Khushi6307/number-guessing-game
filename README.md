# 🎯 Number Guessing Game
A professional, interactive command-line game built using Python. The game challenges the player to guess a randomly generated number within a limited number of attempts, featuring strict input validation.

---

## ✨ Features

- 🔢 Randomly generates a secret number between **1 and 100** each round
- ⚠️ **10-attempt limit** — adds tension and a real losing condition
- 📈 📉 Directional hints after every guess (higher / lower)
- 🛡️ Input validation — handles non-integers and out-of-range values gracefully
- 🔄 **Play again** prompt after every round, no restart needed

---

## 🎮 How to Play

1. Run the script — the game picks a secret number from **1 to 100**
2. Enter your guess when prompted
3. The game tells you if the answer is **higher** or **lower**
4. You have **10 attempts** to find the number
5. Win by guessing correctly, or lose when attempts run out
6. Choose to **play again** or exit after each round

---

## 📁 Project Structure

```
number-guessing-game/
│
├── main.py            # Main game script
└── README.md          # Project documentation
```

---

## 🧠 How It Works

| Function | Description |
|---|---|
| `get_valid_guess()` | Loops until the user inputs a valid integer between 1–100 |
| `play_game()` | Runs a single round — generates number, handles guesses and hints |
| `__main__` block | Entry point — supports multiple rounds with the play-again loop |

---

## 🚀 How to Run Locally

Clone the repository:
```bash
git clone https://github.com/Khushi6307/number-guessing-game.git
```
Navigate to the directory:
```bash
cd number-guessing-game
```
Run the script:
```bash
python main.py
```

---

## 🖥️ Sample Output

```
=== 🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯 ===
Guess the number (1-100): 50
📈 Higher number please! (9 attempts left)
Guess the number (1-100): 75
📉 Lower number please! (8 attempts left)
Guess the number (1-100): 63
🎉 Congratulations! You guessed the number 63 correctly in 3 attempts!

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye. 👋
```

---

## 💻 Tech Used

- **Language:** Python 3
- **Module:** `random` (built-in)
- **Input handling:** `try-except` for safe validation

---

## 👩‍💻 Author

**Khushi Sharma**
GitHub: https://github.com/Khushi6307
