# 🏓 Pong

A classic Pong game built with Python's `turtle` module. This project is part of my **100 Days of Code** challenge.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-orange)
![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)

> ⚠️ **Work in progress** — this project is still under active development. Some features (like collision edge-cases and game-over handling) are not fully finished yet.

## About

A two-player recreation of the classic Pong arcade game. Each player controls a paddle and tries to score by getting the ball past their opponent's side of the screen.

## Features

- Two independently controlled paddles
- Ball movement with wall bouncing
- Paddle collision bounce
- Live scoreboard for both players
- Currently missing: game-over screen, win condition, ball speed increase over time

## How to Play

- **Right paddle:** `Up` / `Down` arrow keys
- **Left paddle:** `W` / `S` keys
- The ball bounces off the top and bottom walls, and off the paddles
- Score a point when the ball passes your opponent's side
- First to reach a set score should win *(win condition not yet implemented)*

## Project Structure
- main.py         # Game loop and main logic
- ball.py         # Ball class: movement and bounce logic
- paddle.py       # Paddle class: paddle movement
- scoreboard.py   # Scoreboard class: score tracking and display



## Known Issues / To Do

- [ ] Add game-over screen and win condition
- [ ] Increase ball speed after paddle hits
- [ ] Fine-tune paddle/ball collision boundaries
- [ ] Add restart functionality

## Built With

- [Python](https://www.python.org/) — programming language
- [turtle](https://docs.python.org/3/library/turtle.html) — built-in graphics library

## Part of 100 Days of Code

This project was built as part of the **100 Days of Code** challenge, a commitment to code every day for 100 days while building real projects to practice and improve Python skills.

