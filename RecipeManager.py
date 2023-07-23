from recipe import Recipe


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, title):
        self.recipes.append(Recipe(title))

    def remove_recipe(self, index):
        if 0 <= index < len(self.recipes):
            self.recipes.pop(index)

    def edit_recipe(self, index, new_title):
        if 0 <= index < len(self.recipes):
            self.recipes[index].set_title(new_title)

    def display_recipe(self, index):
        if 0 <= index < len(self.recipes):
            return self.recipes[index]
        
