from recipe import Recipe

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

    def update_recipe(self, recipe_index, new_recipe):
        self.recipes[recipe_index] = new_recipe
    
    def delete_recipe(self, recipe_index):
        self.recipes.pop(recipe_index)




