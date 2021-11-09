# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 16:08:26 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 23:12:10 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from time import sleep

if __name__ == "__main__":
 
    #Classes importation
    sys.path.append(".")
    from recipe import Recipe
    from book import Book

    #New variable of class Recipe
    test = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    #Print the attributes of the class
    print(test.name);
    print(test.cooking_lvl);
    print(test.cooking_time);
    print(test.ingredients);
    print(test.description);
    print(test.recipe_type);
    #Error management
    print("\nERRORS MANAGEMENT")
    test = Recipe()
    test = Recipe(1, 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    test = Recipe("", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    test = Recipe("Pizza", 0, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    test = Recipe("Pizza", 9, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    test = Recipe("Pizza", 3, -10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    test = Recipe("Pizza", 3, 10, "Pizza pasta Tomato salsa Mozarella", "It's delicious", "lunch")
    test = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella", 5], "It's delicious", "lunch")
    test = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], 4, "lunch")
    test = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "dinner")
    #Print the recipe with the class method str
    print()
    test = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    to_print = str(test)
    print(to_print)

    #Create a cookbook with the new class
    cookbook = Book("book")
    #Add a new recipe in te book
    recipe_to_add = Recipe("Pizza", 3, 10, ["Pizza pasta", "Tomato salsa", "Mozarella"], "It's delicious", "lunch")
    cookbook.add_recipe(recipe_to_add)
    #Check the dates 
    print(cookbook.creation_date)
    print(cookbook.last_update)
    sleep(1)
    #Add a new recipe in te book
    recipe_to_add = Recipe("Pates", 2, 10, ["Pasta", "Butter"], "Al dente", "starter")
    cookbook.add_recipe(recipe_to_add)
    #Add a new recipe in te book
    recipe_to_add = Recipe("Pates2", 2, 10, ["Pasta", "Butter"], "Al dente", "starter")
    cookbook.add_recipe(recipe_to_add)
    print(cookbook.recipes_list)
    #Check the dates 
    print(cookbook.creation_date)
    print(cookbook.last_update)
    #Get all the recipes in the starter dictionary
    cookbook.get_recipes_by_types("starter")
    #Print the recipe of 'Pates'
    cookbook.get_recipe_by_name("Pates")
