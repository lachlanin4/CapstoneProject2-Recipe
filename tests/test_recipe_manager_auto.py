"""
Automatic test of recipe manager
"""
from pathlib import Path

from context import recipemanager
from context import recipe
from recipemanager import RecipeManager

path = Path("./testdata")


def pretty_print_recipe(_recipe: recipe.Recipe):
    """
    Allow simple printing of a recipe
    """
    print(
        str(f"Description: {_recipe.description} \n " +
            f"No. Servings: {_recipe.no_servings} \n " +
            f"Callories per portion: {_recipe.calories_per_portion} \n")
    )
    print("Ingredients:")
    for ingredient in _recipe.ingredients:
        print(ingredient.pretty_format())
    print("\nInstructions:")
    for instruction in _recipe.instructions:
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
    str(f"Number of recipes in list now {len(testrecipemanager.recipes)} " +
        f"and its {testrecipemanager.recipes[0].title}")
)
assert len(testrecipemanager.recipes) == no_recipes_read_in - 1

print("Adding apple pie back in")
testrecipemanager.add_recipe(apple_pie)

print(
    str(f"Number of recipes in list now {len(testrecipemanager.recipes)} " +
        f"and its {testrecipemanager.recipes[0].title} and " +
        f"{testrecipemanager.recipes[1].title}")
)

print("Updating apple pie")
apple_pie.description = "It really is a nice apple pie"
testrecipemanager.update_recipe(testrecipemanager.recipes[1], apple_pie)

for recipe in testrecipemanager.recipes:
    pretty_print_recipe(recipe)
