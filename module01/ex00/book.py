# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 16:08:31 by cmariot           #+#    #+#              #
#    Updated: 2021/11/09 23:11:40 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

class Book:

    def __init__(self, name):
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.name = name
        self.recipes_list = {"starter" : {}, "lunch" : {}, "dessert" : {}}
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for type in self.recipes_list:
            for key in self.recipes_list[type]:
                if key == name:
                    txt = name + " recipe :\n"
                    txt += "Recipe type : " + type + "\n"
                    txt += "Ingrediens : "
                    for ingredient in self.recipes_list[type][name]["ingredients"]:
                        txt += ingredient + ", "
                    txt = txt[:-2] + "\n"
                    txt += "You must have a cooking lvl of " + str(self.recipes_list[type][name]["cooking_lvl"]) + ", "
                    txt += "and " + str(self.recipes_list[type][name]["cooking_time"]) + " minutes of your time.\n"
                    txt += "Description : " + self.recipes_list[type][name]["description"] 
                    print(txt)
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in self.recipes_list[recipe_type]:
            print(key)
        pass ;

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type][recipe.name] = {"name":recipe.name, "cooking_lvl":recipe.cooking_lvl, "cooking_time":recipe.cooking_time, "ingredients":recipe.ingredients, "description":recipe.description, "recipe_type":recipe.recipe_type}
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pass
