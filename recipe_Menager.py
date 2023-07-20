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

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def update_recipe(self, recipe_index, new_recipe):
        self.recipes[recipe_index] = new_recipe
    
    def delete_recipe(self, recipe_index):
        self.recipes.pop(recipe_index)




