class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def update_recipe(self, recipe_index, new_recipe):
        self.recipes[recipe_index] = new_recipe
      #on this point I am confused, because I can see 2 meanings:
      # 1. change older recipe for new one and I had choosen this version
      # 2. change the integrent in recipe

    def delete_recipe(self, recipe_index):
        self.recipes.pop(recipe_index)

    def display_recipes(self):
        for recipe in self.recipes:
            print(recipe)


##
##tests
##
recipe_manager = RecipeManager()

recipe1 = {'name': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'bacon', 'eggs']}
recipe2 = {'name': 'Chicken Curry', 'ingredients': ['chicken', 'curry powder', 'coconut milk']}

recipe_manager.add_recipe(recipe1)
recipe_manager.add_recipe(recipe2)

#recipe_manager.display_recipes()

recipe3 = {'name': 'Beef Stroganoff', 'ingredients': ['beef', 'mushrooms', 'sour cream']}
recipe_manager.update_recipe(0, recipe3)

#recipe_manager.display_recipes()

#recipe_manager.delete_recipe(0)

recipe_manager.display_recipes()