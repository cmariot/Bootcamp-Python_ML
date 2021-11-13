# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/11 00:04:38 by cmariot           #+#    #+#              #
#    Updated: 2021/11/13 15:09:53 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from random import random

def generator(text, sep, option = None):
    if (option == None):
        text = text.split(sep);
        for word in text:
            yield word

if __name__ == "__main__":
    #Program without option
    if (len(sys.argv) == 3):
        for word in generator(sys.argv[1], sys.argv[2]):
            print(word)
    #If there is an option create a list, add words to the list
    elif (len(sys.argv) == 4):
        words = []
        for word in generator(sys.argv[1], sys.argv[2]):
            words.append(word)
        option = sys.argv[3]
        # Shuffle the words and print them
        if (option == "shuffle"):
            shuffled = sorted(words, key=lambda x: random())
            for word in shuffled:
                print(word)
        # Remove the words that aren't unique
        elif (option == "unique"):
            unique = []
            for item in words:
                if item not in unique:
                    unique.append(item)
            for word in unique:
                print(word)
        elif (option == "ordered"):
            words.sort()
            for word in words:
                print(word)
        else:
            print("ERROR")
    else:
        print("Error, usage :\n\tpython generator.py 'text' 'sep' 'option'")

