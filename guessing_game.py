"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
import statistics

def start_game():
    print("Welcome to the random number guessing game")

    random_number = random.randint(1, 10)
    game_over = False
    guess_attempts = []
    current_game_guess_attempts = []
    high_score = 0

    while game_over == False:
        # Handle display of high score at the beginning of the game
        if (len(guess_attempts) == 0):
            if high_score == 0:
                print("There is currently no high score\n")
            else:
                print(f'The current high score is {high_score}\n')

        player_input = input('Guess the random number: ')

        # Check if the input by the player can be parsed into an integer, do not allow strings or floats
        try:
            valid_number_check = int(player_input)
        except ValueError:
            print(f"'{player_input}' is not a valid number. Please do not enter letters or decimals")
            continue

        if valid_number_check == random_number:
            guess_attempts.append(valid_number_check)
            current_game_guess_attempts.append(valid_number_check)

            # Handles first run through
            if high_score == 0:
                high_score = len(guess_attempts)
            # if the new score is less than previous score, set the new high score
            if len(guess_attempts) < high_score:
                high_score = len(guess_attempts)
            
            print("Congratulations you won the game!")
            print(f'It took you {len(current_game_guess_attempts)} to guess the correct number for this game')
            print(f'The mean of all the numbers you guessed is {statistics.mean(guess_attempts)}')
            print(f'The median of all the numbers you guessed is {statistics.median(guess_attempts)}')
            print(f'The mode of all the numbers you guessed is {statistics.mode(guess_attempts)}')

            # Handles playing again
            will_player_play_again_answered = False
            while will_player_play_again_answered == False:
                play_again_prompt = input('\nWould you like to play again (Y/N): ')
                if play_again_prompt.lower() == "y":
                    current_game_guess_attempts = []
                    random_number = random.randint(1, 10)
                    will_player_play_again_answered = True
                elif play_again_prompt.lower() == "n":
                    print("The game is over, Thank you for playing!")
                    will_player_play_again_answered = True
                    return
                else:
                    print("Sorry please enter Y or N")
        
        # Handle out of range numbers
        elif valid_number_check > 10 or valid_number_check < 0:
            print("The number that you have entered is out of range")
            guess_attempts.append(valid_number_check)
            current_game_guess_attempts.append(valid_number_check)
        elif valid_number_check > random_number:
            print("It's lower")
            guess_attempts.append(valid_number_check)
            current_game_guess_attempts.append(valid_number_check)
        elif valid_number_check < random_number:
            print("It's higher")
            guess_attempts.append(valid_number_check)
            current_game_guess_attempts.append(valid_number_check)
    return 

start_game()
