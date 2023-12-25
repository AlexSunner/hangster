# Hangster
Welcome to Hangster, a command-line Hangman game implemented in Python! 
Hangster provides an entertaining and challenging experience where players can test
their word-guessing skills while enjoying the classic game of Hangman.

![Mockup](https://raw.githubusercontent.com/AlexSunner/hangster/main/images/mockup.jpg)

## Overview
Hangster offers three difficulty levels — easy, medium, and hard — each with its own set of words to guess. Players are prompted to choose a difficulty level, and from there, the game unfolds as they attempt to guess the hidden word letter by letter. The game includes ASCII art for the Hangman and provides feedback on correct and incorrect guesses.

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

### Code Validator
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the code.

Errors were found and handled correctly (lines of code being too long).

### Other Resources Used
[Google](https://google.com/) was a valuable resource throughout the project, providing insights into Python syntax, game development best practices, and troubleshooting specific challenges.

[Slack](https://slack.com/) served as a collaborative platform, allowing me to seek advice from the programming community, share progress updates, and receive timely feedback on coding challenges encountered during the Hangster game development.

I supplemented my learning by watching Python tutorials on [YouTube](https://youtube.com/), gaining insights into the basic structure and syntax of the language from experienced developers and educators.

## Testing
### Unit Testing
1. Function: choose_word(difficulty)
- Scenario: Ensure the function returns a valid word based on the chosen difficulty level.
- Procedure: Call the function with various difficulty levels and check if the returned word is in the corresponding word list.

2. Function: display_word(word, guessed_letters)
- Scenario: Confirm that the function correctly displays the current state of the word with guessed letters.
- Procedure: Test the function with different words and guessed letter combinations.

3. Function: print_hangman_art(incorrect_attempts)
- Scenario: Verify that the function prints the correct Hangman ASCII art based on the number of incorrect attempts.
- Procedure: Call the function with different values of incorrect_attempts and check if the printed art matches the expected result.

### Integration Tests

1. Game Initialization
- Scenario: Ensure the game initializes correctly with user input for difficulty.
- Procedure: Provide valid and invalid inputs for difficulty during game initialization and verify that the game prompts the user appropriately.

2. Letter Guessing
- Scenario: Confirm that the game handles letter guessing correctly.
- Procedure: Guess both correct and incorrect letters and check if the game responds accordingly, updating the display and guessed letters.

3. Game Over and Winning Conditions
- Scenario: Verify that the game ends correctly when the maximum attempts are reached or when the word is guessed.
- Procedure: Play the game to completion under different conditions and ensure that the correct end messages are displayed.

### User Interface (UI) Testing

1. Color Display
- Scenario: Check if colored text is displayed correctly in the console.
- Procedure: Run the game and confirm that the colored text for messages, prompts, and ASCII art is visually appealing.

2. Input Validation
- Scenario: Validate user input for difficulty and letter guessing.
- Procedure: Enter valid and invalid inputs during different stages of the game and ensure the game responds appropriately.

## Deployment
The Hangman game is deployed on Heroku, providing a convenient way for users to access and enjoy the game.
[Hangster Game](https://hangster-f7c352ecfda2.herokuapp.com/)

### Deploying to Heroku
1. Log into Heroku website.
2. From the Dashboard page, select "New" and then "Create new app."
3. Assign a name for the application, select the region and then select "Create app."
4. Once the application is created, from the submenu at the top, select "Settings" and then "Reveal Config Vars" to set up config vars.
5. In the KEY input field, enter "PORT" all in capitals and enter "8000" for the VALUE input field and select "Add." If there are other config vars required to run the application, add those here. For this application, there is no other config var required.
6. Scroll down to the "Buildpacks" section and select "Add buildpack."
7. Add buildpacks required to run the application. For this application, "Python" and "Nodejs" are required.
The order of the buildpacks is important. "Python" should be the first and then "Nodejs." If they are not in the correct order, click and drag to change.
8. Select "Deploy" from the submenu at the top.
Under the "Deployment method" section, select "GitHub" to connect to GitHub.
Under the "Connect to GitHub" section, enter the name of the repository and select "Search."
Once the repository is located, select "Connect" to connect the repository to the application within Heroku.
9. Select either "Enable Automatic Deploys" which will deploy a new version of the application every time changes are pushed to GitHub or opt for "Manual Deploy." For this application, "Automatic Deploys" was selected.
10. Once the application is deployed, scroll back to the top of the screen and select "Open app."
If "Enable Automatic Deploys" has been selected, the application will be built and available after the next changes are pushed to GitHub.

### Local Deployment
If you prefer to run the game locally on your machine, follow these steps:

1. Clone the Repository:
- Clone the Hangster game repository from GitHub to your local machine using the following command in the terminal: git clone https://github.com/AlexSunner/hangster.git

2. Install Dependencies:
- Install the necessary dependencies by running the following command in the terminal: pip install -r requirements.txt

3. Run the Game:
- Execute the game script by running the following command in the terminal: python3 run.py

4. Enjoy the Hangster Experience:
- Have fun playing Hangster locally on your machine!

### Forking the GitHub Repository
If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under your account)
3. Your repository has now been 'Forked' and you have a copy to work on

### Cloning the GitHub Repository

Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Codeanywhere or whatever editor you use & select the directory location where you would like the clone created
5. In the terminal type 'git clone' & then paste the link you copied in GitHub
6. Press enter and your local clone will be created.

## Credits

1. ASCII Art for Hangster:
- The ASCII art for the Hangster game was taken and modified from [Chris Horton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)

2. Colorful Text Printing:
- The print_color_text function, adding vibrant colors to the game, was taken from [Stack Overflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)

3. Readme Structure Inspiration:
- The structure and formatting of this README were inspired by [Shizuka Donaghue's Melting Snowman](https://github.com/ShizukaDonaghue/melting-snowman/blob/main/README.md). Special thanks for providing a clear and well-organized template. Especially the Deployment to Heroku part.

4. Game Improvement Ideas:
- Many thanks to my mentor, Harry Dhillon, for providing valuable insights and ideas that significantly contributed to the enhancement of the Hangster game.