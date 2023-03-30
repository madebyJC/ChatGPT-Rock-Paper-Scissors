import tkinter as tk
import random

# Define a dictionary to map the choice names to their index
CHOICES = {'rock': 0, 'paper': 1, 'scissors': 2}

# Define a function to get the computer's choice
def get_computer_choice():
    return random.choice(list(CHOICES.keys()))

# Define a function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice - computer_choice) % 3 == 1:
        return "You win!"
    else:
        return "Computer wins!"

# Define a function to handle the button click event
def play_game():
    # Get the player's choice
    player_choice = CHOICES[player_choice_var.get()]

    # Get the computer's choice
    computer_choice = CHOICES[get_computer_choice()]

    # Determine the winner
    result_label.config(text=determine_winner(player_choice, computer_choice))

# Create the GUI window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create the player's choice label and radio buttons
player_choice_label = tk.Label(window, text="Choose your move:")
player_choice_label.pack()

player_choice_var = tk.StringVar()
player_choice_var.set('rock')

rock_button = tk.Radiobutton(window, text='Rock', variable=player_choice_var, value='rock')
rock_button.pack()

paper_button = tk.Radiobutton(window, text='Paper', variable=player_choice_var, value='paper')
paper_button.pack()

scissors_button = tk.Radiobutton(window, text='Scissors', variable=player_choice_var, value='scissors')
scissors_button.pack()

# Create the play button
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
