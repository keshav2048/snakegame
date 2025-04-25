# 🐍 Snake Game – Python (Turtle Graphics)

A simple, classic Snake game built with Python's `turtle` module. Move the snake, eat the food, and grow your score — but don’t run into yourself!

---

## 🎮 Features

- Real-time control using arrow keys
- Snake grows with each food eaten
- Game ends if the snake hits itself
- Score is displayed and saved to a `.txt` file
- Clean structure: split into modules (`food.py`, `snake.py`, `scoreboard.py`)

---

## 🧠 Tech Stack

- Python 3.x
- `turtle` (standard library)

---

## 📂 Project Structure

```bash
snake-game/
│
├── snake game.py        # Main game loop
├── snake.py             # Snake movement logic
├── food.py              # Food generation logic
├── scoreboard.py        # Score display and tracking
├── score.txt            # Stores high score
├── __pycache__/         # Python cache (ignored)
└── .idea/               # IDE config (optional, can be ignored)
