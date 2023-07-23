from ingredient import Ingredient
from recipe import Recipe
from typing import List
from glob import glob
from yaml import load, dump, Dumper, Loader
from pathlib import Path


class RecipeManager:
    def __init__(self):
        self.recipes: List[Recipe] = []

    def add_recipe(self, recipe_to_add: Recipe):
        if len(self.recipes) > 0:
            self.recipes.append(recipe_to_add)
        else:
            self.recipes = [recipe_to_add]

    def update_recipe(self, recipe_to_update: Recipe, updated_recipe: Recipe):
        found = False
        for x, rec in enumerate(self.recipes):
            if rec._title == recipe_to_update._title:
                self.recipes[x] = updated_recipe
                found = True
                break

        if not found:
            raise ("I couldn't find the recipe to update")

    def delete_recipe(self, recipe_to_delete: Recipe):
        self.recipes.remove(recipe_to_delete)

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
            self.recipes = data_sets

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
