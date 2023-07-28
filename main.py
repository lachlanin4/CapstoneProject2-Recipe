from ingredient import Ingredient
from recipe import Recipe
from typing import List
from glob import glob
from yaml import load, dump, Dumper, Loader
from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk

class Recipe:
    def __init__(self, title, ingredients, description, preparing_time, kcal_per_portion):
        self.title = title
        self.ingredients = ingredients
        self.description = description
        self.preparing_time = preparing_time
        self.kcal_per_portion = kcal_per_portion

class RecipeManager:
    def __init__(self):
        self._recipes: List[Recipe] = []


    def recipes(self):
        return self._recipes

    def add_recipe(self, recipe_to_add: Recipe):
        if len(self._recipes) > 0:
            self._recipes.append(recipe_to_add)
        else:
            self._recipes = [recipe_to_add]

    def update_recipe(self, recipe_to_update: Recipe, updated_recipe: Recipe):
        found = False
        for x, rec in enumerate(self._recipes):
            if rec._title == recipe_to_update._title:
                self._recipes[x] = updated_recipe
                found = True
                break

        if not found:
            raise ("I couldn't find the recipe to update")

    def delete_recipe(self, recipe_to_delete: Recipe):
        found = False
        for x, rec in enumerate(self._recipes):
            if rec._title == recipe_to_delete._title:
                del self._recipes[x]
                found = True
                break

        if not found:
            raise ("I couldn't find the recipe to update")

    def read_recipes_from_files(self, path: Path):

        # Create a list to contain returned objects from reading files
        data_sets = []

        # Get a list of yml files that are already in the path
        yaml_files = path.glob("*.yml")

        # Iterate a list of yaml file previously found in the route path
        for recipeFile in yaml_files:

            # Open the file as read only
            f = open(recipeFile, "r")

            # Read the file
            stream = f.read()

            # Load the data
            data = load(stream, Loader=Loader)

            # Append the data
            data_sets.append(data)

            # Close the file
            f.close()

        if len(data_sets) > 0:
            self._recipes = data_sets

    def write_recipe_to_file(
        self, recipe: Recipe, directory_path: Path, name=None, overwrite=False
    ):
        file_name = "default.py"
        if name == None:
            # Create a file name based on the name of the recipe
            file_name = str(recipe.title.strip() + ".yml").replace(" ", "_")
        else:
            file_name = name

        # Create a path to the file to be written based upon the route path and the filename
        path = directory_path.joinpath(file_name)

        # If the file already exists - don't bother
        if path.is_file() and not overwrite:
            raise ("File alread exists and you don't want to overwrite")
        else:
            # Open the file for writing
            f = open(path, "w")

            # Create a dump of the recipe class representation
            data = dump(recipe, Dumper=Dumper)

            # Write the dumped data to file
            f.write(data)

            # Close the file
            f.close()







class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.invitation = "Recipe Manager"
        self.recipe_manager = RecipeManager()

        frame_main = ttk.Frame()
        frame_main.pack(fill=tk.BOTH, expand=True)

        btn_show_invitation = ttk.Button(frame_main, text="Welcome in Recipe Manager!", command=self.show_invitation)
        btn_show_invitation.pack(padx=10, pady=10)

    def show_invitation(self):
        invitation_window = InvitationWindow(self, invitation=self.invitation, recipe_manager=self.recipe_manager)


class InvitationWindow(tk.Toplevel):
    def __init__(self, master, invitation, recipe_manager):
        super().__init__(master)

        self.recipe_manager = recipe_manager
        self.invitation = invitation

        frame_main = tk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)

        lbl_invitation = tk.Label(frame_main, text=f"{self.invitation}")
        lbl_invitation.pack(padx=50, pady=50)

        self.recipe_frame = ttk.Frame(self)
        self.recipe_frame.pack(fill=tk.BOTH, expand=True)

        btn_select_to_display_recipe = ttk.Button(master=self.recipe_frame, text="Display Recipe", command=self.display)
        btn_select_to_display_recipe.pack(padx=10, pady=10)

        btn_select_to_add_recipe = ttk.Button(master=self.recipe_frame, text="Add Recipe", command=self.add)
        btn_select_to_add_recipe.pack(padx=10, pady=10)

        btn_select_to_edit_recipe = ttk.Button(master=self.recipe_frame, text="Edit Recipe", command=self.edit)
        btn_select_to_edit_recipe.pack(padx=10, pady=10)

        btn_select_to_remove_recipe = ttk.Button(master=self.recipe_frame, text="Remove Recipe", command=self.remove)
        btn_select_to_remove_recipe.pack(padx=10, pady=10)

    def display(self):
        print("Display Recipe button clicked!")
        display_window = DisplayWindow(self, self.recipe_manager)
        display_window.display_recipes()

    def add(self):
        print("Add Recipe button clicked!")
        add_recipe_window = AddRecipeWindow(self, self.recipe_manager)
        add_recipe_window.add_recipe()

    def edit(self):
        print("Edit Recipe button clicked!")

    def remove(self):
        print("Remove Recipe button clicked!")


