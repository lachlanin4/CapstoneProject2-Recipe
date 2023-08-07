"""
This is the Main window for the GUI
"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from pathlib import Path
from recipemanager import RecipeManager
from recipe import Recipe
from ingredient import Ingredient


class MainWindow(tk.Tk):  # 3
    """
    Main Window Class
    """

    def __init__(self):
        """
        This is the init
        """
        super().__init__()

        self.invitation = "Recipe Manager"
        self.recipe_manager = RecipeManager()

        frame_main = ttk.Frame()
        frame_main.pack(fill=tk.BOTH, expand=True)

        lbl_invitation = tk.Label(
            frame_main,
            text=str(
                "Welcome in Recipe Menager! If you are ready to continue"
                + " press the button: Run Recipe Menager!"
            ),
        )
        lbl_invitation.pack(padx=10, pady=10)
        btn_show_invitation = ttk.Button(
            frame_main, text="Run Recipe Manager!", command=self.show_invitation
        )
        btn_show_invitation.pack(padx=10, pady=10)

    def show_invitation(self):
        """
        This is the show invitation method
        """
        InvitationWindow(
            self, invitation=self.invitation, recipe_manager=self.recipe_manager
        )


class InvitationWindow(tk.Toplevel):  # 4
    """
    This is the Invitation Window class
    """

    def __init__(self, master, invitation, recipe_manager):
        """
        This is the invitation window init method
        """
        super().__init__(master)

        self.recipe_manager = recipe_manager
        self.invitation = invitation
        self.display_window = None

        frame_main = tk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)

        lbl_invitation = tk.Label(
            frame_main, text=f"{self.invitation}", font="Helvetica 20 bold"
        )
        lbl_invitation.pack(padx=50, pady=50)

        self.recipe_frame = ttk.Frame(self)
        self.recipe_frame.pack(fill=tk.BOTH, expand=True)

        lbl_instuctions = tk.Label(
            frame_main,
            text=str(
                "Instructions\n\n\n\n Menu window:\n"
                + "1. Click add recipe- to add recipes.\n"
                + "2. Click Display Recipe- to see your recipes.\n"
                + "3. Click Edit Recipes- to choose and modify yours "
                + " recipes. \n "
                + "4. Click Remove Recipe- to choose and delete recipe. "
                + "\n\n\n "
                "After every single action like clicking display, add, "
                + "edit, remove close the actiton window, and continue "
                + "your actions with recipes in manu window!"
            ),
        )
        lbl_instuctions.pack(padx=50, pady=50)

        self.instuctions = ttk.Frame(self)
        self.instuctions.pack(fill=tk.BOTH, expand=True)

        btn_select_to_display_recipe = ttk.Button(
            master=self.recipe_frame, text="Display Recipe", command=self.display
        )
        btn_select_to_display_recipe.pack(padx=10, pady=10)

        btn_select_to_add_recipe = ttk.Button(
            master=self.recipe_frame, text="Add Recipe", command=self.add
        )
        btn_select_to_add_recipe.pack(padx=10, pady=10)

        btn_select_to_edit_recipe = ttk.Button(
            master=self.recipe_frame, text="Edit Recipe", command=self.edit
        )
        btn_select_to_edit_recipe.pack(padx=10, pady=10)

        btn_select_to_remove_recipe = ttk.Button(
            master=self.recipe_frame, text="Remove Recipe", command=self.remove
        )
        btn_select_to_remove_recipe.pack(padx=10, pady=10)

        btn_select_to_load_recipes = ttk.Button(
            master=self.recipe_frame, text="Load Recipes", command=self.load
        )
        btn_select_to_load_recipes.pack(padx=10, pady=10)

        btn_select_to_save_recipes = ttk.Button(
            master=self.recipe_frame, text="Save Recipes", command=self.save
        )
        btn_select_to_save_recipes.pack(padx=10, pady=10)

    def display(self):
        """
        This is the display window method
        """
        print("Display Recipe button clicked!")
        self.display_window = DisplayWindow(self, self.recipe_manager)
        self.display_window.display_recipes()

    def add(self):
        """
        This is the add recipe window method
        """
        print("Add Recipe button clicked!")
        AddRecipeWindow(self, self.recipe_manager)

    def edit(self):
        """
        This is the edit recipe window method
        """
        print("Edit Recipe button clicked!")
        EditRecipeWindow(self, self.recipe_manager)

    def remove(self):
        """
        This is the remove recipe window method
        """
        print("Remove Recipe button clicked!")
        RemoveRecipeWindow(self, self.recipe_manager)

    def load(self):
        """
        This is the load recipes method
        """
        print("Load Recipes button clicked!")
        folder_selected = filedialog.askdirectory(parent=self)
        self.recipe_manager.read_recipes_from_files(Path(folder_selected))

    def save(self):
        """
        This is the save recipes method
        """
        print("Save Recipes button clicked!")
        folder_selected = filedialog.askdirectory(parent=self)
        for recipe in self.recipe_manager.recipes:
            self.recipe_manager.write_recipe_to_file(
                recipe=recipe, directory_path=Path(folder_selected), overwrite=True
            )


class DisplayWindow(tk.Toplevel):
    """
    This displays the window
    """

    def __init__(self, master, recipe_manager):
        """
        This is the init method
        """
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.text_widget = tk.Text(self.frame_main, wrap="word")
        self.text_widget.pack(padx=50, pady=50, fill=tk.BOTH, expand=True)

    def display_recipes(self):
        """
        This is the display recipes
        """
        self.update_text_widget()

    def update_text_widget(self):
        """
        This is the update text widget method
        """
        self.text_widget.delete(1.0, tk.END)

        recipes = self.recipe_manager.recipes

        for i, recipe in enumerate(recipes, 1):

            ingredients_string = ", ".join(str(e.name) for e in recipe.ingredients)

            recipe_details = (
                f"Recipe {i}\n"
                f"Title: {recipe.title}\n"
                f"Ingredients: {ingredients_string}\n"
                f"Description: {recipe.description}\n"
                f"Preparing Time: {recipe.preperation_time}\n"
                f"Dietary Info: {recipe.calories_per_portion}\n\n"
            )

            self.text_widget.insert(tk.END, recipe_details)


class AddRecipeWindow(tk.Toplevel):
    """
    This displays the recipe window
    """

    def __init__(self, master, recipe_manager):
        """
        This is the init for the recipe window
        """
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.lbl_title = ttk.Label(self.frame_main, text="Title:")
        self.lbl_title.pack(padx=10, pady=5)

        self.entry_title = ttk.Entry(self.frame_main)
        self.entry_title.pack(padx=10, pady=5)

        self.lbl_ingredients = ttk.Label(
            self.frame_main, text="Ingredients (comma-separated):"
        )
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

        self.lbl_kcal_info = ttk.Label(self.frame_main, text="Calorie per portion:")
        self.lbl_kcal_info.pack(padx=10, pady=5)

        self.entry_kcal_info = ttk.Entry(self.frame_main)
        self.entry_kcal_info.pack(padx=10, pady=5)

        self.btn_add_recipe = ttk.Button(
            self.frame_main, text="Add Recipe", command=self.add_recipe
        )
        self.btn_add_recipe.pack(padx=10, pady=5)

    def add_recipe(self):
        """
        This is the add recipe method
        """
        recipe_title = self.entry_title.get()
        ingredients_list = []
        recipe_ingredients = self.entry_ingredients.get().split(",")
        for ingredient in recipe_ingredients:
            ingredients_list.append(
                Ingredient(
                    name=ingredient, amount=1, units="each", alergens=[], callories=0
                )
            )

        recipe_description = self.entry_description.get()
        recipe_preparing_time = self.entry_preparing_time.get()
        recipe_kcal_per_portion_info = self.entry_kcal_info.get()

        recipe = Recipe(
            title=recipe_title,
            ingredients=ingredients_list,
            no_servings=1,
            description=recipe_description,
            preperation_time=recipe_preparing_time,
            calories_per_portion=recipe_kcal_per_portion_info,
            instructions="",
        )

        if self.recipe_manager.add_recipe(recipe):
            print("Recipe added successfully!")

            if self.master.winfo_children():
                for child in self.master.winfo_children():
                    if isinstance(child, DisplayWindow):
                        child.update_text_widget()

        else:
            print("Failed to add the recipe.")

        self.destroy()


class RemoveRecipeWindow(tk.Toplevel):
    """
    This allows the removal of a recipe
    """

    def __init__(self, master, recipe_manager):
        """
        This is the init for the remove recipe window
        """
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.lbl_select_recipe = ttk.Label(self.frame_main, text="Select Recipe:")
        self.lbl_select_recipe.pack(padx=10, pady=5)

        self.recipe_listbox = tk.Listbox(self.frame_main)
        self.recipe_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.btn_remove_recipe = ttk.Button(
            self.frame_main, text="Remove Recipe", command=self.remove_recipe
        )
        self.btn_remove_recipe.pack(padx=10, pady=5)

        self.update_recipe_list()

    def update_recipe_list(self):
        """
        This is the update recipe list method
        """
        self.recipe_listbox.delete(0, tk.END)
        recipes = self.recipe_manager.recipes
        for recipe in recipes:
            self.recipe_listbox.insert(tk.END, recipe.title)

    def remove_recipe(self):
        """
        This is the remove recipe list method
        """
        selected_index = self.recipe_listbox.curselection()
        if not selected_index:
            return

        recipe_title = self.recipe_listbox.get(selected_index[0])
        recipe_to_delete = None

        for recipe in self.recipe_manager.recipes:
            if recipe.title == recipe_title:
                recipe_to_delete = recipe
                break

        if recipe_to_delete:
            if self.recipe_manager.delete_recipe(recipe_to_delete):
                print("Recipe removed successfully!")

                if self.master.winfo_children():
                    for child in self.master.winfo_children():
                        if isinstance(child, DisplayWindow):
                            child.update_text_widget()
            else:
                print("Failed to remove the recipe.")
        else:
            print("Recipe not found!")

        self.destroy()


class EditRecipeWindow(tk.Toplevel):
    """
    This allows the editing of a recipe
    """

    def __init__(self, master, recipe_manager):
        """
        This is the init for the edit recipe window
        """
        super().__init__(master)
        self.recipe_manager = recipe_manager

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.lbl_select_recipe = ttk.Label(self.frame_main, text="Select Recipe:")
        self.lbl_select_recipe.pack(padx=10, pady=5)

        self.recipe_listbox = tk.Listbox(self.frame_main)
        self.recipe_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.btn_edit_recipe = ttk.Button(
            self.frame_main, text="Edit Recipe", command=self.edit_recipe
        )
        self.btn_edit_recipe.pack(padx=10, pady=5)

        self.update_recipe_list()

    def update_recipe_list(self):
        """
        This is the update recipe list method
        """
        self.recipe_listbox.delete(0, tk.END)
        recipes = self.recipe_manager.recipes
        for recipe in recipes:
            self.recipe_listbox.insert(tk.END, recipe.title)

    def edit_recipe(self):
        """
        This is the edit recipe method
        """
        selected_index = self.recipe_listbox.curselection()
        if not selected_index:
            return

        recipe_title = self.recipe_listbox.get(selected_index[0])
        recipe_to_edit = None

        for recipe in self.recipe_manager.recipes:
            if recipe.title == recipe_title:
                recipe_to_edit = recipe
                break

        if recipe_to_edit:
            EditRecipeDetailsWindow(self, recipe_to_edit)
        else:
            print("Recipe not found!")


class EditRecipeDetailsWindow(tk.Toplevel):
    """
    This allows the editing of a recipes details
    """

    def __init__(self, master, recipe):
        """
        This is the init for the edit recipe details window
        """
        super().__init__(master)
        self.recipe_manager = master.recipe_manager
        self.recipe_to_edit = recipe

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        self.lbl_title = ttk.Label(self.frame_main, text="Title:")
        self.lbl_title.pack(padx=10, pady=5)

        self.entry_title = ttk.Entry(self.frame_main)
        self.entry_title.insert(tk.END, recipe.title)
        self.entry_title.pack(padx=10, pady=5)

        self.lbl_ingredients = ttk.Label(
            self.frame_main, text="Ingredients (comma-separated):"
        )
        self.lbl_ingredients.pack(padx=10, pady=5)

        self.entry_ingredients = ttk.Entry(self.frame_main)
        ingredients_string = ", ".join(str(e.name) for e in recipe.ingredients)
        self.entry_ingredients.insert(tk.END, ingredients_string)
        self.entry_ingredients.pack(padx=10, pady=5)

        self.lbl_description = ttk.Label(self.frame_main, text="Description:")
        self.lbl_description.pack(padx=10, pady=5)

        self.entry_description = ttk.Entry(self.frame_main)
        self.entry_description.insert(tk.END, recipe.description)
        self.entry_description.pack(padx=10, pady=5)

        self.lbl_preparing_time = ttk.Label(self.frame_main, text="Preparing Time:")
        self.lbl_preparing_time.pack(padx=10, pady=5)

        self.entry_preparing_time = ttk.Entry(self.frame_main)
        self.entry_preparing_time.insert(tk.END, recipe.preperation_time)
        self.entry_preparing_time.pack(padx=10, pady=5)

        self.lbl_kcal_info = ttk.Label(self.frame_main, text="Calorie per portion:")
        self.lbl_kcal_info.pack(padx=10, pady=5)

        self.entry_kcal_info = ttk.Entry(self.frame_main)
        self.entry_kcal_info.insert(tk.END, recipe.calories_per_portion)
        self.entry_kcal_info.pack(padx=10, pady=5)

        self.btn_save_changes = ttk.Button(
            self.frame_main, text="Save Changes", command=self.save_changes
        )
        self.btn_save_changes.pack(padx=10, pady=5)

    def save_changes(self):
        """
        This is the save changes method
        """
        recipe_title = self.entry_title.get()
        ingredients_list = []
        recipe_ingredients = self.entry_ingredients.get().split(", ")
        for ingredient in recipe_ingredients:
            ingredients_list.append(
                Ingredient(
                    name=ingredient, amount=1, units="each", alergens=[], callories=0
                )
            )

        recipe_description = self.entry_description.get()
        recipe_preparing_time = self.entry_preparing_time.get()
        recipe_kcal_per_portion_info = self.entry_kcal_info.get()

        updated_recipe = Recipe(
            title=recipe_title,
            ingredients=ingredients_list,
            no_servings=1,
            description=recipe_description,
            preperation_time=recipe_preparing_time,
            calories_per_portion=recipe_kcal_per_portion_info,
            instructions="",
        )

        if self.recipe_manager.update_recipe(self.recipe_to_edit, updated_recipe):
            print("Recipe updated successfully!")

            if self.master.winfo_children():
                for child in self.master.winfo_children():
                    if isinstance(child, DisplayWindow):
                        child.update_text_widget()
        else:
            print("Failed to update the recipe.")

        self.destroy()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.title("Recipe Manager")
    main_window.mainloop()
