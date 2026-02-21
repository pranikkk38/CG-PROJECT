# 🎮 Maze Runner Game

**Python | Pygame | 2D Game Development**

---

## 📌 Project Overview

This project is a 2D Maze Runner game developed using **Pygame**.  
The player controls a character and must navigate through a maze, avoid enemies, and reach the goal to win.

**The game includes:**

- 🕹️ Keyboard-controlled player movement  
- 🧱 Wall-based maze structure  
- 👾 Multiple enemies  
- 🏁 Goal-based winning system  
- 🔁 Restart functionality  
- 📢 Win/Lose messages  

---

## 🎯 Game Objective

- Move the player using arrow keys  
- Avoid colliding with enemies  
- Reach the goal to win  
- Restart the game after win or loss  

---

## 📂 Project Structure
Maze_Runner/
│
├── assets/
│ ├── player.png
│ ├── goal.png
│ ├── enemy1.png
│ ├── enemy2.png
│ └── enemy3.png
│
├── main.py
└── README.md

---


## ⚙️ Requirements

Make sure **Python** is installed on your system.  

Install **Pygame**:

pip install pygame

---
▶️ How to Run
Step 1: Download or Clone the Project
git clone https://github.com/your-username/Maze_Runner.git
cd Maze_Runner

Or download and extract the ZIP file.

Step 2: Place Image Files

Ensure the following image files are in the assets/ folder:
player.png  
goal.png  
enemy1.png  
enemy2.png  
enemy3.png

Step 3: Run the Program
python main.py

---

🖼️ Output / Screenshots
Game interface

<img width="741" height="777" alt="maze_start" src="https://github.com/user-attachments/assets/7960483d-77a2-466d-8566-01322f44c14d" />

---

Win Interface

<img width="725" height="770" alt="win" src="https://github.com/user-attachments/assets/38c94132-1214-4dc8-af8e-4e3ec83de960" />

---

Loss Interface

<img width="739" height="773" alt="loss" src="https://github.com/user-attachments/assets/66a7a77f-02a8-454c-bba1-4c131a4bb5e4" />

---

🎮 Controls
| Key            | Action       |
| -------------- | ------------ |
| ⬅️ Left Arrow  | Move Left    |
| ➡️ Right Arrow | Move Right   |
| ⬆️ Up Arrow    | Move Up      |
| ⬇️ Down Arrow  | Move Down    |
| R              | Restart Game |
| ❌ Close Button | Exit Game    |

---

📷 Game Features

🧱 Maze Walls: Walls restrict player movement and form the maze.
👾 Enemies: Multiple enemies act as obstacles.
🏁 Goal Area: Reaching the goal completes the game.
🔁 Restart System: Players can restart after winning or losing.
📢 Game Messages: Win and lose messages are displayed on the screen.

---

⚙️ Technical Implementation

Game window created using Pygame display module
Movement handled through keyboard input
Collision detection using pygame.Rect and colliderect()
Game states managed using boolean variables
Rendering done using blit() and display.update()
Frame rate controlled using clock.tick(60)

---

📚 Learning Outcome

Through this project, I learned:

✔️ Basics of game development in Python
✔️ Working with Pygame library
✔️ Implementing game loops
✔️ Handling keyboard input
✔️ Collision detection techniques
✔️ Game state management
✔️ Object-based programming

---

👨‍💻 Author

Pranik Baral
https://github.com/pranikkk38

---






