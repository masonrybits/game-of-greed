# Game of Greed

**Author**: Ting Luo
**Version**: 1.0.0 

## Overview
A dice game that welcomes users and takes in dices input and returns the score.

## Getting Started
The user is required to first navigating to the folder contatining the source codes. The user can then enter the virtual environment (by typing "pipenv shell") and run the source codes (by typing "python3 game_of_greed.py") and test suites (by typing "pytest") in Python3.


## Architecture
The pytest framewrok is installed for testing purpose. The counter framework in istalled for counting purpose.


## API
The Game class has attributes _print and _input that make reference to the default print and input functions, as well as a method play that returns a welcome message, a prompt and a correspoding response. A method calculate_score that counts the total score for each round of game.

## Change Log
12-10-2019 7:00 AM - Added play method to Game class & tested.