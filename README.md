
# 🧩 Maze Generator & Solver (Pygame)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-Game%20Dev-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

A Python + Pygame project that visually demonstrates a **perfect maze generator and solver** using Depth-First Search (DFS) and backtracking.

The project focuses on algorithm visualization, showing how a maze is built and solved step by step in real time.

---

## 🎯 Project Features

* 🧠 Perfect maze generation using DFS (stack-based backtracking)
* 🔴 Real-time maze solving using backtracking algorithm
* 🟢 Green dot shows current generation position
* 🔴 Red dot shows current solver position
* 🔵 Blue cells show dead-end paths during solving
* 🧱 Grid-based maze representation using `northWall` and `eastWall`
* 🎬 Smooth animated visualization with controlled speed

---

## 📁 Project Structure

```
graphics_project/
│
├── main.py   # Pygame loop and visualization control
├── maze.py   # Maze generation and solver logic
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install pygame
```

---

## ▶️ How to Run

Run the program using:

```bash
python main.py
```

---

## 🧠 How It Works

### 🟢 Maze Generation (DFS Algorithm)

* Start with a full grid where all walls exist
* Begin at cell (0, 0)
* Check unvisited neighboring cells
* Randomly choose one neighbor
* Remove the wall between current and chosen cell
* Push current cell into a stack
* If no neighbors exist → backtrack using stack
* Repeat until all cells are visited

This ensures a **perfect maze (no cycles, fully connected)**.

---

### 🔴 Maze Solving (Backtracking Algorithm)

* Start from the entrance (left side of maze)
* Move through open paths (no walls)
* Use a stack to track the path
* If a dead end is reached:

  * Mark it as a blue cell
  * Backtrack to previous position
* Continue until reaching the exit (right side)

---

## 🎨 Visualization Guide

| Element      | Color | Meaning                     |
| ------------ | ----- | --------------------------- |
| 🟢 Green dot | Green | Current generation position |
| 🔴 Red dot   | Red   | Current solver position     |
| 🔵 Blue cell | Blue  | Dead-end / backtracked path |

---

## ⏱️ Animation Control

You can control speed using:

* `clock.tick(30)` → controls FPS
* `time.sleep(0.03)` → slows generation and solving steps

Increase values → slower animation
Decrease values → faster animation

---

## 🧱 Core Concepts Used

* Depth-First Search (DFS)
* Stack-based backtracking
* Grid-based maze representation
* Wall system using:

  * `northWall`
  * `eastWall`
* Real-time visualization with Pygame
* Algorithm simulation and animation

---

## 🚀 Possible Improvements

* 🎚️ Add speed control slider
* ⏯️ Pause / resume functionality
* 🟡 Highlight final shortest path
* 🎮 Keyboard interaction for stepping
* 🔊 Sound effects for movement
* 📏 Custom maze size input

---

## 👨‍💻 Author

* **Name:** Selamawit Mulat
* **Email:** [selamawitmulat138@gmail.com](mailto:selamawitmulat138@gmail.com)
* **GitHub:** SelamawitMulat
* **Class ID:** UGR/1033/16
* **Section:** 1

---

## 📚 Learning Goals

This project demonstrates understanding of:

* Graph traversal algorithms (DFS)
* Backtracking techniques
* Real-time graphics rendering with Pygame
* Grid-based data structures
* Algorithm visualization principles

