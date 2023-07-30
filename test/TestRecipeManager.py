import sys
import os
import time
sys.path.append("../")
from recipemanager import RecipeManager
from recipe import Recipe
from ingredient import Ingredient

class TestRecipeManager(RecipeManager):
    def __init__(self, path):
        super().__init__()
        self._path = path

    def clear_screen(self):
        if os.name == 'nt':
           os.system('cls')
        else:
           os.system('clear')

    def pretty_print_recipe(self, recipe: Recipe):
        print(
            f" Title: {recipe.title} \n Description: {recipe.description} \n No. Servings: {recipe.no_servings} \n Callories per portion: {recipe.calories_per_portion} \n"
        )
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(ingredient.pretty_format())
        print("\nInstructions:")
        for instruction in recipe.instructions:
            print(f"\n{instruction}")

    def display_recipes(self):
        self.clear_screen()
        for recipe in self.recipes:
            self.clear_screen()
            self.pretty_print_recipe(recipe)
            input("Please press return for next")

        if not self.recipes:
            print("No recipes to display.")
            return

    def display_recipes_summary(self, display_only:bool = False):
        self.clear_screen()
        if not self.recipes:
            print("No recipes to display.")
            time.sleep(5)
            return None
        entries = dict()
        menu_entry = 0
        for i, recipe in enumerate(self.recipes):
            menu_entry += 1
            entries[str(menu_entry)] = recipe
            print(f"{menu_entry}: {recipe.title}")

        entry = input("Select an entry number or anything else to return to the main menu: ")

        if entry in entries:
            if display_only:
                self.clear_screen()
                self.pretty_print_recipe(entries[entry])
                input("Press return to return")
            return entries[entry]
        else:
            print("Entry not in list")
            return None

    def add_ingredient_menu(self, new_recipe):
        self.clear_screen()
        number_ingredients = -1
        ingredients = []

        response = input("How many ingredients does this recipe have?")

        while number_ingredients == -1:
            try:
                number_ingredients = int(response)
            except:
                print("That is not a number")
                response = input("How many ingredients does this recipe have?")

        if number_ingredients <= 0:
            print("No ingredients added returning")
            return

        for count in range(number_ingredients):
            name = input("Please enter the name of the ingredient: ")
            amount = input("Please enter the amount of the ingredient: ")
            units = input("Please enter the units for the amount: ")
            alergens = input("Please enter the alergens for the ingredient as a comma seperated list: ").split(",")
            calories = input("Please enter the amount of calories for the amount of the ingredient: ")
            ingredients.append(Ingredient(name=name, amount=amount, units=units, alergens=alergens, callories=calories))

        new_recipe.add_ingredients(ingredients)


    def add_recipe_from_input(self):
        self.clear_screen()
        title = input("Enter the title of the dish: ")
        new_recipe = Recipe(title)
        description = input("Enter the description: ")
        no_servings = int(input("Enter the number of servings: "))
        calories_per_portion = int(input("Enter the calories per portion: "))
        self.add_ingredient_menu(new_recipe)
        instructions = input("Enter the instructions: ").split(",")
        new_recipe._description = description  # Set description directly
        new_recipe.no_servings = no_servings
        new_recipe.calories_per_portion = calories_per_portion
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
        overwrite = False
        choice = input("Do you want to overwrite any pre-exisiting files: ")

        if (choice == "Y") or (choice == "y"):
            overwrite = True

        for recipe in self.recipes:
            try:
                RecipeManager.write_recipe_to_file(self, recipe, self._path, overwrite=overwrite)
            except:
                print(f"Unable to write {recipe.title}")

    def menu(self):

        self.clear_screen()
        print("1. Do you want to display recipes?")
        print("2. Do you want to add recipes?")
        print("3. Do you want to update recipe?")
        print("4. Do you want to delete recipe?")
        print("5. Do you want to write recipes to disc?")
        print("6. Do you want to read recipes from disc?")
        print("7. Do you want to exit the recipe manager?")
        print("8. Do you want to display a summary list of recipes?")
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
        elif choice == "8":
            self.display_recipes_summary(display_only = True)
        else:
            print("Invalid choice.")

        return True
