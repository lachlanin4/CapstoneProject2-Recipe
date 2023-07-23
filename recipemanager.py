from ingredient import Ingredient
from recipe import Recipe
from typing import List

class RecipeManager:
    def __init__(self):
        self.recipes:List[Recipe] = []

    def add_recipe(self, recipe_to_add: Recipe):
        if len(self.recipes) > 0:
            self.recipes.append(recipe_to_add)
        else:
            self.recipes = [recipe_to_add]

    def update_recipe(self, recipe_to_update: Recipe, updated_recipe: Recipe):
        found = False
        for x, rec in enumerate(self.recipes):
            if rec._title == recipe_to_update._title:
                self.recipes[x] = updated_recipe
                found = True
                break

        if not found:
            raise ("I couldn't find the recipe to update")

    
    def delete_recipe(self, recipe_to_delete: Recipe):
        self.recipes.remove(recipe_to_delete)