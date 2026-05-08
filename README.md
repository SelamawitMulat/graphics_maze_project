# 🧩 Maze Generator & Solver (Pygame)

A Python + Pygame project that visually demonstrates a **perfect maze generator and solver** using Depth-First Search (DFS) and backtracking algorithms.

The project focuses on algorithm visualization, showing every step in real time with smooth animation.

---

## 🎯 Project Features

- 🧠 Perfect maze generation using DFS (stack-based backtracking)
- 🔴 Real-time maze solving using backtracking
- 🟢 Green dot shows current position during generation
- 🔴 Red dot shows current solver position
- 🔵 Blue cells show dead-end paths
- 🧱 Grid-based maze using north and east walls
- 🎬 Smooth animated visualization with controlled speed

---

## 📁 Project Structure


graphics_project/
│
├── main.py # Handles pygame loop and visualization
├── maze.py # Maze generation and solving logic


---

## ⚙️ Requirements

Install Python and Pygame:

```bash
pip install pygame
▶️ How to Run

Run the project using:

python main.py
🧠 How It Works
🟢 Maze Generation (DFS Algorithm)
Start with all walls intact
Begin at cell (0, 0)
Use a stack to track path exploration
Randomly select unvisited neighbors
Remove walls between connected cells
If stuck, backtrack using stack
Continue until all cells are visited
🔴 Maze Solving (Backtracking Algorithm)
Start from entrance (0, 0)
Move only through open paths (no walls)
Push each visited cell onto a stack
If a dead end is reached:
Mark it as blue
Backtrack to previous cell
Continue until reaching bottom-right goal
🎨 Visualization Guide
Element	Color	Meaning
🟢 Green dot	Generation	Current DFS generation cell
🔴 Red dot	Solver	Current solving position
🔵 Blue cell	Dead end	Backtracked path
⏱️ Animation Speed Control

The project uses controlled timing for smooth visualization:

clock.tick(30) → controls FPS (main loop speed)
time.sleep(0.03) → slows generation and solving steps

You can adjust these values to make the animation faster or slower.

🧱 Technical Concepts Used
Depth-First Search (DFS)
Stack-based backtracking
Grid-based maze representation
Wall system using:
northWall
eastWall
Real-time rendering with Pygame
Algorithm visualization techniques
🚀 Possible Improvements
🎚️ Speed control slider (user adjustable)
⏯️ Pause / resume feature
🟡 Highlight final shortest path
📏 Custom maze sizes
🔊 Sound effects for steps
🎮 Interactive controls (keyboard/mouse)
👨‍💻 Author

Built as a learning project to understand:

Algorithms (DFS & backtracking)
Game loops using Pygame
Visualization of complex logic
Grid-based systems