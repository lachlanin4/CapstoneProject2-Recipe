# Create a noddy form of recipe class
#I move recipe menager to one file with recipe
class Recipe:
   def __init__(self, name, instructions, ingredients):
      self._name = name
      self._instructions = instructions
      self._ingredients = ingredients

   @property
   def name(self):
      return self._name

   @property
   def instructions(self):
      return self._instructions

   @property
   def ingredients(self):
      return self._ingredients

   def pretty_description(self):
      pretty_str = str(f"{self._name}, instructions are {self._instructions} using {self._ingredients}")
      return pretty_str
      
class RecipeManager:
    def __init__(self):
        self.recipes = []

    def menu(self):
        print("1. Do you want to display recipes?")
        print("2. Do you want to add recipes?")
        print("3.Do you want to upadate recipe?")
        print("4. Do you want to delete recipe?")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.display_recipes()
        elif choice == "2":
            self.add_recipe_from_input()
        elif choice == "3":
            self.update_recipe_from_input()
        elif choice == "4":
            self.delete_recipe_from_input()
        else:
            print("Invalid choice.")


    def display_recipes(self):
        if not self.recipes:
            print("No recipes.")
            return
        for recipe in self.recipes:
            print(recipe)
        return str(self.recipes)
            
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


    def add_recipe_from_input(self):
        name = input("Enter the name of the dish: ")
        instructions = input("Enter the instructions: ")
        ingredients = input("Enter the ingredients (comma-separated): ").split(",")
        
        new_recipe = Recipe(name, instructions, ingredients)
        self.add_recipe(new_recipe)
        print("Recipe added.")

    def update_recipe_from_input(self):
        name_to_update = input("Enter the name of the recipe to update: ")
        found = False

        for recipe in self.recipes:
            if recipe.name == name_to_update:
                instructions = input("Enter the updated instructions: ")
                ingredients = input("Enter the updated ingredients: ").split(",")

                updated_recipe = Recipe(name_to_update, instructions, ingredients)
                self.update_recipe(recipe, updated_recipe)
                print("Recipe updated successfully.")
                found = True
                break

        if not found:
            print("Recipe not found. Unable to update.")

    def delete_recipe_from_input(self):
        name_to_delete = input("Enter the name of the recipe to delete: ")
        found = False

        for recipe in self.recipes:
            if recipe.name == name_to_delete:
                self.delete_recipe(recipe)
                print("Recipe deleted successfully.")
                found = True
                break

        if not found:
            print("Recipe not found.")




