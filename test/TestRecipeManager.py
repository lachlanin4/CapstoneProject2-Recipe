import sys
sys.path.append("../")
from recipemanager import RecipeManager
from recipe import Recipe
from ingredient import Ingredient

class TestRecipeManager(RecipeManager):
    def __init__(self, path):
        super().__init__()
        self._path = path


    def pretty_print_recipe(self, recipe: Recipe):
        print(
            f"Description: {recipe.description} \n No. Servings: {recipe.no_servings} \n Callories per portion: {recipe.calories_per_portion} \n"
        )
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(ingredient.pretty_format())
        print("\nInstructions:")
        for instruction in recipe.instructions:
            print(f"\n{instruction}")

    def display_recipes(self):
        for recipe in self.recipes:
            self.pretty_print_recipe(recipe)

        if not self.recipes:
            print("No recipes to display.")
            return

    def add_recipe_from_input(self):
        title = input("Enter the title of the dish: ")
        description = input("Enter the description: ")
        no_servings = int(input("Enter the number of servings: "))
        calories_per_portion = int(input("Enter the calories per portion: "))
        ingredients = input("Enter the ingredients: ").split(",")
        instructions = input("Enter the instructions: ").split(",")

        new_recipe = Recipe(title)
        new_recipe._description = description  # Set description directly
        new_recipe.no_servings = no_servings
        new_recipe.calories_per_portion = calories_per_portion
        for ingredient in ingredients:
            new_recipe.add_ingredients([Ingredient(name=ingredient.strip(), amount=1, units="each", alergens=[], callories=100)])
        new_recipe.instructions = instructions
        
        RecipeManager.add_recipe(self, new_recipe)
        print("Recipe added.")

    def update_recipe_from_input(self):
        title_to_update = input("Enter the name of the recipe to update: ")
        found = False
        for recipe in self.recipes:
            if recipe._title == title_to_update:
                description = input("Enter the updated description: ")
                no_servings = int(input("Enter the updated number of servings: "))
                calories_per_portion = int(input("Enter the updated calories per portion: "))
                ingredients = input("Enter the updated ingredients: ").split(",")
                instructions = input("Enter the updated instructions: ").split(",")
                updated_recipe = Recipe(title_to_update)
                updated_recipe.description = description
                updated_recipe.no_servings = no_servings
                updated_recipe.calories_per_portion = calories_per_portion
                for ingredient in ingredients:
                    updated_recipe.add_ingredients([Ingredient(name=ingredient.strip(), amount=1, units="each", alergens=[], callories=100)])
                updated_recipe.instructions = instructions

                self.update_recipe(recipe, updated_recipe)
                print("Recipe updated successfully.")
                found = True
                break

        if not found:
            print("Recipe not found.")

    def delete_recipe_from_input(self):
        title_to_delete = input("Enter the name of the recipe to delete: ")
        found = False

        for recipe in self.recipes:
            if recipe._title == title_to_delete:
                self.delete_recipe(recipe)
                print("Recipe deleted successfully.")
                found = True
                break

        if not found:
            print("Recipe not found. Unable to delete.")

    def write_recipe_from_input(self):
        for recipe in self.recipes:
            RecipeManager.write_recipe_to_file(self, recipe, self._path)

    def menu(self):
        print("1. Do you want to display recipes?")
        print("2. Do you want to add recipes?")
        print("3. Do you want to update recipe?")
        print("4. Do you want to delete recipe?")
        print("5. Do you want to write recipes to disc?")
        print("6. Do you want to read recipes from disc?")
        print("7. Do you want to exit the recipe manager?")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.display_recipes()
        elif choice == "2":
            self.add_recipe_from_input()
        elif choice == "3":
            self.update_recipe_from_input()
        elif choice == "4":
            self.delete_recipe_from_input()
        elif choice == "5":
            self.write_recipe_from_input()
        elif choice == "6":
            RecipeManager.read_recipes_from_files(self, self._path)
        elif choice == "7":
            return False
        else:
            print("Invalid choice.")

        return True