class DisplayWindow(tk.Toplevel):
    def __init__(self, master, recipe_manager):
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.text_widget = tk.Text(self.frame_main, wrap="word")
        self.text_widget.pack(padx=50, pady=50, fill=tk.BOTH, expand=True)

    def display_recipes(self):
        self.update_text_widget()

    def update_text_widget(self):
        self.text_widget.delete(1.0, tk.END)

        recipes = self.recipe_manager.recipes()

        for i, recipe in enumerate(recipes):
            recipe_title = recipe.title
            recipe_ingredients = ", ".join(recipe.ingredients)
            recipe_description = recipe.description
            recipe_preparing_time = recipe.preparing_time
            recipe_dietary_info = recipe.dietary_info

            recipe_details = f"Recipe {i+1}\nTitle: {recipe_title}\nIngredients: {recipe_ingredients}\nDescription: {recipe_description}\nPreparing Time: {recipe_preparing_time}\nDietary Info: {recipe_dietary_info}\n\n"

            self.text_widget.insert(tk.END, recipe_details)


class AddRecipeWindow(tk.Toplevel):
    def __init__(self, master, recipe_manager):
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.lbl_title = ttk.Label(self.frame_main, text="Title:")
        self.lbl_title.pack(padx=10, pady=5)

        self.entry_title = ttk.Entry(self.frame_main)
        self.entry_title.pack(padx=10, pady=5)

        self.lbl_ingredients = ttk.Label(self.frame_main, text="Ingredients (comma-separated):")
        self.lbl_ingredients.pack(padx=10, pady=5)

        self.entry_ingredients = ttk.Entry(self.frame_main)
        self.entry_ingredients.pack(padx=10, pady=5)

        self.lbl_description = ttk.Label(self.frame_main, text="Description:")
        self.lbl_description.pack(padx=10, pady=5)

        self.entry_description = ttk.Entry(self.frame_main)
        self.entry_description.pack(padx=10, pady=5)

        self.lbl_preparing_time = ttk.Label(self.frame_main, text="Preparing Time:")
        self.lbl_preparing_time.pack(padx=10, pady=5)

        self.entry_preparing_time = ttk.Entry(self.frame_main)
        self.entry_preparing_time.pack(padx=10, pady=5)

        self.lbl_dietary_info = ttk.Label(self.frame_main, text="Calorie per portion:")
        self.lbl_dietary_info.pack(padx=10, pady=5)

        self.entry_dietary_info = ttk.Entry(self.frame_main)
        self.entry_dietary_info.pack(padx=10, pady=5)

        self.btn_add_recipe = ttk.Button(self.frame_main, text="Add Recipe", command=self.add_recipe)
        self.btn_add_recipe.pack(padx=10, pady=5)

    def add_recipe(self):
        title = self.entry_title.get()
        ingredients = self.entry_ingredients.get().split(", ")
        description = self.entry_description.get()
        preparing_time = self.entry_preparing_time.get()
        dietary_info = self.entry_dietary_info.get()

        recipe = Recipe(title, ingredients, description, preparing_time, dietary_info)
        self.recipe_manager.add_recipe(recipe)

        # Update the DisplayWindow with the new recipe
        display_window = self.master.winfo_children()[0]  # Get the DisplayWindow instance
        display_window.update_text_widget()

        self.destroy()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.title("Main Window")

    main_window.mainloop()