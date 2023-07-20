from recipe import Recipe

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def display_recipes(self):
        for recipe in self.recipes:
            print(recipe)
            return self.recipes
            
    def stringify_recipes(self):
        recipes_str = str("")
        for recipe in self.recipes:
            recipes_str += ', ' + recipe.pretty_description()
        return str(recipes_str)

    def add_recipe(self, recipe_to_add: Recipe):
        self.recipes.append(recipe_to_add)

    def update_recipe(self, recipe_to_update: Recipe, updated_recipe: Recipe):
        found = False
        for x, rec in enumerate(self.recipes):
            if rec.name == recipe_to_update.name:
                self.recipes[x] = updated_recipe
                found = True
                break

        if not found:
            print("I couldn't find the recipe")
    
    def delete_recipe(self, recipe_to_delete: Recipe):
        found = False
        for x, rec in enumerate(self.recipes):
            if rec.name == recipe_to_delete.name:
                del self.recipes[x]
                found = True
                break

        if not found:
            print("I couldn't find the recipe")
