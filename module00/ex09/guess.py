# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 11:47:46 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 12:24:40 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import random

def atoi(str):
    number = 0
    sign = 1;
    if (str[0] == '-'):
        sign = -1;
        str = str[1:];
    elif (str[0] == '+'):
        str = str[1:];
    if (len(str) == 0):
        return None;
    i = 0
    while (i < len(str)):
        if (str[i] >= '0' and str[i] <= '9'):
            number = number * 10 + (ord(str[i]) - ord('0'))
        else:
            return None;
        i = i + 1
    return (sign * number);

def guess():
    instructions = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n"""
    print(instructions)
    try_number = 1
    random_number = random.randint(1, 99)
    while (1):
        choice = input("What's your guess between 1 and 99?\n>> ")
        if (choice == 'exit'):
            return ;
        choice = atoi(choice)
        if (choice == None):
            print("That's not a number");
        elif (choice > random_number):
            print("Too high!");
        elif (choice < random_number):
            print("Too low!");
        else:
            if (choice == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if (try_number == 1):
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in", try_number, "attempts!")
            return ;
        try_number += 1

if __name__ == "__main__":
    guess();
