# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 23:19:51 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 23:53:41 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Parent class
class GotCharacter:
    def __init__(self, name):
        self.first_name = name
        self.is_alive = True

# Child class that inherits of the GotCharacter class
class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

if __name__ == "__main__":
    arya = Stark("Arya");
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)

