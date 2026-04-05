# Pong by Dishita

Two players. One keyboard. A ball that does not forgive sloppy paddle placement.

Play in your browser: https://your-live-link-here.netlify.app — no install required.

---

## Two Versions One Game

This repo contains two implementations of the same game — the original Python build and a browser native web version built so anyone can play it via a shareable link.

---

## Version 1 — Python (main.py)

Built with Python 3.11 and the turtle module. No external dependencies.

- wn.tracer(0) and wn.update() for manual frame control and smooth animation
- Ball physics via dx and dy delta values reversed on collision
- Coordinate range collision detection for walls and paddles
- Paddle boundary clamping to prevent off screen movement
- winsound bounce audio (Windows only commented out for cross platform compatibility)
- Win condition at 10 points with clean loop exit

Run locally:

git clone https://github.com/dishita-b/pong_db.git
cd pong_db
python main.py

Controls: W and S for Player A | Arrow Up and Down for Player B | Q to Quit

---

## Version 2 — Web (index.html)

Vanilla HTML CSS and JavaScript. Single file. No frameworks no build tools.

- requestAnimationFrame() game loop for display synced frames
- HTML5 Canvas 2D API for rendering
- State based keydown and keyup input handling (smoother than event driven)
- Progressive ball speed — each paddle hit multiplies dx by 1.05
- Paddle hit position influences exit angle via dy offset
- Speed clamped at dx ±12 and dy ±8 to keep gameplay fair
- Arcade visual design with scanline overlay glow effects Orbitron font and cyan orange color coding per player

Controls: W and S for Player A | Arrow Up and Down for Player B | SPACE to Replay

---

## Tech Comparison

| | Python | Web |
|---|---|---|
| Loop | while True with manual update | requestAnimationFrame() |
| Rendering | turtle module | HTML5 Canvas |
| Input | onkeypress() | keydown and keyup state |
| Physics | Fixed delta reversal | Progressive speed and angle |
| Sound | winsound Windows only | — |
| Deployment | Local only | Shareable link |

---

## Author

Dishita Barman
LinkedIn: https://www.linkedin.com/in/dishita-barman5/
GitHub: https://github.com/dishita-b
