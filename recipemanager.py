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
        recipe_to_update.set_description(updated_recipe.get_description())
        recipe_to_update.set_no_servings(updated_recipe.get_no_servings())
        recipe_to_update.set_calories_per_portion(updated_recipe.get_calories_per_portion())
        recipe_to_update.set_ingredients(updated_recipe.get_ingredients())
        recipe_to_update.set_instructions(updated_recipe.get_instructions())
    
    def delete_recipe(self, recipe_to_delete: Recipe):
        self.recipes.remove(recipe_to_delete)
