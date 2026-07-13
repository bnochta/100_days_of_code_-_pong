# 🏓 Pong

A classic Pong game built with Python's `turtle` module. This project is part of my **100 Days of Code** challenge.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-orange)

## About

A two-player recreation of the classic Pong arcade game. Each player controls a paddle and tries to score by getting the ball past their opponent's side of the screen. First player to reach 5 points wins.

## Features

- Two independently controlled paddles
- Ball movement with wall and paddle bouncing
- Ball speed increases after each paddle hit
- Ball resets to the center with a random direction after each point
- Live scoreboard tracking both players' scores
- Win condition: first to 5 points wins, with a "WINS!" message displayed

## How to Play

- **Right paddle:** `Up` / `Down` arrow keys
- **Left paddle:** `W` / `S` keys
- The ball bounces off the top and bottom walls, and off the paddles
- The ball speeds up slightly every time it hits a paddle
- Score a point when the ball passes your opponent's side
- First player to reach 5 points wins the game

## Project Structure
- main.py         # Game loop and main logic
- ball.py         # Ball class: movement, bounce logic, and speed increase
- paddle.py       # Paddle class: paddle movement
- scoreboard.py   # Scoreboard class: score tracking, display, and win detection

## Possible Future Improvements

- [ ] Limit paddle movement to stay within screen bounds
- [ ] Add restart functionality after a win

## Built With

- [Python](https://www.python.org/) — programming language
- [turtle](https://docs.python.org/3/library/turtle.html) — built-in graphics library

## Part of 100 Days of Code

This project was built as part of the **100 Days of Code** challenge, a commitment to code every day for 100 days while building real projects to practice and improve Python skills.