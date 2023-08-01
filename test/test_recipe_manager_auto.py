import sys

sys.path.append("../")
from recipemanager import RecipeManager
from recipe import Recipe
from ingredient import Ingredient
from pathlib import Path
from testrecipemanager import TestRecipeManager

path = Path("./testdata")


def pretty_print_recipe(recipe: Recipe):
    print(
        f"Description: {recipe.description} \n No. Servings: {recipe.no_servings} \n Callories per portion: {recipe.calories_per_portion} \n"
    )
    print("Ingredients:")
    for ingredient in recipe.ingredients:
        print(ingredient.pretty_format())
    print("\nInstructions:")
    for instruction in recipe.instructions:
        print(f"\n{instruction}")


testrecipemanager = RecipeManager()

testrecipemanager.read_recipes_from_files(path)

no_recipes_read_in = len(testrecipemanager.recipes)
print(f"{no_recipes_read_in} read in")

for recipe in testrecipemanager.recipes:
    pretty_print_recipe(recipe)

print(f"Deleting {testrecipemanager.recipes[0].title}")
apple_pie = testrecipemanager.recipes[0]
testrecipemanager.delete_recipe(testrecipemanager.recipes[0])

print(
    f"Number of recipes in list now {len(testrecipemanager.recipes)} and its {testrecipemanager.recipes[0].title}"
)
assert len(testrecipemanager.recipes) == no_recipes_read_in - 1

print("Adding apple pie back in")
testrecipemanager.add_recipe(apple_pie)

print(
    f"Number of recipes in list now {len(testrecipemanager.recipes)} and its {testrecipemanager.recipes[0].title} and {testrecipemanager.recipes[1].title}"
)

print("Updating apple pie")
apple_pie.description = "It really is a nice apple pie"
testrecipemanager.update_recipe(testrecipemanager.recipes[1], apple_pie)

for recipe in testrecipemanager.recipes:
    pretty_print_recipe(recipe)
