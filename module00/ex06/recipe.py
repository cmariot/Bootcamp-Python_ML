if __name__ == "__main__":
    cookbook = {sandwich = {'ingredients': 'ham, bread and tomatoes', 'meal': 'lunch', 'prep_time': '10 minutes'},
                cake = {'ingredients': 'flour, suggar and eggs', 'meal': 'dessert', 'prep_time': '60 minutes'},
                salad = {'ingredients': 'avocado, arugula, tomatoes and spinach', 'meal': 'lunch', 'prep_time': '15 minutes'}}
    for keys, value in cookbook.items():
        print(cookbook.keys());
