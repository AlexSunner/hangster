# Hangster
Welcome to Hangster, a command-line Hangman game implemented in Python! 
Hangster provides an entertaining and challenging experience where players can test
their word-guessing skills while enjoying the classic game of Hangman.

## Overview
Hangster offers three difficulty levels—easy, medium, and hard—each with its own set of words to guess. Players are prompted to choose a difficulty level, and from there, the game unfolds as they attempt to guess the hidden word letter by letter. The game includes ASCII art for the Hangman and provides feedback on correct and incorrect guesses.

## Live Website
[Hangster](https://hangster-f7c352ecfda2.herokuapp.com/)

## Repository
[GitHub Repository](https://github.com/AlexSunner/hangster)

## UX & Design

### User Stories
Choosing a Difficulty:
As a player, I want to select a difficulty level at the start of the game to tailor the challenge to my skill level.

Interactive Gameplay:
As a player, I want to guess letters interactively to uncover the hidden word and enjoy an engaging gaming experience.

Visual Feedback:
As a player, I want to see visual representations of the Hangman for correct and incorrect guesses to track my progress.

Game Over Scenario:
As a player, I want the game to end when I run out of attempts, displaying the correct word, to know the outcome.

Error Handling:
As a player, I want clear error messages for invalid inputs (e.g., difficulty level) so that I can correct and continue playing.

Replayability:
As a player, I want the option to replay the game with different difficulty levels and word sets for continued challenge and enjoyment.

### Logic Flow
I created this visual representation of the game logic. Follow the flowchart to understand the dynamic interactions and decision points that shape
the player's experience in this classic Hangman game.

![Flowchart](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/flowchart.jpg)

## Features
### Difficulties
Choose from easy, medium and hard difficulty levels, each with its unique set of words.

![Difficulty](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/difficulty1.jpg)

### Max Attempts
Navigate the challenge of Hangster as you make strategic guesses, mindful of the limited attempts available before facing the consequences.

![Max Attempts](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/attempts2.jpg)

### Winning Scenario
Celebrate your victory in Hangster by successfully guessing the word, unlocking the winning scenario and showcasing your word-guessing prowess.

![Winning](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/congratulations4.jpg)

### Game Over Scenario
Witness the outcome of your gameplay journey in the game over scenario, where the correct word is revealed, marking the end of your Hangster adventure.

![Game Over](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/gameover3.jpg)

### Error Handling
User-friendly error messages guide players in case of invalid inputs, ensuring a smooth gaming experience.

## Python Libraries Used
### random
This module provides functions for generating pseudo-random numbers. In the Hangster game, it's used to randomly select a word from a predefined list.

## Technologies Used
### Python
The contents and structure of the game was built in Python.

### Developing Tools Used
[Gitpod](https://www.gitpod.io/) was employed as the integrated development environment (IDE) for this project, providing a seamless and collaborative coding environment accessible through a web browser.

[GitHub](https://github.com/) was utilized for code storage and version control, enabling the management of commits and facilitating collaborative development for the Hangman game.

[Heroku](https://heroku.com/) served as the platform for deploying the Hangman game, enabling the project to be accessible online and showcasing the game to a broader audience.

