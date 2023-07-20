from recipe_Menager import RecipeManager
from recipe import Recipe

# Test the code
recipe_manager = RecipeManager()

recipe1 = Recipe(name = 'Spaghetti Carbonara', instructions = 'cook',  ingredients = ['spaghetti', 'bacon', 'eggs'])
recipe2 = Recipe(name = 'Chicken Curry', instructions = 'cook',  ingredients = ['chicken', 'curry powder', 'coconut milk'])

# Using the setter to add recipes
recipe_manager.add_recipe = recipe1
recipe_manager.add_recipe = recipe2

print("Original recipes:")
print(recipe_manager.display_recipes)

recipe3 = {'name': 'Beef Stroganoff', 'ingredients': ['beef', 'mushrooms', 'sour cream']}
recipe_manager.update_recipe(0, recipe3)

print(recipe_manager.display_recipes)

recipe_manager.delete_recipe(0)

print(recipe_manager.display_recipes)

#recipe_manager.delete_recipe(0)


