"""
Recipe Manager class
"""
from typing import List
from pathlib import Path
from yaml import load, dump, Dumper, Loader
from recipe import Recipe


class RecipeManager:
    """
    Recipe Manager Class
    """

    def __init__(self):
        """
        Init for recipe manager
        """
        self._recipes: List[Recipe] = []

    @property
    def recipes(self):
        """
        Getter for recipes
        """
        return self._recipes

    def add_recipe(self, recipe_to_add: Recipe):
        """
        Method to add a recipe to the list
        """
        if len(self._recipes) > 0:
            self._recipes.append(recipe_to_add)
        else:
            self._recipes = [recipe_to_add]
        return True

    def update_recipe(self, recipe_to_update: Recipe, updated_recipe: Recipe):
        """
        Method to update a recipe
        """
        found = False
        for _x, rec in enumerate(self._recipes):
            if rec.title == recipe_to_update.title:
                self._recipes[_x] = updated_recipe
                found = True
                break

        if not found:
            raise "I couldn't find the recipe to update"

        return found

    def delete_recipe(self, recipe_to_delete: Recipe) -> bool:
        """
        Method to delete a recipe from a list
        """
        found = False
        for _x, rec in enumerate(self._recipes):
            if rec.title == recipe_to_delete.title:
                del self._recipes[_x]
                found = True
                break

        if not found:
            raise "I couldn't find the recipe to update"

        return found

    def read_recipes_from_files(self, path: Path):
        """
        Method to read a set of recipes from file
        """
        # Create a list to contain returned objects from reading files
        data_sets = []

        # Get a list of yml files that are already in the path
        yaml_files = path.glob("*.yml")

        # Iterate a list of yaml file previously found in the route path
        for recipe_file in yaml_files:

            # Open the file as read only
            _f = open(recipe_file, "r")

            # Read the file
            stream = _f.read()

            # Load the data
            data = load(stream, Loader=Loader)

            # Append the data
            data_sets.append(data)

            # Close the file
            _f.close()

        if len(data_sets) > 0:
            self._recipes = data_sets

    @classmethod
    def write_recipe_to_file(
        cls, recipe: Recipe, directory_path: Path, name=None, overwrite=False
    ):
        """
        Method to write a set of recipes to files on disc
        """
        file_name = "default.py"
        if name is None:
            # Create a file name based on the name of the recipe
            file_name = str(recipe.title.strip() + ".yml").replace(" ", "_")
        else:
            file_name = name

        # Create a path to the file to be written based upon the route path and the filename
        path = directory_path.joinpath(file_name)

        # If the file already exists - don't bother
        if path.is_file() and not overwrite:
            raise "File alread exists and you don't want to overwrite"

        # Open the file for writing
        _f = open(path, "w")

        # Create a dump of the recipe class representation
        data = dump(recipe, Dumper=Dumper)

        # Write the dumped data to file
        _f.write(data)

        # Close the file
        _f.close()
