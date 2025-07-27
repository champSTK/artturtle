# 🐢 Art Turtle

Welcome to the **Art Turtle**, a fun and visual Python app where you control a turtle to create digital drawings using keyboard input and colorful brushes.

This project is a modern, extended version of a beginner turtle art app I made when I first started learning Python. It now supports saving projects, loading previous work, color selection, shape changes, and exporting artwork as PNG images.

---

## ✨ Features

- 🎨 Move the turtle using keyboard keys (WASD or arrow keys)
- 🖌️ Brush color selection (with keyboard shortcuts)
- 🧭 Diagonal movement support (Q, E, Z, C)
- 🐢 Change turtle brush shape (Arrow, Circle, Turtle, etc.)
- 💾 Save/Load your artwork as `.json` projects
- 🖼 Export your canvas as a `.png` image
- 🧽 Eraser mode toggle via middle mouse click
- 🔄 Persistent project loading via start screen
- ✅ Clean UI and responsive canvas
- 🐍 Fully written in Python using `tkinter` and `turtle`

---

## 🎮 Controls

### Movement:
-  `WASD`: Move turtle
-  `Arrow up key`: move in a straight line
- `Q/E/Z/C`: Diagonal movement

### Color shortcuts:
- `B`: Blue
- `G`: Green
- `R`: Red
- `L`: Black
- `Y`: Yellow
- `O`: Orange

### Mouse:
- `Left click`: Pen up
- `Right click`: Pen down
- `Middle click`: Toggle eraser mode

---

## 📁 File Menu

- **Save Project** – Save your drawing steps (`.json`)
- **Load Project** – Reload previous drawings
- **Save as Image** – Capture canvas as `.png`
- **Exit** – Close the app

---

## Version

- artmainoldv.py(old)
- artone.py(latest)

## 🛠 Requirements

- Python 3.10+
- Required libraries:
  ```bash
  pip install pillow
