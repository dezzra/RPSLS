# Introduction to Interactive Programming in Python
# Week 1 Mini-Project: Rock Paper Scissors Lizard Spock

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(player_choice):
    if player_choice == "rock":
        return 0
    elif player_choice == "Spock":
        return 1
    elif player_choice == "paper":
        return 2
    elif player_choice == "lizard":
        return 3
    elif player_choice == "scissors":
        return 4
    else:
        print("Error: Invalid player choice.")
    
def number_to_name(comp_number):
    if comp_number == 0:
        return "rock"
    if comp_number == 1: 
        return "Spock"
    if comp_number == 2:
        return "paper"
    if comp_number == 3:
        return "lizard"
    if comp_number == 4:
        return "scissors"

def rpsls(player_choice): 
    
    print("Player chooses " + player_choice)
    
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    
    comp_choice = number_to_name(comp_number)
    
    print("Computer chooses " + comp_choice)
    
    if (comp_number + 1) % 5 == player_number:
        print("Player wins!")
    elif (comp_number + 2) % 5 == player_number:
        print("Player wins!")
    elif comp_number == player_number:
        print("It's a tie.")
    elif (comp_number + 3) % 5 == player_number:
        print("Computer wins!")
    elif (comp_number + 4) % 5 == player_number:
        print("Computer wins!")
    else: 
        print("Error! Nobody wins.")
    print("")

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

rpsls("fork")
