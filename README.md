
# 👻 Ghost Chase Game

A simple survival game built with **Pygame**.
You control a red ghost with the arrow keys while another ghost chases you randomly.
Your goal: **survive as long as possible** without colliding with the enemy ghost.

---

## 📂 Project Structure

```

ghost-chase-game/
├── README.md            # Project documentation
├── main.py              # Main game file
├── requirements.txt     # Dependencies (pygame)
├── assets/              # Images/sounds folder
│   ├── player.png
│   └── enemy.png
└── LICENSE

````

---

## ⚙️ Requirements

* Python 3.7 or higher (recommended: 3.8+)
* Pygame library

Install dependencies:

```bash
pip install pygame
````

---

## ▶️ How to Run

Save the code as `main.py` and run:

```bash
python main.py
```

Make sure the image files exist in your project (e.g., `assets/player.png` and `assets/enemy.png`).
If you run without images, Pygame will throw an error.

---

## 🎮 Controls

* **Arrow Keys**: Move the player ghost
* **Survive!**: Avoid the enemy ghost
* **Score**: Increases the longer you survive
* If collision happens → **Game Over** with your score

---

## 🕹️ Game Logic

1. **Player movement**:

   * Controlled by the arrow keys (`K_UP`, `K_DOWN`, `K_LEFT`, `K_RIGHT`).
   * Restricted within the screen boundaries.

2. **Enemy movement**:

   * Moves automatically across the screen.
   * Bounces off edges and changes direction randomly.

3. **Collision detection**:

   * Uses `rect.colliderect()`.
   * If player collides with enemy → Game Over.

4. **Score system**:

   * Score increases every frame.
   * When collision occurs, score resets to zero.

---

## 🚀 Features to Add

* [ ] High Score system (save to `highscore.txt`)
* [ ] Multiple ghosts with increasing difficulty
* [ ] Background music and sound effects
* [ ] Timer-based score instead of frame count
* [ ] Start menu and restart button

---

## 🛠️ Common Issues

**Error: `pygame.error: Couldn't open image`**
→ Make sure image files are in the correct folder and path matches.

**Error: `No available video device`**
→ Run locally on a computer with a display (not on headless server).

```

---

تحبي أضيفلك كمان **لقطة شاشة (screenshot)** أو **GIF قصير للعبة** جوه الـ README (عشان شكل الريبو يبقى جذاب أكتر)؟
```
