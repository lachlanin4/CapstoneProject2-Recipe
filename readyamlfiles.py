from glob import glob
from yaml import load, dump
from pathlib import Path

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Create a noddy form of recipe class
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


# Route path for recipe files
route_path = "/home/lachlan"

# Get a list of yml files that are already in the path
yaml_files = glob(f"{route_path}/*.yml")

# Create a list to contain returned objects from reading files
data_sets = []

# Create a basic recipe for rice pudding
rice_pudding = Recipe(name="Rice Pudding", instructions=["1. Open Tin", "2. Warm Rice Pudding", "3. Serve"], ingredients=["Rice Pudding", "Jam", "Cream"])

# Create a basic recipe for scrambled eggs
scrambled_eggs = Recipe(name="Scrambled Eggs", instructions=["1. Break eggs in a bowl", "2. Whisk up eggs", "3. Cook in hot pan with butter"], ingredients=["Eggs", "Butter"])

# Create an iterable list of recipes to write to files
recipes_to_write = [rice_pudding, scrambled_eggs]

# Iterate the list of recipes
for recipe in recipes_to_write:

   # Create a file name based on the name of the recipe
   file_name = str(recipe.name + ".yml").replace(" ", "_")
   
   # Create a path to the file to be written based upon the route path and the filename
   path = Path(route_path + "/" + file_name)
   
   # If the file already exists - don't bother
   if path.is_file():
      next
   else:
      # Open the file for writing
      f = open(path, 'w')
      
      # Create a dump of the recipe class representation
      data=dump(recipe, Dumper=Dumper)
      
      # Write the dumped data to file
      f.write(data)
      
      # Close the file
      f.close()
   
# Iterate a list of yaml file previously found in the route path
for recipeFile in yaml_files:

   # Open the file as read only
   f = open(recipeFile, 'r')

   # Read the file
   stream = f.read()

   # Load the data
   data = load(stream, Loader=Loader)

   # Append the data
   data_sets.append(data)

# Print out the read data sets as original class type (i.e. Recipe class)
for data_set in data_sets:
   print(data_set.name)
   print(data_set.instructions)
   print(data_set.ingredients)
