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
        request_test = "How many ingredients does this recipe have?: "

        response = input(request_test)

        while number_ingredients == -1:
            try:
                number_ingredients = int(response)
            except:
                print("That is not a number")
                response = input(request_test)

        if number_ingredients <= 0:
            print("No ingredients added returning")
            return

        for count in range(number_ingredients):
            name = input(f"\nPlease enter the name of ingredient {count + 1}: ")
            amount = input("Please enter the amount of the ingredient: ")
            units = input("Please enter the units for the amount: ")
            alergens = input("Please enter the alergens for the ingredient as a comma seperated list: ").split(",")
            calories = input("Please enter the amount of calories for the amount of the ingredient: ")
            ingredients.append(Ingredient(name=name, amount=amount, units=units, alergens=alergens, callories=calories))

        new_recipe.add_ingredients(ingredients)

    def add_instructions_menu(self, new_recipe):
        self.clear_screen()
        number_instructions = -1
        instructions = []
        request_text = "How many instructions does this recipe have?: "

        response = input(request_text)

        while number_instructions == -1:
            try:
                number_instructions = int(response)
            except:
                print("That is not a number")
                response = input(request_text)

        if number_instructions <= 0:
            print("No instructions added returning")
            return

        for count in range(number_instructions):
            instruction_level = count + 1
            instruction = input(f"Please enter instruction for number {instruction_level}: ")
            instructions.append(f"{instruction_level}: {instruction}")

        new_recipe.instructions = instructions


    def add_recipe_from_input(self):
        self.clear_screen()
        title = input("Enter the title of the dish: ")
        new_recipe = Recipe(title)
        description = input("Enter the description: ")
        no_servings = int(input("Enter the number of servings: "))
        calories_per_portion = int(input("Enter the calories per portion: "))
        self.add_ingredient_menu(new_recipe)
        self.add_instructions_menu(new_recipe)
        new_recipe._description = description  # Set description directly
        new_recipe.no_servings = no_servings
        new_recipe.calories_per_portion = calories_per_portion
        
        RecipeManager.add_recipe(self, new_recipe)
        print("Recipe added.")

    def update_recipe_from_input(self):
        updated_recipe = self.display_recipes_summary()
        if updated_recipe == None:
            print("No valid selection")
            return

        def check_for_update(field:str, current):
            print(f"Current {field} is: {current}")
            response = input("Do you want to modify y/n?: ")
            if response in ["y", "Y"]:
               return input("Enter the updated {field}: ")
            else:
               return current

        updated_recipe.description = check_for_update(field = "Description", current = updated_recipe.description)
        updated_recipe.no_servings = int(check_for_update(field = "No Servings", current = updated_recipe.no_servings))
        updated_recipe.calories_per_portion = int(check_for_update(field = "No Calories Per Portion", current = updated_recipe.calories_per_portion))

        updated_ingredients = []

        for i, ingredient in enumerate(updated_recipe.ingredients):
            response = input(f"Ingredient is {ingredient.name}, do you want to change or remove y/n?: ")
            if response in ["y","Y"]:
                name = input(f"\nPlease enter the name of ingredient or return to remove: {ingredient.name}: ")
                if name != "":
                    amount = input("Please enter the amount of the ingredient: ")
                    units = input("Please enter the units for the amount: ")
                    alergens = input("Please enter the alergens for the ingredient as a comma seperated list: ").split(",")
                    calories = input("Please enter the amount of calories for the amount of the ingredient: ")
                    updated_ingredients.append(Ingredient(name=name, amount=amount, units=units, alergens=alergens, callories=calories))
                else:
                    print(f"Removing ingredient {ingredient.name}")
            else:
                updated_ingredients.append(ingredient)

        updated_recipe.ingredients = updated_ingredients;

        updated_instructions = []
        instruction_count = 0
        print(len(updated_recipe.instructions))
        for i, instruction in enumerate(updated_recipe.instructions):
            split_instruction = ':'.join(instruction.split(':')[1:])
            response = input(f"Instruction is {split_instruction}, do you want to change or remove y/n?: ")
            if response in ["y","Y"]:
                updated_instruction = input(f"Please enter the updated instruction or return to remove: ")
                if updated_instruction != "":
                    instruction_count += 1
                    updated_instructions.append(f"{instruction_count}: {updated_instruction}")
                else:
                    print(f"Removing instruction {instruction}")
            else:
                instruction_count += 1
                updated_instructions.append(f"{instruction_count}: {split_instruction}")

        updated_recipe.instructions = updated_instructions;


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
