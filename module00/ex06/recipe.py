# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 17:17:02 by cmariot           #+#    #+#              #
#    Updated: 2021/11/08 21:03:27 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_keys(dictionary):
    for keys, values in cookbook[dictionary].items():
        print(keys)

def print_values(dictionary):
    for keys, values in cookbook[dictionary].items():
        print(values)

def print_keys_and_values(dictionary):
    for keys, values in cookbook[dictionary].items():
        print(keys, ":", values)

def print_recipe(recipe_name):
    print("Recipe for", recipe_name, ":")
    print("Ingredient list :", cookbook[recipe_name]['ingredients'])
    print("To be eaten for", cookbook[recipe_name]['meal'])
    print("Takes", cookbook[recipe_name]['prep_time'], "of cooking.");

def del_recipe(recipe_name):
    del cookbook[recipe_name]
    print(recipe_name, "has been deleted from cookbook.");

def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {}
    cookbook[recipe_name]['ingredients'] = ingredients
    cookbook[recipe_name]['meal'] = meal 
    cookbook[recipe_name]['prep_time'] = prep_time

def print_recipes_names():
    for id, value in cookbook.items():
        print(id)

if __name__ == "__main__":
    #Initial Cookbook
    cookbook = {'sandwich' : {'ingredients': 'ham, bread and tomatoes', 'meal': 'lunch', 'prep_time': '10 minutes'},
                "cake" : {'ingredients': 'flour, suggar and eggs', 'meal': 'dessert', 'prep_time': '60 minutes'},
               "salad" : {'ingredients': 'avocado, arugula, tomatoes and spinach', 'meal': 'lunch', 'prep_time': '15 minutes'}}
    
    while 1:
        print("""Please select an option by typing the corresponding number:
        1: Add a recipe
        2: Delete a recipe
        3: Print a recipe
        4: Print the cookbook
        5: Quit\n""")
        choice = input(">> ")
        if choice == "1":
            recipe_name = input("Recipe name ? ")
            ingredients = input("What are the ingredients ? ")
            meal = input("When will we eat it ? ")
            prep_time = input("How long for this recipe preparation ? ")
            add_recipe(recipe_name, ingredients, meal, prep_time);
            print("\nRecipe added.\n");
            print_recipe(recipe_name);
            print("\n");
        elif choice == "2":
            recipe_name = input("Which recipe to delete ? ")
            del_recipe(recipe_name)
        elif choice == "3":
            recipe_name = input("Which recipe would you like to see ? ");
            print_recipe(recipe_name);
            print("\n");
        elif choice == "4":
            print("List of recipes :");
            print_recipes_names();
            print("\n");
        elif choice == "5":
            break ;
        else:
            print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")

