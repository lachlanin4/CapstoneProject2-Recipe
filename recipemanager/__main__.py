"""
This allows command line operation of the recipe manager
"""
import os
import time
from pathlib import Path

from recipe import Recipe
from ingredient import Ingredient
from recipemanager import RecipeManager

class CommandLineRecipeManager(RecipeManager):
    """
    The is a derived class for recipe manager operation via commandline
    """
    def __init__(self, path):
        """
        This is the constructor
        """
        super().__init__()
        self._path = path

    @classmethod
    def clear_screen(cls):
        """
        This clears the screen
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @classmethod
    def pretty_print_recipe(cls, _recipe: Recipe):
        """
        This prints a recipe
        """
        print(
            str(f" Title: {_recipe.title} \n Description: {_recipe.description} \n ") +
            str(f"No. Servings: {_recipe.no_servings} \n ") +
            str(f"Callories per portion: {_recipe.calories_per_portion} \n ") +
            str(f"Preperation Time: {_recipe.preperation_time} \n")
        )
        print("Ingredients:")
        for _ingredient in _recipe.ingredients:
            print(_ingredient.pretty_format())
        print("\nInstructions:")
        for instruction in _recipe.instructions:
            print(f"\n{instruction}")

    def display_recipes(self):
        """
        This displays a recipe
        """
        self.clear_screen()
        for _recipe in self.recipes:
            self.clear_screen()
            self.pretty_print_recipe(_recipe)
            input("Please press return for next")

        if not self.recipes:
            print("No recipes to display.")
            return

    def display_recipes_summary(self, display_only: bool = False):
        """
        This displays a recipe summary
        """
        self.clear_screen()
        if not self.recipes:
            print("No recipes to display.")
            time.sleep(5)
            return None
        entries = dict()
        menu_entry = 0
        for i, _recipe in enumerate(self.recipes):
            menu_entry = i + 1
            entries[str(menu_entry)] = _recipe
            print(f"{menu_entry}: {_recipe.title}")

        entry = input(
            "Select an entry number or anything else to return to the main menu: "
        )

        if entry in entries:
            if display_only:
                self.clear_screen()
                self.pretty_print_recipe(entries[entry])
                input("Press return to return")
            return entries[entry]

        print("Entry not in list")
        return None

    def add_ingredient_menu(self, new_recipe):
        """
        This displays an ingredients summary
        """
        self.clear_screen()
        number_ingredients = -1
        ingredients = []
        request_test = "How many ingredients does this recipe have?: "

        response = input(request_test)

        while number_ingredients == -1:
            try:
                number_ingredients = int(response)
            except ValueError:
                print("That is not a number")
                response = input(request_test)

        if number_ingredients <= 0:
            print("No ingredients added returning")
            return

        for count in range(number_ingredients):
            name = input(f"\nPlease enter the name of ingredient {count + 1}: ")
            amount = input("Please enter the amount of the ingredient: ")
            units = input("Please enter the units for the amount: ")
            alergens = input(
                "Please enter the alergens for the ingredient as a comma seperated list: "
            ).split(",")
            calories = input(
                "Please enter the amount of calories for the amount of the ingredient: "
            )
            ingredients.append(
                Ingredient(
                    name=name,
                    amount=amount,
                    units=units,
                    alergens=alergens,
                    callories=calories,
                )
            )

        new_recipe.add_ingredients(ingredients)

    def add_instructions_menu(self, new_recipe):
        """
        This displays an instructions menu
        """
        self.clear_screen()
        number_instructions = -1
        instructions = []
        request_text = "How many instructions does this recipe have?: "

        response = input(request_text)

        while number_instructions == -1:
            try:
                number_instructions = int(response)
            except ValueError:
                print("That is not a number")
                response = input(request_text)

        if number_instructions <= 0:
            print("No instructions added returning")
            return

        for count in range(number_instructions):
            instruction_level = count + 1
            instruction = input(
                f"Please enter instruction for number {instruction_level}: "
            )
            instructions.append(f"{instruction_level}: {instruction}")

        new_recipe.instructions = instructions

    def add_recipe_from_input(self):
        """
        This adds a recipe from the command line
        """
        self.clear_screen()
        title = input("Enter the title of the dish: ")
        new_recipe = Recipe(title)
        description = input("Enter the description: ")
        no_servings = int(input("Enter the number of servings: "))
        calories_per_portion = int(input("Enter the calories per portion: "))
        self.add_ingredient_menu(new_recipe)
        self.add_instructions_menu(new_recipe)
        new_recipe.description = description  # Set description directly
        new_recipe.no_servings = no_servings
        new_recipe.calories_per_portion = calories_per_portion
        new_recipe.preperation_time = int(input("Enter the prep time in mins: "))

        RecipeManager.add_recipe(self, new_recipe)
        print("Recipe added.")

    def update_recipe_from_input(self):
        """
        This updates a recipe from the command line
        """
        updated_recipe = self.display_recipes_summary()
        if updated_recipe is None:
            print("No valid selection")
            return

        def check_for_update(field: str, current):
            print(f"Current {field} is: {current}")
            response = input("Do you want to modify y/n?: ")
            if response in ["y", "Y"]:
                return input(f"Enter the updated {field}: ")

            return current

        updated_recipe.description = check_for_update(
            field="Description", current=updated_recipe.description
        )
        updated_recipe.no_servings = int(
            check_for_update(field="No Servings", current=updated_recipe.no_servings)
        )
        updated_recipe.calories_per_portion = int(
            check_for_update(
                field="No Calories Per Portion",
                current=updated_recipe.calories_per_portion,
            )
        )
        updated_recipe.preperation_time = int(
            check_for_update(
                field="Enter the prep time in mins",
                current=updated_recipe.preperation_time,
            )
        )

        updated_ingredients = []

        for _i, _ingredient in enumerate(updated_recipe.ingredients):
            response = input(
                f"Ingredient {_i + 1}: is {_ingredient.name}, " +
                "do you want to change or remove y/n?: "
            )
            if response in ["y", "Y"]:
                name = input(
                    str("\nPlease enter the name of ingredient or " +
                        f"return to remove: {_ingredient.name}: ")
                )
                if name != "":
                    amount = input("Please enter the amount of the ingredient: ")
                    units = input("Please enter the units for the amount: ")
                    alergens = input(
                        "Please enter the alergens for the ingredient as a comma seperated list: "
                    ).split(",")
                    calories = input(
                        "Please enter the amount of calories for the amount of the ingredient: "
                    )
                    updated_ingredients.append(
                        Ingredient(
                            name=name,
                            amount=amount,
                            units=units,
                            alergens=alergens,
                            callories=calories,
                        )
                    )
                else:
                    print(f"Removing ingredient {_ingredient.name}")
            else:
                updated_ingredients.append(_ingredient)

        updated_recipe.ingredients = updated_ingredients

        updated_instructions = []
        instruction_count = 0

        if len(updated_recipe.instructions) == 0:
            self.add_instructions_menu(updated_recipe)
        else:
            for _i, instruction in enumerate(updated_recipe.instructions):
                instruction_split = instruction.split(":")
                if len(instruction_split) > 1:
                    split_instruction = ":".join(instruction_split[1:])
                else:
                    split_instruction = instruction_split[0]
                response = input(
                    str(f"Instruction {_i + 1}: is {split_instruction}, " +
                        "do you want to change or remove y/n?: ")
                )
                if response in ["y", "Y"]:
                    updated_instruction = input(
                        "Please enter the updated instruction or return to remove: "
                    )
                    if updated_instruction != "":
                        instruction_count += 1
                        updated_instructions.append(
                            f"{instruction_count}: {updated_instruction}"
                        )
                    else:
                        print(f"Removing instruction {instruction}")
                else:
                    instruction_count += 1
                    updated_instructions.append(
                        f"{instruction_count}: {split_instruction}"
                    )

            updated_recipe.instructions = updated_instructions

    def delete_recipe_from_input(self):
        """
        This deletes a recipe from the command line
        """
        title_to_delete = input("Enter the name of the recipe to delete: ")
        found = False

        for _recipe in self.recipes:
            if _recipe.title == title_to_delete:
                self.delete_recipe(_recipe)
                print("Recipe deleted successfully.")
                found = True
                break

        if not found:
            print("Recipe not found. Unable to delete.")

    def write_recipe_from_input(self):
        """
        This writes a recipe from the command line
        """
        overwrite = False
        choice = input("Do you want to overwrite any pre-exisiting files: ")

        if choice in ("Y", "y"):
            overwrite = True

        for _recipe in self.recipes:
            try:
                RecipeManager.write_recipe_to_file(
                    recipe=_recipe, directory_path=self._path, overwrite=overwrite
                )
            except IOError as _e:
                print(f"Unable to write {_recipe.title}: error {_e}")
            except Exception as _x: # pylint: disable=W0703
                print(f"Error during write {_recipe.title}: error {_x}")

    def menu(self):
        """
        This displays a menu from the command line
        """
        self.clear_screen()
        print("1. Do you want to display a summary list of recipes?")
        print("2. Do you want to display all recipes?")
        print("3. Do you want to add recipes?")
        print("4. Do you want to update recipe?")
        print("5. Do you want to delete recipe?")
        print("6. Do you want to write recipes to disc?")
        print("7. Do you want to read recipes from disc?")
        print("8. Do you want to exit the recipe manager?")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.display_recipes_summary(display_only=True)
        elif choice == "2":
            self.display_recipes()
        elif choice == "3":
            self.add_recipe_from_input()
        elif choice == "4":
            self.update_recipe_from_input()
        elif choice == "5":
            self.delete_recipe_from_input()
        elif choice == "6":
            self.write_recipe_from_input()
        elif choice == "7":
            RecipeManager.read_recipes_from_files(self, self._path)
        elif choice == "8":
            return False
        else:
            print("Invalid choice.")

        return True

if __name__ == "__main__":
    data_path = input("Please input path to data: ")
    while not Path(data_path).is_dir():
        print("Path not a directory - please try again")
        data_path = input("Please input path to data: ")

    clrecipemanager = CommandLineRecipeManager(Path(data_path))
    Run = True

    while Run:
        Run = clrecipemanager.menu()

    print("Thank you for using recipe manager!")
