class RecipeManager:
    def __init__(self):
        self.recipes = []

    @property
    def display_recipes(self):
        for recipe in self.recipes:
          print(recipe)
        return self.recipes
          
    @display_recipes.getter
    def display_recipes(self):
      return str(self.recipes)

    @display_recipes.setter
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        return str(recipe)


  

    def update_recipe(self, recipe_index, new_recipe):
        self.recipes[recipe_index] = new_recipe
        return str(new_recipe)


    def delete_recipe(self, recipe_index):
        self.recipes.pop(recipe_index)
        return str(recipe_index)




# Test the code
recipe_manager = RecipeManager()

recipe1 = ['name', 'Spaghetti Carbonara', 'ingredients', 'spaghetti', 'bacon', 'eggs']
recipe2 = ['name', 'Chicken Curry', 'ingredients', 'chicken', 'curry powder', 'coconut milk']

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


