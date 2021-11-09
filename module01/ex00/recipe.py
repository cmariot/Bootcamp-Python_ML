# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 16:08:28 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 19:53:53 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Recipe:

    def __init__(*args):    
        #Arguments check
        if (len(args) != 7):
            print("""ERROR, class definition :
            \rpizza = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")""")
            return ;
        self = args[0]
        name = args[1]
        cooking_lvl = args[2]
        cooking_time = args[3]
        ingredients = args[4]
        description = args[5]
        recipe_type = args[6]
        #Name
        if (type(name) == str):
            if (len(name) > 0):
                self.name = name;
            else:
                print("The recipe name is empty ...")
                return ;
        else:
            print("The name must be a str.")
            return ;
        #Cooking lvl
        if (type(cooking_lvl) == int):
            if (cooking_lvl >= 1 and cooking_lvl <= 5):
                self.cooking_lvl = cooking_lvl;
            else:
                print("the cooking lvl must be sup. at 1 and inf. at 5");
                return ;
        else:
            print("The cooking lvl must be an int");
            return ;
        #Cooking time
        if (type(cooking_time) == int):
            if (cooking_time >= 0):
                self.cooking_time = cooking_time;
            else:
                print("The cooking_time must be > 0")
                return ;
        else:
            print("The cooking time must be an integer");
            return ;
        #Ingredients
        if (type(ingredients) == list):
            i = 0;
            while (i < len(ingredients)):
                if (type(ingredients[i]) != str):
                        print("The ingredients list must only composed by str");
                        return ;
                i += 1;
            self.ingredients = ingredients;
        else:
            print("The ingredients must be in a list");
            return ;
        #Description
        if (type(description) == str):
            self.description = description;
        else:
            print("The description must be a str");
            return ;
        #Recipe_type
        if (type(recipe_type) == str):
            if (recipe_type == 'starter' or recipe_type == 'lunch' or recipe_type == 'dessert'):
                self.recipe_type = recipe_type;
            else:
                print("The recipe_type must only be a 'starter', 'lunch' or 'dessert'")
                return ;
        else:
            print("The recipe_type must be a str");
            return ;

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.name + " recipe :\n"
        txt += "Recipe type : " + self.recipe_type + "\n"
        txt += "Ingrediens : "
        for ingredient in self.ingredients:
            txt += ingredient + ", "
        txt = txt[:-2] + "\n"
        txt += "You must have a cooking lvl of " + str(self.cooking_lvl) + ", "
        txt += "and " + str(self.cooking_time) + " minutes of your time.\n"
        txt += "Description : " + self.description
        return txt
